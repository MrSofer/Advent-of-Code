import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;


public static final String PATH = "input.txt";

public record Equation(List<Long> factors, char operator){
    long eval(){
        long res = (operator == '+') ? 0 : 1;
        for (long factor: factors) { res = (operator == '+') ? res + factor : res * factor ; }
        return res;
    }

}

public static class MathHomework {

    protected List<String> readFile(String path){
        Path filePath = Path.of(path);

        try {
            return Files.readAllLines(filePath);
        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    protected List<Equation> buildEquations(List<String> fileContents){

        List<String> rows = fileContents.subList(0, fileContents.size() - 1);
        String operators = fileContents.getLast();
        int width = fileContents.stream().mapToInt(String::length).max().orElse(0);

        List<Equation> equations = new ArrayList<>();
        List<Long> currFactors = new ArrayList<>(Collections.nCopies(rows.size(),0L));
        char currOperator = '\0';

        for (int col = 0; col <= width; col++) {

            if (col < operators.length() && operators.charAt(col) != ' ') currOperator = operators.charAt(col);

            boolean hasDigit = false;

            for (int row = 0; row < rows.size(); row++){
                if (col < rows.get(row).length() && Character.isDigit(rows.get(row).charAt(col))){
                    currFactors.set(row,(currFactors.get(row) * 10) + (rows.get(row).charAt(col) - '0'));
                    hasDigit = true;
                }
            }

            if (!hasDigit){
                equations.add(new Equation(currFactors,currOperator));
                currFactors = new ArrayList<>(Collections.nCopies(rows.size(),0L));
            }

        }

        equations.add(new Equation(currFactors,currOperator));

        return equations;
    }

    protected List<Equation> buildCephalopodEquations(List<String> fileContents){

        List<String> rows = fileContents.subList(0, fileContents.size() - 1);
        String operators = fileContents.getLast();
        int width = fileContents.stream().mapToInt(String::length).max().orElse(0);

        List<Equation> equations = new ArrayList<>();
        List<Long> currFactors = new ArrayList<>();
        char currOperator = '\0';

        for (int col = 0 ; col <= width ; col++){

            if (col < operators.length() && operators.charAt(col) != ' ') currOperator = operators.charAt(col);

            long num = 0;
            boolean hasDigit = false;

            for (String row : rows){
                if (col < row.length() && Character.isDigit(row.charAt(col))){
                    num = (num * 10) + (row.charAt(col) - '0');
                    hasDigit = true;
                }
            }

            if (hasDigit) currFactors.add(num);
            else if (!currFactors.isEmpty()){
                equations.add(new Equation(currFactors,currOperator));
                currFactors = new ArrayList<>();
            }
        }
        return equations;
    }

    public MathHomework(String path){

        List<String> fileContents = readFile(path);

        List<Equation> equations = buildEquations(fileContents);

        System.out.println(equations.stream().mapToLong(Equation::eval).sum());


        //System.out.println(CalculateEquations(cephalopodEquations));

        /*for (int i = 0 ; i < equations.factors.size() ; i++){
            System.out.println("factors " + i + " size " + equations.factors.get(i).size());
            for (int j = 0; j < equations.factors.get(i).size(); j++) {
                System.out.println(equations.factors.get(i).get(j) + ",");
            }
        }
        System.out.println("operator size " + equations.operators.size());
        for (int i = 0; i < equations.operators.size(); i++) {
            System.out.println(equations.operators.get(i) + ",");
        }*/

    }

}


void main(){
    MathHomework mathHomework = new MathHomework(PATH);
}