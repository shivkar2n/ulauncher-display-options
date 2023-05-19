from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


class XrandrExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        items.append(ExtensionResultItem(icon='images/primary.svg',
                                         name='Primary',
                                         description='Use only laptop display',
                                         on_enter=RunScriptAction('/usr/bin/xrandr --output eDP-1 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI-1 --off')))

        items.append(ExtensionResultItem(icon='images/secondary.svg',
                                         name='Secondary',
                                         description='Use only monitor display',
                                         on_enter=RunScriptAction('/usr/bin/xrandr --output eDP-1 --off --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal')))

        items.append(ExtensionResultItem(icon='images/duplicate.svg',
                                         name='Duplicate',
                                         description='Duplicate picture on both displays',
                                         on_enter=RunScriptAction('xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal')))

        items.append(ExtensionResultItem(icon='images/duplicate.svg',
                                         name='Extend',
                                         description='Extend picture on both displays',
                                         on_enter=RunScriptAction('xrandr --output eDP-1 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal')))

        return RenderResultListAction(items)


if __name__ == '__main__':
    XrandrExtension().run()
