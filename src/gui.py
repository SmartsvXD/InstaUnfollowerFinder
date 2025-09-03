import customtkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import os
import math
import src.utils as u
from sys import platform


class App:
    # region CLASS_VARIABLES
    WIDTH = 510
    PLUSWIDTH = 510 + 487
    HEIGHT = 457

    if platform == "win32":
        TITLE_FONT_SIZE = 8
        TITLE_SHIFT = 6

        DELAY_SLIDE_SIDE = 0
        STEPS_SLIDE_SIDE = 1
        EXTRA_DELAY_SLIDE_SIDE = 10

        EXTRA_FRAME = 1
        FRAME_SHIFT = 14
    else:
        TITLE_FONT_SIZE = 9
        TITLE_SHIFT = 0

        DELAY_SLIDE_SIDE = 3
        STEPS_SLIDE_SIDE = 20
        EXTRA_DELAY_SLIDE_SIDE = 0

        EXTRA_FRAME = 0
        FRAME_SHIFT = 0

    WIDTH += FRAME_SHIFT

    EXTRA_STEPS_SLIDE_SIDE = 50

    N_BUTTONS_SIDE_GRID = 15

    # endregion

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
        if platform == "win32":
            self.root.iconbitmap(os.path.join(u.basePath, "icon.ico"))

        self.initFrame()
        self.initTitle()
        self.initMyName()
        self.initHoverLabel()
        self.initMainButtons()
        self.initSide()
        self.initVersionLabel()

        self.root.update()

        self.checkVersion()

    def checkVersion(self):
        newVersion = u.checkVersion()
        if newVersion[0]:
            risposta = messagebox.askyesno(
                title="Update Available",
                message=f"A new version is available!\n\n{newVersion[1]} -> {newVersion[2]}\n\nDo you want to visit the release page to download it?",
            )

            if risposta:
                webbrowser.open(
                    "https://github.com/SmartsvXD/InstaUnfollowerFinder/releases/latest"
                )

    def updateFrame(self, flip):
        flop = not (flip)

        if flop:
            self.frameA.configure(
                text="# " * (17 + self.EXTRA_FRAME)
                + "#"
                + (
                    ("\n" + "*" + " " * ((17 + self.EXTRA_FRAME) * 2 - 1) + "*")
                    + ("\n" + "#" + " " * ((17 + self.EXTRA_FRAME) * 2 - 1) + "#")
                )
                * 7
                + ("\n" + "*" + " " * ((17 + self.EXTRA_FRAME) * 2 - 1) + "*")
                + "\n"
                + "# " * (17 + self.EXTRA_FRAME)
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
                text="* " * (17 + self.EXTRA_FRAME)
                + "*"
                + (
                    ("\n" + "#" + " " * ((17 + self.EXTRA_FRAME) * 2 - 1) + "#")
                    + ("\n" + "*" + " " * ((17 + self.EXTRA_FRAME) * 2 - 1) + "*")
                )
                * 7
                + ("\n" + "#" + " " * ((17 + self.EXTRA_FRAME) * 2 - 1) + "#")
                + "\n"
                + "* " * (17 + self.EXTRA_FRAME)
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

    def error(self, text):
        messagebox.showerror(
            title="Error",
            message=text,
        )

    def info(self, text):
        messagebox.showinfo(title="Info", message=text)

    # region INIT_FUNCTIONS

    def initFrame(self):
        self.frameA = tk.CTkLabel(
            self.root,
            font=("Courier New", 24, "bold"),
            text_color="purple",
            text="* " * (17 + self.EXTRA_FRAME)
            + "*"
            + ("\n" + "*" + " " * ((17 + self.EXTRA_FRAME) * 2 - 1) + "*") * 15
            + "\n"
            + "* " * (17 + self.EXTRA_FRAME)
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
        self.frameB.place(x=490 + self.FRAME_SHIFT, y=-2)

    def initTitle(self):
        self.titleA = tk.CTkLabel(
            self.root,
            text_color="magenta",
            font=("Courier New", self.TITLE_FONT_SIZE, "bold"),
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
            font=("Courier New", self.TITLE_FONT_SIZE, "bold"),
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
            font=("Courier New", self.TITLE_FONT_SIZE, "bold"),
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
        self.titleA.place(x=30, y=70, anchor="w")
        self.titleB.place(x=30, y=137 + self.TITLE_SHIFT, anchor="w")
        self.titleC.place(x=30, y=204 + self.TITLE_SHIFT * 2, anchor="w")

    def initMyName(self):
        self.myName = tk.CTkLabel(
            self.root,
            text="by SmartsvXD 2025",
            font=("Courier New", 12, "bold"),
            bg_color="#2C2C2C",
            text_color="#a0a0a0",
        )
        self.myName.place(x=265, y=160 + self.TITLE_SHIFT + 1, anchor="nw")

    def initHoverLabel(self):
        if platform != "win32":
            self.hoverLabel = tk.CTkLabel(
                self.root,
                text=">",
                font=("Courier New", 18, "bold"),
                text_color="gold",
                bg_color="#2C2C2C",
            )
            self.hoverLabel.place_forget()

    def initMainButtons(self):
        button_configs = [
            {
                "text": "Find Unfollowers",
                "command": self.showUnfollowersOpen,
            },
            {
                "text": "Open Meta Account Center",
                "command": lambda: webbrowser.open(
                    "https://accountscenter.instagram.com/info_and_permissions/?theme=dark"
                ),
            },
            {
                "text": "Load JSONS",
                "command": self.openJSONs,
            },
            {
                "text": "Edit Whitelist",
                "command": self.editWhitelistOpen,
            },
        ]

        self.buttons = []
        for i, config in enumerate(button_configs):
            btn = tk.CTkButton(
                self.root,
                text=config["text"],
                font=("Courier New", 18, "bold"),
                anchor="nw",
                text_color="#f0f0f0",
                fg_color="#2c2c2c",
                hover_color="#2c2c2c" if platform != "win32" else "#333333",
                corner_radius=0,
                command=config["command"],
                width=240,
                height=30,
            )
            btn.place(x=50, y=270 + 30 * i, anchor="w")
            self.buttons.append(btn)

            if platform != "win32":
                btn.bind("<Enter>", lambda event: self.onEnterHoverLabel(event))
                btn.bind("<Leave>", self.onLeaveHoverLabel)

    def initSide(self):
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
            bg_color="#2c2c2c",
        )
        self.closeSideB.place(x=510 - 2 + self.FRAME_SHIFT, y=22, anchor="nw")

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
            bg_color="#2c2c2c",
        )
        self.nPage.place(x=510 + 487 / 2 - 20 + self.FRAME_SHIFT, y=25, anchor="n")
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
            bg_color="#2c2c2c",
        )
        self.prevPageB.place(
            x=self.nPage.winfo_x() - 40 + self.FRAME_SHIFT, y=22, anchor="ne"
        )

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
            bg_color="#2c2c2c",
        )
        self.nextPageB.place(
            x=self.nPage.winfo_x() + self.nPage.winfo_width() + 40 + self.FRAME_SHIFT,
            y=22,
            anchor="nw",
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
                bg_color="#2c2c2c",
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
                    bg_color="#2c2c2c",
                )
            )
            for _ in range(self.N_BUTTONS_SIDE_GRID)
        )

        for i in range(self.N_BUTTONS_SIDE_GRID):
            self.sideGridNames[i].place(
                x=80 + 487 + self.FRAME_SHIFT, y=45 + 25 * i, anchor="nw"
            )
            self.sideGridBtns[i].place(
                x=55 + 487 + self.FRAME_SHIFT, y=45 + 25 * i, anchor="nw"
            )

        def update():
            return

        self.updateSide = update

    def initVersionLabel(self):
        self.version = tk.CTkLabel(
            self.root,
            text=f"v{u.checkVersion()[1]}",
            font=("Courier New", 12, "bold"),
            bg_color="#2C2C2C",
            text_color="#666666",
        )
        self.version.place(x=20, y=410, anchor="nw")

    # endregion

    # region HOVER_LABEL_FUNCTIONS

    def onEnterHoverLabel(self, event):
        widget = event.widget
        x = widget.winfo_rootx() - self.root.winfo_rootx() - 5
        y = widget.winfo_rooty() - self.root.winfo_rooty() + 11
        self.hoverLabel.place(x=x, y=y, anchor="e")

    def onLeaveHoverLabel(self, event):
        self.hoverLabel.place_forget()

    # endregion

    # region SIDE_FUNCTIONS

    def openSide(self, i=0):
        currentWidth = self.root.winfo_width()

        if i < self.STEPS_SLIDE_SIDE and currentWidth < self.PLUSWIDTH:
            newWidth = int(
                currentWidth + (self.PLUSWIDTH - self.WIDTH) / self.STEPS_SLIDE_SIDE
            )
            self.root.geometry(f"{newWidth}x{self.HEIGHT}")
            if platform == "win32":
                self.root.update()
            self.root.after(self.DELAY_SLIDE_SIDE, self.openSide, i + 1)
        else:
            self.root.geometry(f"{self.PLUSWIDTH}x{self.HEIGHT}")
            if platform == "win32":
                self.root.update()

    def closeSide(self, i=0):
        if platform == "win32":
            currentWidth = self.root.winfo_width() * 0.8
        else:
            currentWidth = self.root.winfo_width()

        if i < self.STEPS_SLIDE_SIDE and currentWidth > self.WIDTH:
            newWidth = int(
                currentWidth + ((self.WIDTH - self.PLUSWIDTH) / self.STEPS_SLIDE_SIDE)
            )
            if newWidth < self.WIDTH:
                newWidth = self.WIDTH

            self.root.geometry(f"{newWidth}x{self.HEIGHT}")
            if platform == "win32":
                self.root.update()
            self.root.after(
                self.DELAY_SLIDE_SIDE + self.EXTRA_DELAY_SLIDE_SIDE,
                self.closeSide,
                i + 1,
            )
        else:
            self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
            if platform == "win32":
                self.root.update()

        self.page = 0

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

    # endregion

    # region MAIN_BUTTONS_FUNCTIONS

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

    # endregion

    def run(self):
        self.updateFrame(0)
        self.root.mainloop()


def main():
    app = App()
    app.run()
