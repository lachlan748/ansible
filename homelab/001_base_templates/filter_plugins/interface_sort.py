def ios_sort(interfaces):
    if isinstance(interfaces, list):
        return sorted(interfaces, key=normalize_ios_interface)
    elif isinstance(interfaces, dict):
        return sorted(interfaces.items(), key=lambda x: normalize_ios_interface(x[0]))

def normalize_ios_interface(value):
    if isinstance(value, int):
        return value

    order = {
        'Loopback': 0,
        'Port-channel': 1,
        'GigabitEthernet': 2,
    }

    import re
    x = [order.get(re.match('\D*', value).group().lower())]
    x.extend(map(int, filter(None, re.split('\D+', value))))
    return tuple(x)

class FilterModule(object):
    def filters(self):
        return {
            'ios_sort': ios_sort,
        }
