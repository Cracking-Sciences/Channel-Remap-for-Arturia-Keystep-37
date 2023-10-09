#name=Arturia Keystep 37 Channel Map

'''
Presented by Cracking Sciences 
'''

import transport



def event_print(event):
    print(f"handled {event.handled},\
        timestamp {event.timestamp},\
        status {event.status},\
        data1 {event.data1},\
        data2 {event.data2},\
        port {event.port},\
        note {event.note},\
        velocity {event.velocity},\
        pressure {event.pressure},\
        progNum {event.progNum},\
        controlNum {event.controlNum},\
        controlVal {event.controlVal},\
        midiId {event.midiId},\
        midiChan {event.midiChan}")

BUTTON_RECORD = 0x32
BUTTON_STOP = 0x33
BUTTON_PLAY = 0x36

def OnMidiMsg(event):
    pass
    # event_print(event)

def OnControlChange(event):
    event.handled = False
    if event.data1 == BUTTON_RECORD:
        # print(f'{"Disabled" if transport.isRecording() else "Enabled"} recording')
        transport.record()
        event.handled = True
    elif event.data1 == BUTTON_STOP and event.data2 > 0:
        # print('Stopped playback')
        transport.stop()
        event.handled = True
    elif event.data1 == BUTTON_PLAY and event.data2 > 0:
        # print(f'{"Paused" if transport.isPlaying() else "Started"} playback')
        transport.start()
        event.handled = True
    else:
        # Mod Strip and Knobs
        event.status -= event.midiChan
        event.midiChan = 0
    # event_print(event)
def OnPitchBend(event):
    # Pitch Strip
    event.handled = False
    event.status -= event.midiChan
    event.midiChan = 0
    # event_print(event)

def OnChannelPressure(event):
    # Channel Aftertouch
    event.handled = False
    event.status -= event.midiChan
    event.midiChan = 0
    # event_print(event)

# csric | 2023