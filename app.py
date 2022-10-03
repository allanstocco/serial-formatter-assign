from flask import Flask, render_template, request


app = Flask(__name__)


def format_serial_number(serial, length):
    # Getting serial clean and capitalized
    s_clear = "".join(serial.upper().split("-"))

    # Using an array to work my string
    new_string = []
    for i in range(0, len(s_clear), length):
        if len(s_clear) % length == 0:
            new_string.append(s_clear[i:i+length])

        else:
            if i == 0:
                new_string.insert(0, s_clear[i])

            i += len(s_clear) % length
            new_string.append(s_clear[i:i+length])

    s_formated = "-".join(new_string)

    # Checking if odd number we must remove a
    if s_formated[-1] == "-":
        s_formated = s_formated[:-1]
        return s_formated
    else:
        return s_formated


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        serial = request.form.get("serial")
        l = request.form.get("length")
        if serial and l is not None:
            res = format_serial_number(str(serial), int(l))
            return render_template("code_generator.html", res=res)
        else:
            return render_template("code_generator.html", err="Fill the fields before submit.")
    return render_template("code_generator.html")
