# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListTranscodeJobsResponseBody(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ListTranscodeJobsResponseBodyJobs] = None,
        next_page_token: str = None,
        request_id: str = None,
    ):
        # The list of jobs.
        self.jobs = jobs
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. The token of the next page is returned after you call this operation for the first time.
        self.next_page_token = next_page_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.ListTranscodeJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTranscodeJobsResponseBodyJobs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        input_group: List[main_models.ListTranscodeJobsResponseBodyJobsInputGroup] = None,
        job_count: int = None,
        name: str = None,
        output_group: List[main_models.ListTranscodeJobsResponseBodyJobsOutputGroup] = None,
        parent_job_id: str = None,
        percent: int = None,
        request_id: str = None,
        schedule_config: main_models.ListTranscodeJobsResponseBodyJobsScheduleConfig = None,
        status: str = None,
        submit_time: str = None,
        trigger_source: str = None,
        user_data: str = None,
    ):
        # The time when the job was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the job was complete. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The input group of the job. An input of a single file indicates a transcoding job. An input of multiple files indicates an audio and video stream merge job.
        self.input_group = input_group
        # The number of subjobs.
        self.job_count = job_count
        # The job name.
        self.name = name
        # The output group of the job.
        self.output_group = output_group
        # The main job ID.
        self.parent_job_id = parent_job_id
        # The completion percentage of the job.
        self.percent = percent
        # The ID of the request that submitted the job.
        self.request_id = request_id
        # The scheduling configuration of the job.
        self.schedule_config = schedule_config
        # The state of the job.
        # 
        # *   Success: At least one of the subjobs is successful.
        # *   Fail: All subjobs failed.
        self.status = status
        # The time when the job was submitted. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.submit_time = submit_time
        # The source of the job. Valid values:
        # 
        # *   API
        # *   WorkFlow
        # *   Console
        self.trigger_source = trigger_source
        # The user data.
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        result['InputGroup'] = []
        if self.input_group is not None:
            for k1 in self.input_group:
                result['InputGroup'].append(k1.to_map() if k1 else None)

        if self.job_count is not None:
            result['JobCount'] = self.job_count

        if self.name is not None:
            result['Name'] = self.name

        result['OutputGroup'] = []
        if self.output_group is not None:
            for k1 in self.output_group:
                result['OutputGroup'].append(k1.to_map() if k1 else None)

        if self.parent_job_id is not None:
            result['ParentJobId'] = self.parent_job_id

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        self.input_group = []
        if m.get('InputGroup') is not None:
            for k1 in m.get('InputGroup'):
                temp_model = main_models.ListTranscodeJobsResponseBodyJobsInputGroup()
                self.input_group.append(temp_model.from_map(k1))

        if m.get('JobCount') is not None:
            self.job_count = m.get('JobCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.output_group = []
        if m.get('OutputGroup') is not None:
            for k1 in m.get('OutputGroup'):
                temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroup()
                self.output_group.append(temp_model.from_map(k1))

        if m.get('ParentJobId') is not None:
            self.parent_job_id = m.get('ParentJobId')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class ListTranscodeJobsResponseBodyJobsScheduleConfig(DaraModel):
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

class ListTranscodeJobsResponseBodyJobsOutputGroup(DaraModel):
    def __init__(
        self,
        output: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupOutput = None,
        process_config: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfig = None,
    ):
        # The output file configuration.
        self.output = output
        # The job processing configuration.
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ProcessConfig') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfig()
            self.process_config = temp_model.from_map(m.get('ProcessConfig'))

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfig(DaraModel):
    def __init__(
        self,
        combine_configs: List[main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigCombineConfigs] = None,
        encryption: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigEncryption = None,
        image_watermarks: List[main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarks] = None,
        is_inherit_tags: bool = None,
        subtitles: List[main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitles] = None,
        text_watermarks: List[main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTextWatermarks] = None,
        transcode: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscode = None,
    ):
        # The multi-input stream merge configuration.
        self.combine_configs = combine_configs
        # The encryption settings.
        self.encryption = encryption
        # The watermark configuration for an image.
        self.image_watermarks = image_watermarks
        # Indicates whether the tags of the input stream are inherited in the output stream. This parameter does not take effect when the input is not a media asset. Default value: false.
        self.is_inherit_tags = is_inherit_tags
        # The subtitle configuration.
        self.subtitles = subtitles
        # The configurations of the text watermarks.
        self.text_watermarks = text_watermarks
        # The transcoding configuration.
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

        if self.is_inherit_tags is not None:
            result['IsInheritTags'] = self.is_inherit_tags

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
                temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigCombineConfigs()
                self.combine_configs.append(temp_model.from_map(k1))

        if m.get('Encryption') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigEncryption()
            self.encryption = temp_model.from_map(m.get('Encryption'))

        self.image_watermarks = []
        if m.get('ImageWatermarks') is not None:
            for k1 in m.get('ImageWatermarks'):
                temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarks()
                self.image_watermarks.append(temp_model.from_map(k1))

        if m.get('IsInheritTags') is not None:
            self.is_inherit_tags = m.get('IsInheritTags')

        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitles()
                self.subtitles.append(temp_model.from_map(k1))

        self.text_watermarks = []
        if m.get('TextWatermarks') is not None:
            for k1 in m.get('TextWatermarks'):
                temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTextWatermarks()
                self.text_watermarks.append(temp_model.from_map(k1))

        if m.get('Transcode') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscode()
            self.transcode = temp_model.from_map(m.get('Transcode'))

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscode(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters of the template.
        self.overwrite_params = overwrite_params
        # The template ID.
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParams(DaraModel):
    def __init__(
        self,
        audio: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsAudio = None,
        container: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsContainer = None,
        mux_config: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig = None,
        tags: Dict[str, str] = None,
        video: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsVideo = None,
    ):
        # The audio settings.
        self.audio = audio
        # The encapsulation format settings.
        self.container = container
        # The encapsulation settings.
        self.mux_config = mux_config
        self.tags = tags
        # The video settings.
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.container:
            self.container.validate()
        if self.mux_config:
            self.mux_config.validate()
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

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('MuxConfig') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Video') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsVideo(DaraModel):
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
        # The average bitrate of the video.
        # 
        # *   Valid values: [10,50000].
        # *   Unit: Kbit/s.
        self.bitrate = bitrate
        # The buffer size.
        # 
        # *   Valid values: [1000,128000].
        # *   Default value: 6000.
        # *   Unit: KB.
        self.bufsize = bufsize
        # The encoding format.
        self.codec = codec
        # The constant rate factor.
        # 
        # *   Valid values: [0,51].
        # *   Default value: 23 if the encoding format is H.264, or 26 if the encoding format is H.265.
        # 
        # If this parameter is set, the value of Bitrate becomes invalid.
        self.crf = crf
        # The method of video cropping. Valid values:
        # 
        # *   border: automatically detects and removes black bars.
        # *   A value in the width:height:left:top format: crops the videos based on the custom settings. Example: 1280:800:0:140.
        self.crop = crop
        # The frame rate.
        # 
        # *   Valid values: (0,60].
        # *   The value is 60 if the frame rate of the input video exceeds 60.
        # *   Default value: the frame rate of the input video.
        self.fps = fps
        # The maximum number of frames between two keyframes.
        # 
        # *   Valid values: [1,1080000].
        # *   Default value: 250.
        self.gop = gop
        # The height of the output video.
        # 
        # *   Valid values: [128,4096].
        # *   Unit: pixels.
        # *   Default value: the height of the input video.
        self.height = height
        # Indicates whether the auto-rotate screen feature is enabled.
        self.long_short_mode = long_short_mode
        # The maximum bitrate of the output video. Valid values: [10,50000]. Unit: Kbit/s.
        self.maxrate = maxrate
        # The black bars added to the video.
        # 
        # *   Format: width:height:left:top.
        # *   Example: 1280:800:0:140.
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
        # Indicates whether the video was removed.
        self.remove = remove
        # The scan mode. Valid values: interlaced and progressive.
        self.scan_mode = scan_mode
        # The width of the output video.
        # 
        # *   Valid values: [128,4096].
        # *   Unit: pixels.
        # *   Default value: the width of the input video.
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

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig(DaraModel):
    def __init__(
        self,
        segment: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment = None,
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment(DaraModel):
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

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsContainer(DaraModel):
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

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        remove: str = None,
        samplerate: str = None,
        volume: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume = None,
    ):
        # The audio bitrate of the output file.
        # 
        # *   Valid values: [8,1000].
        # *   Unit: Kbit/s.
        # *   Default value: 128.
        self.bitrate = bitrate
        # The number of sound channels. Default value: 2.
        self.channels = channels
        # The audio codec. Valid values: AAC, MP3, VORBIS, and FLAC. Default value: AAC.
        self.codec = codec
        # The audio codec profile. If the Codec parameter is set to AAC, the valid values are aac_low, aac_he, aac_he_v2, aac_ld, and aac_eld.
        self.profile = profile
        # Indicates whether the audio stream is deleted.
        self.remove = remove
        # The sampling rate.
        # 
        # *   Default value: 44100.
        # *   Valid values: 22050, 32000, 44100, 48000, and 96000.
        # *   Unit: Hz.
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume(DaraModel):
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

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTextWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTextWatermarksOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters of the template.
        self.overwrite_params = overwrite_params
        # The template ID.
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTextWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigTextWatermarksOverwriteParams(DaraModel):
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
        # Indicates whether the text size was adjusted based on the output video dimensions. true / false, default: false
        self.adaptive = adaptive
        # The border color.
        self.border_color = border_color
        # The border width.
        self.border_width = border_width
        # The watermark text. Base64 encoding is not required. The string must be encoded in UTF-8.
        self.content = content
        # The transparency of the watermark.
        self.font_alpha = font_alpha
        # The color of the text.
        self.font_color = font_color
        # The font of the text.
        self.font_name = font_name
        # The size of the text.
        self.font_size = font_size
        # The distance of the watermark from the left edge.
        self.left = left
        # The distance of the watermark from the top edge.
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

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitles(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitlesOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters of the template.
        self.overwrite_params = overwrite_params
        # The template ID.
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitlesOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitlesOverwriteParams(DaraModel):
    def __init__(
        self,
        char_enc: str = None,
        file: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitlesOverwriteParamsFile = None,
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitlesOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigSubtitlesOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media object.
        # 
        # *   If Type is set to OSS, the URL of an OSS object is returned. Both the OSS and HTTP protocols are supported.
        # *   If Type is set to Media, the ID of a media asset is returned.
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

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters of the template.
        self.overwrite_params = overwrite_params
        # The template ID.
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParams(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        file: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParamsFile = None,
        height: str = None,
        refer_pos: str = None,
        timeline: main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline = None,
        width: str = None,
    ):
        # The position of the watermark on the x-axis.
        self.dx = dx
        # The position of the watermark on the y-axis.
        self.dy = dy
        # The watermark image file.
        self.file = file
        # The height of the output video.
        self.height = height
        # The reference position of the watermark. Valid values: TopLeft, TopRight, BottomLeft, and BottomRight. Default value: TopLeft.
        self.refer_pos = refer_pos
        # The timeline settings.
        self.timeline = timeline
        # The width of the output video.
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
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('Timeline') is not None:
            temp_model = main_models.ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        # The duration of the stream. Valid values: the number of seconds or "ToEND".
        self.duration = duration
        # The beginning of the time range for which data was queried.
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

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigImageWatermarksOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media object. If Type is set to OSS, the URL of an OSS object is returned. Both the OSS and HTTP protocols are supported. If Type is set to Media, the ID of a media asset is returned.
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

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigEncryption(DaraModel):
    def __init__(
        self,
        cipher_text: str = None,
        decrypt_key_uri: str = None,
        encrypt_type: str = None,
    ):
        # The ciphertext of HTTP Live Streaming (HLS) encryption.
        self.cipher_text = cipher_text
        # The endpoint of the decryption service for HLS encryption.
        self.decrypt_key_uri = decrypt_key_uri
        # The encryption type.
        self.encrypt_type = encrypt_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CipherText') is not None:
            self.cipher_text = m.get('CipherText')

        if m.get('DecryptKeyUri') is not None:
            self.decrypt_key_uri = m.get('DecryptKeyUri')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        return self

class ListTranscodeJobsResponseBodyJobsOutputGroupProcessConfigCombineConfigs(DaraModel):
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

class ListTranscodeJobsResponseBodyJobsOutputGroupOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        output_url: str = None,
        type: str = None,
    ):
        # The media object. If Type is set to OSS, the URL of an OSS object is returned. Both the OSS and HTTP protocols are supported. If Type is set to Media, the ID of a media asset is returned.
        self.media = media
        # The URL of the transcoded output stream. This parameter is required only when the output is a media asset.
        self.output_url = output_url
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

class ListTranscodeJobsResponseBodyJobsInputGroup(DaraModel):
    def __init__(
        self,
        input_url: str = None,
        media: str = None,
        type: str = None,
    ):
        # The URL of the media asset. This parameter is specified only when the media asset is transcoded.
        self.input_url = input_url
        # The media object.
        # 
        # *   If Type is set to OSS, the URL of an OSS object is returned. Both the OSS and HTTP protocols are supported.
        # *   If Type is set to Media, the ID of a media asset is returned.
        self.media = media
        # The type of the media object. Valid values:
        # 
        # *   OSS: an Object Storage Service (OSS) object.
        # *   Media: a media asset.
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

