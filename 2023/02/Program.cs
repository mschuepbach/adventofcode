
var input = await File.ReadAllLinesAsync("input.txt");

void Part1()
{
    var result = 0;

    foreach (var line in input)
    {
        var x = line.Split(':');
        var gameId = int.Parse(x[0].Replace("Game ", null));
        var games = x[1].Split(";");
        var isPossible = true;

        foreach (var game in games)
        {
            var sets = game.Split(",");
            foreach (var set in sets)
            {
                var y = set.Trim().Split(' ');
                var number = int.Parse(y[0]);
                var color = y[1];

                var setIsPossible = color switch
                {
                    "red" => number <= 12,
                    "green" => number <= 13,
                    "blue" => number <= 14,
                    _ => false
                };

                if (!setIsPossible)
                    isPossible = false;
            }
        }

        if (isPossible)
            result += gameId;
    }

    Console.WriteLine($"Part 1: {result}");
}

void Part2()
{

    Console.WriteLine($"Part 2: ");
}

Part1();
Part2();
