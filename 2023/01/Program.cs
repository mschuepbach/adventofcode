
var input = await File.ReadAllLinesAsync("input.txt");

void Part1()
{
    var result = input
        .Sum(line =>
        {
            var first = line.First(character => char.IsDigit(character));
            var last = line.Last(character => char.IsDigit(character));
            return int.Parse($"{first}{last}");
        });

    Console.WriteLine($"Part 1: {result}");
}

void Part2()
{
    string[] numbers = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        ..Enumerable.Range(1, 9).Select(i => i.ToString())];

    var result = input
        .Sum(line =>
        {
            var numbersInLine = numbers.Where(n => line.Contains(n));
            var first = Array.IndexOf(numbers, numbersInLine.MinBy(n => line.IndexOf(n))) % 9 + 1;
            var last = Array.IndexOf(numbers, numbersInLine.MaxBy(n => line.LastIndexOf(n))) % 9 + 1;
            return int.Parse($"{first}{last}");
        });

    Console.WriteLine($"Part 2: {result}");
}

Part1();
Part2();
