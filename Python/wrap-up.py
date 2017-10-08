def getSeason():
    originalMonth = raw_input("What month are we in? Provide the three letter abbreviation.")
    month = originalMonth.lower() #Convert month to lowercase so entry is insensitive

    winter = ['dec','jan','feb']
    spring = ['mar', 'apr', 'may']
    summer = ['jun', 'jul', 'aug']
    fall   = ['sep', 'oct', 'nov']

    if month in winter:
        print('Winter');
    elif month in spring:
        print('Spring');
    elif month in summer:
        print('Summer')
    elif month in fall:
        print('Fall');
    else:
        print('Month not found')

# getSeason()

def getCelsius(degreeFarenheit):
    degreeCelsius =(degreeFarenheit - 32) / 1.8
    return round(degreeCelsius,2)


#getCelsius(55)

def getFahrenheit(degreeCelsius):
    degreeFarenheit = (degreeCelsius * 1.8) + 32
    return degreeFarenheit

# getFahrenheit(10)

def temperatureConverter(temp, destination):
    if destination == 'C':
        return getCelsius(temp);
    elif destination == 'F':
        return getFahrenheit(temp);


def temperatureConverterV2(temp, destination):
    if destination == 'C':
        return getCelsius(temp);
    elif destination == 'F':
        return getFahrenheit(temp);
    if destination != 'C' or destination != 'F':
        return ('Error: Invalid temperature scale; Must be F or C')

#print temperatureConverter(55, 'C') # 12.7777777778
#print temperatureConverter(10, 'F') # 50.0
#print temperatureConverterV2(55, 'X')



#define the list of vowels
#create a counter
#for every letter in the argument, search if letter is in vowel list. If yes, increment counter. If no, don't increment counter.
#once there are no more letters yet, print counter.


def vowelCounter():
    word = raw_input("Pick a word.")
    return word
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelCount = 0
    for letter in word:
        if letter in vowels:
            vowelCount = vowelCount + 1;
        else:
            vowelCount = vowelCount
    return vowelCount

vowelCounter()


#print vowelCounter('apples') # Expected: 2
#print vowelCounter('aeiou') # Expected: 5
#print vowelCounter('why') # Expected: 0
#print vowelCounter('mississippi') # Expected: 4
