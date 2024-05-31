import math
def make_readable(seconds):
    if seconds < 60:
        if seconds == 0:
            return "00:00:00"
        return f"00:00:{seconds}"
    elif seconds >= 60 and seconds < 3600:
        if seconds % 60 == 0:
            if len(str(seconds // 60)) == 1:
                return f"00:0{seconds // 60}:{seconds % 60}0"
            return f"00:{math.floor(seconds / 60)}:00"
        elif len(str(seconds // 60)) == 1:
            return f"00:0{seconds // 60}:{seconds % 60}"
        return f"00:{seconds // 60}:{seconds % 60}"
    else:
        hours = seconds // 3600
        minutes = (seconds - (hours * 3600)) // 60
        minute = (seconds - (hours * 3600))
        second = minute - minutes * 60 
        if seconds % 3600 == 0: 
            if len(str(seconds // 3600)) == 1:
                return f"0{seconds // 3600}:00:00"
            return f"{seconds // 3600}:00:00"
        
        elif seconds % 3600 != 0:
            if len(str(second)) == 1:
                return f"{seconds // 3600}:{minutes}:0{second}"
            
            elif len(str(hours)) == 1:
                if len(str(minutes)) == 1:
                    if len(str(second)) == 1:
                        return f"0{seconds // 3600}:0{minutes}:0{second}"
                    return f"0{seconds // 3600}:0{minutes}:{second}"
                elif len(str(second)) == 1:
                    return f"0{seconds // 3600}:{minutes}:0{second}"
                
                
                
                return f"0{seconds // 3600}:{minutes}:{second}"
                
            elif len(str(minutes)) == 1:
                if len(str(second)) == 1:
                    return f"{seconds // 3600}:{minutes}:0{second}"
                return f"{seconds // 3600}:0{minutes}:{second}"
                
            return f"{hours}:{minutes}:{second}"
        
print(make_readable(6231))


