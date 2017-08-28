package Week2;

import java.util.ArrayList;
import java.util.List;

import DataStructures.Interval;

public class insertIntervals {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        
		List<Interval> result = new ArrayList<Interval>();
		int counter = 0;
		
		/*add all non conflicting intervals first : 
		i.e. intervals whose end times are before newInterval's start time*/
		for(int i=0;i<intervals.size();i++){
			if(intervals.get(i).end<newInterval.start){
				result.add(intervals.get(i));
				counter++;
			}
			
		}
		
		//now merge overlapping intervals
		while(counter<intervals.size() && intervals.get(counter).start<=newInterval.end){
			newInterval = new Interval(Math.min(newInterval.start, intervals.get(counter).start),
					Math.max(newInterval.end, intervals.get(counter).end));
			counter++;
		}
		
		result.add(newInterval);
		
		//add rest of the non overlapping intervals
		while(counter<intervals.size()){
			result.add(intervals.get(counter));
			counter++;
		}
		return result;
    }
}
