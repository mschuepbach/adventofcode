
var input = await File.ReadAllLinesAsync("input.txt");

void Part1()
{
    var result = input.Sum(line =>
    {
        var separatorIndex = line.IndexOf('|');
        var startIndex = line.IndexOf(':') + 2;
        var winning = line[startIndex..(separatorIndex - 1)].Split(' ').Where(c => c.Length > 0).Select(int.Parse).ToArray();
        var numbers = line[(separatorIndex + 1)..].Split(' ').Where(c => c.Length > 0).Select(int.Parse).ToArray();
        var count = winning.Intersect(numbers).Count();
        return (int)Math.Pow(2, count - 1);
    });

    Console.WriteLine($"Part 1: {result}");
}

void Part2()
{
    var dict = new Dictionary<int, int>();

    for (int i = 1; i <= input.Length; i++)
    {
        var line = input[i - 1];
        var separatorIndex = line.IndexOf('|');
        var startIndex = line.IndexOf(':') + 2;
        var winning = line[startIndex..(separatorIndex - 1)].Split(' ').Where(c => c.Length > 0).Select(int.Parse).ToArray();
        var numbers = line[(separatorIndex + 1)..].Split(' ').Where(c => c.Length > 0).Select(int.Parse).ToArray();
        var matchingCount = winning.Intersect(numbers).Count();
        if (!dict.TryAdd(i, 1))
            dict[i] += 1;
        var cardCount = dict.TryGetValue(i, out var count) ? count : 1;

        for (int j = i + 1; j <= Math.Min(input.Length, i + matchingCount); j++)
        {
            if (!dict.TryAdd(j, cardCount))
                dict[j] += cardCount;
        }
    };

    Console.WriteLine($"Part 2: {dict.Sum(d => d.Value)}");
}

Part1();
Part2();
