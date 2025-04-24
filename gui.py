import customtkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import os


class App:
    WIDTH = 510
    PLUSWIDTH = 510 + 487
    HEIGHT = 457

    def __init__(self):
        self.root = tk.CTk()
        self.root.configure(bg="#2C2C2C")
        self.root.title("InstaUnfollowerFinder")
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.resizable(False, False)

        self.frameA = tk.CTkLabel(
            self.root,
            font=("Courier New", 24, "bold"),
            text_color="purple",
            text="* " * 17
            + "*"
            + ("\n" + "*" + " " * (17 * 2 - 1) + "*") * 15
            + "\n"
            + "* " * 17
            + "*",
            bg_color="#2C2C2C",
        )
        self.frameB = tk.CTkLabel(
            self.root,
            font=("Courier New", 24, "bold"),
            text_color="purple",
            text="* " * 17
            + "*"
            + ("\n" + "*" + " " * (17 * 2 - 1) + "*") * 15
            + "\n"
            + "* " * 17
            + "*",
            bg_color="#2C2C2C",
        )
        self.frameA.place(x=2, y=-2)
        self.frameB.place(x=490, y=-2)

        self.titleA = tk.CTkLabel(
            self.root,
            text_color="magenta",
            font=("Courier New", 9, "bold"),
            text="""
██╗███╗   ██╗███████╗████████╗ █████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║
██║██║ ╚████║███████║   ██║   ██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
                                            
        """,
            bg_color="#2C2C2C",
            justify="left",
        )
        self.titleB = tk.CTkLabel(
            self.root,
            text_color="magenta",
            font=("Courier New", 9, "bold"),
            text="""
██╗   ██╗███╗   ██╗███████╗ ██████╗ ██╗     ██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
██║   ██║████╗  ██║██╔════╝██╔═══██╗██║     ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
██║   ██║██╔██╗ ██║█████╗  ██║   ██║██║     ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██║     ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
║██████╔╝██║ ╚████║██║     ╚██████╔╝███████╗███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
                                                                                            
        """,
            bg_color="#2C2C2C",
            justify="left",
        )
        self.titleC = tk.CTkLabel(
            self.root,
            text_color="magenta",
            font=("Courier New", 9, "bold"),
            text="""
███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                             
""",
            bg_color="#2C2C2C",
            justify="left",
        )
        self.titleA.place(x=30, y=60, anchor="w")
        self.titleB.place(x=30, y=127, anchor="w")
        self.titleC.place(x=30, y=194, anchor="w")

        closeSideB = tk.CTkButton(
            self.root,
            text="<<",
            font=("Courier New", 18, "bold"),
            anchor="center",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#333333",
            corner_radius=0,
            command=self.closeSide,
            width=20,
            height=20,
        )
        closeSideB.place(x=21 + 487, y=22, anchor="nw")

        self.findUnfollowersB = tk.CTkButton(
            self.root,
            text="Find Unfollowers",
            font=("Courier New", 18, "bold"),
            anchor="nw",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#2c2c2c",
            corner_radius=0,
            command=self.openSide,
            width=240,
            height=30,
        )
        self.opeMetaAccountCenterB = tk.CTkButton(
            self.root,
            text="Open Meta Account Center",
            font=("Courier New", 18, "bold"),
            anchor="nw",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#2c2c2c",
            corner_radius=0,
            command=lambda: webbrowser.open(
                "https://accountscenter.instagram.com/info_and_permissions/?theme=dark"
            ),
            width=240,
            height=30,
        )
        self.loadJSONSB = tk.CTkButton(
            self.root,
            text="Load JSONS",
            font=("Courier New", 18, "bold"),
            anchor="nw",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#2c2c2c",
            corner_radius=0,
            command=self.openJSONS,
            width=240,
            height=30,
        )
        self.editWhitelistB = tk.CTkButton(
            self.root,
            text="Edit Whitelist",
            font=("Courier New", 18, "bold"),
            anchor="nw",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#2c2c2c",
            corner_radius=0,
            command=lambda: print("Ciaoo"),
            width=240,
            height=30,
        )

        self.findUnfollowersB.place(x=50, y=270, anchor="w")
        self.opeMetaAccountCenterB.place(x=50, y=300, anchor="w")
        self.loadJSONSB.place(x=50, y=330, anchor="w")
        self.editWhitelistB.place(x=50, y=360, anchor="w")

        self.hoverLabel = tk.CTkLabel(
            self.root,
            text=">",
            font=("Courier New", 18, "bold"),
            text_color="gold",
            bg_color="#2C2C2C",
        )
        self.hoverLabel.place_forget()

        self.findUnfollowersB.bind(
            "<Enter>", lambda event: self.onEnterHoverLabel(event)
        )
        self.findUnfollowersB.bind("<Leave>", self.onLeaveHovelLabel)

        self.opeMetaAccountCenterB.bind(
            "<Enter>", lambda event: self.onEnterHoverLabel(event)
        )
        self.opeMetaAccountCenterB.bind("<Leave>", self.onLeaveHovelLabel)

        self.loadJSONSB.bind("<Enter>", lambda event: self.onEnterHoverLabel(event))
        self.loadJSONSB.bind("<Leave>", self.onLeaveHovelLabel)

        self.editWhitelistB.bind("<Enter>", lambda event: self.onEnterHoverLabel(event))
        self.editWhitelistB.bind("<Leave>", self.onLeaveHovelLabel)

    def openSide(self, steps=20, delay=3, i=0):
        currentWidth = self.root.winfo_width()

        if i < steps and currentWidth < self.PLUSWIDTH:
            newWidth = int(currentWidth + (self.PLUSWIDTH - self.WIDTH) / steps)
            self.root.geometry(f"{newWidth}x{self.HEIGHT}")
            self.root.after(delay, self.openSide, steps, delay, i + 1)
        else:
            self.root.geometry(f"{self.PLUSWIDTH}x{self.HEIGHT}")

    def closeSide(self, steps=20, delay=3, i=0):
        currentWidth = self.root.winfo_width()

        if i < steps and currentWidth > self.WIDTH:
            newWidth = int(currentWidth + (self.WIDTH - self.PLUSWIDTH) / steps)
            self.root.geometry(f"{newWidth}x{self.HEIGHT}")
            self.root.after(delay, self.closeSide, steps, delay, i + 1)
        else:
            self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")

    def openJSONS(self):
        files = filedialog.askopenfilenames(
            title="Select followers_1.json and following.json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        )
        
        if not len(files):
            return

        if len(files) != 2:
            messagebox.showerror(
                title="Error",
                message="Wrong files selected.\nYou need to select followers_1.json and following.json.",
            )
            return

        followersPath, followingPath = None, None
        for file in files:
            if os.path.basename(file) == "followers_1.json":
                followersPath = file
            elif os.path.basename(file) == "following.json":
                followingPath = file
            else:
                messagebox.showerror(
                    title="Error",
                    message="Invalid files.\n You need to select followers_1.json and following.json.",
                )
                return

        if not (followersPath and followingPath):
            messagebox.showerror(
                title="Error",
                message="Invalid files.\n You need to select followers_1.json and following.json.",
            )
            return

    def onEnterHoverLabel(self, event):
        widget = event.widget
        x = widget.winfo_rootx() - self.root.winfo_rootx() - 5
        y = widget.winfo_rooty() - self.root.winfo_rooty() + 11
        self.hoverLabel.place(x=x, y=y, anchor="e")

    def onLeaveHovelLabel(self, event):
        self.hoverLabel.place_forget()

    def updateFrame(self, flip):
        flop = not (flip)

        if flop:
            self.frameA.configure(
                text="# " * 17
                + "#"
                + (
                    ("\n" + "*" + " " * (17 * 2 - 1) + "*")
                    + ("\n" + "#" + " " * (17 * 2 - 1) + "#")
                )
                * 7
                + ("\n" + "*" + " " * (17 * 2 - 1) + "*")
                + "\n"
                + "# " * 17
                + "#",
            )
            self.frameB.configure(
                text="# " * 17
                + "#"
                + (
                    ("\n" + "*" + " " * (17 * 2 - 1) + "*")
                    + ("\n" + "#" + " " * (17 * 2 - 1) + "#")
                )
                * 7
                + ("\n" + "*" + " " * (17 * 2 - 1) + "*")
                + "\n"
                + "# " * 17
                + "#",
            )
        else:
            self.frameA.configure(
                text="* " * 17
                + "*"
                + (
                    ("\n" + "#" + " " * (17 * 2 - 1) + "#")
                    + ("\n" + "*" + " " * (17 * 2 - 1) + "*")
                )
                * 7
                + ("\n" + "#" + " " * (17 * 2 - 1) + "#")
                + "\n"
                + "* " * 17
                + "*",
            )
            self.frameB.configure(
                text="* " * 17
                + "*"
                + (
                    ("\n" + "#" + " " * (17 * 2 - 1) + "#")
                    + ("\n" + "*" + " " * (17 * 2 - 1) + "*")
                )
                * 7
                + ("\n" + "#" + " " * (17 * 2 - 1) + "#")
                + "\n"
                + "* " * 17
                + "*",
            )

        self.root.after(500, self.updateFrame, flop)

    def run(self):
        self.updateFrame(0)
        self.root.mainloop()


app = App()
app.run()
