# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitTranscodeJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        input_group: List[main_models.SubmitTranscodeJobRequestInputGroup] = None,
        name: str = None,
        output_group: List[main_models.SubmitTranscodeJobRequestOutputGroup] = None,
        schedule_config: main_models.SubmitTranscodeJobRequestScheduleConfig = None,
        user_data: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The input group of the job. An input of a single file indicates a transcoding job. An input of multiple files indicates an audio and video stream merge job.
        # 
        # This parameter is required.
        self.input_group = input_group
        # The job name.
        self.name = name
        # The output group of the job.
        # 
        # This parameter is required.
        self.output_group = output_group
        # The scheduling information about the job.
        self.schedule_config = schedule_config
        # The custom settings. The value must be in the JSON format and can be up to 512 bytes in length. You can specify a [custom callback URL](https://help.aliyun.com/document_detail/451631.html).
        self.user_data = user_data

    def validate(self):
        if self.input_group:
            for v1 in self.input_group:
                 if v1:
                    v1.validate()
        if self.output_group:
            for v1 in self.output_group:
                 if v1:
                    v1.validate()
        if self.schedule_config:
            self.schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['InputGroup'] = []
        if self.input_group is not None:
            for k1 in self.input_group:
                result['InputGroup'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        result['OutputGroup'] = []
        if self.output_group is not None:
            for k1 in self.output_group:
                result['OutputGroup'].append(k1.to_map() if k1 else None)

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.input_group = []
        if m.get('InputGroup') is not None:
            for k1 in m.get('InputGroup'):
                temp_model = main_models.SubmitTranscodeJobRequestInputGroup()
                self.input_group.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.output_group = []
        if m.get('OutputGroup') is not None:
            for k1 in m.get('OutputGroup'):
                temp_model = main_models.SubmitTranscodeJobRequestOutputGroup()
                self.output_group.append(temp_model.from_map(k1))

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitTranscodeJobRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # The ID of the MPS queue to which the job was submitted.
        self.pipeline_id = pipeline_id
        # The priority of the job. Valid values: 1 to 10. The greater the value, the higher the priority.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class SubmitTranscodeJobRequestOutputGroup(DaraModel):
    def __init__(
        self,
        output: main_models.SubmitTranscodeJobRequestOutputGroupOutput = None,
        process_config: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfig = None,
    ):
        # The output file configuration.
        # 
        # This parameter is required.
        self.output = output
        # The job processing configuration.
        # 
        # This parameter is required.
        self.process_config = process_config

    def validate(self):
        if self.output:
            self.output.validate()
        if self.process_config:
            self.process_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.process_config is not None:
            result['ProcessConfig'] = self.process_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ProcessConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfig()
            self.process_config = temp_model.from_map(m.get('ProcessConfig'))

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfig(DaraModel):
    def __init__(
        self,
        combine_configs: List[main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigCombineConfigs] = None,
        encryption: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigEncryption = None,
        image_watermarks: List[main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarks] = None,
        subtitles: List[main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitles] = None,
        text_watermarks: List[main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTextWatermarks] = None,
        transcode: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscode = None,
    ):
        # The multi-input stream merge configuration.
        self.combine_configs = combine_configs
        # The encryption settings.
        self.encryption = encryption
        # The watermark configuration of an image.
        self.image_watermarks = image_watermarks
        # The subtitle configuration.
        self.subtitles = subtitles
        # The configurations of the text watermark.
        self.text_watermarks = text_watermarks
        # The transcoding configuration.
        # 
        # This parameter is required.
        self.transcode = transcode

    def validate(self):
        if self.combine_configs:
            for v1 in self.combine_configs:
                 if v1:
                    v1.validate()
        if self.encryption:
            self.encryption.validate()
        if self.image_watermarks:
            for v1 in self.image_watermarks:
                 if v1:
                    v1.validate()
        if self.subtitles:
            for v1 in self.subtitles:
                 if v1:
                    v1.validate()
        if self.text_watermarks:
            for v1 in self.text_watermarks:
                 if v1:
                    v1.validate()
        if self.transcode:
            self.transcode.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CombineConfigs'] = []
        if self.combine_configs is not None:
            for k1 in self.combine_configs:
                result['CombineConfigs'].append(k1.to_map() if k1 else None)

        if self.encryption is not None:
            result['Encryption'] = self.encryption.to_map()

        result['ImageWatermarks'] = []
        if self.image_watermarks is not None:
            for k1 in self.image_watermarks:
                result['ImageWatermarks'].append(k1.to_map() if k1 else None)

        result['Subtitles'] = []
        if self.subtitles is not None:
            for k1 in self.subtitles:
                result['Subtitles'].append(k1.to_map() if k1 else None)

        result['TextWatermarks'] = []
        if self.text_watermarks is not None:
            for k1 in self.text_watermarks:
                result['TextWatermarks'].append(k1.to_map() if k1 else None)

        if self.transcode is not None:
            result['Transcode'] = self.transcode.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.combine_configs = []
        if m.get('CombineConfigs') is not None:
            for k1 in m.get('CombineConfigs'):
                temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigCombineConfigs()
                self.combine_configs.append(temp_model.from_map(k1))

        if m.get('Encryption') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigEncryption()
            self.encryption = temp_model.from_map(m.get('Encryption'))

        self.image_watermarks = []
        if m.get('ImageWatermarks') is not None:
            for k1 in m.get('ImageWatermarks'):
                temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarks()
                self.image_watermarks.append(temp_model.from_map(k1))

        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitles()
                self.subtitles.append(temp_model.from_map(k1))

        self.text_watermarks = []
        if m.get('TextWatermarks') is not None:
            for k1 in m.get('TextWatermarks'):
                temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTextWatermarks()
                self.text_watermarks.append(temp_model.from_map(k1))

        if m.get('Transcode') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscode()
            self.transcode = temp_model.from_map(m.get('Transcode'))

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscode(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters of the template.
        self.overwrite_params = overwrite_params
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.overwrite_params:
            self.overwrite_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overwrite_params is not None:
            result['OverwriteParams'] = self.overwrite_params.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverwriteParams') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParams(DaraModel):
    def __init__(
        self,
        audio: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsAudio = None,
        container: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsContainer = None,
        mux_config: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig = None,
        trans_config: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig = None,
        video: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsVideo = None,
    ):
        # The audio settings.
        self.audio = audio
        # The encapsulation format settings.
        self.container = container
        # The encapsulation settings.
        self.mux_config = mux_config
        # The conditional transcoding configurations.
        self.trans_config = trans_config
        # The video settings.
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.container:
            self.container.validate()
        if self.mux_config:
            self.mux_config.validate()
        if self.trans_config:
            self.trans_config.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()

        if self.container is not None:
            result['Container'] = self.container.to_map()

        if self.mux_config is not None:
            result['MuxConfig'] = self.mux_config.to_map()

        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config.to_map()

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('MuxConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('TransConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('Video') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsVideo(DaraModel):
    def __init__(
        self,
        abr_max: str = None,
        bitrate: str = None,
        bufsize: str = None,
        codec: str = None,
        crf: str = None,
        crop: str = None,
        fps: str = None,
        gop: str = None,
        height: str = None,
        long_short_mode: str = None,
        maxrate: str = None,
        pad: str = None,
        pix_fmt: str = None,
        preset: str = None,
        profile: str = None,
        remove: str = None,
        scan_mode: str = None,
        width: str = None,
    ):
        # The maximum adaptive bitrate (ABR). This parameter takes effect only for Narrowband HD 1.0. Valid values: [10,50000]. Unit: Kbit/s.
        self.abr_max = abr_max
        # The average video bitrate. Valid values: [10,50000]. Unit: Kbit/s.
        self.bitrate = bitrate
        # The buffer size. Valid values: [1000,128000]. Default value: 6000. Unit: KB.
        self.bufsize = bufsize
        # The encoding format.
        self.codec = codec
        # The constant rate factor (CRF). Valid values: [0,51]. Default value: 23 if the encoding format is H.264, or 26 if the encoding format is H.265.
        # 
        # >  If this parameter is specified, the setting of the bitrate becomes invalid.
        self.crf = crf
        # The method of video cropping. Valid values:
        # 
        # *   border: automatically detects and removes black bars.
        # *   A value in the width:height:left:top format: crops the videos based on the custom settings. Example: 1280:800:0:140.
        self.crop = crop
        # The frame rate. Valid values:(0,60]. Default value: the frame rate of the input file.
        # 
        # >  The value is 60 if the frame rate of the input file exceeds 60.
        self.fps = fps
        # The maximum number of frames between keyframes. Valid values: [1,1080000]. Default value: 250.
        self.gop = gop
        # The height of the video. Valid values: [128,4096]. Unit: pixels. Default value: the original height of the video.
        self.height = height
        # Specifies whether to enable the auto-rotate screen feature.
        self.long_short_mode = long_short_mode
        # The maximum bitrate of the video. Valid values: [10,50000]. Unit: Kbit/s.
        self.maxrate = maxrate
        # The black bars added to the video. Format: width:height:left:top. Example: 1280:800:0:140.
        self.pad = pad
        # The pixel format of the video. Valid values: standard pixel formats such as yuv420p and yuvj420p.
        self.pix_fmt = pix_fmt
        # The preset video algorithm. This parameter takes effect only if the encoding format is H.264. Valid values: veryfast, fast, medium, slow, and slower. Default value: medium.
        self.preset = preset
        # The encoding profile. Valid values: baseline, main, and high.
        # 
        # *   baseline: applicable to mobile devices.
        # *   main: applicable to standard-definition devices.
        # *   high: applicable to high-definition devices.
        # 
        # Default value: high.
        self.profile = profile
        # Specifies whether to remove the video.
        self.remove = remove
        # The scan mode. Valid values: interlaced and progressive.
        self.scan_mode = scan_mode
        # The width of the video. Valid values: [128,4096]. Unit: pixels. Default value: the original width of the video.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abr_max is not None:
            result['AbrMax'] = self.abr_max

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.bufsize is not None:
            result['Bufsize'] = self.bufsize

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.crf is not None:
            result['Crf'] = self.crf

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.height is not None:
            result['Height'] = self.height

        if self.long_short_mode is not None:
            result['LongShortMode'] = self.long_short_mode

        if self.maxrate is not None:
            result['Maxrate'] = self.maxrate

        if self.pad is not None:
            result['Pad'] = self.pad

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.preset is not None:
            result['Preset'] = self.preset

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.remove is not None:
            result['Remove'] = self.remove

        if self.scan_mode is not None:
            result['ScanMode'] = self.scan_mode

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbrMax') is not None:
            self.abr_max = m.get('AbrMax')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Bufsize') is not None:
            self.bufsize = m.get('Bufsize')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Crf') is not None:
            self.crf = m.get('Crf')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('LongShortMode') is not None:
            self.long_short_mode = m.get('LongShortMode')

        if m.get('Maxrate') is not None:
            self.maxrate = m.get('Maxrate')

        if m.get('Pad') is not None:
            self.pad = m.get('Pad')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Preset') is not None:
            self.preset = m.get('Preset')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Remove') is not None:
            self.remove = m.get('Remove')

        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig(DaraModel):
    def __init__(
        self,
        adj_dar_method: str = None,
        is_check_audio_bitrate: str = None,
        is_check_audio_bitrate_fail: str = None,
        is_check_reso: str = None,
        is_check_reso_fail: str = None,
        is_check_video_bitrate: str = None,
        is_check_video_bitrate_fail: str = None,
        trans_mode: str = None,
    ):
        # The method that is used to adjust the resolution. This parameter takes effect only if both the Width and Height parameters are specified. You can use this parameter together with the LongShortMode parameter.
        # 
        # Valid values: rescale, crop, pad, and none.
        # 
        # Default value: none.
        self.adj_dar_method = adj_dar_method
        # Specifies whether to check the audio bitrate. You can specify only one of the IsCheckAudioBitrate and IsCheckAudioBitrateFail parameters. The priority of the IsCheckAudioBitrateFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the bitrate of the input audio is less than that of the output audio, the bitrate of the input audio is used for transcoding.
        # *   false: does not check the video resolution.
        # 
        # Default value:
        # 
        # *   If this parameter is not specified and the codec of the output audio is different from that of the input audio, the default value is false.
        # *   If this parameter is not specified and the codec of the output audio is the same as that of the input audio, the default value is true.
        self.is_check_audio_bitrate = is_check_audio_bitrate
        # Specifies whether to check the audio bitrate. You can specify only one of the IsCheckAudioBitrate and IsCheckAudioBitrateFail parameters. The priority of the IsCheckAudioBitrateFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the bitrate of the input audio is less than that of the output audio, the transcoding job fails.
        # *   false: does not check the video resolution.
        # 
        # Default value: false.
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        # Specifies whether to check the video resolution. You can specify only one of the IsCheckReso and IsCheckResoFail parameters. The priority of the IsCheckResoFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the width or height of the input video is less than that of the output video, the resolution of the input video is used for transcoding.
        # *   false: does not check the video resolution.
        # 
        # Default value: false.
        self.is_check_reso = is_check_reso
        # Specifies whether to check the video resolution. You can specify only one of the IsCheckReso and IsCheckResoFail parameters. The priority of the IsCheckResoFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the width or height of the input video is less than that of the output video, the transcoding job fails.
        # *   false: does not check the video resolution.
        # 
        # Default value: false.
        self.is_check_reso_fail = is_check_reso_fail
        # Specifies whether to check the video bitrate. You can specify only one of the IsCheckVideoBitrate and IsCheckVideoBitrateFail parameters. The priority of the IsCheckVideoBitrateFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the bitrate of the input video is less than that of the output video, the bitrate of the input video is used for transcoding.
        # *   false: does not check the video resolution.
        # 
        # Default value: false.
        self.is_check_video_bitrate = is_check_video_bitrate
        # Specifies whether to check the video bitrate. You can specify only one of the IsCheckVideoBitrate and IsCheckVideoBitrateFail parameters. The priority of the IsCheckVideoBitrateFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the bitrate of the input video is less than that of the output video, the transcoding job fails.
        # *   false: does not check the video resolution.
        # 
        # Default value: false.
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        # The video transcoding mode. Valid values:
        # 
        # *   onepass: You can set this parameter to onepass if the Bitrate parameter is set to ABR. The encoding speed of this mode is faster than that of the twopass mode.
        # *   twopass: You can set this parameter to twopass if the Bitrate parameter is set to VBR. The encoding speed of this mode is slower than that of the onepass mode.
        # *   CBR: the constant bitrate mode.
        # 
        # Default value: onepass.
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

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig(DaraModel):
    def __init__(
        self,
        segment: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment = None,
    ):
        # The segment settings.
        self.segment = segment

    def validate(self):
        if self.segment:
            self.segment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.segment is not None:
            result['Segment'] = self.segment.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Segment') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment(DaraModel):
    def __init__(
        self,
        duration: str = None,
        force_seg_time: str = None,
    ):
        # The segment length.
        self.duration = duration
        # The forced segmentation point in time.
        self.force_seg_time = force_seg_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.force_seg_time is not None:
            result['ForceSegTime'] = self.force_seg_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ForceSegTime') is not None:
            self.force_seg_time = m.get('ForceSegTime')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsContainer(DaraModel):
    def __init__(
        self,
        format: str = None,
    ):
        # The container format.
        self.format = format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        remove: str = None,
        samplerate: str = None,
        volume: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume = None,
    ):
        # The audio bitrate of the output file. Valid values: [8,1000]. Unit: Kbit/s. Default value: 128.
        self.bitrate = bitrate
        # The number of sound channels. Default value: 2.
        self.channels = channels
        # The audio codec. Valid values: AAC, MP3, VORBIS, and FLAC. Default value: AAC.
        self.codec = codec
        # The audio codec profile. If the Codec parameter is set to AAC, the valid values are aac_low, aac_he, aac_he_v2, aac_ld, and aac_eld.
        self.profile = profile
        # Specifies whether to delete the audio stream.
        self.remove = remove
        # The sampling rate. Valid values: 22050, 32000, 44100, 48000, and 96000. Default value: 44100. Unit: Hz.
        self.samplerate = samplerate
        # The volume configurations.
        self.volume = volume

    def validate(self):
        if self.volume:
            self.volume.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.remove is not None:
            result['Remove'] = self.remove

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

        if self.volume is not None:
            result['Volume'] = self.volume.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Remove') is not None:
            self.remove = m.get('Remove')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        if m.get('Volume') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume(DaraModel):
    def __init__(
        self,
        integrated_loudness_target: str = None,
        loudness_range_target: str = None,
        method: str = None,
        true_peak: str = None,
    ):
        # The output volume.
        self.integrated_loudness_target = integrated_loudness_target
        # The volume range.
        self.loudness_range_target = loudness_range_target
        # The volume adjustment method. Valid values:
        self.method = method
        # The peak volume.
        self.true_peak = true_peak

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.integrated_loudness_target is not None:
            result['IntegratedLoudnessTarget'] = self.integrated_loudness_target

        if self.loudness_range_target is not None:
            result['LoudnessRangeTarget'] = self.loudness_range_target

        if self.method is not None:
            result['Method'] = self.method

        if self.true_peak is not None:
            result['TruePeak'] = self.true_peak

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntegratedLoudnessTarget') is not None:
            self.integrated_loudness_target = m.get('IntegratedLoudnessTarget')

        if m.get('LoudnessRangeTarget') is not None:
            self.loudness_range_target = m.get('LoudnessRangeTarget')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('TruePeak') is not None:
            self.true_peak = m.get('TruePeak')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTextWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTextWatermarksOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters of the template.
        self.overwrite_params = overwrite_params
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.overwrite_params:
            self.overwrite_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overwrite_params is not None:
            result['OverwriteParams'] = self.overwrite_params.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverwriteParams') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigTextWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigTextWatermarksOverwriteParams(DaraModel):
    def __init__(
        self,
        adaptive: str = None,
        border_color: str = None,
        border_width: int = None,
        content: str = None,
        font_alpha: str = None,
        font_color: str = None,
        font_name: str = None,
        font_size: int = None,
        left: str = None,
        top: str = None,
    ):
        # Specifies whether to the font size based on the output video dimensions. true / false, default: false
        self.adaptive = adaptive
        # The outline color of the text watermark. Default value: black. For more information, see BorderColor.
        self.border_color = border_color
        # The outline width of the text watermark.
        # 
        # *   Default value: 0.
        # *   Valid values: (0,4096].
        self.border_width = border_width
        # The watermark text. Base64 encoding is not required. The string must be encoded in UTF-8.
        self.content = content
        # The transparency of the text.
        # 
        # *   Valid values: (0,1].
        # *   Default value: 1.
        self.font_alpha = font_alpha
        # The color of the text.
        self.font_color = font_color
        # The font of the text. Default value: SimSun.
        self.font_name = font_name
        # The size of the text.
        # 
        # *   Default value: 16.
        # *   Valid values: (4,120).
        self.font_size = font_size
        # The left margin of the text watermark.
        # 
        # *   Default value: 0.
        # *   Valid values: [0,4096].
        self.left = left
        # The top margin of the text.
        # 
        # *   Default value: 0.
        # *   Valid values: [0,4096].
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptive is not None:
            result['Adaptive'] = self.adaptive

        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width is not None:
            result['BorderWidth'] = self.border_width

        if self.content is not None:
            result['Content'] = self.content

        if self.font_alpha is not None:
            result['FontAlpha'] = self.font_alpha

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_name is not None:
            result['FontName'] = self.font_name

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.left is not None:
            result['Left'] = self.left

        if self.top is not None:
            result['Top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adaptive') is not None:
            self.adaptive = m.get('Adaptive')

        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FontAlpha') is not None:
            self.font_alpha = m.get('FontAlpha')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitles(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitlesOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters of the template.
        self.overwrite_params = overwrite_params
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.overwrite_params:
            self.overwrite_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overwrite_params is not None:
            result['OverwriteParams'] = self.overwrite_params.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverwriteParams') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitlesOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitlesOverwriteParams(DaraModel):
    def __init__(
        self,
        char_enc: str = None,
        file: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitlesOverwriteParamsFile = None,
        format: str = None,
    ):
        # The file encoding format.
        self.char_enc = char_enc
        # The subtitle file.
        self.file = file
        # The format of the subtitle file.
        self.format = format

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.char_enc is not None:
            result['CharEnc'] = self.char_enc

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.format is not None:
            result['Format'] = self.format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharEnc') is not None:
            self.char_enc = m.get('CharEnc')

        if m.get('File') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitlesOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigSubtitlesOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media object.
        # 
        # *   If Type is set to OSS, set this parameter to the URL of an OSS object. Both the OSS and HTTP protocols are supported.
        # *   If Type is set to Media, set this parameter to the ID of a media asset.
        self.media = media
        # The type of the media object. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters of the template.
        self.overwrite_params = overwrite_params
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.overwrite_params:
            self.overwrite_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overwrite_params is not None:
            result['OverwriteParams'] = self.overwrite_params.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverwriteParams') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParams(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        file: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParamsFile = None,
        height: str = None,
        refer_pos: str = None,
        timeline: main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline = None,
        width: str = None,
    ):
        # The horizontal offset of the watermark relative to the output video. Default value: 0.
        # 
        # The following value types are supported:
        # 
        # *   Integer: the pixel value of the horizontal offset.
        # 
        #     *   Valid values: [8,4096].
        #     *   Unit: pixels.
        # 
        # *   Decimal: the ratio of the horizontal offset to the width of the output video.
        # 
        #     *   Valid values: (0,1).
        #     *   The decimal number can be accurate to four decimal places, such as 0.9999. Excessive digits are automatically discarded.
        self.dx = dx
        # The vertical offset of the watermark relative to the output video. Default value: 0.
        # 
        # The following value types are supported:
        # 
        # *   Integer: the pixel value of the horizontal offset.
        # 
        #     *   Valid values: [8,4096].
        #     *   Unit: pixels.
        # 
        # *   Decimal: the ratio of the vertical offset to the height of the output video.
        # 
        #     *   Valid values: (0,1).
        #     *   The decimal number can be accurate to four decimal places, such as 0.9999. Excessive digits are automatically discarded.
        self.dy = dy
        # The watermark image file.
        self.file = file
        # The height of the watermark image in the output video. The following value types are supported:
        # 
        # *   Integer: the pixel value of the watermark height.
        # 
        #     *   Valid values: [8,4096].
        #     *   Unit: pixels.
        # 
        # *   Decimal: the ratio of the watermark height to the height of the output video.
        # 
        #     *   Valid values: (0,1).
        #     *   The decimal number can be accurate to four decimal places, such as 0.9999. Excessive digits are automatically discarded.
        self.height = height
        # The position of the watermark.
        # 
        # *   Valid values: TopRight, TopLeft, BottomRight, and BottomLeft.
        # *   Default value: TopRight.
        self.refer_pos = refer_pos
        # The time settings of the dynamic watermark.
        self.timeline = timeline
        # The width of the watermark in the output video. The following value types are supported:
        # 
        # *   Integer: the pixel value of the watermark width.
        # 
        #     *   Valid values: [8,4096].
        #     *   Unit: pixels.
        # 
        # *   Decimal: the ratio of the watermark width to the width of the output video.
        # 
        #     *   Valid values: (0,1).
        #     *   The decimal number can be accurate to four decimal places, such as 0.9999. Excessive digits are automatically discarded.
        self.width = width

    def validate(self):
        if self.file:
            self.file.validate()
        if self.timeline:
            self.timeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dx is not None:
            result['Dx'] = self.dx

        if self.dy is not None:
            result['Dy'] = self.dy

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.height is not None:
            result['Height'] = self.height

        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos

        if self.timeline is not None:
            result['Timeline'] = self.timeline.to_map()

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')

        if m.get('Dy') is not None:
            self.dy = m.get('Dy')

        if m.get('File') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('Timeline') is not None:
            temp_model = main_models.SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        # The time range in which the watermark is displayed.
        # 
        # *   Valid values: integers and ToEND.
        # *   Default value: ToEND.
        self.duration = duration
        # The beginning of the time range in which the watermark is displayed.
        # 
        # *   Unit: seconds.
        # *   Value values: integers.
        # *   Default value: 0.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigImageWatermarksOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media object.
        # 
        # *   If Type is set to OSS, set this parameter to the URL of an OSS object. Both the OSS and HTTP protocols are supported.
        # *   If Type is set to Media, set this parameter to the ID of a media asset.
        self.media = media
        # The type of the media object. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigEncryption(DaraModel):
    def __init__(
        self,
        cipher_text: str = None,
        decrypt_key_uri: str = None,
        encrypt_type: str = None,
        key_service_type: str = None,
    ):
        # The ciphertext of HTTP Live Streaming (HLS) encryption.
        self.cipher_text = cipher_text
        # The address of the decryption service for HLS encryption.
        self.decrypt_key_uri = decrypt_key_uri
        # Specifies the encryption type. Valid values:
        # 
        # *   PrivateEncryption: Alibaba Cloud proprietary cryptography
        # *   HLSEncryption: HTTP Live Streaming (HLS) encryption
        self.encrypt_type = encrypt_type
        # The key service type for HLS encryption. Valid values:
        # 
        # *   KMS
        # *   Base64
        self.key_service_type = key_service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cipher_text is not None:
            result['CipherText'] = self.cipher_text

        if self.decrypt_key_uri is not None:
            result['DecryptKeyUri'] = self.decrypt_key_uri

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.key_service_type is not None:
            result['KeyServiceType'] = self.key_service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CipherText') is not None:
            self.cipher_text = m.get('CipherText')

        if m.get('DecryptKeyUri') is not None:
            self.decrypt_key_uri = m.get('DecryptKeyUri')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('KeyServiceType') is not None:
            self.key_service_type = m.get('KeyServiceType')

        return self

class SubmitTranscodeJobRequestOutputGroupProcessConfigCombineConfigs(DaraModel):
    def __init__(
        self,
        audio_index: str = None,
        duration: float = None,
        start: float = None,
        video_index: str = None,
    ):
        # The audio stream index.
        # 
        # This parameter is required.
        self.audio_index = audio_index
        # The duration of the input stream. The default value is the duration of the video.
        self.duration = duration
        # The start time of the input stream. Default value: 0.
        self.start = start
        # The video stream index.
        # 
        # This parameter is required.
        self.video_index = video_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_index is not None:
            result['AudioIndex'] = self.audio_index

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        if self.video_index is not None:
            result['VideoIndex'] = self.video_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioIndex') is not None:
            self.audio_index = m.get('AudioIndex')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('VideoIndex') is not None:
            self.video_index = m.get('VideoIndex')

        return self

class SubmitTranscodeJobRequestOutputGroupOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        output_url: str = None,
        type: str = None,
    ):
        # The media object.
        # 
        # *   If Type is set to OSS, set this parameter to the URL of an OSS object. Both the OSS and HTTP protocols are supported.
        # 
        # >  Before you use the OSS bucket in the URL, you must add the bucket on the [Storage Management](https://help.aliyun.com/document_detail/609918.html) page of the IMS console.
        # 
        # *   If Type is set to Media, set this parameter to the ID of a media asset.
        # 
        # This parameter is required.
        self.media = media
        # The URL of the output stream.\\
        # This parameter takes effect only when Type is set to Media. You can select a specific file within the media asset as an output.\\
        # Supported placeholders:
        # 
        # *   {MediaId}: the ID of the media asset.
        # *   {JobId}: the ID of the transcoding subjob.
        # *   {MediaBucket}: the bucket to which the media asset belongs.
        # *   {ExtName}: the file suffix, which uses the output format of the transcoding template.
        # *   {DestMd5}: the MD5 value of the transcoded output file.\\
        #     Notes:
        # 
        # 1.  This parameter must contain the {MediaId} and {JobId} placeholders.
        # 2.  The output bucket is the same as the bucket to which the media asset belongs.
        self.output_url = output_url
        # The type of the media object. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitTranscodeJobRequestInputGroup(DaraModel):
    def __init__(
        self,
        input_url: str = None,
        media: str = None,
        type: str = None,
    ):
        # The URL of the input stream.
        # 
        # *   This parameter takes effect only when Type is set to Media. You can select a specific file within the media asset as an input.
        # *   The system checks whether the input URL exists within the media asset.
        self.input_url = input_url
        # The media object.
        # 
        # *   If Type is set to OSS, set this parameter to the URL of an OSS object. Both the OSS and HTTP protocols are supported.
        # 
        # >  Before you use the OSS bucket in the URL, you must add the bucket on the [Storage Management](https://help.aliyun.com/document_detail/609918.html) page of the Intelligent Media Services (IMS) console.
        # 
        # *   If Type is set to Media, set this parameter to the ID of a media asset.
        # 
        # This parameter is required.
        self.media = media
        # The type of the media object. Valid values:
        # 
        # *   OSS: an Object Storage Service (OSS) object.
        # *   Media: a media asset.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_url is not None:
            result['InputUrl'] = self.input_url

        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputUrl') is not None:
            self.input_url = m.get('InputUrl')

        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

