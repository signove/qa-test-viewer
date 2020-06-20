# -*- coding: utf-8 -*-
import time
import os
import notify2
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key
import pyautogui, sys
import rpchecker as checker

print('######  Record-Playback Tool   #########')
print('# Press F2 to capture the test result  #')
print('# Press ESC to quit                    #')
print('########################################')

mode = ''
filename = ''
testname = ''
checker.rpConfig()
tstFolder = '{0}/tests/{1}'.format(os.getcwd(), checker.rpWorkspace())
stopped = False
dragStart = (0, 0)
dragEnd = (0, 0)
hotkeys = []


def stop():
    global stopped
    stopped = True
    checker.stop()


def notify(message):
    ICON_PATH = '{0}/tl.png'.format(os.getcwd())
    notify2.init("RpTool Notifier")
    n = notify2.Notification(None, icon=ICON_PATH)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(5000)
    n.update('RpTool - Testing {0}'.format(testname), message)
    n.show()

def getImgFileName():
    return filename.replace('.txt', '.png')

def createDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def specialKey(key):
    global hotkeys
    args = key.split('.')
    if args[1] in ['ctrl', 'shift', 'alt']:
        hotkeys.append(args[1])
    elif len(args) == 2:
        pyautogui.press(args[1])
    else:
        print('Ignored key {0}'.format(key))

def click(x, y, time):
    pyautogui.moveTo(x, y, time)
    pyautogui.click()

def record(action):
    global filename
    try:
        outputFile = open(filename, 'a')
        outputFile.write(action)
        outputFile.write('\n')
        outputFile.close()
    except:
        print('Error opening file {0}'.format(filename))

def hotkeyHandler():
    global hotkeys
    if len(hotkeys) == 2:
        print('hotkey {0}+{1}'.format(hotkeys[0], hotkeys[1]))
        pyautogui.hotkey(hotkeys[0], hotkeys[1])
        hotkeys = []
    elif len(hotkeys) == 3:
        print('hotkey {0}+{1}+{2}'.format(hotkeys[0], hotkeys[1], hotkeys[2]))
        pyautogui.hotkey(hotkeys[0], hotkeys[1], hotkeys[2])
        hotkeys = []

def clickHandler(cmd, args):
    x = int(args[1])
    y = int(args[2])
    time = int(args[3])
    click(x, y, time)
    print('{0} {1} {2} {3}'.format(cmd, x, y, time))

def keyHandler(args):
    global hotkeys

    key = args[1]
    if len(key) == 1:
        # if key == '@':
        #    pyautogui.hotkey('shift', '2')
        if key == '/':
            pyautogui.press('divide')
        if len(hotkeys) > 0:
            hotkeys.append(key)
            hotkeyHandler()
        else:
            pyautogui.typewrite(key, 0.1)
        print('key {}'.format(key))
    else:
        print('special key {}'.format(key))
        specialKey(key)


# args = ['scroll', 'up/down', 'dx', 'dy' ]
def scrollHandler(args):
    direction = args[1]
    dy = args[3]
    pyautogui.scroll(dy)  # up/down


# args = ['drag', x1, y2, x2, y2]
def dragHandler(args):
    x1 = int(args[1])
    y1 = int(args[2])
    x2 = int(args[3])
    y2 = int(args[4])
    print('drag from {0} {1} to {2} {3}'.format(x1, y1, x2, y2))
    pyautogui.dragTo(x2, y2, 1, button='left')


def execute(actions):
    global stopped
    notify('Playback test {}'.format(testname))
    for action in actions:
        if stopped == True:
            notify('Stoping test {}!'.format(testname))
            break
        args = action.split(' ')
        cmd = args[0]
        if cmd == 'click':
            clickHandler(cmd, args)
        elif cmd == 'check':
            checker.rpResult(getImgFileName())
        elif cmd == 'key':
            keyHandler(args)
        elif cmd == 'scroll':
            scrollHandler(args)
        elif cmd == 'drag':
            dragHandler(args)
        else:
            print('Invalid action {}'.format(cmd))


