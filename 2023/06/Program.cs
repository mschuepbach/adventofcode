
using System.Text.RegularExpressions;

var input = await File.ReadAllLinesAsync("input.txt");

void Part1()
{
    var times = Regex.Matches(input[0], @"\d+").Select(m => int.Parse(m.Value)).ToArray();
    var distances = Regex.Matches(input[1], @"\d+").Select(m => int.Parse(m.Value)).ToArray();
    var result = 1;

    for (var i = 0; i < times.Length; i++)
    {
        var time = times[i];
        var bestDistance = distances[i];
        var wins = 0;

        for (var j = 1; j < time - 1; j++)
        {
            var timeLeft = time - j;
            var distance = j * timeLeft;
            if (distance > bestDistance)
                wins++;
        }

        result *= wins;
    }

    Console.WriteLine($"Part 1: {result}");
}

void Part2()
{
    input = input.Select(l => l.Replace(" ", null)).ToArray();
    var time = long.Parse(Regex.Match(input[0], @"\d+").Value);
    var bestDistance = long.Parse(Regex.Match(input[1], @"\d+").Value);
    var result = 1;
    var wins = 0;

    for (long i = 1; i < time - 1; i++)
    {
        var timeLeft = time - i;
        var distance = i * timeLeft;
        if (distance > bestDistance)
            wins++;
    }

    result *= wins;

    Console.WriteLine($"Part 2: {result}");
}

Part1();
Part2();
