"""Example program to show how to read a multi-channel time series from LSL."""

from time import sleep
from pylsl import StreamInlet, resolve_stream
from write_data import write_data

def main():
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    LENGTH = 3000

    collected_data = list()
    i = 0
    label = 0

    while True:
        element = list()
        sample, _ = inlet.pull_sample()
        sample.pop(0)
        sample.pop(0)
        sample.pop(0)
        sample.pop(-1)
        sample.pop(-1)
        element.append(sample)
        element.append(label)
        collected_data.append(element)
        i += 1
        print(i)
        # sleep(0.001)
        if (i > LENGTH):
            key = input("Press any key to continue... (press q to stop)")
            if (key == 'q'):
                break
            label += 1
            i = 0

    print(f"Generated {LENGTH} elements for {label + 1} labels.")
    print("They are available in ../models/realTimeData.csv")
    write_data(data=collected_data, path="../models/realTimeData.csv")
    

if __name__ == '__main__':
    main()