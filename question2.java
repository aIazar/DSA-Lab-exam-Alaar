import java.util.Stack;
class stack{
    public static void main(String[] args) {
        Stack<String> cars = new Stack<String>();
        cars.push("toyota");
        cars.push("nissan");
        cars.push("land rover");
        System.out.println(cars);

        cars.pop(); // This time land rover is removed
        cars.pop(); // This time nissan is removed
        System.out.println(cars);

    }
}