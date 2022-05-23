using System.Diagnostics.CodeAnalysis;
using Newtonsoft.Json;
using System.IO;
using System.Xml;

namespace Moravia.Homework
{
    class Program
    {
        static void Main(string[] args)
        {
            const string DirectoryPath = @"..\\..\\Source Files";
            string[] sourceFileName = Directory.GetFiles(DirectoryPath);
            
          
            foreach (string fileName in sourceFileName)
            {
                ProcessFile(fileName);
            }
         
        }

        
        // converting xml to json file
        private static void ProcessFile(string fileName)
        {
          
            string xml = File.ReadAllText(fileName);

            XmlDocument doc = new XmlDocument();
            doc.LoadXml(xml);

            string json = JsonConvert.SerializeXmlNode(doc);

            File.WriteAllText(fileName.Replace(".xml", ".json"), json);
            
            // source directory
            const string DirectoryPath = @"..\\..\\Source Files";
            string[] sourceFileName = Directory.GetFiles(DirectoryPath);
            
            // target directory
            const string DestinationPath = @"..\\..\\Target Files";
            string[] targetFileName = Directory.GetFiles(DestinationPath);
            
            // copy all files to the target directory
            foreach (var item in sourceFileName)
            {
                File.Copy(item, DestinationPath + Path.GetFileName(item));
            }
            
        }
        
       
    }
}
