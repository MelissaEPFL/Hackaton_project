namespace Loupedeck.DemoPlugin
{
    using System;
    using System.Net;
    using System.Threading;
    using System.Threading.Tasks;

    public class StaticEventDrivenButton : PluginDynamicCommand
    {
        public static bool CheckStatusCode(string url)
        {
            try
            {
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
                request.Method = "GET";

                using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
                {
                    if (response.StatusCode == HttpStatusCode.OK)
                    {
                        Console.WriteLine("Request successful - Status Code 200");
                        return true;
                    }
                    else
                    {
                        Console.WriteLine($"Request failed - Status Code {response.StatusCode}");
                        return false;
                    }
                }
            }
            catch (WebException e)
            {
                Console.WriteLine($"Request exception: {e.Message}");
                return false;
            }
        }

        public static byte[] DownloadFileAsBytes(string fileUrl)
        {
            try
            {
                WebClient webClient = new WebClient();

                // Download the file into a byte array
                byte[] fileData = webClient.DownloadData(fileUrl);

                // Dispose WebClient
                webClient.Dispose();

                return fileData;
            }
            catch (Exception ex)
            {
                // Handle exceptions (you might want to log or manage the error)
                Console.WriteLine("Error occurred: " + ex.Message);
                return null; // Or throw an exception based on your use case
            }
        }

        public static void ExecuteInBackground(StaticEventDrivenButton button)
        {
            while (true)
            {
                // Wait for 5 seconds
                Thread.Sleep(2000);
                if (button != null)
                {
                    var new_image = StaticEventDrivenButton.DownloadFileAsBytes("http://localhost:5000/button/1/image");
                    button.SetImage(new_image);
                }

            }

        }
        private byte[] image_as_byte = null;

        public StaticEventDrivenButton()
            : base(displayName: "StaticEventDrivenButton", description: "Button that can be configured to target a backend server.", groupName: "Event Driven")
        {
            Thread thread = new Thread(() => StaticEventDrivenButton.ExecuteInBackground(this));
            thread.Start();
        }

        public void SetImage(byte[] image)
        {
            this.ActionImageChanged();
        }
        protected override BitmapImage GetCommandImage(String actionParameter, PluginImageSize imageSize)
        {
            using (var bitmapBuilder = new BitmapBuilder(imageSize))
            {
                if (this.image_as_byte != null)
                {
                    return BitmapImage.FromArray(this.image_as_byte);
                }

                return bitmapBuilder.ToImage();
            }
        }


        protected override void RunCommand(String text)
        {
            if (!CheckStatusCode("http://localhost:5000/button/1/launch"))
            {

            }
        }
    }
}