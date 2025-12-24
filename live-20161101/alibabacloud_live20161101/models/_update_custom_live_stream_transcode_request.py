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
        # The name of the application to which the stream belongs, and it cannot be modified.
        # 
        # This parameter is required.
        self.app = app
        # Audio transcoding bitrate. Unit: kbps, value range: 1 to 1000.
        self.audio_bitrate = audio_bitrate
        # Number of audio channels. Values: 
        # - 1: Mono. 
        # - 2: Stereo.
        self.audio_channel_num = audio_channel_num
        # Audio encoding format. Values: 
        # - aac 
        # - mp3
        self.audio_codec = audio_codec
        # Audio encoding. Values: 
        # - aac_low
        #  - aac_he
        #  - aac_he_v2 
        # - aac_ld
        self.audio_profile = audio_profile
        # Audio sampling rate. Values: 22050, 32000, 44100, 48000, 96000. Unit: Hz.
        # > If **AudioProfile** is set to **aac_ld**, the sampling rate must not exceed 44100.
        self.audio_rate = audio_rate
        # The source-based bitrate settings. This parameter takes precedence over other bitrate settings. The following fields must be included:
        # 
        # *   **UpLimit**: the maximum bitrate. Set this field to an integer from 128 to 10000. The value must be greater than the minimum bitrate.
        # *   **LowerLimit**: the minimum bitrate. Set this field to an integer from 128 to 10000. The value must be smaller than the maximum bitrate.
        # *   **Factor**: the ratio of the output bitrate to the source bitrate. Valid values: 0.1 to 1. The value is accurate to one decimal place. A value of 1 indicates that the output video has the same bitrate as the source video.
        self.bitrate_with_source = bitrate_with_source
        self.de_interlaced = de_interlaced
        # Streamer domain name, unmodifiable.
        # 
        # This parameter is required.
        self.domain = domain
        # Encryption configuration. JSON format, with the following fields: 
        # -  EncryptType: Type of encryption. Fixed value is aliyun.
        #  -  KmsKeyID: User\\"s KMS master key ID. 
        # -  KmsKeyExpireInterval: Key rotation period. Value range: 60~3600, unit: seconds.
        # > When using DRM encryption, KmsKeyID cannot be modified.
        self.encrypt_parameters = encrypt_parameters
        # Other source-based settings. The following fields are included:
        # 
        # *   **KeyFrameOpen**: Valid values: yes and no.
        # *   **Copyts**: Valid values: yes and no.
        # *   **SeiMode**: Valid values: 0, 1, and 2. 0 specifies that no supplemental enhancement information (SEI) messages are passed through, 1 specifies that part of SEI messages are passed through, and 2 specifies that all SEI messages are passed through.
        self.ext_with_source = ext_with_source
        # Transcode video frame rate. Unit: FPS, value range: 1 to 60.
        self.fps = fps
        # The source-based frame rate settings. This parameter takes precedence over other frame rate settings. The following fields must be included:
        # 
        # *   **UpLimit**: the maximum frame rate. Set this field to an integer from 1 to 60. The value must be greater than the minimum frame rate.
        # *   **LowerLimit**: the minimum frame rate. Set this field to an integer from 1 to 60. The value must be smaller than the maximum frame rate.
        self.fps_with_source = fps_with_source
        # Video GOP (Group of Pictures), supports units in frames or seconds. When the unit is frames, the value should be {number}; when the unit is seconds, the value should be {number}s. 
        # - For frames, the range is 1 to 3000. 
        # - For seconds, the range is 1 to 20s.
        self.gop = gop
        # Video transcoding height. Unit: pixels. The value must meet the following three conditions:
        #  - Height ≥ 100: The height of the video must be no less than 100 pixels.
        #  - max(Height, Width) ≤ 2560: The larger of the video\\"s width and height cannot exceed 2560.
        #  - min(Height, Width) ≤ 1440: The smaller of the video\\"s width and height cannot exceed 1440.
        #  > For 265 narrowband HD templates, the maximum resolution is 1280×720.
        self.height = height
        # Specifies whether to enable triggered transcoding. Valid values:
        # 
        # *   **yes**: enables triggered transcoding.
        # *   **no**: disables triggered transcoding.
        self.lazy = lazy
        self.owner_id = owner_id
        # Encoding level. A set of specific encoding features supported by the video, generally, the higher the value, the better the picture quality, but also the higher the resources consumed for encoding and decoding. Values: 
        # - 1: baseline (suitable for mobile devices).
        #  - 2: main (suitable for standard resolution devices). 
        # - 3: high (suitable for high-resolution devices).
        self.profile = profile
        self.region_id = region_id
        # The source-based resolution settings. This parameter takes precedence over other resolution settings. The following fields must be included:
        # 
        # *   **Type**: You can set this field to short, long, or screen. short specifies that the resolution of the output video is adapted to the shorter side, long specifies that the resolution of the output video is adapted to the longer side, and screen specifies that the output video has an adaptive resolution.
        # 
        # *   **Value**:
        # 
        #     *   Set this field to 360, 480, 540, 720, or 1080 if the Type field is set to short.
        #     *   Set this field to 640, 848, 960, 1280, or 1920 if the Type field is set to long.
        #     *   Set this field to 640\\*360, 848\\*480, 960\\*540, 1280\\*720, or 1920\\*1080 if the Type field is set to screen.
        self.res_with_source = res_with_source
        # Custom name of the transcoding template, not modifiable.
        # 
        # This parameter is required.
        self.template = template
        # Custom transcoding template type, unmodifiable.
        # 
        # This parameter is required.
        self.template_type = template_type
        # Video transcoding bitrate. Unit: kbps, value range: 1 to 6000.
        # > The actual bitrate of the transcoded video will try to be as close as possible to the one you set, but it cannot be guaranteed to be exactly the same, especially when the set bitrate is too high or too low.
        self.video_bitrate = video_bitrate
        # Video transcoding width. Unit: pixels. The value must meet the following three conditions: 
        # - Width ≥ 100: The video width must be no less than 100 pixels. 
        # - max(Height, Width) ≤ 2560: The larger of the video\\"s height and width cannot exceed 2560. 
        # - min(Height, Width) ≤ 1440: The smaller of the video\\"s height and width cannot exceed 1440.
        # > For 265 narrowband HD templates, the maximum resolution is 1280×720.
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

