import comtypes
from pycaw.constants import CLSID_MMDeviceEnumerator
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, IMMDeviceEnumerator
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import time

# Initialize the COM library for the current thread
comtypes.CoInitialize()

def adjust_mic_volume():
    # Get the enumerator for the audio devices
    enumerator = comtypes.CoCreateInstance(
        CLSID_MMDeviceEnumerator,
        IMMDeviceEnumerator,
        comtypes.CLSCTX_INPROC_SERVER
    )
    # Get the collection of active audio capture (microphone) devices
    mics = enumerator.EnumAudioEndpoints(1, 1)  # 1 for capture devices, 1 for active devices only
    count = mics.GetCount()
    for i in range(count):
        # Get the specific capture device
        mic = mics.Item(i)
        # Activate the IAudioEndpointVolume interface
        interface = mic.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Get the current volume level as a scalar
        current_level = volume.GetMasterVolumeLevelScalar()
        print(f"Current volume of device {i}: {current_level * 100}%")
        # If the volume drops below 95%, set it back to 100%
        if current_level < 0.95:
            print(f"Increasing volume of device {i} to 100%")
            volume.SetMasterVolumeLevelScalar(1.0, None)

while True:
    adjust_mic_volume()
    time.sleep(3)  # Check every second