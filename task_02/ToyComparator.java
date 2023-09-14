import java.util.Comparator;

public class ToyComparator implements Comparator<Toy> {

    @Override
    public int compare(Toy toy1, Toy toy2) {
        return toy2.getLikelihood() - toy1.getLikelihood();
    }
}
