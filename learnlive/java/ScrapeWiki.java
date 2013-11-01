/** This class will scrape wikipedia
 */

import java.util.*;
import java.io.*;
import java.net.*;

public class ScrapeWiki {

    public void scrape() {
        Queue<String> urls = new LinkedList<String>();
        String startingUrl = "http://en.wikipedia.org/wiki/Category:Cooking";
        urls.add(startingUrl);
        while (!urls.isEmpty()) {
            // read in the url and parse out the relevant links
            // print current node
            String url = urls.remove();
            System.out.println(url);

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

        if (endIndex == -1 || startIndex == -1) return;

        String relevantSubstring = page.substring(startIndex, endIndex);

        int location = relevantSubstring.indexOf(" href=\"");
        while (location != -1) {
            location += 7;
            int locationOfQuotation = relevantSubstring.indexOf("\"", location);
            String link = relevantSubstring.substring(location, locationOfQuotation);
            String url = "http://en.wikipedia.org" + link;
            if (addToQueue)
                queue.add(url);
            else
            {
                if(url.indexOf("Wikipedia:FAQ") == -1)
                    System.out.println(url);
            }
            location = relevantSubstring.indexOf(" href=\"", locationOfQuotation);
        }
    }


    public static void main(String[] args) {
        // main function to execute the scraping
        ScrapeWiki sc = new ScrapeWiki();
        sc.scrape();
    }
}
