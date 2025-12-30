# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitTranscodeJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transcode_parent_job: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJob = None,
    ):
        # The request ID.
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJob()
            self.transcode_parent_job = temp_model.from_map(m.get('TranscodeParentJob'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJob(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        input_group: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobInputGroup] = None,
        job_count: int = None,
        name: str = None,
        output_group: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroup] = None,
        parent_job_id: str = None,
        percent: int = None,
        request_id: str = None,
        schedule_config: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobScheduleConfig = None,
        status: str = None,
        submit_time: str = None,
        transcode_job_list: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobList] = None,
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
        # The state of the job. Success: At least one of the subjobs is successful. Fail: All subjobs failed.
        self.status = status
        # The time when the job was submitted. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.submit_time = submit_time
        # The list of subjobs.
        self.transcode_job_list = transcode_job_list
        # The source of the job. Valid values: API, WorkFlow, and Console.
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
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobInputGroup()
                self.input_group.append(temp_model.from_map(k1))

        if m.get('JobCount') is not None:
            self.job_count = m.get('JobCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.output_group = []
        if m.get('OutputGroup') is not None:
            for k1 in m.get('OutputGroup'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroup()
                self.output_group.append(temp_model.from_map(k1))

        if m.get('ParentJobId') is not None:
            self.parent_job_id = m.get('ParentJobId')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        self.transcode_job_list = []
        if m.get('TranscodeJobList') is not None:
            for k1 in m.get('TranscodeJobList'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobList()
                self.transcode_job_list.append(temp_model.from_map(k1))

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        input_group: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListInputGroup] = None,
        job_id: str = None,
        job_index: int = None,
        name: str = None,
        out_file_meta: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMeta = None,
        output: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutput = None,
        parent_job_id: str = None,
        process_config: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfig = None,
        request_id: str = None,
        schedule_config: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListScheduleConfig = None,
        status: str = None,
        submit_result_json: Dict[str, Any] = None,
        submit_time: str = None,
        user_data: str = None,
    ):
        # The time when the job was created.
        self.create_time = create_time
        # The time when the job was complete.
        self.finish_time = finish_time
        # The input group of the job. An input of a single file indicates a transcoding job. An input of multiple files indicates an audio and video stream merge job.
        self.input_group = input_group
        # The subjob ID.
        self.job_id = job_id
        # The index number of the subjob in the entire job.
        self.job_index = job_index
        # The job name.
        self.name = name
        # The media information about the video generated by the job.
        self.out_file_meta = out_file_meta
        # The output file configuration.
        self.output = output
        # The main job ID.
        self.parent_job_id = parent_job_id
        # The transcoding configuration.
        self.process_config = process_config
        # The ID of the request that submitted the job.
        self.request_id = request_id
        # The scheduling information about the job.
        self.schedule_config = schedule_config
        # The state of the transcoding job. Valid values:
        # 
        # *   Init: The job is submitted.
        # *   Processing: The job is in progress.
        # *   Success: The job is successful.
        # *   Fail: The job failed.
        # *   Deleted: The job is deleted.
        self.status = status
        # The job submission result.
        self.submit_result_json = submit_result_json
        # The time when the job was submitted.
        self.submit_time = submit_time
        # The user data.
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
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListInputGroup()
                self.input_group.append(temp_model.from_map(k1))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobIndex') is not None:
            self.job_index = m.get('JobIndex')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutFileMeta') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMeta()
            self.out_file_meta = temp_model.from_map(m.get('OutFileMeta'))

        if m.get('Output') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ParentJobId') is not None:
            self.parent_job_id = m.get('ParentJobId')

        if m.get('ProcessConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfig()
            self.process_config = temp_model.from_map(m.get('ProcessConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListScheduleConfig()
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListScheduleConfig(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfig(DaraModel):
    def __init__(
        self,
        combine_configs: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigCombineConfigs] = None,
        encryption: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigEncryption = None,
        image_watermarks: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarks] = None,
        subtitles: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitles] = None,
        text_watermarks: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarks] = None,
        transcode: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscode = None,
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
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigCombineConfigs()
                self.combine_configs.append(temp_model.from_map(k1))

        if m.get('Encryption') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigEncryption()
            self.encryption = temp_model.from_map(m.get('Encryption'))

        self.image_watermarks = []
        if m.get('ImageWatermarks') is not None:
            for k1 in m.get('ImageWatermarks'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarks()
                self.image_watermarks.append(temp_model.from_map(k1))

        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitles()
                self.subtitles.append(temp_model.from_map(k1))

        self.text_watermarks = []
        if m.get('TextWatermarks') is not None:
            for k1 in m.get('TextWatermarks'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarks()
                self.text_watermarks.append(temp_model.from_map(k1))

        if m.get('Transcode') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscode()
            self.transcode = temp_model.from_map(m.get('Transcode'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscode(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParams = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParams(DaraModel):
    def __init__(
        self,
        audio: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudio = None,
        container: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsContainer = None,
        mux_config: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfig = None,
        trans_config: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsTransConfig = None,
        video: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsVideo = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('MuxConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('TransConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('Video') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsVideo(DaraModel):
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
        # The maximum ABR. This parameter takes effect only for Narrowband HD 1.0. Valid values: [10,50000]. Unit: Kbit/s.
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
        # *   Default value: 23 if the encoding format is H.264, or Default value when the Codec parameter is set to H.265: 26.
        # 
        # If this parameter is specified, the value of Bitrate becomes invalid.
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
        # Specifies whether to enable the auto-rotate screen feature.
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
        # Specifies whether to remove the video.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsTransConfig(DaraModel):
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
        # Default values:
        # 
        # *   If this parameter is not specified and the codec of the output audio is different from that of the input audio, the default value is false.
        # *   If this parameter is not specified and the codec of the output audio is the same as that of the input audio, the default value is true.
        self.is_check_audio_bitrate = is_check_audio_bitrate
        # Specifies whether to check the audio bitrate. You can specify only one of the IsCheckAudioBitrate and IsCheckAudioBitrateFail parameters. The priority of the IsCheckAudioBitrateFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the bitrate of the input audio is less than that of the output audio, the transcoding job fails.
        # *   false: does not check the video resolution. This is the default value.
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        # Specifies whether to check the video resolution. You can specify only one of the IsCheckReso and IsCheckResoFail parameters. The priority of the IsCheckResoFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the width or height of the input video is less than that of the output video, the resolution of the input video is used for transcoding.
        # *   false: does not check the video resolution. This is the default value.
        self.is_check_reso = is_check_reso
        # Specifies whether to check the video resolution. You can specify only one of the IsCheckReso and IsCheckResoFail parameters. The priority of the IsCheckResoFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the width or height of the input video is less than that of the output video, the transcoding job fails.
        # *   false: does not check the video resolution. This is the default value.
        self.is_check_reso_fail = is_check_reso_fail
        # Specifies whether to check the video bitrate. You can specify only one of the IsCheckVideoBitrate and IsCheckVideoBitrateFail parameters. The priority of the IsCheckVideoBitrateFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the bitrate of the input video is less than that of the output video, the bitrate of the input video is used for transcoding.
        # *   false: does not check the video resolution. This is the default value.
        self.is_check_video_bitrate = is_check_video_bitrate
        # Specifies whether to check the video bitrate. You can specify only one of the IsCheckVideoBitrate and IsCheckVideoBitrateFail parameters. The priority of the IsCheckVideoBitrateFail parameter is higher. Valid values:
        # 
        # *   true: checks the video resolution. If the bitrate of the input video is less than that of the output video, the transcoding job fails.
        # *   false: does not check the video resolution. This is the default value.
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        # The video transcoding mode. Valid values:
        # 
        # *   onepass: You can set this parameter to onepass if the Bitrate parameter is set to ABR. This is the default value. The encoding speed of this mode is faster than that of the twopass mode.
        # *   twopass: You can set this parameter to twopass if the Bitrate parameter is set to VBR. The encoding speed of this mode is slower than that of the onepass mode.
        # *   CBR: the constant bitrate mode.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfig(DaraModel):
    def __init__(
        self,
        segment: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfigSegment = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsMuxConfigSegment(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsContainer(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        remove: str = None,
        samplerate: str = None,
        volume: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudioVolume = None,
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
        # Specifies whether to delete the audio stream.
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTranscodeOverwriteParamsAudioVolume(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarksOverwriteParams = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigTextWatermarksOverwriteParams(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitles(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParams = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParams(DaraModel):
    def __init__(
        self,
        char_enc: str = None,
        file: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParamsFile = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigSubtitlesOverwriteParamsFile(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParams = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParams(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        file: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsFile = None,
        height: str = None,
        refer_pos: str = None,
        timeline: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsTimeline = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('Timeline') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsTimeline(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigImageWatermarksOverwriteParamsFile(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigEncryption(DaraModel):
    def __init__(
        self,
        cipher_text: str = None,
        decrypt_key_uri: str = None,
        encrypt_type: str = None,
        key_service_type: str = None,
    ):
        # The ciphertext of HLS encryption.
        self.cipher_text = cipher_text
        # The address of the decryption service for HLS encryption.
        self.decrypt_key_uri = decrypt_key_uri
        # Specifies the encryption type.
        self.encrypt_type = encrypt_type
        # The type of the key service. Valid values: KMS and Base64.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListProcessConfigCombineConfigs(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        output_url: str = None,
        type: str = None,
    ):
        # The media object.
        # 
        # *   If Type is set to OSS, set this parameter to the URL of an OSS object. Both the OSS and HTTP protocols are supported.
        # *   If Type is set to Media, set this parameter to the ID of a media asset.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMeta(DaraModel):
    def __init__(
        self,
        audio_stream_info_list: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaAudioStreamInfoList] = None,
        file_basic_info: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaFileBasicInfo = None,
        video_stream_info_list: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaVideoStreamInfoList] = None,
    ):
        # The information about the audio stream.
        self.audio_stream_info_list = audio_stream_info_list
        # The basic file information.
        self.file_basic_info = file_basic_info
        # The information about the video stream.
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
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k1))

        if m.get('FileBasicInfo') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k1 in m.get('VideoStreamInfoList'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k1))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaVideoStreamInfoList(DaraModel):
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
        # The average frame rate.
        self.avg_fps = avg_fps
        # The bitrate.
        self.bit_rate = bit_rate
        # The name of the encoding format.
        self.codec_long_name = codec_long_name
        # The encoding format.
        self.codec_name = codec_name
        # The tag of the encoding format.
        self.codec_tag = codec_tag
        # The tag string of the encoding format.
        self.codec_tag_string = codec_tag_string
        # The time base of the encoder.
        self.codec_time_base = codec_time_base
        # The display aspect ratio.
        self.dar = dar
        # The duration of the stream. Unit: seconds.
        self.duration = duration
        # The frame rate.
        self.fps = fps
        # Indicates whether the video stream contains bidirectional frames (B-frames). Valid values:
        # 
        # *   0: The stream contains no B-frames.
        # *   1: The stream contains one B-frame.
        # *   2: The stream contains multiple consecutive B-frames.
        self.has_bframes = has_bframes
        # The height of the output video.
        self.height = height
        # The sequence number of the stream.
        self.index = index
        # The language of the stream.
        self.lang = lang
        # The codec level.
        self.level = level
        # The total number of frames.
        self.num_frames = num_frames
        # The pixel format.
        self.pix_fmt = pix_fmt
        # The encoder profile.
        self.profile = profile
        # The rotation angle of the video image. Valid values: 0, 90, 180, and 270. Default value: 0.
        self.rotate = rotate
        # The aspect ratio of the area from which the sampling points are collected.
        self.sar = sar
        # The start time of the stream.
        self.start_time = start_time
        # The time base.
        self.time_base = time_base
        # The width of the output video.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaFileBasicInfo(DaraModel):
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
        # The video bitrate.
        self.bitrate = bitrate
        # The duration of the video. Unit: seconds.
        self.duration = duration
        # The file name.
        self.file_name = file_name
        # The file size. Unit: bytes.
        self.file_size = file_size
        # The state of the file.
        self.file_status = file_status
        # The file type. Valid values: source_file and transcode_file.
        self.file_type = file_type
        # The URL of the file.
        self.file_url = file_url
        # The name of the video format.
        self.format_name = format_name
        # The height of the output video.
        self.height = height
        # The ID of the media asset.
        self.media_id = media_id
        # The region in which the file resides.
        self.region = region
        # The width of the output video.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListOutFileMetaAudioStreamInfoList(DaraModel):
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
        # The bitrate.
        self.bitrate = bitrate
        # The sound channel layout.
        self.channel_layout = channel_layout
        # The number of sound channels.
        self.channels = channels
        # The name of the encoding format.
        self.codec_long_name = codec_long_name
        # The encoding format.
        self.codec_name = codec_name
        # The encoder tag.
        self.codec_tag = codec_tag
        # The name of the encoder tag.
        self.codec_tag_string = codec_tag_string
        # The time base of the encoder.
        self.codec_time_base = codec_time_base
        # The duration of the stream. Unit: seconds.
        self.duration = duration
        # The sequence number of the stream.
        self.index = index
        # The language of the stream.
        self.lang = lang
        # The sample format.
        self.sample_fmt = sample_fmt
        # The sampling rate. Unit: Hz.
        self.sample_rate = sample_rate
        # The start time of the stream.
        self.start_time = start_time
        # The time base.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobTranscodeJobListInputGroup(DaraModel):
    def __init__(
        self,
        input_url: str = None,
        media: str = None,
        type: str = None,
    ):
        # The URL of the input stream:
        # 
        # *   This parameter takes effect only when Type is set to Media. You can select a specific file within the media asset as an input.
        # *   The system checks whether the input URL exists within the media asset.
        self.input_url = input_url
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobScheduleConfig(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroup(DaraModel):
    def __init__(
        self,
        output: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupOutput = None,
        process_config: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfig = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ProcessConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfig()
            self.process_config = temp_model.from_map(m.get('ProcessConfig'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfig(DaraModel):
    def __init__(
        self,
        combine_configs: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigCombineConfigs] = None,
        encryption: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigEncryption = None,
        image_watermarks: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarks] = None,
        subtitles: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitles] = None,
        text_watermarks: List[main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarks] = None,
        transcode: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscode = None,
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
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigCombineConfigs()
                self.combine_configs.append(temp_model.from_map(k1))

        if m.get('Encryption') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigEncryption()
            self.encryption = temp_model.from_map(m.get('Encryption'))

        self.image_watermarks = []
        if m.get('ImageWatermarks') is not None:
            for k1 in m.get('ImageWatermarks'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarks()
                self.image_watermarks.append(temp_model.from_map(k1))

        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitles()
                self.subtitles.append(temp_model.from_map(k1))

        self.text_watermarks = []
        if m.get('TextWatermarks') is not None:
            for k1 in m.get('TextWatermarks'):
                temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarks()
                self.text_watermarks.append(temp_model.from_map(k1))

        if m.get('Transcode') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscode()
            self.transcode = temp_model.from_map(m.get('Transcode'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscode(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParams = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParams(DaraModel):
    def __init__(
        self,
        audio: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudio = None,
        container: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsContainer = None,
        mux_config: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig = None,
        trans_config: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig = None,
        video: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsVideo = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('MuxConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('TransConfig') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('Video') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsVideo(DaraModel):
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
        # The maximum ABR. This parameter takes effect only for Narrowband HD 1.0.
        # 
        # *   Valid values: [10,50000].
        # *   Unit: Kbit/s.
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
        # *   Default value: 23 if the encoding format is H.264, or Default value when the Codec parameter is set to H.265: 26.
        # 
        # If this parameter is specified, the value of Bitrate becomes invalid.
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
        # Specifies whether to enable the auto-rotate screen feature.
        self.long_short_mode = long_short_mode
        # The maximum bitrate of the output video.
        # 
        # *   Valid values: [10,50000].
        # *   Unit: Kbit/s.
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
        # Specifies whether to remove the video.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsTransConfig(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfig(DaraModel):
    def __init__(
        self,
        segment: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsMuxConfigSegment(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsContainer(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        remove: str = None,
        samplerate: str = None,
        volume: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume = None,
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
        # Specifies whether to delete the audio stream.
        self.remove = remove
        # The sampling rate.
        # 
        # *   Valid values: 22050, 32000, 44100, 48000, and 96000. Default value: 44100.
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTranscodeOverwriteParamsAudioVolume(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarksOverwriteParams = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigTextWatermarksOverwriteParams(DaraModel):
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
        # Specifies whether to the font size based on the output video dimensions.
        # 
        # *   true: false
        # *   default: false
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitles(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParams = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParams(DaraModel):
    def __init__(
        self,
        char_enc: str = None,
        file: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParamsFile = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigSubtitlesOverwriteParamsFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media object. If Type is set to OSS, set this parameter to the URL of an OSS object. Both the OSS and HTTP protocols are supported. If Type is set to Media, set this parameter to the ID of a media asset.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarks(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParams = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParams(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        file: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsFile = None,
        height: str = None,
        refer_pos: str = None,
        timeline: main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline = None,
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
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('Timeline') is not None:
            temp_model = main_models.SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline()
            self.timeline = temp_model.from_map(m.get('Timeline'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsTimeline(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigImageWatermarksOverwriteParamsFile(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigEncryption(DaraModel):
    def __init__(
        self,
        cipher_text: str = None,
        decrypt_key_uri: str = None,
        encrypt_type: str = None,
        key_service_type: str = None,
    ):
        # The ciphertext of HLS encryption.
        self.cipher_text = cipher_text
        # The address of the decryption service for HLS encryption.
        self.decrypt_key_uri = decrypt_key_uri
        # Specifies the encryption type.
        self.encrypt_type = encrypt_type
        # The type of the key service. Valid values: KMS and Base64.
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupProcessConfigCombineConfigs(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobOutputGroupOutput(DaraModel):
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

class SubmitTranscodeJobResponseBodyTranscodeParentJobInputGroup(DaraModel):
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

