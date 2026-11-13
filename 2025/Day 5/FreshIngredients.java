import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

public static final String PATH = "input.txt";

protected record RangesAndIDs(List<long[]> Ranges, List<Long> IDs) {}

public static class FreshIngredients{

    protected String readFile(String path){
        Path filePath = Path.of(path);

        try {
            return Files.readString(filePath);
        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    protected RangesAndIDs getRangesAndIDs(String fileContents){

        List<long[]> Ranges = new ArrayList<>();
        List<Long> IDs = new ArrayList<>();

        String[] Unpacked = fileContents.split("\r\n");

        int i = 0;
        do {

            long[] Range = Arrays.stream(Unpacked[i].split("-"))
                    .mapToLong(Long::parseLong)
                    .toArray();
            Ranges.add(Range);
            i++;
        }while (!Unpacked[i].isEmpty());

        i++;

        while(i < Unpacked.length){

            IDs.add(Long.parseLong(Unpacked[i]));

            i++;
        }

        return new RangesAndIDs(Ranges,IDs);

    }

    protected List<long[]> MergeIntervals(List<long[]> Ranges){

        Ranges.sort(Comparator.comparingLong(Range -> Range[0]));

        List<long[]> MergedIntervals = new ArrayList<>();
        long[] toAdd = Ranges.getFirst().clone();

        for (int i = 1 ; i < Ranges.size() ; i++){
            if (Ranges.get(i)[0] <= toAdd[1]){
                toAdd[1] = Long.max(toAdd[1], Ranges.get(i)[1]);
            }
            else{
                MergedIntervals.add(toAdd);
                toAdd = Ranges.get(i).clone();
            }
        }

        MergedIntervals.add(toAdd);
        return MergedIntervals;
    }

    protected int CountFreshIngredients(List<long[]> MergedIntervals, List<Long> IDs){

        int totalFreshIngredients = 0;
        int idIndex = 0;
        int intervalIndex = 0;

        Collections.sort(IDs);

        while (idIndex < IDs.size() && intervalIndex < MergedIntervals.size()) {

            if (IDs.get(idIndex) <= MergedIntervals.get(intervalIndex)[1]) {
                if (IDs.get(idIndex) >= MergedIntervals.get(intervalIndex)[0]) {
                    totalFreshIngredients++;
                }
                idIndex++;
            } else {
                intervalIndex++;
            }
        }
        return totalFreshIngredients;
    }

    protected long SumIntervalsLengths(List<long[]> MergedIntervals){

        long total = 0;

        for (long[] Interval : MergedIntervals){
            total += Interval[1] - Interval[0] + 1;
        }

        return total;
    }

    public FreshIngredients(String path) {
        String fileContents = readFile(path);

        RangesAndIDs fileRecord = getRangesAndIDs(fileContents);
        List<long[]> Ranges = fileRecord.Ranges();
        List<Long> IDs = fileRecord.IDs();

        List<long[]> MergedIntervals = MergeIntervals(Ranges);

        System.out.println("The total amount of fresh ingredients is: " + CountFreshIngredients(MergedIntervals, IDs));
        System.out.println("The total sum of ingredient ID ranges consider to be fresh is " + SumIntervalsLengths(MergedIntervals));

    }
}

void main() {
     FreshIngredients fe = new FreshIngredients(PATH);
}