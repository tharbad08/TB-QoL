using DynamiteRubble;
using HarmonyLib;
using Opolame.MoreTunnels.Scripts;
using Timberborn.BlockSystem;
using Timberborn.TerrainSystem;
using TonWolfe.DeepMines;
using UnityEngine;

namespace Tharbad08.DynamiteRubbleCompat;

// Check real terrain state: a tunnel can explode without removing terrain.
readonly record struct TerrainSnapshot(Vector3Int Coordinates, bool WasTerrain)
{
    public static TerrainSnapshot Capture(ITerrainService terrainService, BlockObject blockObject)
    {
        Vector3Int coordinates = blockObject.Coordinates;
        return new(coordinates, terrainService.Underground(coordinates));
    }

    public void SpawnRubbleIfRemoved(ITerrainService terrainService)
    {
        if (!WasTerrain || terrainService.Underground(Coordinates))
        {
            return;
        }

        // Reuse the original mod's Dirt amount and recovered-goods queue.
        DynamiteRubbleService.Instance?.SpawnDirt(Coordinates, 1);
    }
}

[HarmonyPatch(typeof(TWTunnel), "Explode")]
static class MoreMinesTunnelPatch
{
    // These fields are private upstream. Harmony field injection avoids
    // manually reflecting over private game/mod implementation details.
    static void Prefix(
        ITerrainService ____terrainService,
        BlockObject ____blockObject,
        out TerrainSnapshot __state)
    {
        __state = TerrainSnapshot.Capture(____terrainService, ____blockObject);
    }

    static void Postfix(ITerrainService ____terrainService, TerrainSnapshot __state)
    {
        __state.SpawnRubbleIfRemoved(____terrainService);
    }
}

[HarmonyPatch(typeof(ImprovedTunnel), "Explode")]
static class MoreTunnelsExplosionPatch
{
    static void Prefix(
        ITerrainService ____terrainService,
        BlockObject ____blockObject,
        out TerrainSnapshot __state)
    {
        __state = TerrainSnapshot.Capture(____terrainService, ____blockObject);
    }

    static void Postfix(ITerrainService ____terrainService, TerrainSnapshot __state)
    {
        __state.SpawnRubbleIfRemoved(____terrainService);
    }
}
