using System;
using System.Collections.Generic;

public class Validator
{
    public static bool SimpleSubmissionIsValid(CustomsSubmision submission)
    {
        if (
            !String.IsNullOrEmpty(submission.birthyear) &&
            !String.IsNullOrEmpty(submission.issueYear) &&
            !String.IsNullOrEmpty(submission.expirationYear) &&
            !String.IsNullOrEmpty(submission.height) &&
            !String.IsNullOrEmpty(submission.hairColor) &&
            !String.IsNullOrEmpty(submission.eyeColor) &&
            !String.IsNullOrEmpty(submission.passportId)
        )
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public static bool ComplexSubmissionIsValid(CustomsSubmision submission)
    {
            bool birthYearValid = BirthyearIsValid(submission);
            bool issueYearValid = IssueYearIsValid(submission);
            bool expirationYearValid = ExpirationYearIsValid(submission);
            bool heightValid = HeightIsValid(submission);
            bool hairColorValid = HairColorIsValid(submission);
            bool eyeColorValid = EyeColorIsValid(submission);
            bool passportIdValid = PassportIdIsValid(submission);

        if (
            birthYearValid &&
            issueYearValid &&
            expirationYearValid &&
            heightValid &&
            hairColorValid &&
            eyeColorValid &&
            passportIdValid
        )
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    private static bool BirthyearIsValid(CustomsSubmision submission)
    {
        try
        {
            int birthYearAsInt = int.Parse(submission.birthyear);
            return (birthYearAsInt >= 1920 && birthYearAsInt <= 2002);
        }
        catch (Exception e)
        {
            return false;
        }
    }

    private static bool IssueYearIsValid(CustomsSubmision submission)
    {
        try
        {
            int issueYearAsInt = int.Parse(submission.issueYear);
            return (issueYearAsInt >= 2010 && issueYearAsInt <= 2020);
        }
        catch (Exception e)
        {
            return false;
        }
    }

    private static bool ExpirationYearIsValid(CustomsSubmision submission)
    {
        try
        {
            int expirationYearAsInt = int.Parse(submission.expirationYear);
            return (expirationYearAsInt >= 2020 && expirationYearAsInt <= 2030);
        }
        catch (Exception e)
        {
            return false;
        }
    }

    private static bool HeightIsValid(CustomsSubmision submission)
    {
        bool isValid = false;
        string heightString = submission.height;
        try
        {
            if (heightString.Contains("cm"))
            {
                heightString = heightString.Replace("cm", "");
                int heightInt = int.Parse(heightString);

                isValid = (heightInt >= 150 && heightInt <= 193);
            }
            else if (heightString.Contains("in"))
            {
                heightString = heightString.Replace("in", "");
                int heightInt = int.Parse(heightString);

                isValid = (heightInt >= 59 && heightInt <= 76);
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
        return isValid;
    }

    private static bool HairColorIsValid(CustomsSubmision submission)
    {
        string hairColor = submission.hairColor;

        if (!String.IsNullOrEmpty(hairColor) && hairColor[0] == '#')
        {
            return hairColor.Length == 7;
        }

        return false;
    }

    private static bool EyeColorIsValid(CustomsSubmision submission)
    {
        List<string> validEyeColors = new List<string> { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" };

        return validEyeColors.Contains(submission.eyeColor);
    }

    private static bool PassportIdIsValid(CustomsSubmision submission)
    {
        string passportId = submission.passportId;

        if (passportId.Length == 9)
        {
            try
            {
                int.Parse(passportId);
                return true;
            }
            catch(Exception e)
            {
                Console.WriteLine(e);
            }
        }
        return false;
    }
}