def on_click(x, y, button, pressed):
    global startTime
    global endTime
    global duration
    global dragStart
    global stopped
    endTime = time.time()
    duration = int(endTime - startTime)
    startTime = endTime
    if pressed:
        dragStart = (x, y)
        print('click at {0} {1} {2}'.format(x, y, duration))
        record('click {0} {1} {2}'.format(x, y, duration))
    else:
        x1 = dragStart[0]
        y1 = dragStart[1]
        x2 = dragEnd[0]
        y2 = dragEnd[1]
        if x1 != x2 and y1 != y2:
            if not stopped:
                record('drag {0} {1} {2} {3}'.format(x1, y1, x2, y2))
                print('drag from {0} to {1}'.format(dragStart, dragEnd))


def on_move(x, y):
    global dragEnd
    dragEnd = (x, y)


def on_press(key):
    try:
        print('press {0}'.format(key.char))
        record('key {0}'.format(key.char))
    except AttributeError:
        record('key {0}'.format(key))


def on_scroll(x, y, dx, dy):
    print('scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
    if dy < 0:
        record('scroll down {0} {1}'.format(dx, dy))
    else:
        record('scroll up {0} {1}'.format(dx, dy))


def on_release(key):
    global stopped
    print('released mouse')
    try:
        print('release key {0}'.format(key))
        if key == Key.f2:
            stopped = True
            checker.rpCapture(getImgFileName())
            record('check {0}'.format(getImgFileName()))
            stopped = False
        if key == Key.esc:
            return False  # stop
    except:
        print('special key {0}'.format(key))


def playMode():
    try:
        with open(filename) as tstFile:
            actions = []
            for line in tstFile:
                action = line.replace('\n', '')
                actions.append(action)
            execute(actions)
    except FileNotFoundError as err:
        print('Error {}'.format(err))


def recMode():
    notify('Recording...')
    with MouseListener(on_click=on_click, on_scroll=on_scroll, on_move=on_move) as listener:
        with KeyboardListener(on_press=on_press, on_release=on_release) as listener:
            listener.join()


def delMode():
    print('Deleting file {}'.format(filename))
    if os.path.exists(filename):
        os.remove(filename)
        os.remove(getImgFileName())
    else:
        print('File {} does not exist.'.format(filename))


def listFiles():
    global tstFolder
    files = []
    # r-root, d-directory, f-file
    for r, d, f in os.walk(tstFolder):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    for f in files:
        print(f)
    return files


def listMode():
    global tstFolder
    checker.rpConfig()
    tstFolder = '{0}/tests/{1}'.format(os.getcwd(), checker.rpWorkspace())
    return listFiles()


def listRoutines():
    global tstFolder
    tstFolder = '{0}/tests/routines'.format(os.getcwd())
    return listFiles()


def start(testname, mode):
    global stopped
    global startTime
    global filename
    global tstFolder
    stopped = False
    startTime = time.time()
    checker.setTestName(testname)
    if ".txt" in testname:
        testname = testname.replace('.txt', '')

    if mode in ['rec', 'play', 'del', 'list']:
        createDir(tstFolder)
        filename = '{0}/{1}.txt'.format(tstFolder, testname)
    elif mode in ['rec-free', 'play-free', 'del-free', 'list-free']:
        tstFolder = '{0}/tests/routines'.format(os.getcwd())
        createDir(tstFolder)
        filename = '{0}/{1}.txt'.format(tstFolder, testname)
    else:
        print('mode unknow {}'.format(mode))

    print('Started mode={0} file={1}'.format(mode, filename))
    try:
        if mode in ['rec', 'rec-free']:
            recMode()
        elif mode in ['play', 'play-free']:
            playMode()
        elif mode in ['del', 'del-free']:
            delMode()
        elif mode in ['list', 'list-free']:
            listMode()
        else:
            print('Unknow mode {0}, try rec, play, rec-free or play-free'.format(mode))
    except KeyboardInterrupt:
        print('\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Error too few arguments, expected 02 arguments: Mode TestCaseName')
    else:
        mode = sys.argv[1]
        testname = sys.argv[2]
        start(testname, mode)
