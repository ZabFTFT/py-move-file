import os


def move_file(command: str) -> None:
    input_command, path_file_in, path_file_out = command.split()

    if input_command != "mv":
        return
    if ("/" or "\\") not in path_file_out:
        os.rename(path_file_in, path_file_out)
        return

    output_directory_file_path = os.path.join(os.getcwd(), path_file_out)
    output_directory_path = os.path.split(output_directory_file_path)[0]
    try:
        if os.path.exists(output_directory_path):
            raise FileExistsError("File already exists!")
    except FileExistsError as e:
        print(e)
    else:
        os.makedirs(output_directory_path)

    with (
        open(path_file_in, "r") as file_in,
        open(output_directory_file_path, "w") as file_out,
    ):
        file_out.write(file_in.read())
    os.remove(path_file_in)
