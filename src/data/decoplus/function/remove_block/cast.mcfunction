execute if block ~ ~ ~ #decoplus:player_head{components:{"minecraft:custom_data":{deco:1b}}} run return run setblock ~ ~ ~ air
execute if entity @s[distance=10..] run return fail

execute positioned ^ ^ ^.2 run function decoplus:remove_block/cast