import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

#battery age
G.add_node("ba", ba_y=0.2, ba_n=0.8)

#alternator broken
G.add_node("ab", ab_y=0.1, ab_n=0.9)

#fanbelt broken
G.add_node("fb", fb_y=0.3, fb_n=0.7)

#battery dead
G.add_node("bd", ba_y_bd_y=0.7, ba_n_bd_y=0.2, ba_y_bd_n=0.3, ba_n_bd_n=0.8)

#no charging
G.add_node("nc", ab_y_fb_y_nc_y=0.75, ab_y_fb_n_nc_y=0.4, ab_n_fb_y_nc_y=0.6, ab_n_fb_n_nc_y=0.1,
                 ab_y_fb_y_nc_n=0.25, ab_y_fb_n_nc_n=0.6, ab_n_fb_y_nc_n=0.4, ab_n_fb_n_nc_n=0.9)

#battery flat
G.add_node("bf", bd_y_nc_y_bf_y=0.95, bd_y_nc_n_bf_y=0.85, bd_n_nc_y_bf_y=0.8, bd_n_nc_n_bf_y=0.1,
                 bd_y_nc_y_bf_n=0.05, bd_y_nc_n_bf_n=0.15, bd_n_nc_y_bf_n=0.2, bd_n_nc_n_bf_n=0.9)

#no oil
G.add_node("no", no_y=0.05, no_n=0.95)

#lights
G.add_node("l", bf_y_l_y=0.05, bf_n_l_y=0.9, bf_y_l_n=0.95, bf_n_l_n=0.1)

#gas guage
G.add_node("gg", bf_y_gg_y=0.1, bf_n_gg_y=0.95, bf_y_gg_n=0.9, bf_n_gg_n=0.05)

#dipstick level
G.add_node("dl", no_y_dl_y=0.95, no_n_dl_y=0.3, no_y_dl_n=0.05, no_n_dl_n=0.7)

#car wont start
G.add_node("cws",bf_y_no_y_cws_y=0.90, bf_y_no_n_cws_y=0.9,bf_n_no_y_cws_y= 0.30, bf_n_no_n_cws_y=0.15,
                 bf_y_no_y_cws_n=0.10, bf_y_no_n_cws_n=0.1, bf_n_no_y_cws_n=0.70, bf_n_no_n_cws_n=0.85)


G.add_edges_from([
    ("ba", "bd"),
    ("ab", "nc"),
    ("fb", "nc"),
    ("bd", "bf"),
    ("nc", "bf"),
    ("bf", "l"),
    ("bf", "gg"),
    ("bf", "cws"),
    ("no", "dl"),
    ("no", "cws"),
])


#create the figure for Bayesian network

pos = {
    "ba": (0, 4),
    "ab": (2, 4),
    "fb": (4, 4),
    "no": (5, 2),
    "bd": (1, 3),
    "nc": (3, 3),
    "bf": (2, 2),
    "dl": (6, 1),
    "l": (0, 1),
    "gg": (2, 1),
    "cws": (4, 1),
}


labels = { 

    "ba": "battery\nage",
    "ab": "alternator\nbroken",
    "fb": "fanbelt\nbroken",
    "no": "no oil",
    "bd": "battery\ndead",
    "nc": "no charging",
    "bf": "battery flat",
    "dl": "dipstick",
    "l": "lights",
    "gg": "gas guage",
    "cws": "car won't\nstart",
}

plt.figure(figsize=(8, 6))

nx.draw_networkx_nodes(G, pos, node_size=2200, node_color="blue", linewidths=0.25)

nx.draw_networkx_edges(G, pos, edgelist= G.edges, width=3, arrowstyle="->", arrowsize=50, connectionstyle="arc3,rad=0.05" )

nx.draw_networkx_labels(G, pos, labels= labels, font_size=7, font_color="white", font_weight="bold")

plt.title("Bayesian Network", fontsize=20)
plt.axis("off")
plt.tight_layout()
plt.show()