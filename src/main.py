from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import NumericProperty
from jnius import autoclass

# Access Android classes
CameraManager = autoclass('android.hardware.camera2.CameraManager')
Context = autoclass('android.content.Context')

class NightLightApp(MDApp):
    brightness = NumericProperty(50)

    def build(self):
        return Builder.load_file('helloworld.kv')

    def on_start(self):
        self.camera_manager = self.get_camera_manager()
        self.camera_id = self.get_camera_id()

    def get_camera_manager(self):
        activity = PythonActivity.mActivity
        return activity.getSystemService(Context.CAMERA_SERVICE)

    def get_camera_id(self):
        camera_id_list = self.camera_manager.getCameraIdList()
        return camera_id_list[0] if camera_id_list else None

    def set_flashlight_brightness(self, brightness):
        if self.camera_id:
            # Convert brightness to a float between 0.0 and 1.0
            brightness_level = brightness / 100.0
            self.camera_manager.setTorchMode(self.camera_id, True)
            # Note: Direct control of brightness might not be supported on all devices
            # This is a placeholder for actual brightness control logic
            print(f"Setting flashlight brightness to {brightness_level}")

    def increase_brightness(self):
        if self.brightness < 100:
            self.brightness += 10
            self.set_flashlight_brightness(self.brightness)

    def decrease_brightness(self):
        if self.brightness > 0:
            self.brightness -= 10
            self.set_flashlight_brightness(self.brightness)

    def toggle_light(self, instance, value):
        if value:
            self.set_flashlight_brightness(self.brightness)
        else:
            if self.camera_id:
                self.camera_manager.setTorchMode(self.camera_id, False)

if __name__ == '__main__':
    NightLightApp().run()
