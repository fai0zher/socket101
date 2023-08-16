import java.io.*;
public class testPrintWriter{
	public static void main(String[] args) {
	try{
			String msg = "nigga";
			File h = new File("test1.txt");
			File f = new File("test2.txt");

			PrintWriter pout = new PrintWriter(f);
		
			pout.println(msg);
			pout.println("hello dudue");
			pout.flush(); // save content with .flush()

			pout = new PrintWriter(h);
			pout.print("I  fuck YOU ");

			pout.flush();
			pout.close(); 



	}catch(Exception e){e.printStackTrace();}
	}
}