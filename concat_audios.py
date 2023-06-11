import os
import glob


def concat_audios(lis, file_location):
    st = ["ffmpeg"]
    for i in range(len(lis)):
        st.append("-i")
        st.append(lis[i])
    st.append("-filter_complex")
    st = ' '.join(st) + " "
    for i in range(len(lis)):
        st = st + "[" + str(i) + ":0]"

    st = st + "concat=n=" + str(len(lis)) + ":v=0:a=1[out] -map [out] " + file_location
    print(st)

    # try:
        # os.remove(file_location)
    # except:
    #     pass
    # os.system(st)


if __name__ == '__main__':

    lst = glob.glob("./audios/*")

    concat_audios(lst, ".")
