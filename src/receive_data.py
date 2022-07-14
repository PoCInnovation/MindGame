"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream
from write_data import write_data


def main():
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    collected_data = list()
    i = 0
    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        element = list()
        sample, timestamp = inlet.pull_sample()
        sample.pop(0)
        sample.pop(0)
        sample.pop(0)
        sample.pop(-1)
        sample.pop(-1)
        element.append(sample)
        label = 1
        if i > 1000:
            label = 0
        element.append(label)
        collected_data.append(element)
        print(i)
        i += 1
        if i > 2000:
            break

    print(collected_data[0], end="\n\n--------------\n")
    write_data(data=collected_data, path="../models/realTimeData.csv")
    

if __name__ == '__main__':
    main()
