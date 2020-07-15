class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a_hour = ((360 * (hour % 12) / 12) + ((360 / 12) * minutes / 60))
        a_minutes = (360 * minutes / 60)
        
        diff = (a_minutes - a_hour)
        if diff < 0:
            diff += 360
            
        return min(diff, 360-diff)