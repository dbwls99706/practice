def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    for i in commands:
        if pos <= op_end and pos >= op_start:
            pos = op_end
        h, m = map(int, pos.split(":"))
        
        if i=="next":
            m += 10
            if m >= 60:
                pos = f"{h+1:02}:{m%60:02}"
            else:
                pos = f"{h:02}:{m:02}"
            if pos > video_len:
                pos = video_len
        if i=="prev":
            m -= 10
            if m >= 0:
                pos = f"{h:02}:{m:02}"
            elif h > 0:
                pos = f"{h-1:02}:{m+60:02}"
            else:
                pos="00:00"
        if pos <= op_end and pos >= op_start:
            pos = op_end
            
    return pos