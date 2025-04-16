# Re-enable the armor stand
execute as @e[type=armor_stand,distance=..1.2] run data merge entity @s {Marker:0b,Invisible:0b,Tags:[deco_armorstand]}

# Destroy the armor stand & drop the decoration item
execute as @e[type=armor_stand,distance=..1.2] run damage @s 1 arrow

# Destroy the decoration
kill @e[type=minecraft:block_display,distance=..1.2]
kill @e[type=minecraft:item_display,distance=..1.2]
kill @e[type=minecraft:text_display,distance=..1.2]
kill @e[type=minecraft:interaction,distance=..1.2]
kill @s