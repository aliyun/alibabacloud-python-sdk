# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRtsLiveStreamTranscodeRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        audio_bitrate: int = None,
        audio_channel_num: int = None,
        audio_codec: str = None,
        audio_profile: str = None,
        audio_rate: int = None,
        delete_bframes: bool = None,
        domain: str = None,
        fps: int = None,
        gop: str = None,
        height: int = None,
        lazy: str = None,
        opus: bool = None,
        owner_id: int = None,
        profile: int = None,
        region_id: str = None,
        template: str = None,
        template_type: str = None,
        video_bitrate: int = None,
        width: int = None,
    ):
        # The name of the application to which the live stream belongs. Value requirements:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   We recommend that you specify a name that is more than three characters in length. The name must start with a letter or digit.
        # 
        # This parameter is required.
        self.app = app
        # The bitrate of the output audio. Unit: Kbit/s. Valid values: **1** to **1000**.
        # 
        # >  This parameter is required if you set the TemplateType parameter to audio.
        self.audio_bitrate = audio_bitrate
        # The number of sound channels. Valid values:
        # 
        # *   **1**: mono
        # *   **2**: stereo
        self.audio_channel_num = audio_channel_num
        # The audio encoder. Valid values:
        # 
        # *   **aac**
        # *   **mp3**
        # 
        # > If you want to use the Opus encoding format, set the Opus parameter to true.
        self.audio_codec = audio_codec
        # The audio codec profile. Valid values:
        # 
        # *   **aac_low**
        # *   **aac_he**
        # *   **aac_he_v2**
        # *   **aac_ld**
        self.audio_profile = audio_profile
        # The audio sampling rate. Valid values: **22050 to 96000**. The value 44100 is commonly used. Unit: Hz.
        # 
        # > If you set the AudioProfile parameter to aac_ld, the audio sampling rate cannot exceed 44,100 Hz.
        self.audio_rate = audio_rate
        # Specifies whether to remove B-frames during transcoding. Valid values:
        # 
        # >  This parameter is required if you set the TemplateType parameter to h264, h264-nbhd, or h264-origin.
        # 
        # *   **true**: removes B-frames.
        # *   **false**: retains B-frames. This is the default value.
        # 
        # > If you do not specify this parameter, the default value **false** is used.
        self.delete_bframes = delete_bframes
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        # The frame rate of the output video. Unit: FPS. Valid values: **1** to **60**.
        # 
        # >  This parameter is required if you set the TemplateType parameter to h264, h264-nbhd, or h264-origin.
        self.fps = fps
        # The group of pictures (GOP) size of the output video. This parameter is used to specify the keyframe interval. Unit: seconds. Valid values: **1** to **3**.
        self.gop = gop
        # The height of the output video. Unit: pixels.
        # 
        # >  This parameter is required if you set the TemplateType parameter to h264, h264-nbhd, or h264-origin.
        # 
        # The value must comply with the following rules:****
        # 
        # *   **Height ≥ 100**: The height of the video is no less than 100 pixels.
        # *   **max(Height,Width) ≤ 2560**: The width or height of the video, whichever is greater, cannot exceed 2,560 pixels.
        # *   **min(Height,Width) ≤ 1440**: The width or height of the video, whichever is smaller, cannot exceed 1,440 pixels.
        # 
        # For example, a resolution of 1560 × 1560 pixels is invalid.
        # 
        # > An original quality template needs to retain the source information. Therefore, the video resolution cannot exceed 4K.
        self.height = height
        # Specifies whether to trigger transcoding only when a stream is pulled. Valid values:
        # 
        # *   **yes**: triggers transcoding only when a stream is pulled.
        # *   **no**: triggers transcoding whenever a stream is ingested, no matter whether the stream is pulled.
        self.lazy = lazy
        # Specifies whether to transcode audio to the Opus format to be compatible with native WebRTC. Valid values:
        # 
        # *   **true**: transcodes audio to the Opus format.
        # *   **false**: does not transcode audio to the Opus format.
        # 
        # > If you do not specify this parameter, the default value **false** is used.
        self.opus = opus
        self.owner_id = owner_id
        # The codec profile. The video codec profile determines how ApsaraVideo Live performs codec on the video. In normal cases, a greater value indicates a higher image quality and requires more codec resources. Valid values:
        # 
        # *   **1**: baseline, which is suitable for mobile devices.
        # *   **2**: main, which is suitable for standard-definition devices.
        # *   **3**: high, which is suitable for high-definition devices.
        self.profile = profile
        self.region_id = region_id
        # The name of the transcoding template. Value requirements:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   We recommend that you specify a name that is more than three characters in length. The name must start with a letter or digit.
        # 
        # > The name cannot be the same as that of a default transcoding template.
        # 
        # This parameter is required.
        self.template = template
        # The type of the transcoding template.
        # 
        # If you set this parameter to h264, h264-nbhd, or h264-origin, you must also specify the Height, Width, FPS, VideoBitrate, and DeleteBframes parameters. Valid values:
        # 
        # *   **h264**: H.264 standard transcoding template.
        # *   **h264-nbhd**: H.264 Narrowband HD™ transcoding template.
        # *   **h264-origin**: H.264 original quality template. If you use this type of template, the same transcoding parameters of the video source are retained by default.
        # *   **audio**: audio-only transcoding template. If you use this type of template, images are removed from the video source and an audio-only stream is generated. In addition, you must also specify the AudioBitrate parameter.
        # 
        # This parameter is required.
        self.template_type = template_type
        # The bitrate of the output video. Unit: Kbit/s. Valid values: **1** to **6000**.
        # 
        # >  This parameter is required if you set the TemplateType parameter to h264, h264-nbhd, or h264-origin.
        # 
        # > The bitrate of the output video is as close to the value that you specify as possible, but not exactly the same as the value, especially when the value is excessively large or small.
        self.video_bitrate = video_bitrate
        # The width of the output video. Unit: pixels.
        # 
        # >  This parameter is required if you set the TemplateType parameter to h264, h264-nbhd, or h264-origin.
        # 
        # The value must comply with the following rules:
        # 
        # *   **Width ≥ 100**: The width of the video is no less than 100 pixels.
        # *   **max(Height,Width) ≤ 2560**: The width or height of the video, whichever is greater, cannot exceed 2,560 pixels.
        # *   **min(Height,Width) ≤ 1440**: The width or height of the video, whichever is smaller, cannot exceed 1,440 pixels.
        # 
        # For example, a resolution of 1560 × 1560 pixels is invalid.
        # 
        # > An original quality template needs to retain the source information. Therefore, the video resolution cannot exceed 4K.
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

        if self.delete_bframes is not None:
            result['DeleteBframes'] = self.delete_bframes

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.fps is not None:
            result['FPS'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.height is not None:
            result['Height'] = self.height

        if self.lazy is not None:
            result['Lazy'] = self.lazy

        if self.opus is not None:
            result['Opus'] = self.opus

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('DeleteBframes') is not None:
            self.delete_bframes = m.get('DeleteBframes')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('FPS') is not None:
            self.fps = m.get('FPS')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Lazy') is not None:
            self.lazy = m.get('Lazy')

        if m.get('Opus') is not None:
            self.opus = m.get('Opus')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

