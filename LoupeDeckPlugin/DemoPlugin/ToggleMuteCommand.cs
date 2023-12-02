namespace Loupedeck.DemoPlugin
{
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    public static class RuntimeButton
    {
    }

    public class EventDrivenButton : PluginDynamicCommand
    {
        public static void ExecuteInBackground(EventDrivenButton button)
        {
            while (true)
            {
                // Wait for 5 seconds
                Thread.Sleep(5000);
                if (button != null)
                {
                    // Adding 5 to the counter
                    button.IncreaseCounter(10);
                }

            }

        }

        private int counter = 0;
        private string suffix = string.Empty;

        public EventDrivenButton()
            : base(displayName: "EventDrivenButton", description: "Button that can be configured to target a backend server.", groupName: "Event Driven")
        {
            this.MakeProfileAction("text;Enter chat message to send:");
            Thread thread = new Thread(() => EventDrivenButton.ExecuteInBackground(this));
            thread.Start();
        }

        public void IncreaseCounter(Int32 i)
        {
            // Increasing the counter
            this.counter += i;
            this.ActionImageChanged();
        }
        protected override BitmapImage GetCommandImage(String actionParameter, PluginImageSize imageSize)
        {
            using (var bitmapBuilder = new BitmapBuilder(imageSize))
            {
                //bitmapBuilder.SetBackgroundImage(EmbeddedResources.ReadImage("MyPlugin.EmbeddedResources.MyImage.png"));
                //bitmapBuilder.DrawText(this.counter.ToString());
                bitmapBuilder.DrawText(this.suffix.ToString());

                return bitmapBuilder.ToImage();
            }
        }


        protected override void RunCommand(String text)
        {
            this.suffix = text;
            this.counter = 0;
            this.ActionImageChanged();
        }
    }
}