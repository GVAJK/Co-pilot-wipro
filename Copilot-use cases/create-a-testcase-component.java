import com.visualpathit.account.beans.Components;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ComponentsTest {

    private Components components;

    @BeforeEach
    public void setUp() {
        components = new Components();
    }

    @Test
    public void testActiveHost() {
        String host = "localhost";
        components.setActiveHost(host);
        assertEquals(host, components.getActiveHost());
    }

    @Test
    public void testActivePort() {
        String port = "8080";
        components.setActivePort(port);
        assertEquals(port, components.getActivePort());
    }

    // Add similar tests for the rest of the fields

    @Test
    public void testRabbitMqHost() {
        String host = "localhost";
        components.setRabbitMqHost(host);
        assertEquals(host, components.getRabbitMqHost());
    }

    @Test
    public void testRabbitMqPort() {
        String port = "5672";
        components.setRabbitMqPort(port);
        assertEquals(port, components.getRabbitMqPort());
    }

    // Continue with the rest of the fields...
}
