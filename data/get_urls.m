%goes through StationInventoryEN.csv and filters down to weather stations that we want

clear
clc

saveIt = 1; %1 if you want to write .txt file with URLs, 0 if not

filename = 'StationInventoryEN.xls';
output_filename = 'whistler_URLS.txt';
stationID_whistler = 348; %station that has daily data from 1976 - present
yearRange = [1976,2017];

[num text raw] = xlsread(filename); %raw: cell with string and numerical data

datacell = raw(4:end,:);
stationID = cell2mat(datacell(2:end,4));
latitude = cell2mat(datacell(2:end,7));
longitude = cell2mat(datacell(2:end,8));
elevation = cell2mat(datacell(2:end,11));
daily_firstyr = cell2mat(datacell(2:end,16));
daily_lastyr = cell2mat(datacell(2:end,17));
    
ind = find(stationID==stationID_whistler); %indices of stations that have data from before 1997 through 2017

stationID = stationID(ind);
latitude = latitude(ind);
longitude = longitude(ind);
elevation = elevation(ind);
daily_firstyr = daily_firstyr(ind);
daily_lastyr = daily_lastyr(ind);

n = yearRange(2) - yearRange(1); %number of years -1 in data to look at
for kk = 1:length(stationID) %loop through rows of data (each kk is a different station)
    id = num2str(stationID(kk)); %station ID
    i = 1;
    for year = yearRange(1):yearRange(1)+n %loop through years for each station       
        yearstr = num2str(year); 
        index = (kk-1)*(n+1) + i;
        URL(index,:) = strcat("http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=",id,"&Year=",yearstr,"&Month=1&Day=14&timeframe=2&submit=Download+Data");
        i = i+1;      
    end
end

if saveIt
    disp('Saving...')
    %write URL to a .txt file, each line a line in URL
    fid = fopen(output_filename, 'wt');
    fprintf(fid, '%s\n', URL);
    fclose(fid);
end
