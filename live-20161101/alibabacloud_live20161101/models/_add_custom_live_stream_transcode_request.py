# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCustomLiveStreamTranscodeRequest(DaraModel):
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
        kms_key_expire_interval: str = None,
        kms_key_id: str = None,
        kms_uid: str = None,
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
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.app = app
        # The bitrate of the output audio. Unit: Kbit/s. Valid values: **1 to 1000**.
        self.audio_bitrate = audio_bitrate
        # The number of sound channels. Valid values:
        # 
        # *   **1**: mono.
        # *   **2**: binaural.
        self.audio_channel_num = audio_channel_num
        # The audio encoding format. Valid values:
        # 
        # *   **AAC**
        # *   **MP3**
        self.audio_codec = audio_codec
        # The audio encoding profile. Valid values:
        # 
        # *   **aac_low**
        # *   **aac_he**
        # *   **aac_he_v2**
        # *   **aac_ld**
        self.audio_profile = audio_profile
        # The audio sampling rate. Valid values: **22050 to 96000**.
        # 
        # 
        # >Notice: If you set AudioProfile to **aac_ld**, the audio sampling rate cannot exceed 44100.
        self.audio_rate = audio_rate
        # The source-based bitrate settings. This parameter takes precedence over other bitrate settings. The following fields must be included:
        # 
        # *   **UpLimit**: the maximum bitrate limit. Valid values: an integer from 128 to 10000. The value must be greater than the minimum bitrate.
        # *   **LowerLimit int** : the minimum bitrate rate. Valid values: an integer from 128 to 10000. The value must be smaller than the maximum bitrate.
        # *   **Factor**: The ratio of the output bitrate to the source bitrate. Valid values: 0.1 to 1. The value is accurate to one decimal place. A value of 1 indicates that the output video has the same bitrate as the source video.
        self.bitrate_with_source = bitrate_with_source
        self.de_interlaced = de_interlaced
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        # Encryption configuration. In JSON format, the fields are explained as follows:
        # - **EncryptType**: Encryption type. Fixed value is aliyun.
        # - **KmsKeyID**: User KMS master key ID.
        # - **KmsKeyExpireInterval**: Key rotation period. Range: 60~3600, unit: seconds.
        # > If the EncryptParameters is configured, the KmsKeyID, KmsUID, and KmsKeyExpireInterval parameters cannot be empty
        self.encrypt_parameters = encrypt_parameters
        # Other source-based settings, including the following fields:
        # 
        # *   **KeyFrameOpen**: specifies whether to use the key frames of the source video. Valid values: yes or no.
        # *   **Copyts**: specifies whether to use the presentation time stamp (PTS) of the source video. Valid values: yes or no.
        # *   **SeiMode**: specifies whether to pass through supplemental enhancement information (SEI) messages. Valid values: 0, 1, and 2, where 0 specifies that no SEI messages are passed through, 1 specifies that part of SEI messages are passed through, and 2 specifies that all SEI messages are passed through.
        self.ext_with_source = ext_with_source
        # The frame rate of the output video. Unit: frames per second (FPS). Valid values: **1 to 60**.
        self.fps = fps
        # The source-based frame rate settings. This parameter takes precedence over other frame rate settings. The following fields must be included:
        # 
        # *   **UpLimit**: the maximum frame rate. Valid values: an integer from 1 to 60. The value must be greater than the minimum frame rate.
        # *   **LowerLimit**: the minimum frame rate. Valid values: an integer from 1 to 60. The value must be smaller than the maximum frame rate.
        self.fps_with_source = fps_with_source
        # The Group of Picture (GOP) size of the video. Unit: frames or seconds.
        # 
        # *   Unit: frames. Valid values: **1 to 3000**.
        # *   Unit: seconds. Valid value: **1 to 20**.
        self.gop = gop
        # The height of the output video. Unit: pixel. Valid values:
        # 
        # The value must comply with all the following rules:
        # 
        # *   **Height ≥ 100**: The height of the video is greater than or equal to 100 pixels.
        # *   **max(Height,Width) ≤ 2560**: The width or height of the video, whichever is greater, cannot exceed 2,560 pixels.
        # *   **min(Height,Width) ≤ 1440**: The width or height of the video, whichever is smaller, cannot exceed 1,440 pixels.
        # 
        # > The resolution of the output video that is transcoded by using the H.265 Narrowband HD™ transcoding template cannot exceed 1280 × 720 pixels.
        self.height = height
        # The rotation period of the CMK. Valid values: 60 to 3600. Unit: seconds.
        self.kms_key_expire_interval = kms_key_expire_interval
        # The ID of the customer master key (CMK) that you created in Key Management Service (KMS).
        self.kms_key_id = kms_key_id
        # The ID of your KMS account.
        self.kms_uid = kms_uid
        # Specifies whether to use the load-on-demand mechanism for transcoding. Valid values: yes and no. Default value: **yes**.
        self.lazy = lazy
        self.owner_id = owner_id
        # The video encoding profile. The profile defines a set of parameters that are used to encode a video. In most cases, a greater value indicates better image quality and higher resource consumption. Valid values:
        # 
        # *   **1**: baseline. This value is suitable for mobile devices.
        # *   **2**: main. This value is suitable for standard-definition devices.
        # *   **3**: high. This value is suitable for high-definition devices.
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
        # The name of the custom transcoding template.
        # 
        # > The name can contain digits, letters, and hyphens (-), and must start with a letter or digit. The name must be different from the names of any default transcoding templates.
        # 
        # This parameter is required.
        self.template = template
        # The type of the custom transcoding template. Valid values:
        # 
        # *   **h264**: custom H.264 standard transcoding.
        # *   **h264-nbhd**: custom H.264 Narrowband HD™ transcoding.
        # *   **h265**: custom H.265 standard transcoding.
        # *   **h265-nbhd**: custom H.265 Narrowband HD™ transcoding.
        # *   **audio**: audio-only transcoding.
        # 
        # > If you set **TemplateType** to **h264**, **h264-nbhd**, **h265**, or **h265-nbhd**, the **Height**, **Width**, **FPS**, and **VideoBitrate** parameters are required.
        # 
        # This parameter is required.
        self.template_type = template_type
        # The bitrate of the output video. Unit: Kbit/s. Valid values: **1 to 6000**.
        # 
        # > The bitrate of the output video may not be the same as the value that you specify, but is as close to the value as possible, especially when the value is excessively large or small.
        self.video_bitrate = video_bitrate
        # The width of the output video. Unit: pixel. Valid values:
        # 
        # The value must comply with all the following rules:
        # 
        # *   **Width ≥ 100**: The width of the video is greater than or equal to 100 pixels.
        # *   **max(Height,Width) ≤ 2560**: The width or height of the video, whichever is greater, cannot exceed 2,560 pixels.
        # *   **min(Height,Width) ≤ 1440**: The width or height of the video, whichever is smaller, cannot exceed 1,440 pixels.
        # 
        # > The resolution of the output video that is transcoded by using the H.265 Narrowband HD™ transcoding template cannot exceed 1280 × 720 pixels.
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

        if self.kms_key_expire_interval is not None:
            result['KmsKeyExpireInterval'] = self.kms_key_expire_interval

        if self.kms_key_id is not None:
            result['KmsKeyID'] = self.kms_key_id

        if self.kms_uid is not None:
            result['KmsUID'] = self.kms_uid

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

        if m.get('KmsKeyExpireInterval') is not None:
            self.kms_key_expire_interval = m.get('KmsKeyExpireInterval')

        if m.get('KmsKeyID') is not None:
            self.kms_key_id = m.get('KmsKeyID')

        if m.get('KmsUID') is not None:
            self.kms_uid = m.get('KmsUID')

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

