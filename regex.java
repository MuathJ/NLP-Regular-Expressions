import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class q3
{
    public static void main(String[] args) throws IOException
    {


        String content = new String(Files.readAllBytes(Paths.get("content.txt")));

        Pattern p = Pattern.compile("(?<=(^|[;!?\",.]\\s?))(\\w+\\s?){1,4}(?=\\,)");
        Matcher m = p.matcher(content);
        while ( m.find() )
        {
            if (m.group().length() != 0)
                System.out.println( m.group().trim() );
        }
    }
}

// I defined a sentence as anything that ends with ; or ! or ? or " or , or .
// Phrases ends with , and have a max length of 4 words as per requirements
