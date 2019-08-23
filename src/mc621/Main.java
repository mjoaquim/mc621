package mc621;
import java.util.Scanner;
import java.math.*;

import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.lang.Math;
public class Main {
	public static void main(String[] args) {
		 Scanner ent = new Scanner(System.in);
		 int n = ent.nextInt();
		 while(n>0) {
			 int n1 = ent.nextInt();
			 int n2 = ent.nextInt();
			 ArrayList<Integer> l1 = new ArrayList<>();
			 ArrayList<Integer> l2 = new ArrayList<>();
			 
			 while(n1 > 0){
				l1.add(ent.nextInt());
				n1--;
			 }
			 while(n2 > 0){
				l2.add(ent.nextInt());
				n2--;
			 }	
			 l1.sort(null);
			 l2.sort(null);

			int p1 = 0;
            int p2 = 0;
            int r = 0;
            while (p1 < l1.size() && p2 < l2.size()) {
                if (l1.get(p1) == l2.get(p2)) {
                    p1++;
                    p2++;
                } else if (l1.get(p1) < l2.get(p2)) {
                    p1++;
                    r++;
                } else {
                    p2++;
                    r++;
                }
            }
            if (p1 < l1.size()) {
                r += l1.size() - p1;
            } else {
                r += l2.size() - p2;
            }
            System.out.println(r);
			
			 
		 }

	}

}
