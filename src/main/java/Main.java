import org.apache.catalina.startup.Tomcat;

public class Main {
    public static void main(String[] args) throws Exception {
        // Create a Tomcat instance
        Tomcat tomcat = new Tomcat();
        tomcat.setPort(8080);

        // Add a web application context
        tomcat.addWebapp("", new java.io.File("src/main/webapp").getAbsolutePath());

        // Start the server
        tomcat.start();
        tomcat.getServer().await();
    }
}
