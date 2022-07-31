import datetime
import os

from pylsl import StreamInlet, resolve_stream
from write_data import write_data

LENGTH = 3000


def record_eeg():
    print('Looking for an EEG stream...')
    streams = resolve_stream('type', 'EEG')
    inlet = StreamInlet(streams[0])

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
        if i > LENGTH:
            key = input('Press any key to continue... (press q to stop)')
            if key == 'q':
                break
            label += 1
            i = 0

    path = str(datetime.datetime.now()).replace(' ', '').replace('-', '').replace(':', '').replace('.', '')
    path = '../records/' + path + '.csv'

    print(f'Generated {LENGTH} elements for {label + 1} labels.')
    print('They are available in %s' % path)
    os.mkdir('../records') if not os.path.exists('../records') else None
    write_data(data=collected_data, path=path)
    return path
