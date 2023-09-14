
/** Класс описывает сущность Игрушка. */
public class Toy {
    private int id;
    private String name;
    private int likelihood;

    public Toy(int id, String name, int likelihood) {
        this.id = id;
        this.name = name;
        this.likelihood = likelihood;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getLikelihood() {
        return likelihood;
    }
}