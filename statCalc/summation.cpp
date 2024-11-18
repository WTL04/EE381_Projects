#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

double mean(vector<double>& input)
{
    double n = input.size();
    double sum;

    for(double num : input)
    {
        sum+=num;
    }
    sum /= n;
    return sum;
}

double median(vector<double> input)
{
    int n = input.size();
    sort(input.begin(), input.end());
    
    if (n % 2 == 0)
    {
        return (input[n / 2] + input[(n / 2) - 1]) / 2.0;
    }
    else
    {
        return input[n/2];
    }
}

double sum(vector<double>& input)
{
    double sum = 0.0;
    for(double num : input)
    {
        sum+=num;
    }
    return sum;
}


double xSquared(vector<double>& input)
{
    double sum = 0.0;
    for(double num : input)
    {
        sum+=pow(num, 2);
    }
    return sum;
}

double sigmaSquared(vector<double>& input)
{
    double sum = 0.0;
    for(double num : input)
    {
        sum+=num;
    }   
    return pow(sum, 2);
}

double sampleVariance(vector<double>& input)
{
    double n = input.size();
    double s = (xSquared(input) - (sigmaSquared(input)/n))/(n-1);
    return s;
}


int main()
{
    bool repeat = true;
    string yesOrNo;
    vector<double> input;
    string line;

    while (repeat)
    {
        input.clear();
        cout << "Enter the number of elements: " << endl;

        while (getline(cin, line))
        {
            stringstream ss(line);
            double num;
            while (ss >> num)
            {
                input.push_back(num);
            }
            break;
        }

        cout << "x̄ : " << mean(input) << endl;
        cout << "x͂ : " <<  median(input) << endl;
        cout << "Σx : " << sum(input) << endl; 
        cout << "Σx^2 : " << xSquared(input)<< endl;
        cout << "(Σx)^2 : " <<sigmaSquared(input)<< endl;
        cout << "Sample Variance (s) : " << sampleVariance(input) << endl;
        cout << "Sample Standard Deviation : " << sqrt(sampleVariance(input)) << endl;

        cout << endl;
        cout << "Input another set?[Y/N]: ";
        cin >> yesOrNo;
        cin.ignore(); // Clear newline from buffer

        if (yesOrNo == "Y" || yesOrNo == "y")
        {
            repeat = true;
        }
        else
        {
            repeat = false;
            break;
        }

    }



    return 0;
}