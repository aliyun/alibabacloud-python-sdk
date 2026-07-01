# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetTranscodeJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transcode_parent_job: main_models.GetTranscodeJobResponseBodyTranscodeParentJob = None,
    ):
        # Request ID.
        self.request_id = request_id
        # TranscodeParentJobWithSubJobDTO
        self.transcode_parent_job = transcode_parent_job

    def validate(self):
        if self.transcode_parent_job:
            self.transcode_parent_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transcode_parent_job is not None:
            result['TranscodeParentJob'] = self.transcode_parent_job.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TranscodeParentJob') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJob()
            self.transcode_parent_job = temp_model.from_map(m.get('TranscodeParentJob'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJob(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        input_group: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobInputGroup] = None,
        job_count: int = None,
        name: str = None,
        output_group: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroup] = None,
        parent_job_id: str = None,
        percent: int = None,
        request_id: str = None,
        schedule_config: main_models.GetTranscodeJobResponseBodyTranscodeParentJobScheduleConfig = None,
        status: str = None,
        submit_time: str = None,
        transcode_job_list: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobList] = None,
        trigger_source: str = None,
        user_data: str = None,
    ):
        # Job creation time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # Job completion time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.finish_time = finish_time
        # Job input group. A single input represents a transcoding job. Multiple inputs represent an audio-video merging job.
        self.input_group = input_group
        # Number of sub-jobs.
        self.job_count = job_count
        # Job name.
        self.name = name
        # Job output group.
        self.output_group = output_group
        # Parent job ID.
        self.parent_job_id = parent_job_id
        # Job completion percentage.
        self.percent = percent
        # Request ID at job submission.
        self.request_id = request_id
        # Job scheduling configuration.
        self.schedule_config = schedule_config
        # Job status.
        # 
        # - Success: All sub-jobs completed successfully.
        # 
        # - Fail: All sub-jobs failed.
        self.status = status
        # Job submission time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.submit_time = submit_time
        # List of sub-jobs.
        self.transcode_job_list = transcode_job_list
        # Job source.
        # 
        # - API: API
        # 
        # - WorkFlow: Workflow
        # 
        # - Console: Console
        self.trigger_source = trigger_source
        # User data.
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
        if self.transcode_job_list:
            for v1 in self.transcode_job_list:
                 if v1:
                    v1.validate()

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

        result['TranscodeJobList'] = []
        if self.transcode_job_list is not None:
            for k1 in self.transcode_job_list:
                result['TranscodeJobList'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobInputGroup()
                self.input_group.append(temp_model.from_map(k1))

        if m.get('JobCount') is not None:
            self.job_count = m.get('JobCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.output_group = []
        if m.get('OutputGroup') is not None:
            for k1 in m.get('OutputGroup'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroup()
                self.output_group.append(temp_model.from_map(k1))

        if m.get('ParentJobId') is not None:
            self.parent_job_id = m.get('ParentJobId')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        self.transcode_job_list = []
        if m.get('TranscodeJobList') is not None:
            for k1 in m.get('TranscodeJobList'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobList()
                self.transcode_job_list.append(temp_model.from_map(k1))

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        input_group: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListInputGroup] = None,
        job_id: str = None,
        job_index: int = None,
        name: str = None,
        out_file_meta: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMeta = None,
        output: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutput = None,
        parent_job_id: str = None,
        process_config: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfig = None,
        request_id: str = None,
        schedule_config: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListScheduleConfig = None,
        status: str = None,
        submit_result_json: Dict[str, Any] = None,
        submit_time: str = None,
        user_data: str = None,
    ):
        # Job creation time.
        self.create_time = create_time
        # Job completion time.
        self.finish_time = finish_time
        # Job input group. A single input represents a transcoding job. Multiple inputs represent an audio-video merging job.
        self.input_group = input_group
        # Sub-job ID.
        self.job_id = job_id
        # Index of the sub-job within the entire job.
        self.job_index = job_index
        # Job name.
        self.name = name
        # Generated video media information.
        self.out_file_meta = out_file_meta
        # Output media configuration.
        self.output = output
        # Parent job ID.
        self.parent_job_id = parent_job_id
        # Transcoding processing configuration.
        self.process_config = process_config
        # Request ID at job submission.
        self.request_id = request_id
        # Job scheduling information.
        self.schedule_config = schedule_config
        # Transcoding job status
        # 
        # - Init: Submitted.
        # 
        # - Processing: Transcoding.
        # 
        # - Success: Transcoding succeeded.
        # 
        # - Fail: Transcoding failed.
        # 
        # - Deleted: Deleted.
        self.status = status
        # Job submission result.
        self.submit_result_json = submit_result_json
        # Job submission time.
        self.submit_time = submit_time
        # User data.
        self.user_data = user_data

    def validate(self):
        if self.input_group:
            for v1 in self.input_group:
                 if v1:
                    v1.validate()
        if self.out_file_meta:
            self.out_file_meta.validate()
        if self.output:
            self.output.validate()
        if self.process_config:
            self.process_config.validate()
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

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_index is not None:
            result['JobIndex'] = self.job_index

        if self.name is not None:
            result['Name'] = self.name

        if self.out_file_meta is not None:
            result['OutFileMeta'] = self.out_file_meta.to_map()

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.parent_job_id is not None:
            result['ParentJobId'] = self.parent_job_id

        if self.process_config is not None:
            result['ProcessConfig'] = self.process_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_result_json is not None:
            result['SubmitResultJson'] = self.submit_result_json

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

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
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListInputGroup()
                self.input_group.append(temp_model.from_map(k1))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobIndex') is not None:
            self.job_index = m.get('JobIndex')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutFileMeta') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMeta()
            self.out_file_meta = temp_model.from_map(m.get('OutFileMeta'))

        if m.get('Output') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ParentJobId') is not None:
            self.parent_job_id = m.get('ParentJobId')

        if m.get('ProcessConfig') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfig()
            self.process_config = temp_model.from_map(m.get('ProcessConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitResultJson') is not None:
            self.submit_result_json = m.get('SubmitResultJson')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # Pipeline ID.
        self.pipeline_id = pipeline_id
        # Job priority. Higher numbers indicate higher priority. Valid range: 1–10.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfig(DaraModel):
    def __init__(
        self,
        combine_configs: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigCombineConfigs] = None,
        encryption: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigEncryption = None,
        image_watermarks: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarks] = None,
        is_inherit_tags: bool = None,
        subtitles: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitles] = None,
        text_watermarks: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarks] = None,
        transcode: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscode = None,
    ):
        # Multi-input merging configuration
        self.combine_configs = combine_configs
        # Encryption configuration.
        self.encryption = encryption
        # Image watermark configuration.
        self.image_watermarks = image_watermarks
        # Whether to inherit tags from the input stream.
        # This parameter does not take effect if the input is not a media asset.
        # Default value: false
        self.is_inherit_tags = is_inherit_tags
        # Subtitle embedding configuration.
        self.subtitles = subtitles
        # Text watermark configuration.
        self.text_watermarks = text_watermarks
        # Transcoding configuration.
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
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigCombineConfigs()
                self.combine_configs.append(temp_model.from_map(k1))

        if m.get('Encryption') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigEncryption()
            self.encryption = temp_model.from_map(m.get('Encryption'))

        self.image_watermarks = []
        if m.get('ImageWatermarks') is not None:
            for k1 in m.get('ImageWatermarks'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarks()
                self.image_watermarks.append(temp_model.from_map(k1))

        if m.get('IsInheritTags') is not None:
            self.is_inherit_tags = m.get('IsInheritTags')

        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitles()
                self.subtitles.append(temp_model.from_map(k1))

        self.text_watermarks = []
        if m.get('TextWatermarks') is not None:
            for k1 in m.get('TextWatermarks'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarks()
                self.text_watermarks.append(temp_model.from_map(k1))

        if m.get('Transcode') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscode()
            self.transcode = temp_model.from_map(m.get('Transcode'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscode(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParams = None,
        template_id: str = None,
    ):
        # Override parameters. If specified, these parameters override the corresponding template parameters.
        self.overwrite_params = overwrite_params
        # Template ID.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParams(DaraModel):
    def __init__(
        self,
        audio: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudio = None,
        container: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsContainer = None,
        mux_config: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfig = None,
        tags: Dict[str, str] = None,
        trans_config: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsTransConfig = None,
        video: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsVideo = None,
    ):
        # Audio settings.
        self.audio = audio
        # Container format settings.
        self.container = container
        # Muxing settings.
        self.mux_config = mux_config
        self.tags = tags
        # Conditional transcoding parameters.
        self.trans_config = trans_config
        # Video settings.
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

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config.to_map()

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('MuxConfig') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TransConfig') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('Video') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsVideo(DaraModel):
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
        # Maximum ABR bitrate (valid only for narrow-high 1):
        # 
        # - Valid range: [10, 50000].
        # 
        # - Unit: Kbps.
        self.abr_max = abr_max
        # Video average bitrate.
        # 
        # - Valid range: [10, 50000].
        # 
        # - Unit: Kbps.
        self.bitrate = bitrate
        # Buffer size:
        # 
        # - Valid range: [1000, 128000].
        # 
        # - Default value: 6000.
        # 
        # - Unit: Kb.
        self.bufsize = bufsize
        # Encoding format.
        self.codec = codec
        # Bitrate-quality control factor.
        # 
        # - Valid range: [0, 51].
        # 
        # - Default value: 23 for H.264, 26 for H.265.
        # 
        # If Crf is set, the Bitrate setting is ignored.
        self.crf = crf
        # Video cropping. Two methods are supported:
        # 
        # - Automatically detect and crop black bars by setting this parameter to "border".
        # 
        # - Custom cropping in the format: width:height:left:top.
        self.crop = crop
        # Frame rate.
        # 
        # - Valid range: (0, 60].
        #   If the input file frame rate exceeds 60, use 60.
        # 
        # - Default value: input file frame rate.
        self.fps = fps
        # Maximum number of frames between keyframes.
        # 
        # - Valid range: [1, 1080000].
        # 
        # - Default value: 250.
        self.gop = gop
        # Height.
        # 
        # - Valid range: [128, 4096].
        # 
        # - Unit: px.
        # 
        # Default value: original video height.
        self.height = height
        # Whether to enable automatic rotation (long-short edge mode).
        self.long_short_mode = long_short_mode
        # Peak video bitrate:
        # 
        # - Valid range: [10, 50000].
        # 
        # - Unit: Kbps.
        self.maxrate = maxrate
        # Add black bars to the video in the format: width:height:left:top.
        self.pad = pad
        # Video color format.
        # Valid values: yuv420p, yuvj420p, and other standard color formats.
        self.pix_fmt = pix_fmt
        # Video encoder preset. This parameter is supported only for H.264.
        # Supported values: veryfast, fast, medium, slow, slower.
        # Default value: medium.
        # 
        # Default value: medium.
        self.preset = preset
        # Encoding profile.
        # Supported values: baseline, main, high.
        # 
        # - baseline: for mobile devices.
        # 
        # - main: for standard-resolution devices.
        # 
        # - high: for high-resolution devices.
        # 
        # Default value: high.
        self.profile = profile
        # Whether to remove the video.
        self.remove = remove
        # Scan mode.
        # Supported values: interlaced, progressive.
        self.scan_mode = scan_mode
        # Width.
        # 
        # - Valid range: [128, 4096].
        # 
        # - Unit: px.
        # 
        # Default value: original video width.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsTransConfig(DaraModel):
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
        # Resolution adjustment method. This parameter takes effect only when both Width and Height are specified. It can be used together with LongShortMode.
        # 
        # Valid values: rescale, crop, pad, none.
        # 
        # Default value: none.
        # 
        # Example: See how to set resolution.
        self.adj_dar_method = adj_dar_method
        # Whether to check audio bitrate. IsCheckAudioBitrate and IsCheckAudioBitrateFail are mutually exclusive. IsCheckAudioBitrateFail takes precedence.
        # 
        # - true: Check. If the input audio bitrate is lower than the output setting, transcode using the input audio bitrate.
        # 
        # - false: Do not check.
        # 
        # Default value:
        # 
        # - If this parameter is empty and the codec differs from the input source: false.
        # 
        # - If this parameter is empty and the codec matches the input source: true.
        self.is_check_audio_bitrate = is_check_audio_bitrate
        # Whether to check audio bitrate. IsCheckAudioBitrate and IsCheckAudioBitrateFail are mutually exclusive. This parameter takes precedence.
        # 
        # - true: Check. If the input audio bitrate is lower than the output setting, return a transcoding failure.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        # Whether to check video resolution. IsCheckReso and IsCheckResoFail are mutually exclusive. IsCheckResoFail takes precedence.
        # 
        # - true: Check. If the input video resolution (width or height) is smaller than the output setting, transcode using the input video resolution.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_reso = is_check_reso
        # Whether to check video resolution. IsCheckReso and IsCheckResoFail are mutually exclusive. This parameter takes precedence.
        # 
        # - true: Check. If the input video resolution (width or height) is smaller than the output setting, return a transcoding failure.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_reso_fail = is_check_reso_fail
        # Whether to check video bitrate. IsCheckVideoBitrate and IsCheckVideoBitrateFail are mutually exclusive. IsCheckVideoBitrateFail takes precedence.
        # 
        # - true: Check. If the input video bitrate is lower than the output setting, transcode using the input video bitrate.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_video_bitrate = is_check_video_bitrate
        # Whether to check video bitrate. IsCheckVideoBitrate and IsCheckVideoBitrateFail are mutually exclusive. This parameter takes precedence.
        # 
        # - true: Check. If the input video bitrate is lower than the output setting, return a transcoding failure.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        # Video transcoding mode. Valid values:
        # 
        # - onepass: generally used for ABR. Faster encoding than twopass.
        # 
        # - twopass: generally used for VBR. Slower encoding than onepass.
        # 
        # - CBR: constant bitrate mode.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfig(DaraModel):
    def __init__(
        self,
        segment: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfigSegment = None,
    ):
        # Segmentation settings.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfigSegment(DaraModel):
    def __init__(
        self,
        duration: str = None,
        force_seg_time: str = None,
    ):
        # Segment length.
        self.duration = duration
        # Forced segmentation time points.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsContainer(DaraModel):
    def __init__(
        self,
        format: str = None,
    ):
        # Container format.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        remove: str = None,
        samplerate: str = None,
        volume: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudioVolume = None,
    ):
        # Audio bitrate of the output file.
        # 
        # - Valid range: [8, 1000]
        # 
        # - Unit: Kbps
        # 
        # - Default value: 128
        self.bitrate = bitrate
        # Number of sound channels.
        # Default value: 2
        self.channels = channels
        # Audio codec format: AAC, MP3, VORBIS, FLAC.
        # Default value: AAC
        # 
        # Default value: AAC.
        self.codec = codec
        # Audio encoding preset.
        # When Codec is AAC, valid values are aac_low, aac_he, aac_he_v2, aac_ld, aac_eld.
        self.profile = profile
        # Whether to remove the audio stream.
        self.remove = remove
        # Sample rate.
        # 
        # - Supported values: 22050, 32000, 44100, 48000, 96000,
        # 
        # - Unit: Hz
        self.samplerate = samplerate
        # Volume control.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudioVolume(DaraModel):
    def __init__(
        self,
        integrated_loudness_target: str = None,
        loudness_range_target: str = None,
        method: str = None,
        true_peak: str = None,
    ):
        # Target volume.
        self.integrated_loudness_target = integrated_loudness_target
        # Volume range.
        self.loudness_range_target = loudness_range_target
        # Volume adjustment method.
        self.method = method
        # Peak volume.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarksOverwriteParams = None,
        template_id: str = None,
    ):
        # Override parameters. If specified, these parameters override the corresponding template parameters.
        self.overwrite_params = overwrite_params
        # Template ID.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarksOverwriteParams(DaraModel):
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
        # Adjust font size based on output video size. Valid values: true / false. Default: false.
        self.adaptive = adaptive
        # Border color.
        self.border_color = border_color
        # Border width.
        self.border_width = border_width
        # Watermark text. Do not Base64 encode. The string must be UTF-8 encoded.
        self.content = content
        # Transparency.
        self.font_alpha = font_alpha
        # Color.
        self.font_color = font_color
        # Font.
        self.font_name = font_name
        # Font size.
        self.font_size = font_size
        # Watermark position, distance from the left.
        self.left = left
        # Watermark position, distance from the top.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitles(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParams = None,
        template_id: str = None,
    ):
        # Override parameters. If specified, these parameters override the corresponding template parameters.
        self.overwrite_params = overwrite_params
        # Template ID
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParams(DaraModel):
    def __init__(
        self,
        char_enc: str = None,
        file: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParamsFile = None,
        format: str = None,
    ):
        # File encoding format.
        self.char_enc = char_enc
        # Subtitle file.
        self.file = file
        # Subtitle file format.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # Media value:
        # 
        # - If Type is OSS, this field is a URL that supports OSS and HTTP protocols.
        # 
        # - If Type is Media, this field is a media asset ID.
        self.media = media
        # Media object type.
        # Valid values:
        # 
        # - OSS: OSS file.
        # 
        # - Media: Media asset ID.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParams = None,
        template_id: str = None,
    ):
        # Override parameters. If specified, these parameters override the corresponding template parameters.
        self.overwrite_params = overwrite_params
        # Template ID.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParams(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        file: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsFile = None,
        height: str = None,
        refer_pos: str = None,
        timeline: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsTimeline = None,
        width: str = None,
    ):
        # Watermark position, x.
        self.dx = dx
        # Watermark position, y.
        self.dy = dy
        # Watermark image file.
        self.file = file
        # The height of the image watermark.
        self.height = height
        # Reference position: TopLeft, TopRight, BottomLeft, BottomRight.<br>
        # Default value: TopLeft.<br>
        self.refer_pos = refer_pos
        # Display time settings.
        self.timeline = timeline
        # Width.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('Timeline') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsTimeline(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        # Display duration in seconds or "ToEND".
        self.duration = duration
        # Start time.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # Media value:
        # 
        # - If Type is OSS, this field is a URL that supports OSS and HTTP protocols.
        # 
        # - If Type is Media, this field is a media asset ID.
        self.media = media
        # Media object type.
        # Valid values:
        # 
        # - OSS: OSS file.
        # 
        # - Media: Media asset ID.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigEncryption(DaraModel):
    def __init__(
        self,
        cipher_text: str = None,
        decrypt_key_uri: str = None,
        encrypt_type: str = None,
        key_service_type: str = None,
    ):
        # Ciphertext of the encryption key for standard encryption.
        self.cipher_text = cipher_text
        # Decryption service endpoint for standard encryption.
        self.decrypt_key_uri = decrypt_key_uri
        # Encryption type.
        self.encrypt_type = encrypt_type
        # Key service type. Only KMS and Base64 are supported.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigCombineConfigs(DaraModel):
    def __init__(
        self,
        audio_index: str = None,
        duration: float = None,
        start: float = None,
        video_index: str = None,
    ):
        # Audio stream index
        # 
        # This parameter is required.
        self.audio_index = audio_index
        # Duration of the input stream. Default: video duration.
        self.duration = duration
        # Start time of the input stream. Default: 0
        self.start = start
        # Video stream index
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        output_url: str = None,
        type: str = None,
    ):
        # Media value:
        # 
        # - If Type is OSS, this field is a URL that supports OSS and HTTP protocols.
        # 
        # - If Type is Media, this field is a media asset ID.
        self.media = media
        # Transcoded stream URL. Specify this parameter only when outputting to a media stream.
        self.output_url = output_url
        # Media object type.
        # Valid values:
        # 
        # - OSS: OSS file.
        # 
        # - Media: Media asset ID.
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

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMeta(DaraModel):
    def __init__(
        self,
        audio_stream_info_list: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaAudioStreamInfoList] = None,
        file_basic_info: main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaFileBasicInfo = None,
        video_stream_info_list: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaVideoStreamInfoList] = None,
    ):
        # Audio stream information.
        self.audio_stream_info_list = audio_stream_info_list
        # Basic file information.
        self.file_basic_info = file_basic_info
        # Video stream information.
        self.video_stream_info_list = video_stream_info_list

    def validate(self):
        if self.audio_stream_info_list:
            for v1 in self.audio_stream_info_list:
                 if v1:
                    v1.validate()
        if self.file_basic_info:
            self.file_basic_info.validate()
        if self.video_stream_info_list:
            for v1 in self.video_stream_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioStreamInfoList'] = []
        if self.audio_stream_info_list is not None:
            for k1 in self.audio_stream_info_list:
                result['AudioStreamInfoList'].append(k1.to_map() if k1 else None)

        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()

        result['VideoStreamInfoList'] = []
        if self.video_stream_info_list is not None:
            for k1 in self.video_stream_info_list:
                result['VideoStreamInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_stream_info_list = []
        if m.get('AudioStreamInfoList') is not None:
            for k1 in m.get('AudioStreamInfoList'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k1))

        if m.get('FileBasicInfo') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k1 in m.get('VideoStreamInfoList'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k1))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaVideoStreamInfoList(DaraModel):
    def __init__(
        self,
        avg_fps: str = None,
        bit_rate: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        dar: str = None,
        duration: str = None,
        fps: str = None,
        has_bframes: str = None,
        height: str = None,
        index: str = None,
        lang: str = None,
        level: str = None,
        num_frames: str = None,
        pix_fmt: str = None,
        profile: str = None,
        rotate: str = None,
        sar: str = None,
        start_time: str = None,
        time_base: str = None,
        width: str = None,
    ):
        # Average frame rate.
        self.avg_fps = avg_fps
        # Bitrate.
        self.bit_rate = bit_rate
        # Encoding format name.
        self.codec_long_name = codec_long_name
        # Encoding format.
        self.codec_name = codec_name
        # Codec tag.
        self.codec_tag = codec_tag
        # Codec tag string.
        self.codec_tag_string = codec_tag_string
        # Codec time base.
        self.codec_time_base = codec_time_base
        # Display aspect ratio.
        self.dar = dar
        # Duration (unit: seconds).
        self.duration = duration
        # Frame rate.
        self.fps = fps
        # Whether B-frames exist.
        # Valid values:
        # 
        # - 0: No B-frames,
        # 
        # - 1: One B-frame,
        # 
        # - 2: Multiple consecutive B-frames.
        self.has_bframes = has_bframes
        # Height.
        self.height = height
        # Stream index.
        self.index = index
        # Language.
        self.lang = lang
        # Encoding level.
        self.level = level
        # Total number of frames.
        self.num_frames = num_frames
        # Color storage format.
        self.pix_fmt = pix_fmt
        # Encoder preset.
        self.profile = profile
        # Video rotation angle.
        # Valid values: 0, 90, 180, 270.
        # Default value: 0
        self.rotate = rotate
        # Sample aspect ratio.
        self.sar = sar
        # Start time.
        self.start_time = start_time
        # Time base.
        self.time_base = time_base
        # Width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_fps is not None:
            result['Avg_fps'] = self.avg_fps

        if self.bit_rate is not None:
            result['Bit_rate'] = self.bit_rate

        if self.codec_long_name is not None:
            result['Codec_long_name'] = self.codec_long_name

        if self.codec_name is not None:
            result['Codec_name'] = self.codec_name

        if self.codec_tag is not None:
            result['Codec_tag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['Codec_tag_string'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['Codec_time_base'] = self.codec_time_base

        if self.dar is not None:
            result['Dar'] = self.dar

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.has_bframes is not None:
            result['Has_b_frames'] = self.has_bframes

        if self.height is not None:
            result['Height'] = self.height

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.sar is not None:
            result['Sar'] = self.sar

        if self.start_time is not None:
            result['Start_time'] = self.start_time

        if self.time_base is not None:
            result['Time_base'] = self.time_base

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avg_fps') is not None:
            self.avg_fps = m.get('Avg_fps')

        if m.get('Bit_rate') is not None:
            self.bit_rate = m.get('Bit_rate')

        if m.get('Codec_long_name') is not None:
            self.codec_long_name = m.get('Codec_long_name')

        if m.get('Codec_name') is not None:
            self.codec_name = m.get('Codec_name')

        if m.get('Codec_tag') is not None:
            self.codec_tag = m.get('Codec_tag')

        if m.get('Codec_tag_string') is not None:
            self.codec_tag_string = m.get('Codec_tag_string')

        if m.get('Codec_time_base') is not None:
            self.codec_time_base = m.get('Codec_time_base')

        if m.get('Dar') is not None:
            self.dar = m.get('Dar')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Has_b_frames') is not None:
            self.has_bframes = m.get('Has_b_frames')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('Sar') is not None:
            self.sar = m.get('Sar')

        if m.get('Start_time') is not None:
            self.start_time = m.get('Start_time')

        if m.get('Time_base') is not None:
            self.time_base = m.get('Time_base')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaFileBasicInfo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        duration: str = None,
        file_name: str = None,
        file_size: str = None,
        file_status: str = None,
        file_type: str = None,
        file_url: str = None,
        format_name: str = None,
        height: str = None,
        media_id: str = None,
        region: str = None,
        width: str = None,
    ):
        # Video bitrate.
        self.bitrate = bitrate
        # Video duration (unit: seconds).
        self.duration = duration
        # File name.
        self.file_name = file_name
        # File size. Unit: Byte.
        self.file_size = file_size
        # File status.
        self.file_status = file_status
        # File type. Valid values: source_file, transcode_file
        self.file_type = file_type
        # File URL.
        self.file_url = file_url
        # Video format name.
        self.format_name = format_name
        # Height.
        self.height = height
        # Media asset ID.
        self.media_id = media_id
        # File region.
        self.region = region
        # Width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_status is not None:
            result['FileStatus'] = self.file_status

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.format_name is not None:
            result['FormatName'] = self.format_name

        if self.height is not None:
            result['Height'] = self.height

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.region is not None:
            result['Region'] = self.region

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaAudioStreamInfoList(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channel_layout: str = None,
        channels: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: str = None,
        index: str = None,
        lang: str = None,
        sample_fmt: str = None,
        sample_rate: str = None,
        start_time: str = None,
        timebase: str = None,
    ):
        # Bitrate.
        self.bitrate = bitrate
        # Channel layout.
        self.channel_layout = channel_layout
        # Number of sound channels.
        self.channels = channels
        # Encoding format name.
        self.codec_long_name = codec_long_name
        # Encoding format.
        self.codec_name = codec_name
        # Codec tag.
        self.codec_tag = codec_tag
        # Codec tag name.
        self.codec_tag_string = codec_tag_string
        # Codec time base.
        self.codec_time_base = codec_time_base
        # Duration (unit: seconds).
        self.duration = duration
        # Stream index.
        self.index = index
        # Language.
        self.lang = lang
        # Sample format.
        self.sample_fmt = sample_fmt
        # Sample rate (unit: Hz).
        self.sample_rate = sample_rate
        # Start time.
        self.start_time = start_time
        # Time base.
        self.timebase = timebase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListInputGroup(DaraModel):
    def __init__(
        self,
        input_url: str = None,
        media: str = None,
        type: str = None,
    ):
        # Media stream URL. Specify this parameter only when transcoding a media stream.
        self.input_url = input_url
        # Media value:
        # 
        # - If Type is OSS, this field is a URL that supports OSS and HTTP protocols.
        # 
        # - If Type is Media, this field is a media asset ID.
        self.media = media
        # Media object type.
        # Valid values:
        # 
        # - OSS: OSS file.
        # 
        # - Media: Media asset ID.
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

