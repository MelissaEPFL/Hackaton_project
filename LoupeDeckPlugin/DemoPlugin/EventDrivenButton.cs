namespace Loupedeck.DemoPlugin
{
    using System;
    using System.Linq;
    using System.Net;
    using System.Threading;
    using System.Threading.Tasks;

    public class StaticEventDrivenButton : PluginDynamicCommand
    {
        public static Int32 NUMBER_OF_BUTTONS = 5;
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

        public static void ExecuteInBackground(StaticEventDrivenButton button, Int32 i)
        {
            while (true)
            {
                // Wait for 2 seconds
                Thread.Sleep(2000);
                if (button != null)
                {
                    var new_image = StaticEventDrivenButton.DownloadFileAsBytes($"http://localhost:5000/button/{i}/image");
                    button.SetImage(new_image, i);
                }

            }

        }
        private byte[][] image_as_byte = new byte[NUMBER_OF_BUTTONS][];

        public StaticEventDrivenButton()
            : base()
        {
            this.image_as_byte = new byte[NUMBER_OF_BUTTONS][];
            for (var i = 0; i < NUMBER_OF_BUTTONS; i++)
            {
                this.image_as_byte[i] = new byte[80*80];
                Thread thread = new Thread(() => StaticEventDrivenButton.ExecuteInBackground(this, i));
                // Parameter is the switch index
                var actionParameter = i.ToString();

                // Add parameter
                this.AddParameter(actionParameter, $"StaticEventDrivenButton {i}", "EventDrivenButtons");
                thread.Start();
            }
        }

        public void SetImage(byte[] image, Int32 i)
        {
            if (image == null)
            {
                return;
            }
            if (this.image_as_byte == null)
            {
                return;
            }
            if (this.image_as_byte.Length <= i)
            {
                return;
            }
            if (this.image_as_byte[i] == null)
            {
                this.image_as_byte[i] = image.CreateDeepCopy();
                this.ActionImageChanged();

            }
            else if (!this.image_as_byte[i].SequenceEqual(image))
            {
                this.image_as_byte[i] = image.CreateDeepCopy();
                this.ActionImageChanged();
            }
        }
        protected override BitmapImage GetCommandImage(String actionParameter, PluginImageSize imageSize)
        {
            using (var bitmapBuilder = new BitmapBuilder(imageSize))
            {
                if (Int32.TryParse(actionParameter, out var i))
                {
                    if (this.image_as_byte != null)
                    {
                        return BitmapImage.FromArray(this.image_as_byte[i]);
                    }
                }
                return bitmapBuilder.ToImage();
            }
        }


        protected override void RunCommand(String actionParameter)
        {
            if (Int32.TryParse(actionParameter, out var i))
            {
                CheckStatusCode($"http://localhost:5000/button/{i}/launch");
            }
        }
    }
}