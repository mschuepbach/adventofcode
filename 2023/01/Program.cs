
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

    Console.WriteLine($"Part 2: ");
}

Part1();
Part2();
