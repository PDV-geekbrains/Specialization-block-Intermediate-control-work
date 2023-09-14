import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class Program {
    public static void main(String[] args) {
        // #region Инициализация
        String path = "Toys.txt";
        int[] ids = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        String[] names = new String[] { "конструктор", "робот",
                "кукла", "машина", "дом", "чебурашка", "грабли",
                "паровоз", "погремушка" };
        int[] likelihoods = new int[] { 1, 2, 2, 3, 2, 6, 1, 3, 4 };
        // #endregion

        PriorityQueue<Toy> queueOfToys = getQueueOfToys(ids, names, likelihoods);
        List<Toy> listOfToys = getListOfToys(queueOfToys);
        saveToFile(path, listOfToys);
    }

    /**
     * Метод создаёт объекты "Toy" выбирая значения из исходных массивов, а
     * затем формирует из этих объектов упорядоченную очередь. Массивы должны
     * быть одинаковой длины.
     * 
     * @param ids         Массив идентификаторов.
     * @param names       Массив названий.
     * @param likelihoods Массив вероятностей.
     * @return Упорядоченная очередь объектов "Toy".
     */
    private static PriorityQueue<Toy> getQueueOfToys(
            int[] ids, String[] names, int[] likelihoods) {
        PriorityQueue<Toy> queue = new PriorityQueue<Toy>(new ToyComparator());
        for (int i = 0; i < names.length; i++) {
            Toy toy = new Toy(ids[i], names[i], likelihoods[i]);
            queue.add(toy);
        }
        return queue;
    }

    /**
     * Вспомогательный метод. Переводит очередь объектов с список объектов.
     * 
     * @param queue Упорядоченная очередь объектов Toy.
     * @return Упорядоченный список объектов Toy.
     */
    private static List<Toy> getListOfToys(PriorityQueue<Toy> queue) {
        List<Toy> result = new ArrayList<Toy>();
        for (int i = 0; i < 10; i++) {
            Toy toy = queue.poll();
            result.add(toy);
        }
        return result;
    }

    /**
     * Метод сохраняет список в файл. Каждый объект записывается с новой строки.
     * 
     * @param path Путь к файлу.
     * @param list Список подлежащий сохранению.
     */
    private static void saveToFile(String path, List<Toy> list) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(path))) {
            for (Toy toy : list) {
                writer.write(String.format("вероятность: %d, id: %d, название: %s\n",
                        toy.getLikelihood(), toy.getId(), toy.getName()));
            }
        } catch (Exception e) {
            e.getMessage();
        }
    }
}
