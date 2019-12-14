class Nester:
    @staticmethod
    def __validate(source_data, nesting_levels):
        pass

    @staticmethod
    def nest(source_data, nesting_levels):
        Nester.__validate(source_data, nesting_levels)
        output = {}
        for data in source_data:
            nested_dict = output
            for nesting_level in nesting_levels:
                data_nesting_level = data.pop(nesting_level)  # minimise lookups
                if nesting_level != nesting_levels[-1]:
                    if data_nesting_level not in nested_dict:
                        nested_dict[data_nesting_level] = {}
                    nested_dict = nested_dict[data_nesting_level]
                else:  # final nesting
                    if data_nesting_level in nested_dict:
                        nested_dict[data_nesting_level].append(data)
                    else:
                        nested_dict[data_nesting_level] = [data]
        return output

    @staticmethod
    def nest_json(source_data, nesting_levels):
        pass
