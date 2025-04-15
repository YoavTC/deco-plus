# Re-enable the armor stand
data merge entity @e[type=armor_stand,sort=nearest,limit=1] {Invulnerable:0b,Invisible:0b,Tags:[deco_armorstand]}

# Destroy the armor stand & drop the decoration item
damage @e[type=armor_stand,sort=nearest,limit=1] 1 arrow

# Destroy the decoration
kill @e[type=minecraft:block_display,distance=..2]
kill @e[type=minecraft:item_display,distance=..2]
kill @e[type=minecraft:text_display,distance=..2]
kill @e[type=minecraft:interaction,distance=..2]
kill @s