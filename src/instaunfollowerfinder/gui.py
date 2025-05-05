import customtkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import os
import math
import src.instaunfollowerfinder.utils as u


class App:
    WIDTH = 510
    PLUSWIDTH = 510 + 487
    HEIGHT = 457

    STEPS_SLIDE_SIDE = 20
    DELAY_SLIDE_SIDE = 3

    EXTRA_STEPS_SLIDE_SIDE = 50

    N_BUTTONS_SIDE_GRID = 15

    def __init__(self):
        self.followersPath = ""
        self.followingPath = ""

        self.maxPages = 0
        self.page = 0

        self.sideName = None

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

        self.myName = tk.CTkLabel(
            self.root,
            text="by SmartsvXD 2025",
            font=("Courier New", 12, "bold"),
            bg_color="#2C2C2C",
            text_color="#a0a0a0",
        )
        self.myName.place(x=265, y=150, anchor="nw")

        self.findUnfollowersB = tk.CTkButton(
            self.root,
            text="Find Unfollowers",
            font=("Courier New", 18, "bold"),
            anchor="nw",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#2c2c2c",
            corner_radius=0,
            command=self.showUnfollowersOpen,
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
        self.loadJSONsB = tk.CTkButton(
            self.root,
            text="Load JSONS",
            font=("Courier New", 18, "bold"),
            anchor="nw",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#2c2c2c",
            corner_radius=0,
            command=self.openJSONs,
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
            command=self.editWhitelistOpen,
            width=240,
            height=30,
        )

        self.findUnfollowersB.place(x=52, y=272, anchor="w")
        self.opeMetaAccountCenterB.place(x=50, y=300, anchor="w")
        self.loadJSONsB.place(x=50, y=330, anchor="w")
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
        self.findUnfollowersB.bind("<Leave>", self.onLeaveHoverLabel)

        self.opeMetaAccountCenterB.bind(
            "<Enter>", lambda event: self.onEnterHoverLabel(event)
        )
        self.opeMetaAccountCenterB.bind("<Leave>", self.onLeaveHoverLabel)

        self.loadJSONsB.bind("<Enter>", lambda event: self.onEnterHoverLabel(event))
        self.loadJSONsB.bind("<Leave>", self.onLeaveHoverLabel)

        self.editWhitelistB.bind("<Enter>", lambda event: self.onEnterHoverLabel(event))
        self.editWhitelistB.bind("<Leave>", self.onLeaveHoverLabel)

        self.closeSideB = tk.CTkButton(
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
        self.closeSideB.place(x=510 - 2, y=22, anchor="nw")

        self.nPage = tk.CTkLabel(
            self.root,
            text="00/00",
            font=("Courier New", 18, "bold"),
            anchor="center",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            corner_radius=0,
            width=20,
            height=20,
        )
        self.nPage.place(x=510 + 487 / 2 - 20, y=25, anchor="n")
        self.root.update_idletasks()

        self.prevPageB = tk.CTkButton(
            self.root,
            text="<",
            font=("Courier New", 18, "bold"),
            anchor="center",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#333333",
            corner_radius=0,
            command=self.prevPage,
            width=20,
            height=20,
        )
        self.prevPageB.place(x=self.nPage.winfo_x() - 40, y=22, anchor="ne")

        self.nextPageB = tk.CTkButton(
            self.root,
            text=">",
            font=("Courier New", 18, "bold"),
            anchor="center",
            text_color="#f0f0f0",
            fg_color="#2c2c2c",
            hover_color="#333333",
            corner_radius=0,
            command=self.nextPage,
            width=20,
            height=20,
        )
        self.nextPageB.place(
            x=self.nPage.winfo_x() + self.nPage.winfo_width() + 40, y=22, anchor="nw"
        )

        self.sideGridNames = tuple(
            tk.CTkButton(
                self.root,
                width=375,
                height=25,
                font=("Courier New", 18, "bold"),
                anchor="nw",
                text_color="#f0f0f0",
                fg_color="#2c2c2c",
                hover_color="#333333",
                corner_radius=0,
                text="AAAAAAAA",
            )
            for _ in range(self.N_BUTTONS_SIDE_GRID)
        )
        self.sideGridBtns = tuple(
            (
                tk.CTkButton(
                    self.root,
                    width=25,
                    height=25,
                    font=("Courier New", 18, "bold"),
                    anchor="n",
                    text_color="#f0f0f0",
                    fg_color="#2c2c2c",
                    hover_color="#333333",
                    corner_radius=0,
                    text="B",
                )
            )
            for _ in range(self.N_BUTTONS_SIDE_GRID)
        )

        for i in range(self.N_BUTTONS_SIDE_GRID):
            self.sideGridNames[i].place(x=80 + 487, y=45 + 25 * i, anchor="nw")
            self.sideGridBtns[i].place(x=55 + 487, y=45 + 25 * i, anchor="nw")

    def onEnterHoverLabel(self, event):
        widget = event.widget
        x = widget.winfo_rootx() - self.root.winfo_rootx() - 5
        y = widget.winfo_rooty() - self.root.winfo_rooty() + 11
        self.hoverLabel.place(x=x, y=y, anchor="e")

    def onLeaveHoverLabel(self, event):
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

    def openSide(self, i=0):
        currentWidth = self.root.winfo_width()

        if i < self.STEPS_SLIDE_SIDE and currentWidth < self.PLUSWIDTH:
            newWidth = int(
                currentWidth + (self.PLUSWIDTH - self.WIDTH) / self.STEPS_SLIDE_SIDE
            )
            self.root.geometry(f"{newWidth}x{self.HEIGHT}")
            self.root.after(self.DELAY_SLIDE_SIDE, self.openSide, i + 1)
        else:
            self.root.geometry(f"{self.PLUSWIDTH}x{self.HEIGHT}")

    def closeSide(self, i=0):
        currentWidth = self.root.winfo_width()

        if i < self.STEPS_SLIDE_SIDE and currentWidth > self.WIDTH:
            newWidth = int(
                currentWidth + (self.WIDTH - self.PLUSWIDTH) / self.STEPS_SLIDE_SIDE
            )
            self.root.geometry(f"{newWidth}x{self.HEIGHT}")
            self.root.after(self.DELAY_SLIDE_SIDE, self.closeSide, i + 1)
        else:
            self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.page = 0

    def error(self, text):
        messagebox.showerror(
            title="Error",
            message=text,
        )

    def info(self, text):
        messagebox.showinfo(title="Info", message=text)

    def openJSONs(self):
        self.followingPath, self.followersPath = "", ""

        files = filedialog.askopenfilenames(
            title="Select followers_1.json and following.json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        )

        if not len(files):
            return False

        if len(files) != 2:
            self.error(
                "Wrong files selected.\nYou need to select followers_1.json and following.json."
            )
            return False

        for file in files:
            if os.path.basename(file) == "followers_1.json":
                self.followersPath = file
            elif os.path.basename(file) == "following.json":
                self.followingPath = file
            else:
                self.error(
                    "Invalid files.\n You need to select followers_1.json and following.json."
                )
                return False

        if self.followersPath == "" or self.followingPath == "":
            self.error(
                "Invalid files.\n You need to select followers_1.json and following.json."
            )
            return False

        return True

    def updateSide(self):
        return

    def updatePrevNextNPages(self):
        self.nPage.configure(text=f"{self.page + 1}/{self.maxPages}")
        self.root.update_idletasks()

        self.prevPageB.place(x=self.nPage.winfo_x(), y=22, anchor="ne")
        self.nextPageB.place(
            x=self.nPage.winfo_x() + self.nPage.winfo_width(), y=22, anchor="nw"
        )

        self.updateSide()

    def prevPage(self):
        if self.page == 0:
            return

        self.page -= 1
        self.updatePrevNextNPages()

    def nextPage(self):
        if self.page == self.maxPages - 1:
            return

        self.page += 1
        self.updatePrevNextNPages()

    def addToWhitelist(self, unfollower):
        u.addToWhiteList(unfollower, infoF=self.info, errorF=self.error)
        self.showUnfollowers()

    def showUnfollowersOpen(self):
        if self.sideName != "showUnfollowers" and self.sideName is not None:
            self.sideName = "showUnfollowers"
            self.closeSide()
            self.root.after(
                self.DELAY_SLIDE_SIDE
                * (self.STEPS_SLIDE_SIDE + self.EXTRA_STEPS_SLIDE_SIDE),
                self.showUnfollowers,
            )
        else:
            self.sideName = "showUnfollowers"
            self.showUnfollowers()

    def showUnfollowers(self):
        if self.followersPath == "" or self.followingPath == "":
            if not self.openJSONs():
                return

        unfollowers = u.compareLists(
            followersPath=self.followersPath,
            followingPath=self.followingPath,
            infoF=self.info,
            errorF=self.error,
        )

        if unfollowers == []:
            self.sideGridNames[0].configure(
                text="Everyone follows you back!", command=None
            )
            self.sideGridBtns[0].configure(text="", command=None)
            for i in range(1, self.N_BUTTONS_SIDE_GRID):
                self.sideGridNames[i].configure(text="", command=None)
                self.sideGridBtns[i].configure(text="", command=None)

            def update():
                return

            self.updateSide = update

            self.page = 0
            self.maxPages = 1
            self.updatePrevNextNPages()

            self.openSide()
        else:
            self.maxPages = math.ceil(len(unfollowers) / self.N_BUTTONS_SIDE_GRID)
            self.updatePrevNextNPages()

            def update():
                for i in range(self.N_BUTTONS_SIDE_GRID):
                    if i + self.page * self.N_BUTTONS_SIDE_GRID < len(unfollowers):
                        unfollower = unfollowers[
                            i + self.page * self.N_BUTTONS_SIDE_GRID
                        ]
                        self.sideGridNames[i].configure(
                            text=unfollower,
                            command=lambda usr=unfollower: webbrowser.open(
                                f"https://www.instagram.com/{usr}"
                            ),
                        )
                        self.sideGridBtns[i].configure(
                            text="+",
                            text_color="#70a0f0",
                            command=lambda usr=unfollower: self.addToWhitelist(usr),
                        )
                    else:
                        self.sideGridNames[i].configure(text="", command=None)
                        self.sideGridBtns[i].configure(text="", command=None)

            self.updateSide = update
            self.updateSide()

            self.openSide()

    def removeFromWhitelist(self, user):
        u.removeFromWhiteList(user, infoF=self.info, errorF=self.error)
        self.editWhitelist()

    def editWhitelistOpen(self):
        if self.sideName != "editWhitelist" and self.sideName is not None:
            self.sideName = "editWhitelist"
            self.closeSide()
            self.root.after(
                self.DELAY_SLIDE_SIDE
                * (self.STEPS_SLIDE_SIDE + self.EXTRA_STEPS_SLIDE_SIDE),
                self.editWhitelist,
            )
        else:
            self.sideName = "editWhitelist"
            self.editWhitelist()

    def editWhitelist(self):
        whitelist = u.loadWhitelist(infoF=self.info, errorF=self.error)

        if whitelist == []:
            self.sideGridNames[0].configure(text="The whitelist is empty", command=None)
            self.sideGridBtns[0].configure(text="", command=None)
            for i in range(1, self.N_BUTTONS_SIDE_GRID):
                self.sideGridNames[i].configure(text="", command=None)
                self.sideGridBtns[i].configure(text="", command=None)

            def update():
                return

            self.updateSide = update

            self.page = 0
            self.maxPages = 1
            self.updatePrevNextNPages()

            self.openSide()
        else:
            self.maxPages = math.ceil(len(whitelist) / self.N_BUTTONS_SIDE_GRID)
            self.updatePrevNextNPages()

            def update():
                for i in range(self.N_BUTTONS_SIDE_GRID):
                    if i + self.page * self.N_BUTTONS_SIDE_GRID < len(whitelist):
                        user = whitelist[i + self.page * self.N_BUTTONS_SIDE_GRID]
                        self.sideGridNames[i].configure(
                            text=user,
                            command=lambda usr=user: webbrowser.open(
                                f"https://www.instagram.com/{usr}"
                            ),
                        )
                        self.sideGridBtns[i].configure(
                            text="-",
                            text_color="#ff7050",
                            command=lambda usr=user: self.removeFromWhitelist(usr),
                        )
                    else:
                        self.sideGridNames[i].configure(text="", command=None)
                        self.sideGridBtns[i].configure(text="", command=None)

            self.updateSide = update
            self.updateSide()

            self.openSide()

    def run(self):
        self.updateFrame(0)
        self.root.mainloop()


def main():
    app = App()
    app.run()
