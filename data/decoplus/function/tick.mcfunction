# Check for uninstantiated decorations
execute as @e[type=minecraft:armor_stand,tag=!deco_armorstand,predicate=decoplus:is_wearing_deco] positioned as @s run function decoplus:setup_deco

# Check for decorations that should be destroyed
execute as @e[type=minecraft:interaction,tag=deco_triggerbox,nbt={attack:{}}] positioned as @s run function decoplus:destroy_deco