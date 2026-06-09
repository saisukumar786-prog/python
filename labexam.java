// a,b,c Answer - Full Java Code

// Base class
class Printer {

    // Method Overloading
    void printMessage() {
        System.out.println("Printing default message");
    }

    void printMessage(String msg) {
        System.out.println("Printing: " + msg);
    }

    void printMessage(String msg, int times) {
        for (int i = 1; i <= times; i++) {
            System.out.println(msg);
        }
    }
}

// Derived class 1
class RegularPrinter extends Printer {

    // Method Overriding
    void printMessage(String msg) {
        System.out.println("Regular Printer: " + msg);
    }
}

// Derived class 2
class LaserPrinter extends Printer {

    // Method Overriding
    void printMessage(String msg) {
        System.out.println("Laser Printer: " + msg);
    }
}

// Main class
public class PrinterDemo {
    public static void main(String[] args) {

        // a) Different ways depending on inputs
        Printer p = new Printer();
        p.printMessage();
        p.printMessage("Hello");
        p.printMessage("Welcome", 3);

        System.out.println("----------------");

        // b) Different printer types
        Printer p1 = new RegularPrinter();
        Printer p2 = new LaserPrinter();

        p1.printMessage("Document");
        p2.printMessage("Document");

        System.out.println("----------------");

        // c) Same function name in same class
        p.printMessage("Same name methods = Overloading");
    }
}