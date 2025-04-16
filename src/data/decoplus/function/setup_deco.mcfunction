# Spawn decorations
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"fire_log_pile"}] run function decoplus:spawn/fire_log_pile
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"sitting_skeleton"}] run function decoplus:spawn/sitting_skeleton
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"telescope"}] run function decoplus:spawn/telescope
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"controller"}] run function decoplus:spawn/controller
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"lamp"}] run function decoplus:spawn/lamp
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"caution_sign"}] run function decoplus:spawn/caution_sign
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"round_barrel"}] run function decoplus:spawn/round_barrel
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"trash_can"}] run function decoplus:spawn/trash_can

# Rotate decoration
execute as @e[type=!player,type=!minecraft:armor_stand,distance=..1.2] positioned as @s facing entity @p feet run rotate @s ~ 0

# Spawn triggerbox & disable the armor stand
summon interaction ~ ~ ~ {width:1f,height:1f,Tags:["deco_triggerbox"]}
tag @s add deco_armorstand
data merge entity @s {Marker:1b,Invisible:1b}