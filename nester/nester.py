class Nester:
    @staticmethod
    def nest(source_data, nesting_levels):
        output = {}
        for data in source_data:
            nested_dict = output
            for nesting_level in nesting_levels:
                if nesting_level != nesting_levels[-1]:
                    if data[nesting_level] not in nested_dict:
                        nested_dict[data[nesting_level]] = {}
                    nested_dict = nested_dict[data[nesting_level]]
                else:  # final nesting
                    if data[nesting_level] in nested_dict:
                        nested_dict[data[nesting_level]].append(data)
                    else:
                        nested_dict[data[nesting_level]] = [data]
                data.pop(nesting_level)
        return output
