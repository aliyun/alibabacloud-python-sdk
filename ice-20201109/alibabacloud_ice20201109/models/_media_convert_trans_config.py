# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaConvertTransConfig(DaraModel):
    def __init__(
        self,
        adj_dar_method: str = None,
        is_check_audio_bitrate: bool = None,
        is_check_audio_bitrate_fail: bool = None,
        is_check_reso: bool = None,
        is_check_reso_fail: bool = None,
        is_check_video_bitrate: bool = None,
        is_check_video_bitrate_fail: bool = None,
        trans_mode: str = None,
    ):
        # The method for adjusting the resolution. This parameter takes effect only if both the Width and Height parameters are specified. You can use this parameter together with the LongShortMode parameter.
        # 
        # *   Valid values: rescale, crop, pad, and none.
        # *   Default value: none.
        # *
        self.adj_dar_method = adj_dar_method
        # Specifies whether to check the audio bitrate. Mutually exclusive with IsCheckVideoBitrateFail. IsCheckVideoBitrateFail has a higher priority.
        # 
        # *   true: checks the audio bitrate. If the source bitrate is lower than the target, the task will transcode using the source bitrate.
        # 
        # *   false: does not check the audio bitrate.
        # 
        # *   Default value:
        # 
        #     *   If this parameter is not specified and the codec of the output audio is different from that of the input audio, the default value is false.
        #     *   If this parameter is not specified and the codec of the output audio is the same as that of the input audio, the default value is true.
        self.is_check_audio_bitrate = is_check_audio_bitrate
        # Specifies whether to check the audio bitrate. Mutually exclusive with IsCheckAudioBitrate. This parameter has a higher priority.
        # 
        # *   true: checks the audio bitrate. If the source bitrate is lower than the target, the task will fail.
        # *   false: does not check the audio bitrate.
        # *   Default value: false.
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        # Specifies whether to check the video resolution. Mutually exclusive with IsCheckResoFail. IsCheckResoFail has a higher priority.
        # 
        # *   true: checks the video resolution. If the source resolution (width or height) is smaller than the target, the task will transcode using the source resolution.
        # *   false: does not check the video resolution.
        # *   Default value: false.
        self.is_check_reso = is_check_reso
        # Specifies whether to check the video resolution. Mutually exclusive with IsCheckReso. This parameter has a higher priority.
        # 
        # *   true: checks the video resolution. If the source resolution (width or height) is smaller than the target, the task will fail.
        # *   false: does not check the video resolution.
        # *   Default value: false.
        self.is_check_reso_fail = is_check_reso_fail
        # Specifies whether to check the video bitrate. Mutually exclusive with IsCheckVideoBitrateFail. IsCheckVideoBitrateFail has a higher priority.
        # 
        # *   true: checks the video bitrate. If the source bitrate is lower than the target, the task will transcode using the source bitrate.
        # *   false: does not check the video bitrate.
        # *   Default value: false.
        self.is_check_video_bitrate = is_check_video_bitrate
        # Specifies whether to check the video bitrate. Mutually exclusive with IsCheckVideoBitrate. This parameter has a higher priority.
        # 
        # *   true: checks the video bitrate. If the source bitrate is lower than the target, the task will fail.
        # *   false: does not check the video bitrate.
        # *   Default value: false.
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        # The video bitrate control mode. This is only valid for H.264, H.265, and AV1 codecs and must be used with the correct Bitrate or Crf settings. Valid values:
        # 
        # *   CBR: Constant bitrate mode.
        # *   onepass: Typically used for Average bitrate mode (ABR). Faster than twopass.
        # *   twopass: Typically used for variable bitrate mode (VBR). Slower than onepass.
        # *   fixCRF: Constant Rate Factor (quality-based) mode.
        # *   If you specify the Bitrate parameter, the default value of this parameter is onepass. If you do not specify the Bitrate parameter, the default value of this parameter is fixCRF, and the default value of the Crf parameter is used.
        self.trans_mode = trans_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adj_dar_method is not None:
            result['AdjDarMethod'] = self.adj_dar_method

        if self.is_check_audio_bitrate is not None:
            result['IsCheckAudioBitrate'] = self.is_check_audio_bitrate

        if self.is_check_audio_bitrate_fail is not None:
            result['IsCheckAudioBitrateFail'] = self.is_check_audio_bitrate_fail

        if self.is_check_reso is not None:
            result['IsCheckReso'] = self.is_check_reso

        if self.is_check_reso_fail is not None:
            result['IsCheckResoFail'] = self.is_check_reso_fail

        if self.is_check_video_bitrate is not None:
            result['IsCheckVideoBitrate'] = self.is_check_video_bitrate

        if self.is_check_video_bitrate_fail is not None:
            result['IsCheckVideoBitrateFail'] = self.is_check_video_bitrate_fail

        if self.trans_mode is not None:
            result['TransMode'] = self.trans_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjDarMethod') is not None:
            self.adj_dar_method = m.get('AdjDarMethod')

        if m.get('IsCheckAudioBitrate') is not None:
            self.is_check_audio_bitrate = m.get('IsCheckAudioBitrate')

        if m.get('IsCheckAudioBitrateFail') is not None:
            self.is_check_audio_bitrate_fail = m.get('IsCheckAudioBitrateFail')

        if m.get('IsCheckReso') is not None:
            self.is_check_reso = m.get('IsCheckReso')

        if m.get('IsCheckResoFail') is not None:
            self.is_check_reso_fail = m.get('IsCheckResoFail')

        if m.get('IsCheckVideoBitrate') is not None:
            self.is_check_video_bitrate = m.get('IsCheckVideoBitrate')

        if m.get('IsCheckVideoBitrateFail') is not None:
            self.is_check_video_bitrate_fail = m.get('IsCheckVideoBitrateFail')

        if m.get('TransMode') is not None:
            self.trans_mode = m.get('TransMode')

        return self

