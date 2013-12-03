/** This class will scrape wikipedia
 */

import java.util.*;
import java.io.*;
import java.net.*;

public class ScrapeWiki {
    private PrintWriter writer; // this is the writer that writes to the file

    public void scrape(String startingUrl, String filename) throws FileNotFoundException {
        writer = new PrintWriter(filename);
        Queue<String> urls = new LinkedList<String>();
        urls.add(startingUrl);
        while (!urls.isEmpty()) {
            // read in the url and parse out the relevant links
            // print current node
            String url = urls.remove();

            int indexOfName = url.indexOf("Category:");
            if (indexOfName == -1) indexOfName = url.indexOf("wiki/") + 5;
            else {
                indexOfName += 9;
            }
            String name = url.substring(indexOfName);
            writer.print("" + name + ": ");

            String page;
            try {
                page = readURLFromString(url);
                enqueueRelevantLinks(urls, page);
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private String readURLFromString(String url) throws IOException {
        URL uri = new URL(url);
        BufferedReader in = new BufferedReader(new InputStreamReader(uri.openStream()));

        StringBuilder outputPage = new StringBuilder();
        String inputLine;
        while ((inputLine = in.readLine()) != null) {
            outputPage.append(inputLine);
        }
        in.close();

        return outputPage.toString();
    }

    private void enqueueRelevantLinks(Queue<String> queue, String page) {
        int startIndex = page.indexOf("mw-subcategories");
        int endIndex = page.indexOf("mw-pages");
        boolean addToQueue = true;

        if (startIndex == -1 && endIndex != -1) {
            // we are at a leaf node, just get all the links in the leaf node
            startIndex = page.indexOf("mw-pages");
            endIndex = page.indexOf("printfooter");
            addToQueue = false;
        } else if (endIndex == -1 && startIndex != -1) {
            endIndex = page.indexOf("printfooter");
        }

        if (endIndex == -1 || startIndex == -1) return; // safety check

        String relevantSubstring = page.substring(startIndex, endIndex);

        int location = relevantSubstring.indexOf(" href=\"");
        while (location != -1) {
            location += 7;
            int locationOfQuotation = relevantSubstring.indexOf("\"", location);
            String link = relevantSubstring.substring(location, locationOfQuotation);

            int indexOfName = link.indexOf("Category:");
            if (indexOfName == -1) indexOfName = link.indexOf("wiki/") + 5;
            else {
                indexOfName += 9;
            }
            String name = link.substring(indexOfName);

            String url = "http://en.wikipedia.org" + link;
            if (addToQueue) {
                queue.add(url);
                writer.print("" + name + " ");
            }
            else
            {
                if(url.indexOf("Wikipedia:FAQ") == -1)
                    writer.print("" + name + " ");
            }
            location = relevantSubstring.indexOf(" href=\"", locationOfQuotation);
        }
        writer.print("; \n");

    }


    public static void main(String[] args) {
        // main function to execute the scraping
        ScrapeWiki sc = new ScrapeWiki();
        String startingUrl = "http://en.wikipedia.org/wiki/Category:Articles";
        String category = "wiki.txt";
        try {
            sc.scrape(startingUrl, category);
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
