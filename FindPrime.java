public class FindPrime extends Solution {
	public static void bruteForce(int size) {
		System.out.println("Brete Force");
		int[] primes = new int[size];
		int count = 6;

		primes[0] = 2;
		primes[1] = 3;
		primes[2] = 5;
		primes[3] = 7;
		primes[4] = 11;
		primes[5] = 13;
		int next = 17;
		boolean isPrime = true;
		while(count < size){
			for (int i = 0; i < count; i++){
				if (next % primes[i] == 0) {
					//System.out.println(next+" mod "+primes[i]+" is 0");
					isPrime = false;
					break;
				} else {
					//System.out.println(next+"%"+primes[i]+"!=0");
				}
			}

			if(isPrime){
				//System.out.println(count+":"+next);
				primes[count++] = next;
			} else {
				isPrime = true;
			}

			next += 2;
		}

		System.out.println(primes[size-1]);
	}

	//Faster way
	public static boolean isPrime(int n) {
		//1 is not prime
		if (n == 1) return false;
		// 2 and 3
		else if (n < 4) return true;
		// all even
		else if (n % 2 == 0) return false;
		// 5, 7
		else if (n < 9) return true;
		else if (n % 3 == 0) return false;
		else {
			int r = (int)Math.sqrt(n);
			int next = 5;
			while (next <= r){
				//prime is 6k +/-1
				if (n % next == 0) return false;
				if (n % (next+2) == 0) return false;
				next += 6;
			}
			return true;
		}
	}

	public static void answer(int size){
		System.out.println("answer solution");
		int count = 1;
		int candidate = 1;
		while (count < size) {
			candidate+=2;
			if (isPrime(candidate)) count+=1;
		}

		System.out.println(candidate);
	}

	public static void main(String[] args){
		if (args.length != 1){
			System.out.println("Usage: FindPrime [size]");
		}
		int size = Integer.parseInt(args[0]);
		start();
		bruteForce(size);
		end();
		countTime();

		start();
		answer(size);
		end();
		countTime();
	}
}
