import java.io.*;
import java.nio.file.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ChatServlet extends HttpServlet {
    private static final String FILE_PATH = "../data/chatlog.txt";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/plain");
        PrintWriter out = response.getWriter();
        String chatLog = new String(Files.readAllBytes(Paths.get(FILE_PATH)));
        out.println(chatLog);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String message = request.getParameter("message");
        if (message != null && !message.trim().isEmpty()) {
            LocalDateTime now = LocalDateTime.now();
            DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            String timestamp = dtf.format(now);
            String chatEntry = timestamp + " - " + message + "\n";
            Files.write(Paths.get(FILE_PATH), chatEntry.getBytes(), StandardOpenOption.CREATE, StandardOpenOption.APPEND);
        }
        doGet(request, response);
    }
}
