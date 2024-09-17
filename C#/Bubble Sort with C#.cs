using System;

public class Program
{
    public static void Main()
    {
        int[] arr = {63, 3, 47, 36, 0, 87, 21, 93, -14};
        int temp;

        Console.WriteLine("Original: ");
        foreach (int p in arr)
          Console.Write(p + " ");

        for (int j = 0; j <= arr.Length - 2; j++) {
          for (int i = 0; i <= arr.Length - 2; i++) {
              if (arr[i] > arr[i + 1]) {
                temp = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = temp;
              }
          }
        }

        Console.WriteLine("\r\n\r\nSorted: ");
        foreach (int p in arr)
          Console.Write(p + " ");
        Console.Read();
    }
}