import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String filePath = sc.nextLine();
        sc.close();

        int chars = 0;
        int words = 0;
        int lines = 0;
        HashMap<Character, Integer> charFrequencies = new HashMap<>();
        HashMap<String, Integer> wordsFrequencies = new HashMap<>();
        try {
            Scanner fileSc = new Scanner(new File(filePath));
            while(fileSc.hasNextLine()){
                String line = fileSc.nextLine();
                lines++;

                for(int i = 0 ; i < line.length(); i++){
                    chars++;
                    char character = line.charAt(i);
                    if(charFrequencies.containsKey(character)){
                        charFrequencies.put(character, charFrequencies.get(character) + 1);
                    }
                    else {
                        charFrequencies.put(character, 1);
                    }
                }
                String[] wordsInLine = line.split(" ");
                for(String word: wordsInLine){
                    words++;
                    if(wordsFrequencies.containsKey(word)){
                        wordsFrequencies.put(word, wordsFrequencies.get(word) + 1);
                    }
                    else{
                        wordsFrequencies.put(word, 1);
                    }
                }
            }

        } catch (FileNotFoundException e) {
            System.out.println("File not found:" + filePath);
            System.exit(1);
        }

        Character charMostUsed = null;
        int mostUsedFrequency = 0;
        for (Character character : charFrequencies.keySet()) {
            if (charFrequencies.get(character) > mostUsedFrequency) {
                charMostUsed = character;
                mostUsedFrequency = charFrequencies.get(character);
            }
        }
        String mostUsedWord = null;
        int mostUsedFrequencyWord = 0;
        for(String word: wordsFrequencies.keySet()){
            if(wordsFrequencies.get(word) > mostUsedFrequencyWord){
                mostUsedWord = word;
                mostUsedFrequencyWord = wordsFrequencies.get(word);
            }
        }

        String filePathTsv = filePath.replace("\\", "\\\\");
        String stringTsv = filePathTsv + "\t" + 
        chars + "\t" + 
        words + "\t" + 
        lines + "\t" + 
        charMostUsed + "\t" + 
        mostUsedWord + "\t" + 
        mostUsedFrequency + "\t"+ 
        mostUsedFrequencyWord;
        System.out.println(stringTsv);
    }
}