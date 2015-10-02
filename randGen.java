import java.util.*;
 
public class randGen{
	 public static int get_next_rand(double lambda ){
		Random r = new Random();
		double u = r.nextDouble()  ;
//		System.out.println("rand no:"+ u);
//		System.out.println("Math log is "+(Math.log(1 -u) ));
//		System.out.println("lambda"+lambda);
		int rand_no = (int) ((Math.log(1 - u ))/(-lambda)) ;
		System.out.println("rand wait time ="+(rand_no));
	    return rand_no ;
	}
	public static void main(String[] args){
		for(int i=0;i<1000 ;i++){
			int rand_val = get_next_rand((double)1/80);
		//	System.out.println("Rand number gene is :"+get_next_rand(5));
		}
	}
}
