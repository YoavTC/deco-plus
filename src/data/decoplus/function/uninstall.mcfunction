tellraw @a {text:"Removing decorations...",color:"yellow"}
scoreboard objectives add decoplus.old dummy
scoreboard players set count decoplus.old 0

execute as @e[type=minecraft:interaction,tag=deco_triggerbox] positioned as @s run function decoplus:uninstall/remove_old

schedule function decoplus:uninstall/notify 1s