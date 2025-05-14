# Spawn decorations
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"fire_log_pile"}] run function decoplus:spawn/fire_log_pile
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"sitting_skeleton"}] run function decoplus:spawn/sitting_skeleton
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"telescope"}] run function decoplus:spawn/telescope
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"controller"}] run function decoplus:spawn/controller
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"lamp"}] run function decoplus:spawn/lamp
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"caution_sign"}] run function decoplus:spawn/caution_sign
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"round_barrel"}] run function decoplus:spawn/round_barrel
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"trash_can"}] run function decoplus:spawn/trash_can
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"bamboo_flower_cart"}] run function decoplus:spawn/bamboo_flower_cart
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"window_barricades"}] run function decoplus:spawn/window_barricades
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"magma_block_potion"}] run function decoplus:spawn/magma_block_potion
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"sculk_potion"}] run function decoplus:spawn/sculk_potion
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"slime_block_potion"}] run function decoplus:spawn/slime_block_potion
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"little_creeper"}] run function decoplus:spawn/little_creeper
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"firework_small_box"}] run function decoplus:spawn/firework_small_box
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"cookie_oven"}] run function decoplus:spawn/cookie_oven
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"large_candlestick"}] run function decoplus:spawn/large_candlestick
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"wooden_beer_mug"}] run function decoplus:spawn/wooden_beer_mug
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"tiny_tree"}] run function decoplus:spawn/tiny_tree
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"globe"}] run function decoplus:spawn/globe
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"rocks"}] run function decoplus:spawn/rocks
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"fake_herobrine"}] run function decoplus:spawn/fake_herobrine
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"punching_bag"}] run function decoplus:spawn/punching_bag
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"red_clock"}] run function decoplus:spawn/red_clock
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_id:"chess_board"}] run function decoplus:spawn/chess_board

# Rotate decoration
execute as @e[type=!player,type=!minecraft:armor_stand,distance=..1.2] positioned as @s facing entity @p feet run rotate @s ~ 0

# Spawn triggerbox & disable the armor stand
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_size:"small"}] run function decoplus:triggerbox/spawn_small_triggerbox
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_size:"default"}] run function decoplus:triggerbox/spawn_default_triggerbox
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_size:"large"}] run function decoplus:triggerbox/spawn_large_triggerbox
execute if items entity @s armor.chest minecraft:player_head[minecraft:custom_data~{deco_size:"tall"}] run function decoplus:triggerbox/spawn_tall_triggerbox

tag @s add deco_armorstand
data merge entity @s {Marker:1b,Invisible:1b}