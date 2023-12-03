
using System.Text.RegularExpressions;

var input = await File.ReadAllLinesAsync("input.txt");

void Part1()
{
    var width = input[0].Trim().Length;
    var height = input.Length;
    var result = 0;

    for (int i = 0; i < input.Length; i++)
    {
        var line = input[i];
        var matches = Regex.Matches(line, @"\d+");
        foreach (var match in matches.Cast<Match>())
        {
            var isPartNumber = false;
            for (var x = Math.Max(0, match.Index - 1); x <= Math.Min(width - 1, match.Index + match.Length); x++)
            {
                for (var y = Math.Max(0, i - 1); y <= Math.Min(height - 1, i + 1); y++)
                {
                    if (x >= match.Index && x < match.Index + match.Length && y == i)
                        continue;
                    if (input[y][x] != '.')
                        isPartNumber = true;
                }
            }

            if (isPartNumber)
                result += int.Parse(match.Value);
        }
    }

    Console.WriteLine($"Part 1: {result}");
}

void Part2()
{
    var width = input[0].Trim().Length;
    var height = input.Length;
    var potentialGears = new Dictionary<(int, int), List<int>>();

    for (int i = 0; i < input.Length; i++)
    {
        var line = input[i];
        var matches = Regex.Matches(line, @"\d+");
        foreach (var match in matches.Cast<Match>())
        {
            for (var x = Math.Max(0, match.Index - 1); x <= Math.Min(width - 1, match.Index + match.Length); x++)
            {
                for (var y = Math.Max(0, i - 1); y <= Math.Min(height - 1, i + 1); y++)
                {
                    if (x >= match.Index && x < match.Index + match.Length && y == i)
                        continue;
                    if (input[y][x] != '*')
                        continue;
                    var partNumber = int.Parse(match.Value);
                    if (!potentialGears.ContainsKey((x, y)))
                        potentialGears.Add((x, y), [partNumber]);
                    else
                        potentialGears[(x, y)].Add(partNumber);
                    goto breakOut;
                }
            }
        breakOut:;
        }
    }

    var result = potentialGears.Values.Where(v => v.Count == 2).Sum(v => v[0] * v[1]);

    Console.WriteLine($"Part 2: {result}");
}

Part1();
Part2();
