
var input = await File.ReadAllLinesAsync("input.txt");

void Part1()
{
    var result = input.Sum(x =>
    {
        var separatorIndex = x.IndexOf('|');
        var startIndex = x.IndexOf(':') + 2;
        var winning = x[startIndex..(separatorIndex - startIndex - 1)].Split(' ').Where(c => c.Length > 0).Select(int.Parse).ToArray();
        var numbers = x[(separatorIndex + 1)..].Split(' ').Where(c => c.Length > 0).Select(int.Parse).ToArray();
        var count = winning.Intersect(numbers).Count();
        return (int)Math.Pow(2, count - 1);
    });

    Console.WriteLine($"Part 1: {result}");
}

void Part2()
{

    Console.WriteLine($"Part 2: ");
}

Part1();
Part2();
