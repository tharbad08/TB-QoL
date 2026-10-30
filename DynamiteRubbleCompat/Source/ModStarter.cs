using System;
using HarmonyLib;
using Timberborn.ModManagerScene;
using UnityEngine;

namespace Tharbad08.DynamiteRubbleCompat;

public sealed class ModStarter : IModStarter
{
    const string HarmonyId = "tharbad08.DynamiteRubbleCompat";

    public void StartMod(IModEnvironment modEnvironment)
    {
        Harmony harmony = new(HarmonyId);
        try
        {
            harmony.PatchAll();
        }
        catch (Exception exception)
        {
            harmony.UnpatchAll(HarmonyId);
            Debug.LogWarning($"[DynamiteRubbleCompat] Failed to install patches: {exception}");
        }
    }
}
