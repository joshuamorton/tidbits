public class TicTacToe
{

    public static void main(String[] args)
    {
        System.out.prntln("Welcome to the game of Tic Tac Toe!");
        TicTacToe.printBoard(boardState);
    }
    private static void printBoard( List boardState, String[] args)
    {
        int listLength = boardState.size();
        for (x = 0; x < listLength; x = x + 1) {
            System.out.prntln("-------");
            System.out.prntln("\n");
            int smallListLength = boardState.get(x).size();
            for (y = 0; y < smallListLength; y = y + 1){
                System.out.prntln ("|");
                int myValue = boardState.get(x).get(y);
                if (myValue == 0) {
                    System.out.prntln (" ");
                }
                if (myValue == 1) {
                    System.out.prntln ("X");
                }
                if (myValue == 2) {
                    System.out.prntln ("O");
                }
            System.out.prntln ("|");
            System.out.prntln("\n");
            }
        System.out.prntln("-------");
        }
    }
    private static void makeBoard(void args) {
        for (int x = 0; x < 3; x = x + 1) {
            String rowName = "boardRow" + x;
            List rowName = ("");
            rowName.add(0,0);
            rowName.add(1,0);
            rowName.add(2,0);
        }
        List boardState = Array.asList(boardRow1,boardRow2,boardRow3);
    }
}