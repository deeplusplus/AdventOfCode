using System;
using System.Collections.Generic;

namespace Day_4
{
    class Program
    {
        static void Main(string[] args)
        {
            int validPasswordCount = 0;
            string[] lines = System.IO.File.ReadAllLines("./input1.txt");
            string submissionConstructionString = "";
            List<CustomsSubmision> submissions = new List<CustomsSubmision>();            

            foreach (string line in lines)
            {
                if(line == "")
                {
                    CustomsSubmision submission = new CustomsSubmision(submissionConstructionString);
                    submissions.Add(submission);
                    if(Validator.ComplexSubmissionIsValid(submission))
                    {
                        validPasswordCount++;
                    }
                    submissionConstructionString = "";
                }
                else
                {
                    submissionConstructionString = submissionConstructionString + " " + line;
                }
            }

            Console.WriteLine($"Valid Count: {validPasswordCount}");
        }
    }
}
