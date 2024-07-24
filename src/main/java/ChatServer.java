import javax.websocket.*;
import javax.websocket.server.ServerEndpoint;
import java.io.*;
import java.nio.file.*;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

@ServerEndpoint("/chat")
public class ChatServer {
    private static final Set<Session> sessions = Collections.synchronizedSet(new HashSet<>());
    private static final Path chatFile = Paths.get("src/main/resources/chat.txt");

    static {
        try {
            if (!Files.exists(chatFile)) {
                Files.createFile(chatFile);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @OnOpen
    public void onOpen(Session session) throws IOException {
        sessions.add(session);
        session.getBasicRemote().sendText(new String(Files.readAllBytes(chatFile)));
    }

    @OnMessage
    public void onMessage(String message, Session session) throws IOException {
        Files.write(chatFile, (message + "\n").getBytes(), StandardOpenOption.APPEND);
        synchronized (sessions) {
            for (Session s : sessions) {
                if (s.isOpen()) {
                    s.getBasicRemote().sendText(message);
                }
            }
        }
    }

    @OnClose
    public void onClose(Session session) {
        sessions.remove(session);
    }
}
