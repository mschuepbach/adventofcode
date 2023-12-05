
var input = await File.ReadAllTextAsync("input.txt");

void Part1()
{
    var seeds = input.Split('\n')[0].Split(' ')[1..].Select(long.Parse).ToArray();
    var maps = input
        .Replace("\r", null)
        .Split("\n\n")[1..]
        .Select(map => map.Trim().Split('\n')[1..].Select(line => {
            var values = line.Split(' ').Select(long.Parse).ToArray();
            return new { 
                DestinationRangeStart = values[0],
                SourceRangeStart = values[1], 
                Length = values[2],
                SourceRangeEnd = values[1] + values[2] - 1,
            };
        }).ToArray())
        .ToArray();

    var mappedValues = new List<long>();

    foreach (var seed in seeds)
    {
        var mappedValue = seed;
        foreach (var map in maps)
        {
            var range = map.FirstOrDefault(r => mappedValue >= r.SourceRangeStart && mappedValue <= r.SourceRangeEnd);
            if (range != null)
            {
                mappedValue += range.DestinationRangeStart - range.SourceRangeStart;
            }
        }
        mappedValues.Add(mappedValue);
    }

    var result = mappedValues.Min();
    Console.WriteLine($"Part 1: {result}");
}

void Part2()
{

    Console.WriteLine($"Part 2: ");
}

Part1();
Part2();
