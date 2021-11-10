import urwid
import urwid.raw_display

URWID_PALETTE = [("titlebar", "white", "dark blue")]


def main() -> None:
    header = urwid.AttrMap(urwid.Text(u"Hello World!!!"), "titlebar")

    text = urwid.Text(u"Hello World!!!")
    filler = urwid.Filler(text, "top")

    frame = urwid.Frame(filler, header=header)

    #screen = urwid.raw_display.Screen()
    #screen.set_terminal_properties(colors=16)
    loop = urwid.MainLoop(frame, URWID_PALETTE)
    loop.run()


if __name__ == "__main__":
    main()
