public class Solution {
	private static long startTime = 0;
	private static long endTime = 0;

	public static void start() {
		startTime = System.currentTimeMillis();
	}

	public static void end() {
		endTime = System.currentTimeMillis();
	}

	public static void countTime() {
		System.out.println("Spent time is " + (endTime-startTime) + "ms");
		startTime = 0;
		endTime = 0;
	}
	
}
