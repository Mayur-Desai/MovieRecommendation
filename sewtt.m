pe = pyversion;
pe.Version
if pe.Status == "NotLoaded"
    [~,exepath] = system("where python");
    pe = pyversion('Version',exepath);
end