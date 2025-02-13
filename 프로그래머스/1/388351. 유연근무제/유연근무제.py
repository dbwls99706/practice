def solution(schedules, timelogs, startday):
    answer = 0
    week = []
    for i in range(7):
        if (startday - 1 + i) % 7 < 5:
            week.append(i)
            
    
    for i in range(len(schedules)):
        latest_time = schedules[i] + 10
        if (latest_time%100)>=60:
            latest_time = (latest_time // 100 + 1) * 100 + (latest_time % 100 - 60)
            
        late=True
        
        for j in week:
            if timelogs[i][j] > latest_time:
                late=False
                break;
        if late:
            answer+=1
            
    return answer
