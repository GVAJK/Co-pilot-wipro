import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;

import org.junit.Test;
import org.mockito.Mockito;

public class SomeServiceTest {

    @Test
    public void testGet() {
        // Create a mock repository
        SomeRepository mockRepository = Mockito.mock(SomeRepository.class);

        // Define the behavior of the mock
        when(mockRepository.get("someId")).thenReturn("someData");

        // Create the service, passing the mock repository as a dependency
        SomeService service = new SomeService(mockRepository);

        // Call the method under test
        String result = service.get("someId");

        // Verify the result
        assertEquals("someData", result);
    }
}