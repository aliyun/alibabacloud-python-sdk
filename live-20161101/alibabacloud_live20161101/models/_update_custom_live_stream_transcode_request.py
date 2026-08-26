# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomLiveStreamTranscodeRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        audio_bitrate: int = None,
        audio_channel_num: int = None,
        audio_codec: str = None,
        audio_profile: str = None,
        audio_rate: int = None,
        bitrate_with_source: str = None,
        de_interlaced: bool = None,
        domain: str = None,
        encrypt_parameters: str = None,
        ext_with_source: str = None,
        fps: int = None,
        fps_with_source: str = None,
        gop: str = None,
        height: int = None,
        lazy: str = None,
        owner_id: int = None,
        profile: int = None,
        region_id: str = None,
        res_with_source: str = None,
        template: str = None,
        template_type: str = None,
        video_bitrate: int = None,
        width: int = None,
    ):
        # The AppName of the live stream. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.app = app
        # The output audio bitrate. Unit: kbps. Valid values: 1 to **1000**.
        self.audio_bitrate = audio_bitrate
        # The number of audio channels. Valid values:
        # 
        # - 1: mono.
        # 
        # - 2: stereo.
        self.audio_channel_num = audio_channel_num
        # The audio codec. Valid values:
        # 
        # - aac
        # 
        # - mp3
        self.audio_codec = audio_codec
        # The audio profile. Valid values:
        # 
        # - aac_low
        # 
        # - aac_he
        # 
        # - aac_he_v2
        # 
        # - aac_ld
        self.audio_profile = audio_profile
        # The audio sample rate. Valid values: 22050, 32000, 44100, 48000, and 96000. Unit: Hz.
        # 
        # > If you set **AudioProfile** to **aac_ld**, the sample rate cannot exceed 44100.
        self.audio_rate = audio_rate
        # The adaptive bitrate settings. If specified, it overrides the VideoBitrate parameter. Fields:
        # 
        # - **UpLimit (integer):** Required. The upper limit of the bitrate. This must be an integer from 128 to 10000 and greater than the lower limit.
        # 
        # - **LowerLimit (integer):** Required. The lower limit of the bitrate. This must be an integer from 128 to 10000 and less than the upper limit.
        # 
        # - **Factor (float):** Required: The factor by which the source bitrate is multiplied to calculate the output bitrate. Valid values: 0.1 to 1. The value can be accurate to one decimal place. A value of 1 indicates that the output bitrate is the same as the source bitrate.
        self.bitrate_with_source = bitrate_with_source
        # Specifies whether to automatically detect and remove interlacing during transcoding. Deinterlacing converts interlaced video into progressive video.
        # 
        # - true: enables deinterlacing.
        # 
        # - false: keeps the source format. This is the default value.
        self.de_interlaced = de_interlaced
        # The streaming domain. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.domain = domain
        # The encryption settings, formatted as a JSON string.
        # 
        # - **EncryptType**: The encryption type. Set the value to aliyun.
        # 
        # - **KmsKeyID**: The ID of the customer master key (CMK) in Key Management Service (KMS).
        # 
        # - **KmsKeyExpireInterval**: The key rotation period. Unit: seconds. Valid values: **60 to 3600.**
        # 
        # > When you use Digital Rights Management (DRM) encryption, you cannot modify KmsKeyID.
        self.encrypt_parameters = encrypt_parameters
        # Other adaptive settings that align the transcoded stream with the source stream. Fields:
        # 
        # - **KeyFrameOpen**: Specifies whether to align keyframes with the source stream. Valid values: yes and no.
        # 
        # - **Copyts (string)**: Specifies whether to align the presentation timestamp (PTS) with the source stream. Valid values: yes and no.
        # 
        # - **SeiMode**: The pass-through mode for Supplemental Enhancement Information (SEI). Valid values: 0 (disabled), 1 (pass through partial parameters), and 2 (pass through all).
        self.ext_with_source = ext_with_source
        # The frame rate of the output video. Unit: frames per second (FPS). Valid values: 1 to **60**.
        self.fps = fps
        # Adapts the output frame rate based on the source\\"s frame rate, while keeping it within a specified range. If specified, it overrides the FPS parameter. Fields:
        # 
        # - **UpLimit (integer):** Required. The upper limit of the frame rate. This must be an integer from 1 to 60 and greater than the lower limit.
        # 
        # - **LowerLimit (integer):** Required. The lower limit of the frame rate. This must be an integer from 1 to 60 and less than the upper limit.
        self.fps_with_source = fps_with_source
        # The Group of Pictures (GOP) size. The unit can be frame or second. Valid values:
        # 
        # - By frames: 1 to 3000.
        # 
        # - By seconds: 1s to 20s.
        self.gop = gop
        # Output video height in pixels. Requirements:
        # 
        # - **Height ≥ 100**
        # 
        # - **max(Height, Width) ≤ 2560**
        # 
        # - **min(Height, Width) ≤ 1440**
        # 
        # > For h265-nbhd templates, it cannot exceed 720.
        self.height = height
        # Specifies whether to enable on-demand transcoding. Valid values:
        # 
        # - **yes**: Transcoding only starts when the first viewer requests this transcoded stream.
        # 
        # - **no**: Transcoding starts immediately after the stream is published.
        self.lazy = lazy
        self.owner_id = owner_id
        # The video codec profile. A larger value indicates better video quality and higher resource consumption for encoding and decoding. Valid values:
        # 
        # - **1**: baseline (for mobile devices).
        # 
        # - **2**: main (for SD devices).
        # 
        # - **3**: high (for HD devices).
        self.profile = profile
        # The region ID.
        self.region_id = region_id
        # The adaptive resolution settings. If specified, it overrides the Height and Width parameters. Fieds:
        # 
        # - **Type (string):** Required. Valid values:
        # 
        #   - **short**: sets the shorter edge of the video to the specified value and scales the other edge to maintain the original aspect ratio.
        # 
        #   - **long**: sets the longer edge of the video to the specified value and scales the other edge to maintain the original aspect ratio.
        # 
        #   - **screen**: Matches the output to a standard resolution, automatically flipping the dimensions based on the source\\"s orientation.
        # 
        # - **Value (string):** Required. Valid values:
        # 
        #   - For short: 360, 480, 540, 720, and 1080.
        # 
        #   - For long: 640, 848, 960, 1280, and 1920.
        # 
        #   - For screen: 640×360, 848×480, 960×540, 1280×720, and 1920×1080.
        self.res_with_source = res_with_source
        # The custom name of the transcoding template. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.template = template
        # The type of the custom transcoding template. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.template_type = template_type
        # The output video bitrate. Unit: kbps. Valid values: 1 to **6000**.
        # 
        # > The system tries to transcode the video at the specified bitrate. However, the actual bitrate may not be the same as the specified value, especially when the specified value is too high or too low.
        self.video_bitrate = video_bitrate
        # Output video width in pixels.
        # 
        # Requirements:
        # 
        # - **Width ≥ 100**
        # 
        # - **max(Height, Width) ≤ 2560**
        # 
        # - **min(Height, Width) ≤ 1440**
        # 
        # > For h265-nbhd templates, it cannot exceed 1280.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.audio_bitrate is not None:
            result['AudioBitrate'] = self.audio_bitrate

        if self.audio_channel_num is not None:
            result['AudioChannelNum'] = self.audio_channel_num

        if self.audio_codec is not None:
            result['AudioCodec'] = self.audio_codec

        if self.audio_profile is not None:
            result['AudioProfile'] = self.audio_profile

        if self.audio_rate is not None:
            result['AudioRate'] = self.audio_rate

        if self.bitrate_with_source is not None:
            result['BitrateWithSource'] = self.bitrate_with_source

        if self.de_interlaced is not None:
            result['DeInterlaced'] = self.de_interlaced

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.encrypt_parameters is not None:
            result['EncryptParameters'] = self.encrypt_parameters

        if self.ext_with_source is not None:
            result['ExtWithSource'] = self.ext_with_source

        if self.fps is not None:
            result['FPS'] = self.fps

        if self.fps_with_source is not None:
            result['FpsWithSource'] = self.fps_with_source

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.height is not None:
            result['Height'] = self.height

        if self.lazy is not None:
            result['Lazy'] = self.lazy

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.res_with_source is not None:
            result['ResWithSource'] = self.res_with_source

        if self.template is not None:
            result['Template'] = self.template

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('AudioBitrate') is not None:
            self.audio_bitrate = m.get('AudioBitrate')

        if m.get('AudioChannelNum') is not None:
            self.audio_channel_num = m.get('AudioChannelNum')

        if m.get('AudioCodec') is not None:
            self.audio_codec = m.get('AudioCodec')

        if m.get('AudioProfile') is not None:
            self.audio_profile = m.get('AudioProfile')

        if m.get('AudioRate') is not None:
            self.audio_rate = m.get('AudioRate')

        if m.get('BitrateWithSource') is not None:
            self.bitrate_with_source = m.get('BitrateWithSource')

        if m.get('DeInterlaced') is not None:
            self.de_interlaced = m.get('DeInterlaced')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EncryptParameters') is not None:
            self.encrypt_parameters = m.get('EncryptParameters')

        if m.get('ExtWithSource') is not None:
            self.ext_with_source = m.get('ExtWithSource')

        if m.get('FPS') is not None:
            self.fps = m.get('FPS')

        if m.get('FpsWithSource') is not None:
            self.fps_with_source = m.get('FpsWithSource')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Lazy') is not None:
            self.lazy = m.get('Lazy')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResWithSource') is not None:
            self.res_with_source = m.get('ResWithSource')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

