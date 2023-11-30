using System.Diagnostics;

var solutionPath = TryGetSolutionDirectoryInfo();

if (solutionPath == null)
{
    Console.WriteLine("Could not find solution");
    return;
}

var newDay = (Directory.GetDirectories(solutionPath)
    .Max(d => int.TryParse(new DirectoryInfo(d).Name, out var lastDay) ? lastDay : 0) + 1)
    .ToString().PadLeft(2, '0');

var path = Path.Combine(solutionPath, newDay);
Directory.CreateDirectory(path);

var templatePath = "Templates";

var project = await File.ReadAllTextAsync(Path.Combine(templatePath, "Project.csproj.template"));
project = project.Replace("<RootNamespace></RootNamespace>", $"<RootNamespace>_{newDay}</RootNamespace>");
await File.WriteAllTextAsync(Path.Combine(path, $"{newDay}.csproj"), project);

var program = await File.ReadAllTextAsync(Path.Combine(templatePath, "Program.cs.template"));
await File.WriteAllTextAsync(Path.Combine(path, "Program.cs"), program);

File.Create(Path.Combine(path, "input.txt"));

Process.Start("dotnet", new[] {"sln", solutionPath, "add", Path.Combine(solutionPath, newDay, $"{newDay}.csproj") });

static string? TryGetSolutionDirectoryInfo(string? currentPath = null)
{
    var directory = new DirectoryInfo(currentPath ?? Directory.GetCurrentDirectory());
    while (directory != null && directory.GetFiles("*.sln").Length == 0)
    {
        directory = directory.Parent;
    }
    return directory?.FullName;
}