class GetTranscodeJobResponseBodyTranscodeParentJobScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # Pipeline ID.
        self.pipeline_id = pipeline_id
        # Job priority. Higher numbers indicate higher priority. Valid range: 1–10.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroup(DaraModel):
    def __init__(
        self,
        output: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupOutput = None,
        process_config: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfig = None,
    ):
        # Output media configuration.
        self.output = output
        # Job processing configuration.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ProcessConfig') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfig()
            self.process_config = temp_model.from_map(m.get('ProcessConfig'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfig(DaraModel):
    def __init__(
        self,
        combine_configs: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigCombineConfigs] = None,
        encryption: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigEncryption = None,
        image_watermarks: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarks] = None,
        subtitles: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitles] = None,
        text_watermarks: List[main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarks] = None,
        transcode: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscode = None,
    ):
        # Multi-input merging configuration
        self.combine_configs = combine_configs
        # Encryption configuration.
        self.encryption = encryption
        # Image watermark configuration.
        self.image_watermarks = image_watermarks
        # Subtitle embedding configuration.
        self.subtitles = subtitles
        # Text watermark configuration.
        self.text_watermarks = text_watermarks
        # Transcoding configuration.
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
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigCombineConfigs()
                self.combine_configs.append(temp_model.from_map(k1))

        if m.get('Encryption') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigEncryption()
            self.encryption = temp_model.from_map(m.get('Encryption'))

        self.image_watermarks = []
        if m.get('ImageWatermarks') is not None:
            for k1 in m.get('ImageWatermarks'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarks()
                self.image_watermarks.append(temp_model.from_map(k1))

        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitles()
                self.subtitles.append(temp_model.from_map(k1))

        self.text_watermarks = []
        if m.get('TextWatermarks') is not None:
            for k1 in m.get('TextWatermarks'):
                temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarks()
                self.text_watermarks.append(temp_model.from_map(k1))

        if m.get('Transcode') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscode()
            self.transcode = temp_model.from_map(m.get('Transcode'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscode(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParams = None,
        template_id: str = None,
    ):
        # Override parameters. If specified, these parameters override the corresponding template parameters.
        self.overwrite_params = overwrite_params
        # Template ID.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParams(DaraModel):
    def __init__(
        self,
        audio: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudio = None,
        container: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsContainer = None,
        mux_config: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig = None,
        trans_config: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig = None,
        video: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsVideo = None,
    ):
        # Audio settings.
        self.audio = audio
        # Container format settings.
        self.container = container
        # Muxing settings.
        self.mux_config = mux_config
        # Conditional transcoding parameters.
        self.trans_config = trans_config
        # Video settings.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('MuxConfig') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('TransConfig') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('Video') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsVideo(DaraModel):
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
        # Maximum ABR bitrate (valid only for narrow-high 1)
        # 
        # - Valid range: [10, 50000],
        # 
        # - Unit: Kbps.
        self.abr_max = abr_max
        # Video average bitrate.
        # 
        # - Valid range: [10, 50000].
        # 
        # - Unit: Kbps.
        self.bitrate = bitrate
        # Buffer size
        # 
        # - Valid range: [1000, 128000]
        # 
        # - Default value: 6000
        # 
        # - Unit: Kb
        self.bufsize = bufsize
        # Encoding format.
        self.codec = codec
        # Bitrate-quality control factor.
        # 
        # - Valid range: [0, 51].
        # 
        # - Default value: 23 for H.264, 26 for H.265.
        # 
        # - If Crf is set, the Bitrate setting is ignored.
        self.crf = crf
        # Video cropping.
        # Two methods are supported.
        # Automatically detect and crop black bars by setting this parameter to "border".
        # Custom cropping in the format: width:height:left:top.
        # Example: 1280:800:0:140
        self.crop = crop
        # Frame rate.
        # 
        # - Valid range: (0, 60].
        # 
        # - If the input file frame rate exceeds 60, use 60.
        # 
        # - Default value: input file frame rate.
        self.fps = fps
        # Maximum number of frames between keyframes.
        # 
        # - Valid range: [1, 1080000].
        # 
        # - Default value: 250.
        self.gop = gop
        # Height.
        # 
        # - Valid range: [128, 4096].
        # 
        # - Unit: px.
        # 
        # - Default value: original video height.
        self.height = height
        # Whether to enable automatic rotation (long-short edge mode).
        self.long_short_mode = long_short_mode
        # Peak video bitrate
        # 
        # - Valid range: [10, 50000]
        # 
        # - Unit: Kbps.
        self.maxrate = maxrate
        # Black bar padding parameters
        # 
        # - Format: width:height:left:top.
        # 
        # - Example: 1280:800:0:140
        self.pad = pad
        # Video color format.
        # Valid values: yuv420p, yuvj420p, and other standard color formats.
        self.pix_fmt = pix_fmt
        # Video encoder preset. This parameter is supported only for H.264.
        # Supported values: veryfast, fast, medium, slow, slower.
        # Default value: medium.
        self.preset = preset
        # Encoding profile.
        # Supported values: baseline, main, high.
        # 
        # - baseline: for mobile devices.
        # 
        # - main: for standard-resolution devices.
        # 
        # - high: for high-resolution devices.
        # 
        # Default value: high.
        self.profile = profile
        # Whether to remove the video.
        self.remove = remove
        # Scan mode.
        # Supported values: interlaced, progressive.
        self.scan_mode = scan_mode
        # Width.
        # 
        # - Valid range: [128, 4096].
        # 
        # - Unit: px.
        # 
        # - Default value: original video width.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig(DaraModel):
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
        # Resolution adjustment method. This parameter takes effect only when both Width and Height are specified. It can be used together with LongShortMode.
        # 
        # Valid values: rescale, crop, pad, none.
        # 
        # Default value: none.
        self.adj_dar_method = adj_dar_method
        # Whether to check audio bitrate. IsCheckAudioBitrate and IsCheckAudioBitrateFail are mutually exclusive. IsCheckAudioBitrateFail takes precedence.
        # 
        # - true: Check. If the input audio bitrate is lower than the output setting, transcode using the input audio bitrate.
        # 
        # - false: Do not check.
        # 
        # Default value:
        # 
        # - If this parameter is empty and the codec differs from the input source: false.
        # 
        # - If this parameter is empty and the codec matches the input source: true.
        self.is_check_audio_bitrate = is_check_audio_bitrate
        # Whether to check audio bitrate. IsCheckAudioBitrate and IsCheckAudioBitrateFail are mutually exclusive. This parameter takes precedence.
        # 
        # - true: Check. If the input audio bitrate is lower than the output setting, return a transcoding failure.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        # Whether to check video resolution. IsCheckReso and IsCheckResoFail are mutually exclusive. IsCheckResoFail takes precedence.
        # 
        # - true: Check. If the input video resolution (width or height) is smaller than the output setting, transcode using the input video resolution.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_reso = is_check_reso
        # Whether to check video resolution. IsCheckReso and IsCheckResoFail are mutually exclusive. This parameter takes precedence.
        # 
        # - true: Check. If the input video resolution (width or height) is smaller than the output setting, return a transcoding failure.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_reso_fail = is_check_reso_fail
        # Whether to check video bitrate. IsCheckVideoBitrate and IsCheckVideoBitrateFail are mutually exclusive. IsCheckVideoBitrateFail takes precedence.
        # 
        # - true: Check. If the input video bitrate is lower than the output setting, transcode using the input video bitrate.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_video_bitrate = is_check_video_bitrate
        # Whether to check video bitrate. IsCheckVideoBitrate and IsCheckVideoBitrateFail are mutually exclusive. This parameter takes precedence.
        # 
        # - true: Check. If the input video bitrate is lower than the output setting, return a transcoding failure.
        # 
        # - false: Do not check.
        # 
        # Default value: false.
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        # Video transcoding mode. Valid values:
        # 
        # - onepass: generally used for ABR. Faster encoding than twopass.
        # 
        # - twopass: generally used for VBR. Slower encoding than onepass.
        # 
        # - CBR: constant bitrate mode.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig(DaraModel):
    def __init__(
        self,
        segment: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment = None,
    ):
        # Segmentation settings.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment(DaraModel):
    def __init__(
        self,
        duration: str = None,
        force_seg_time: str = None,
    ):
        # Segment length.
        self.duration = duration
        # Forced segmentation time points.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsContainer(DaraModel):
    def __init__(
        self,
        format: str = None,
    ):
        # Container format.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        remove: str = None,
        samplerate: str = None,
        volume: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume = None,
    ):
        # Audio bitrate of the output file.
        # 
        # - Valid range: [8, 1000]
        # 
        # - Unit: Kbps
        # 
        # - Default value: 128
        self.bitrate = bitrate
        # Number of sound channels.
        # Default value: 2
        self.channels = channels
        # Audio codec format: AAC, MP3, VORBIS, FLAC.
        # Default value: AAC
        self.codec = codec
        # Audio encoding preset.
        # When Codec is AAC, valid values are aac_low, aac_he, aac_he_v2, aac_ld, aac_eld.
        self.profile = profile
        # Whether to remove the audio stream.
        self.remove = remove
        # Sample rate.
        # 
        # - Default value: 44100
        # 
        # - Supported values: 22050, 32000, 44100, 48000, 96000,
        # 
        # - Unit: Hz
        self.samplerate = samplerate
        # Volume control.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume(DaraModel):
    def __init__(
        self,
        integrated_loudness_target: str = None,
        loudness_range_target: str = None,
        method: str = None,
        true_peak: str = None,
    ):
        # Target volume.
        self.integrated_loudness_target = integrated_loudness_target
        # Volume range.
        self.loudness_range_target = loudness_range_target
        # Volume adjustment method.
        self.method = method
        # Peak volume.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarksOverwriteParams = None,
        template_id: str = None,
    ):
        # Override parameters. If specified, these parameters override the corresponding template parameters.
        self.overwrite_params = overwrite_params
        # Template ID.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarksOverwriteParams(DaraModel):
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
        # Adjust font size based on output video size. Valid values: true / false. Default: false.
        self.adaptive = adaptive
        # Border color.
        self.border_color = border_color
        # Border width.
        self.border_width = border_width
        # Watermark text. Do not Base64 encode. The string must be UTF-8 encoded.
        self.content = content
        # Transparency.
        self.font_alpha = font_alpha
        # Color.
        self.font_color = font_color
        # Font.
        self.font_name = font_name
        # Font size.
        self.font_size = font_size
        # Watermark position, distance from the left.
        self.left = left
        # Watermark position, distance from the top.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitles(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParams = None,
        template_id: str = None,
    ):
        # Override parameters. If specified, these parameters override the corresponding template parameters.
        self.overwrite_params = overwrite_params
        # Template ID.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParams(DaraModel):
    def __init__(
        self,
        char_enc: str = None,
        file: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParamsFile = None,
        format: str = None,
    ):
        # File encoding format.
        self.char_enc = char_enc
        # Subtitle file.
        self.file = file
        # Subtitle file format.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # Media value:
        # 
        # - If Type is OSS, this field is a URL that supports OSS and HTTP protocols.
        # 
        # - If Type is Media, this field is a media asset ID.
        self.media = media
        # Media object type.
        # Valid values:
        # 
        # - OSS: OSS file.
        # 
        # - Media: Media asset ID.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParams = None,
        template_id: str = None,
    ):
        # Override parameters. If specified, these parameters override the corresponding template parameters.
        self.overwrite_params = overwrite_params
        # Template ID.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParams(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        file: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsFile = None,
        height: str = None,
        refer_pos: str = None,
        timeline: main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline = None,
        width: str = None,
    ):
        # Watermark position, x.
        self.dx = dx
        # Watermark position, y.
        self.dy = dy
        # Watermark image file.
        self.file = file
        # Height.
        self.height = height
        # Reference position: TopLeft, TopRight, BottomLeft, BottomRight. Default: TopLeft.
        self.refer_pos = refer_pos
        # Display time settings.
        self.timeline = timeline
        # Width.
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
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('Timeline') is not None:
            temp_model = main_models.GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        # Display duration in seconds or "ToEND".
        self.duration = duration
        # Start time.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # Media value:
        # 
        # - If Type is OSS, this field is a URL that supports OSS and HTTP protocols.
        # 
        # - If Type is Media, this field is a media asset ID.
        self.media = media
        # Media object type.
        # Valid values:
        # 
        # - OSS: OSS file.
        # 
        # - Media: Media asset ID.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigEncryption(DaraModel):
    def __init__(
        self,
        cipher_text: str = None,
        decrypt_key_uri: str = None,
        encrypt_type: str = None,
        key_service_type: str = None,
    ):
        # Ciphertext of the encryption key for standard encryption.
        self.cipher_text = cipher_text
        # Decryption service endpoint for standard encryption.
        self.decrypt_key_uri = decrypt_key_uri
        # Encryption type.
        self.encrypt_type = encrypt_type
        # Key service type. Only KMS and Base64 are supported.
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigCombineConfigs(DaraModel):
    def __init__(
        self,
        audio_index: str = None,
        duration: float = None,
        start: float = None,
        video_index: str = None,
    ):
        # Audio stream index
        # 
        # This parameter is required.
        self.audio_index = audio_index
        # Duration of the input stream. Default: video duration.
        self.duration = duration
        # Start time of the input stream. Default: 0
        self.start = start
        # Video stream index
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

class GetTranscodeJobResponseBodyTranscodeParentJobOutputGroupOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        output_url: str = None,
        type: str = None,
    ):
        # Media value:
        # 
        # - If Type is OSS, this field is a URL that supports OSS and HTTP protocols.
        # 
        # - If Type is Media, this field is a media asset ID.
        self.media = media
        # Output stream URL.
        self.output_url = output_url
        # Media object type.
        # Valid values:
        # 
        # - OSS: OSS file.
        # 
        # - Media: Media asset ID.
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

class GetTranscodeJobResponseBodyTranscodeParentJobInputGroup(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # Media value:
        # 
        # - If Type is OSS, this field is a URL that supports OSS and HTTP protocols.
        # 
        # - If Type is Media, this field is a media asset ID.
        self.media = media
        # Media object type.
        # Valid values:
        # 
        # - OSS: OSS file.
        # 
        # - Media: Media asset ID.
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

