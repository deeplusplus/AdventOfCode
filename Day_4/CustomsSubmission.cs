using System;

public class CustomsSubmision
{
    public string birthyear = "";
    public string issueYear = "";
    public string expirationYear = "";
    public string height = "";
    public string hairColor = "";
    public string eyeColor = "";
    public string passportId = "";
    public string countryId = "";


    public CustomsSubmision(string submissionString)
    {
        string[] splitSubmissionStrings = submissionString.Trim().Split(' ');        
        string[] entry = new string[2];

        foreach(string keyValueStrings in splitSubmissionStrings)
        {
            entry = keyValueStrings.Split(':');

            switch (entry[0])
            {
                case "byr":
                    birthyear = entry[1];
                    break;
                case "iyr":
                    issueYear = entry[1];
                    break;
                case "eyr":
                    expirationYear = entry[1];
                    break;
                case "hgt":
                    height = entry[1];
                    break;
                case "hcl":
                    hairColor = entry[1];
                    break;
                case "ecl":
                    eyeColor = entry[1];
                    break;
                case "pid":
                    passportId = entry[1];
                    break;
                case "cid":
                    countryId = entry[1];
                    break;
                default:
                    Console.WriteLine($"Found unexpected key:{entry[0]}");
                    break;
            }
        }
    }
}