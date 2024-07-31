import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class DisplayDataServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("application/json");
        PrintWriter out = response.getWriter();

        // Path to your text file
        String filePath = "ChatToAll/src/main/resources/chat.txt";

        // Read the data from the text file
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;
        StringBuilder data = new StringBuilder();
        while ((line = reader.readLine()) != null) {
            data.append(line).append("\\n");
        }
        reader.close();

        // Return the data as JSON
        out.println("{\"data\":\"" + data.toString() + "\"}");
    }
}
