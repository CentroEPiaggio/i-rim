import xlrd

pitch_row_start = 1
pitch_row_end = 69

poster_row_start = 69
poster_row_end = 143

sessions = {
    "DM-I" : ["DM1", "DM2", "DM3"],
    "SP-I" : ["SP1", "SP2"],
    "SM-I" : ["SM1", "SM2", "SM3"],
    "SS-I" : ["SS1", "SS2"]
    }

def get_pitch_sessions(sheet):
    session_list = []

    for i in range (pitch_row_start,pitch_row_end):
        aa = sheet.cell_value(i,7)
        print(aa)
        session_list.append(aa)

    session_list = list(set(session_list))

    print("\n\nTemporary unique session list:")
    print(session_list)

    session_list = [ x for x in session_list if "Q&A" not in x ]
    session_list.pop(0)
    print("\n\nUnique session list:")
    print(session_list)

    for session in session_list:
        print("Element: \n")
        print(session)
        print("\n")

    return session_list

def get_poster_sessions(sheet):
    session_list = []

    for i in range (poster_row_start,poster_row_end):
        aa = sheet.cell_value(i,7)
        session_list.append(aa)

    session_list = list(set(session_list))

    print("\n\nTemporary unique session list:")
    print(session_list)

    session_list = [ x for x in session_list ]
    session_list.pop(0)
    print("\n\nUnique session list:")
    print(session_list)

    for session in session_list:
        print("Element: \n")
        print(session)
        print("\n")

    return session_list

def find_first_session_row(sheet,session):
    for i in range (pitch_row_start,pitch_row_end):
        aa = sheet.cell_value(i,7)
        if session in aa:
            return i

def find_first_poster_row(sheet,session):
    for i in range (poster_row_start,poster_row_end):
        aa = sheet.cell_value(i,7)
        if session in aa:
            return i

def find_last_poster_row(sheet,session):
    k = 0
    for i in range (poster_row_start,poster_row_end):
        aa = sheet.cell_value(i,7)
        if session in aa:
            k = i

    return k

def tex_begin_file(f):
    f.write("\\documentclass{digest}\n")
    f.write("\\begin{document}\n")
    f.write("\\pagestyle{empty}\n")

def tex_end_file(f):
    f.write("\n\\end{document}")


def main():
    print("\n\n\n")

    #input index file
    # Give the location of the file
    loc = ("index.xlsx")

    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    # output file
    f = open('main_digest.tex','w')

    tex_begin_file(f)

    ############ PITCH #############
    session_list = get_pitch_sessions(sheet)

    for session in session_list:
        print("Processing session ", session)
        session_row_start = find_first_session_row(sheet,session)
        session_row_end = session_row_start + 5

        session_title = sheet.cell_value(session_row_start,8)
        print("Session title: ", session_title)

        session_room_date = sheet.cell_value(session_row_start,9)
        print("Session room/date: ", session_room_date)

        session_chair = sheet.cell_value(session_row_start,10)
        print("Session chair: ", session_chair)

        talk_id_list = []
        for talk in range(session_row_start,session_row_end):
            talk_id = sheet.cell_value(talk,0)
            talk_id_list.append(talk_id)
            print("Talk ID: ",talk_id)

        f.write("\\pitch{%s}{%s}{%s}{%s}{%d}{%d}{%d}{%d}{%d}" % (session,session_title,session_room_date,session_chair,talk_id_list[0],talk_id_list[1],talk_id_list[2],talk_id_list[3],talk_id_list[4] ) )
        f.write("\n\n")

    print("\n\n\n")

    ############ POSTER #############
    session_list = get_poster_sessions(sheet)

    for session in session_list:
        print("Processing session ", session)
        session_row_start = find_first_poster_row(sheet,session)
        session_row_end = find_last_poster_row(sheet,session)

        print("Session start: ", session_row_start, ", session end: ", session_row_end)

        session_title = sheet.cell_value(session_row_start,8)
        print("Session title: ", session_title)

        session_room_date = sheet.cell_value(session_row_start,9)
        print("Session room/date: ", session_room_date)

        talk_id_list = []
        for talk in range(session_row_start,session_row_end+1):
            talk_id = sheet.cell_value(talk,0)
            talk_id_list.append(talk_id)
            print("Talk ID: ",talk_id)

        # Add pitches corresponding to this session
        for pitch_session in sessions[session]:
            print("!!!!!!!! ", pitch_session)
            current_session_first_row = find_first_session_row(sheet,pitch_session)
            print("!!!!", current_session_first_row)
            current_session_last_row = current_session_first_row + 5
            for talk in range(current_session_first_row, current_session_last_row):
                talk_id = sheet.cell_value(talk,0)
                talk_id_list.append(talk_id)

        print("###################")
        print(talk_id_list)
        print("###################")

        f.write("\\posterfirst{%s}{%s}{%s}{%d}{%d}{%d}{%d}{%d}" % (session,session_title,session_room_date,talk_id_list[0],talk_id_list[1],talk_id_list[2],talk_id_list[3],talk_id_list[4] ) )
        f.write("\n")

        index = 5
        while index < len(talk_id_list):

            if index == len(talk_id_list) - 1:
                f.write("\\posterone{%d}" % (talk_id_list[index]))
            elif index == len(talk_id_list) - 2:
                f.write("\\postertwo{%d}{%d}" % (talk_id_list[index], talk_id_list[index+1]))
            elif index == len(talk_id_list) - 3:
                f.write("\\posterthree{%d}{%d}{%d}" % (talk_id_list[index], talk_id_list[index+1], talk_id_list[index+2]))
            elif index == len(talk_id_list) - 4:
                f.write("\\posterfour{%d}{%d}{%d}{%d}" % (talk_id_list[index], talk_id_list[index+1], talk_id_list[index+2], talk_id_list[index+3]))
            elif index == len(talk_id_list) - 5:
                f.write("\\posterfive{%d}{%d}{%d}{%d}{%d}" % (talk_id_list[index], talk_id_list[index+1], talk_id_list[index+2], talk_id_list[index+3], talk_id_list[index+4]))
            else:
                f.write("\\postersix{%d}{%d}{%d}{%d}{%d}{%d}" % (talk_id_list[index], talk_id_list[index+1], talk_id_list[index+2], talk_id_list[index+3], talk_id_list[index+4], talk_id_list[index+5]))
            f.write("\n")

            index += 6

        f.write("\n\n")

    print("\n\n\n")

    tex_end_file(f)

    f.close()

if __name__ == "__main__":
    main()
