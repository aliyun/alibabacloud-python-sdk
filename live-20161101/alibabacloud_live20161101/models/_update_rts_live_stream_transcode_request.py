# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRtsLiveStreamTranscodeRequest(DaraModel):
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
        # The AppName of the live stream. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.app = app
        # The output audio bitrate. Unit: kbps. Valid values: 1 to **1000**.
        # 
        # > Required if you set TemplateType to audio.
        self.audio_bitrate = audio_bitrate
        # The number of audio channels. Valid values:
        # 
        # - **1**: mono.
        # 
        # - **2**: stereo.
        self.audio_channel_num = audio_channel_num
        # The audio codec. Valid values:
        # 
        # - aac
        # 
        # - mp3
        # 
        # > To use the Opus codec, set the Opus parameter to true.
        self.audio_codec = audio_codec
        # The audio codec profile. Valid values:
        # 
        # - aac_low
        # 
        # - aac_he
        # 
        # - aac_he_v2
        # 
        # - aac_ld
        self.audio_profile = audio_profile
        # The audio sample rate. Valid values: 22050, 32000, 44100, 48000, 96000. Recommended: 44100. Unit: Hz.
        # 
        # > If AudioProfile is set to aac_ld, the sample rate cannot exceed 44100.
        self.audio_rate = audio_rate
        # Controls whether to remove B-frames from the transcoded output video. Valid values:
        # 
        # - **true**: The transcoded video has no B-frames.
        # 
        # - **false**: The transcoded video contains B-frames. This is the default value.
        # 
        # > Required if you set TemplateType to h264, h264-nbhd, or h264-origin.
        self.delete_bframes = delete_bframes
        # The streaming domain. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.domain = domain
        # The frame rate of the output video. Unit: frames per second (FPS). Valid values: 1 to **60**.
        # 
        # > Required if you set TemplateType to h264, h264-nbhd, or h264-origin.
        self.fps = fps
        # The Group of Pictures (GOP) size, which specifies the keyframe interval. Unit: seconds. Valid values: **1** to **3**.
        self.gop = gop
        # Output video height in pixels.
        # 
        # Requirements:
        # 
        # - Height ≥ 100
        # 
        # - max(Height, Width) ≤ 2560
        # 
        # - min(Height, Width) ≤ 1440
        # 
        # > * Required if you set TemplateType to h264, h264-nbhd, or h264-origin.
        # >
        # > * For h264-origin templates, the resolution can be up to 4K to retain the information of the source stream.
        self.height = height
        # Specifies whether to enable on-demand transcoding. Valid values:
        # 
        # - **yes**: Transcoding only starts when the first viewer requests this transcoded stream.
        # 
        # - **no**: Transcoding starts immediately after the stream is published.
        self.lazy = lazy
        # Specifies whether to use the Opus codec for audio transcoding. This is mainly for compatibility with native WebRTC. Valid values:
        # 
        # - **true**: Transcodes the audio to the Opus format.
        # 
        # - **false**: Does not use the Opus format for transcoding. This is the default value.
        self.opus = opus
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
        # The name of the custom transcoding template. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.template = template
        # The type of the custom transcoding template. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.template_type = template_type
        # The output video bitrate. Unit: kbps. Valid values: 1 to **6000**.
        # 
        # > - Required if you set TemplateType to h264, h264-nbhd, or h264-origin.
        # >
        # > - The system tries to transcode the video at the specified bitrate. However, the actual bitrate may not be the same as the specified value, especially when the specified value is too high or too low.
        self.video_bitrate = video_bitrate
        # Output video width in pixels.
        # 
        # Requirements:
        # 
        # - Width ≥ 100
        # 
        # - max(Height, Width) ≤ 2560
        # 
        # - min(Height, Width) ≤ 1440
        # 
        # > Required if you set TemplateType to h264, h264-nbhd, or h264-origin.
        # 
        # For h264-origin templates, the resolution can be up to 4K to retain the information of the source stream.
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

