# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamTranscodeInfoResponseBody(DaraModel):
    def __init__(
        self,
        domain_transcode_list: main_models.DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeList = None,
        request_id: str = None,
    ):
        # The transcoding configurations.
        self.domain_transcode_list = domain_transcode_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_transcode_list:
            self.domain_transcode_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_transcode_list is not None:
            result['DomainTranscodeList'] = self.domain_transcode_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainTranscodeList') is not None:
            temp_model = main_models.DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeList()
            self.domain_transcode_list = temp_model.from_map(m.get('DomainTranscodeList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeList(DaraModel):
    def __init__(
        self,
        domain_transcode_info: List[main_models.DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfo] = None,
    ):
        self.domain_transcode_info = domain_transcode_info

    def validate(self):
        if self.domain_transcode_info:
            for v1 in self.domain_transcode_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainTranscodeInfo'] = []
        if self.domain_transcode_info is not None:
            for k1 in self.domain_transcode_info:
                result['DomainTranscodeInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_transcode_info = []
        if m.get('DomainTranscodeInfo') is not None:
            for k1 in m.get('DomainTranscodeInfo'):
                temp_model = main_models.DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfo()
                self.domain_transcode_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfo(DaraModel):
    def __init__(
        self,
        custom_transcode_parameters: main_models.DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfoCustomTranscodeParameters = None,
        encrypt_parameters: main_models.DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfoEncryptParameters = None,
        is_lazy: bool = None,
        transcode_app: str = None,
        transcode_name: str = None,
        transcode_template: str = None,
    ):
        # The custom transcoding configuration.
        self.custom_transcode_parameters = custom_transcode_parameters
        # The encryption settings.
        self.encrypt_parameters = encrypt_parameters
        # Indicates whether forcible transcoding is used. Valid values:
        # 
        # *   **true**: Delayed transcoding is used.
        # *   **false**: Forcible transcoding is used.
        self.is_lazy = is_lazy
        # The application name.
        self.transcode_app = transcode_app
        # The main streaming domain.
        self.transcode_name = transcode_name
        # The transcoding template ID. Valid values:
        # 
        # *   **Standard transcoding**:
        # 
        #     *   **lld**: low definition
        #     *   **lsd**: standard definition
        #     *   **lhd**: high definition
        #     *   **lud**: ultra-high definition
        # 
        # *   **Narrowband HD™ transcoding**:
        # 
        #     *   **ld**: low definition
        #     *   **sd**: standard definition
        #     *   **hd**: high definition
        #     *   **ud**: ultra-high definition
        self.transcode_template = transcode_template

    def validate(self):
        if self.custom_transcode_parameters:
            self.custom_transcode_parameters.validate()
        if self.encrypt_parameters:
            self.encrypt_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_transcode_parameters is not None:
            result['CustomTranscodeParameters'] = self.custom_transcode_parameters.to_map()

        if self.encrypt_parameters is not None:
            result['EncryptParameters'] = self.encrypt_parameters.to_map()

        if self.is_lazy is not None:
            result['IsLazy'] = self.is_lazy

        if self.transcode_app is not None:
            result['TranscodeApp'] = self.transcode_app

        if self.transcode_name is not None:
            result['TranscodeName'] = self.transcode_name

        if self.transcode_template is not None:
            result['TranscodeTemplate'] = self.transcode_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTranscodeParameters') is not None:
            temp_model = main_models.DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfoCustomTranscodeParameters()
            self.custom_transcode_parameters = temp_model.from_map(m.get('CustomTranscodeParameters'))

        if m.get('EncryptParameters') is not None:
            temp_model = main_models.DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfoEncryptParameters()
            self.encrypt_parameters = temp_model.from_map(m.get('EncryptParameters'))

        if m.get('IsLazy') is not None:
            self.is_lazy = m.get('IsLazy')

        if m.get('TranscodeApp') is not None:
            self.transcode_app = m.get('TranscodeApp')

        if m.get('TranscodeName') is not None:
            self.transcode_name = m.get('TranscodeName')

        if m.get('TranscodeTemplate') is not None:
            self.transcode_template = m.get('TranscodeTemplate')

        return self

class DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfoEncryptParameters(DaraModel):
    def __init__(
        self,
        encrypt_type: str = None,
        kms_key_expire_interval: str = None,
        kms_key_id: str = None,
    ):
        # The type of encryption. Fixed value: **aliyun**.
        self.encrypt_type = encrypt_type
        # The rotation period of the CMK. Valid values: **60 to 3600**. Unit: seconds.
        self.kms_key_expire_interval = kms_key_expire_interval
        # The ID of the customer master key (CMK) in Key Management Service (KMS).
        self.kms_key_id = kms_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.kms_key_expire_interval is not None:
            result['KmsKeyExpireInterval'] = self.kms_key_expire_interval

        if self.kms_key_id is not None:
            result['KmsKeyID'] = self.kms_key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('KmsKeyExpireInterval') is not None:
            self.kms_key_expire_interval = m.get('KmsKeyExpireInterval')

        if m.get('KmsKeyID') is not None:
            self.kms_key_id = m.get('KmsKeyID')

        return self

class DescribeLiveStreamTranscodeInfoResponseBodyDomainTranscodeListDomainTranscodeInfoCustomTranscodeParameters(DaraModel):
    def __init__(
        self,
        audio_bitrate: int = None,
        audio_channel_num: int = None,
        audio_codec: str = None,
        audio_profile: str = None,
        audio_rate: int = None,
        bframes: str = None,
        bitrate_with_source: Dict[str, Any] = None,
        de_interlaced: bool = None,
        ext_with_source: Dict[str, Any] = None,
        fps: int = None,
        fps_with_source: Dict[str, Any] = None,
        gop: str = None,
        height: int = None,
        res_with_source: Dict[str, Any] = None,
        rts_flag: str = None,
        template_type: str = None,
        video_bitrate: int = None,
        video_profile: str = None,
        width: int = None,
    ):
        # The bitrate of the output audio. Unit: Kbit/s. Valid values: **1 to 1000**.
        self.audio_bitrate = audio_bitrate
        # The number of sound channels. Valid values:
        # 
        # *   **1**: mono
        # *   **2**: binaural
        self.audio_channel_num = audio_channel_num
        # The audio encoding format.
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
        # >  If the value of AudioProfile is **aac_ld**, the audio sampling rate cannot exceed 44100.
        self.audio_rate = audio_rate
        # Indicates whether B-frame removal is enabled. Fixed value: **0**.
        self.bframes = bframes
        # The source-based bitrate settings.
        self.bitrate_with_source = bitrate_with_source
        self.de_interlaced = de_interlaced
        # Other source-based settings.
        self.ext_with_source = ext_with_source
        # The frame rate of the output video. Unit: frames per second (FPS).
        self.fps = fps
        # The source-based frame rate settings.
        self.fps_with_source = fps_with_source
        # The group of pictures (GOP) size of the output video. Unit: frames. Valid values: **1 to 3000**.
        self.gop = gop
        # The height of the output video.
        self.height = height
        # The source-based resolution settings.
        self.res_with_source = res_with_source
        # The Real-Time Transcoding (RTS) flag. Fixed value: **true**.
        # 
        # >  This parameter is returned only if RTS is used for transcoding.
        self.rts_flag = rts_flag
        # The type of the custom transcoding template. Valid values:
        # 
        # *   **h264**: custom H.264 standard transcoding
        # *   **h264-nbhd**: custom H.264 Narrowband HD™ transcoding
        # *   **h265**: custom H.265 standard transcoding
        # *   **h265-nbhd**: custom H.265 Narrowband HD™ transcoding
        # *   **audio**: audio-only transcoding
        self.template_type = template_type
        # The bitrate of the output video. Unit: Kbit/s.
        self.video_bitrate = video_bitrate
        # The video encoding profile. Valid values:
        # 
        # *   **baseline**: suitable for mobile devices.
        # *   **main**: suitable for standard-definition devices.
        # *   **high**: suitable for high-definition devices.
        self.video_profile = video_profile
        # The width of the output video.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.bframes is not None:
            result['Bframes'] = self.bframes

        if self.bitrate_with_source is not None:
            result['BitrateWithSource'] = self.bitrate_with_source

        if self.de_interlaced is not None:
            result['DeInterlaced'] = self.de_interlaced

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

        if self.res_with_source is not None:
            result['ResWithSource'] = self.res_with_source

        if self.rts_flag is not None:
            result['RtsFlag'] = self.rts_flag

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate

        if self.video_profile is not None:
            result['VideoProfile'] = self.video_profile

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Bframes') is not None:
            self.bframes = m.get('Bframes')

        if m.get('BitrateWithSource') is not None:
            self.bitrate_with_source = m.get('BitrateWithSource')

        if m.get('DeInterlaced') is not None:
            self.de_interlaced = m.get('DeInterlaced')

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

        if m.get('ResWithSource') is not None:
            self.res_with_source = m.get('ResWithSource')

        if m.get('RtsFlag') is not None:
            self.rts_flag = m.get('RtsFlag')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')

        if m.get('VideoProfile') is not None:
            self.video_profile = m.get('VideoProfile')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

