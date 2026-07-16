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
        # The time when the job was created. The format is yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The time when the job finished. The format is yyyy-MM-ddTHH:mm:ssZ.
        self.finish_time = finish_time
        # The input group for the job. A single input creates a transcoding job. Multiple inputs create a job to merge audio and video streams.
        self.input_group = input_group
        # The number of sub-jobs.
        self.job_count = job_count
        # The name of the job.
        self.name = name
        # The output group of the job.
        self.output_group = output_group
        # The ID of the parent job.
        self.parent_job_id = parent_job_id
        # The completion percentage of the job.
        self.percent = percent
        # The ID of the request.
        self.request_id = request_id
        # The job scheduling configuration.
        self.schedule_config = schedule_config
        # The status of the job. Success: At least one sub-job succeeded after all sub-jobs are complete. Fail: All sub-jobs failed.
        self.status = status
        # The time when the job was submitted. The format is yyyy-MM-ddTHH:mm:ssZ.
        self.submit_time = submit_time
        # The list of sub-jobs.
        self.transcode_job_list = transcode_job_list
        # The source of the job. Valid values: \\`API\\`, \\`WorkFlow\\`, and \\`Console\\`.
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
        # The time the job was created.
        self.create_time = create_time
        # The time when the job finished.
        self.finish_time = finish_time
        # The input group for the job. A single input creates a transcoding job. Multiple inputs create a media merging job.
        self.input_group = input_group
        # The sub-job ID.
        self.job_id = job_id
        # The index of the sub-job within the entire job.
        self.job_index = job_index
        # The job name.
        self.name = name
        # The media information of the video generated by the job.
        self.out_file_meta = out_file_meta
        # The output media configuration.
        self.output = output
        # The parent job ID.
        self.parent_job_id = parent_job_id
        # The transcoding processing configuration.
        self.process_config = process_config
        # The ID of the request to submit the job.
        self.request_id = request_id
        # The scheduling information for the job.
        self.schedule_config = schedule_config
        # The status of the transcoding job.
        # 
        # - Init: The job is submitted.
        # 
        # - Processing: The job is being transcoded.
        # 
        # - Success: The transcoding is successful.
        # 
        # - Fail: The transcoding failed.
        # 
        # - Deleted: The job is deleted.
        self.status = status
        # The result of the job submission.
        self.submit_result_json = submit_result_json
        # The time when the job was submitted.
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
        # The ID of the pipeline.
        self.pipeline_id = pipeline_id
        # The priority of the task. A larger value indicates a higher priority. The value can be an integer from 1 to 10.
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
        # The configuration for mixing multiple input streams.
        self.combine_configs = combine_configs
        # The encryption configuration.
        self.encryption = encryption
        # The image watermark configuration.
        self.image_watermarks = image_watermarks
        # The configuration for burning in captions.
        self.subtitles = subtitles
        # The text watermark configuration.
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
        # Parameters to overwrite. If you specify these, they replace the corresponding parameters in the template.
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
        # The container format settings.
        self.container = container
        # The multiplexing settings.
        self.mux_config = mux_config
        # The conditional transcoding parameters.
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
        # The maximum bitrate for adaptive bitrate streaming (ABR). This applies only to narrow-high 1. Valid values: [10, 50000]. Unit: Kbps.
        self.abr_max = abr_max
        # The average video bitrate.
        # 
        # - Valid values: [10, 50000].
        # 
        # - Unit: Kbps.
        self.bitrate = bitrate
        # The buffer size.
        # 
        # - Valid values: [1000, 128000]
        # 
        # - Default value: 6000
        # 
        # - Unit: Kb
        self.bufsize = bufsize
        # The encoding format.
        self.codec = codec
        # The constant rate factor (CRF), which controls the trade-off between quality and bitrate.
        # 
        # - Valid values: [0, 51].
        # 
        # - Default values: 23 for H.264 and 26 for H.265.
        # 
        # If you set Crf, the Bitrate setting is ignored.
        self.crf = crf
        # The video cropping method. Two options are available.
        # 
        # - Automatically detect and crop black bars. Set this to border.
        # 
        # - Custom cropping. Format: width:height:left:top. Example: 1280:800:0:140
        self.crop = crop
        # The frame rate.
        # 
        # - Valid values: (0, 60].
        # 
        # - If the frame rate of the input file exceeds 60, the system uses 60.
        # 
        # - Default value: The frame rate of the input file.
        self.fps = fps
        # The maximum number of frames between keyframes.
        # 
        # - Valid values: [1, 1080000].
        # 
        # - Default value: 250.
        self.gop = gop
        # The height.
        # 
        # - Valid values: [128, 4096].
        # 
        # - Unit: px.
        # 
        # - Default value: The original video height.
        self.height = height
        # Specifies whether to enable automatic rotation for portrait or landscape videos (also known as long-side/short-side mode).
        self.long_short_mode = long_short_mode
        # The peak video bitrate. Valid values: [10, 50000]. Unit: Kbps.
        self.maxrate = maxrate
        # The padding configuration for black bars.
        # 
        # - Format: width:height:left:top.
        # 
        # - Example: 1280:800:0:140
        self.pad = pad
        # The video color format. Valid values include yuv420p and yuvj420p.
        self.pix_fmt = pix_fmt
        # The video encoder preset. Only H.264 supports this parameter. Valid values: veryfast, fast, medium, slow, and slower. Default value: medium.
        self.preset = preset
        # The encoding profile. Valid values: baseline, main, and high.
        # 
        # - baseline: For mobile devices.
        # 
        # - main: For standard-resolution devices.
        # 
        # - high: For high-resolution devices.
        # 
        # Default value: high.
        self.profile = profile
        # Specifies whether to remove the video.
        self.remove = remove
        # The scan mode. Valid values: interlaced and progressive.
        self.scan_mode = scan_mode
        # The width.
        # 
        # - Valid values: [128, 4096].
        # 
        # - Unit: px.
        # 
        # - Default value: The original video width.
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
        # The method used to adjust the display aspect ratio. This parameter takes effect only when both Width and Height are specified. You can use it with LongShortMode.
        # 
        # Valid values: rescale, crop, pad, and none.
        # 
        # Default value: none.
        self.adj_dar_method = adj_dar_method
        # Specifies whether to check the audio bitrate. IsCheckAudioBitrate and IsCheckAudioBitrateFail are mutually exclusive. IsCheckAudioBitrateFail has higher priority.
        # 
        # - true: Check the bitrate. If the input audio bitrate is lower than the output setting, transcode at the input bitrate.
        # 
        # - false: Do not check the bitrate.
        # 
        # Default value rules:
        # 
        # - Empty and the codec differs from the input source: false.
        # 
        # - Empty and the codec matches the input source: true.
        self.is_check_audio_bitrate = is_check_audio_bitrate
        # Specifies whether to check the audio bitrate. IsCheckAudioBitrate and IsCheckAudioBitrateFail are mutually exclusive. This parameter has higher priority.
        # 
        # - true: Check the bitrate. If the input audio bitrate is lower than the output setting, return a failure.
        # 
        # - false (default): Do not check the bitrate.
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        # Specifies whether to check the video resolution. IsCheckReso and IsCheckResoFail are mutually exclusive. IsCheckResoFail has higher priority.
        # 
        # - true: Check the resolution. If the input video resolution (width or height) is smaller than the output setting, transcode at the input resolution.
        # 
        # - false (default): Do not check the resolution.
        self.is_check_reso = is_check_reso
        # Specifies whether to check the video resolution. IsCheckReso and IsCheckResoFail are mutually exclusive. This parameter has higher priority.
        # 
        # - true: Check the resolution. If the input video resolution (width or height) is smaller than the output setting, return a failure.
        # 
        # - false (default): Do not check the resolution.
        self.is_check_reso_fail = is_check_reso_fail
        # Specifies whether to check the video bitrate. IsCheckVideoBitrate and IsCheckVideoBitrateFail are mutually exclusive. IsCheckVideoBitrateFail has higher priority.
        # 
        # - true: Check the bitrate. If the input video bitrate is lower than the output setting, transcode at the input bitrate.
        # 
        # - false (default): Do not check the bitrate.
        self.is_check_video_bitrate = is_check_video_bitrate
        # Specifies whether to check the video bitrate. IsCheckVideoBitrate and IsCheckVideoBitrateFail are mutually exclusive. This parameter has higher priority.
        # 
        # - true: Check the bitrate. If the input video bitrate is lower than the output setting, return a failure.
        # 
        # - false (default): Do not check the bitrate.
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        # The video transcoding mode. Valid values:
        # 
        # - onepass (default): Used for ABR. Encoding is faster than twopass.
        # 
        # - twopass: Used for VBR. Encoding is slower than onepass.
        # 
        # - CBR: Constant bitrate mode.
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
        # The segment duration.
        self.duration = duration
        # The forced segment time points.
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
        # - Valid values: [8, 1000]
        # 
        # - Unit: Kbps
        # 
        # - Default value: 128
        self.bitrate = bitrate
        # The number of sound channels. Default value: 2.
        self.channels = channels
        # The audio codec. Valid values: AAC, MP3, VORBIS, and FLAC. Default value: AAC.
        self.codec = codec
        # The audio encoding profile. When Codec is AAC, valid values are aac_low, aac_he, aac_he_v2, aac_ld, and aac_eld.
        self.profile = profile
        # Specifies whether to delete the audio stream.
        self.remove = remove
        # The sample rate.
        # 
        # - Default value: 44100
        # 
        # - Valid values: 22050, 32000, 44100, 48000, and 96000.
        # 
        # - Unit: Hz
        self.samplerate = samplerate
        # The volume control.
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
        # The target loudness level.
        self.integrated_loudness_target = integrated_loudness_target
        # The loudness range.
        self.loudness_range_target = loudness_range_target
        # The volume adjustment method.
        self.method = method
        # The true peak level.
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
        # Parameters to overwrite. If you specify these, they replace the corresponding parameters in the template.
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
        # Adjusts the font size based on the output video size. The default is false.
        self.adaptive = adaptive
        # The outline color.
        # Default: Black.
        # For more values, see BorderColor.
        self.border_color = border_color
        # The outline width.
        # 
        # - Default: 0
        # 
        # - Range: (0,4096]
        self.border_width = border_width
        # The watermark text. It does not need to be Base64 encoded. The string must be UTF-8 encoded.
        self.content = content
        # The font transparency.
        # 
        # - Valid values: (0, 1]
        # 
        # - Default: 1.0
        self.font_alpha = font_alpha
        # The color.
        self.font_color = font_color
        # The font. Default: SimSun.
        self.font_name = font_name
        # The font size.
        # 
        # - Default value: 16
        # 
        # - Valid values: (4, 120)
        self.font_size = font_size
        # The left margin of the text.
        # 
        # - Default: 0
        # 
        # - Valid values: [0, 4096]
        self.left = left
        # The top margin of the text.
        # 
        # - Default: 0
        # 
        # - Valid values: [0, 4096]
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
        # Parameters to overwrite. If you specify these, they replace the corresponding parameters in the template.
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
        # The encoding format of the file.
        self.char_enc = char_enc
        # The subtitle file.
        self.file = file
        # The file format of the caption.
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
        # The value of Media:
        # 
        # - If type is OSS, the value is a URL. The URL supports the OSS and HTTP protocols.
        # 
        # - If type is Media, the value is the media asset ID.
        self.media = media
        # The type of the media object.
        # Valid values:
        # 
        # - OSS: An OSS file.
        # 
        # - Media: The ID of a media asset.
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
        # Parameters to overwrite. If you specify these, they replace the corresponding parameters in the template.
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
        # The horizontal offset of the image watermark relative to the output video. Default value: 0.
        # 
        # Values can be one of the following:
        # 
        # - Integer: The offset in pixels.
        # 
        #   - Valid values: [8, 4096]
        # 
        #   - Unit: px
        # 
        # - Decimal: The ratio of the horizontal offset to the output video width.
        # 
        #   - Valid values: (0, 1)
        # 
        #   - Up to four decimal places are supported, such as 0.9999. Extra digits are automatically discarded.
        self.dx = dx
        # The vertical offset of the image watermark relative to the output video. Default value: 0.
        # 
        # Values can be one of the following:
        # 
        # - Integer: The offset in pixels.
        # 
        #   - Valid values: [8, 4096]
        # 
        #   - Unit: px
        # 
        # - Decimal: The ratio of the vertical offset to the output video height.
        # 
        #   - Valid values: (0, 1)
        # 
        #   - Up to four decimal places are supported, such as 0.9999. Extra digits are automatically discarded.
        self.dy = dy
        # The watermark image file.
        self.file = file
        # The height of the image watermark on the output video. Values can be one of the following:
        # 
        # - Integer: The pixel height of the watermark image.
        # 
        #   - Valid values: [8, 4096]
        # 
        #   - Unit: px
        # 
        # - Decimal: The ratio of the watermark height to the output video height.
        # 
        #   - Valid values: (0, 1)
        # 
        #   - Up to four decimal places are supported, such as 0.9999. Extra digits are automatically discarded.
        self.height = height
        # The position of the watermark.
        # 
        # - Valid values: TopRight (top-right), TopLeft (top-left), BottomRight (bottom-right), and BottomLeft (bottom-left).
        # 
        # - Default value: TopRight.
        self.refer_pos = refer_pos
        # The display time settings for a dynamic watermark.
        self.timeline = timeline
        # The width of the image watermark on the output video. Values can be one of the following:
        # 
        # - Integer: The pixel width of the watermark image.
        # 
        #   - Valid values: [8, 4096]
        # 
        #   - Unit: px
        # 
        # - Decimal: The ratio of the watermark width to the output video width.
        # 
        #   - Valid values: (0, 1)
        # 
        #   - Up to four decimal places are supported, such as 0.9999. Extra digits are automatically discarded.
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
        # The duration of the watermark.
        # 
        # - Valid values: [number, ToEND]
        # 
        # - Default value: ToEND
        self.duration = duration
        # The start time of the watermark.
        # 
        # - Unit: seconds
        # 
        # - Valid values: numbers
        # 
        # - Default value: 0
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
        # The media value:
        # 
        # - If Type is OSS, this is a URL that supports the OSS or HTTP protocol.
        # 
        # - If Type is Media, this is a media asset ID.
        self.media = media
        # The media object type. Valid values:
        # 
        # - OSS: An OSS file.
        # 
        # - Media: A media asset ID.
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
        # The ciphertext of the key for standard encryption.
        self.cipher_text = cipher_text
        # The decryption service endpoint for standard encryption.
        self.decrypt_key_uri = decrypt_key_uri
        # The encryption type.
        self.encrypt_type = encrypt_type
        # The type of the key service. Only KMS and Base64 are supported.
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
        # The index of the audio stream.
        # 
        # This parameter is required.
        self.audio_index = audio_index
        # The duration of the input stream. The default value is the duration of the video.
        self.duration = duration
        # The start time of the input stream. The default value is 0.
        self.start = start
        # The index of the video stream.
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
        # The value of the media asset:
        # 
        # - If type is OSS, the value is a URL. The OSS and HTTP protocols are supported.
        # 
        # - If type is Media, the value is the media asset ID.
        self.media = media
        # The path of the output stream.<br>
        # This parameter is valid only when \\`Type\\` is set to \\`Media\\`. It lets you select a specific file from the media asset for output.<br>
        # The following placeholders are supported:<br><br>
        # 
        # - {MediaId}: The ID of the media asset.
        # 
        # - {JobId}: The ID of the transcoding subtask.
        # 
        # - {MediaBucket}: The bucket where the media asset is stored.
        # 
        # - {ExtName}: The file extension. The value is the output format specified in the transcoding template.
        # 
        # - {DestMd5}: The MD5 hash of the output file.<br>
        #   Note:<br>
        # 
        # 1. This parameter must contain the {MediaId} and {JobId} placeholders.
        # 
        # 2. The output bucket is the same as the bucket where the media asset is stored.
        self.output_url = output_url
        # The media object type.
        # Valid values:
        # 
        # - OSS: An OSS file.
        # 
        # - Media: A media asset ID.
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
        # The audio stream information.
        self.audio_stream_info_list = audio_stream_info_list
        # Basic file information.
        self.file_basic_info = file_basic_info
        # The video stream information.
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
        # The encoding format tag.
        self.codec_tag = codec_tag
        # The text of the encoding format tag.
        self.codec_tag_string = codec_tag_string
        # The codec time base.
        self.codec_time_base = codec_time_base
        # The display aspect ratio.
        self.dar = dar
        # The duration in seconds.
        self.duration = duration
        # The frame rate.
        self.fps = fps
        # Indicates whether B-frames exist.
        # Valid values:
        # 
        # - 0: No B-frames.
        # 
        # - 1: One B-frame.
        # 
        # - 2: Multiple consecutive B-frames.
        self.has_bframes = has_bframes
        # The height of the output video stream.
        self.height = height
        # The index of the stream.
        self.index = index
        # The language.
        self.lang = lang
        # The encoding level.
        self.level = level
        # The total number of frames.
        self.num_frames = num_frames
        # The color storage format.
        self.pix_fmt = pix_fmt
        # The encoder preset.
        self.profile = profile
        # The rotation angle of the video. Valid values: 0, 90, 180, and 270. The default value is 0.
        self.rotate = rotate
        # The sample aspect ratio.
        self.sar = sar
        # The start time.
        self.start_time = start_time
        # The time base.
        self.time_base = time_base
        # The video width.
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
        # The duration of the video in seconds.
        self.duration = duration
        # The name of the file.
        self.file_name = file_name
        # The size of the file in bytes.
        self.file_size = file_size
        # The status of the file.
        self.file_status = file_status
        # The file type. Valid values: source_file and transcode_file.
        self.file_type = file_type
        # The URL of the file.
        self.file_url = file_url
        # The name of the video format.
        self.format_name = format_name
        # The height.
        self.height = height
        # The media asset ID.
        self.media_id = media_id
        # The region where the file is located.
        self.region = region
        # The width of the output file.
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
        # The channel layout.
        self.channel_layout = channel_layout
        # The number of sound channels.
        self.channels = channels
        # The name of the encoding format.
        self.codec_long_name = codec_long_name
        # The encoding format.
        self.codec_name = codec_name
        # The encoder tag.
        self.codec_tag = codec_tag
        # The encoder tag name.
        self.codec_tag_string = codec_tag_string
        # The time base of the encoder.
        self.codec_time_base = codec_time_base
        # The duration in seconds.
        self.duration = duration
        # The index of the stream.
        self.index = index
        # The language.
        self.lang = lang
        # The sampling format.
        self.sample_fmt = sample_fmt
        # The sample rate in Hz.
        self.sample_rate = sample_rate
        # The start time.
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
        # The input stream path:
        # 
        # - This parameter takes effect only when Type is Media. It lets you select a specific file from the media asset as the input.
        # 
        # - The system checks whether the input URL exists in the media asset.
        self.input_url = input_url
        # The media value:
        # 
        # - If Type is OSS, this is a URL that supports the OSS or HTTP protocol.
        # 
        # - If Type is Media, this is a media asset ID.
        self.media = media
        # The media object type. Valid values:
        # 
        # - OSS: An OSS file.
        # 
        # - Media: A media asset ID.
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
        # The pipeline ID.
        self.pipeline_id = pipeline_id
        # The priority of the job. A larger value indicates a higher priority. The value can be an integer from 1 to 10.
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
        # The output media configuration.
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
        # The settings for combining multiple input streams.
        self.combine_configs = combine_configs
        # The encryption configuration.
        self.encryption = encryption
        # The image watermark settings.
        self.image_watermarks = image_watermarks
        # The caption burn-in configuration.
        self.subtitles = subtitles
        # The text watermark configurations.
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
        # The overwrite parameters. If specified, these parameters overwrite the corresponding parameters in the template.
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
        # Audio settings.
        self.audio = audio
        # The container format settings.
        self.container = container
        # The encapsulation settings.
        self.mux_config = mux_config
        # The conditional transcoding parameters.
        self.trans_config = trans_config
        # Video settings
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
        # The maximum bitrate for adaptive bitrate (ABR) streaming. This parameter is valid only for Narrowband HD 1.0.
        # 
        # - Value range: [10, 50000]
        # 
        # - Unit: Kbps
        self.abr_max = abr_max
        # The average video bitrate.
        # 
        # - Value range: [10, 50000].
        # 
        # - Unit: Kbps.
        self.bitrate = bitrate
        # The buffer size.
        # 
        # - Value range: [1000, 128000]
        # 
        # - Default value: 6000
        # 
        # - Unit: Kb
        self.bufsize = bufsize
        # The encoding format.
        self.codec = codec
        # The Constant Rate Factor (CRF).
        # 
        # - The value can be from 0 to 51.
        # 
        # - The default value is 23 for H264 encoding and 26 for H265 encoding.
        # 
        # If Crf is set, the Bitrate setting is ignored.
        self.crf = crf
        # Crops the video frame.
        # Two methods are available.
        # 
        # - To automatically detect and crop black bars, set the parameter to "border".
        # 
        # - To specify a custom crop area, use the width:height:left:top format.
        #   Example: 1280:800:0:140
        self.crop = crop
        # The frame rate.
        # 
        # - Valid values: (0, 60].
        # 
        # - If the input file has a frame rate greater than 60, the frame rate is capped at 60.
        # 
        # - Default: The frame rate of the input file.
        self.fps = fps
        # The maximum number of frames between two keyframes.
        # 
        # - The value must be in the range of [1, 1080000].
        # 
        # - The default value is 250.
        self.gop = gop
        # The height of the video.
        # 
        # - Valid values: [128, 4096].
        # 
        # - Unit: px.
        # 
        # - Default value: The original height of the video.
        self.height = height
        # Specifies whether to enable automatic rotation for landscape and portrait orientations (long and short edge pattern).
        self.long_short_mode = long_short_mode
        # The peak video bitrate.
        # 
        # - Value range: [10, 50000]
        # 
        # - Unit: Kbps
        self.maxrate = maxrate
        # Adds black bars to the video.
        # 
        # - Format: width:height:left:top
        # 
        # - Example: 1280:800:0:140
        self.pad = pad
        # The pixel format of the video. Valid values include standard formats such as yuv420p and yuvj420p.
        self.pix_fmt = pix_fmt
        # The video algorithm preset. This parameter is supported only for H.264. Supported values are veryfast, fast, medium, slow, and slower. The default value is medium.
        self.preset = preset
        # The encoding profile.
        # Supported values are baseline, main, and high.
        # 
        # - baseline: For mobile devices.
        # 
        # - main: For standard-resolution devices.
        # 
        # - high: For high-resolution devices.
        # 
        # Default value: high.
        self.profile = profile
        # Specifies whether to remove the video.
        self.remove = remove
        # The scan mode. Valid values are interlaced and progressive.
        self.scan_mode = scan_mode
        # The width of the output video.
        # 
        # - Valid values: 128 to 4096.
        # 
        # - Unit: px.
        # 
        # - Default value: The original width of the video.
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
        # The method to adjust the resolution. This setting takes effect only when both Width and Height are specified. It can be used with LongShortMode.
        # 
        # Valid values: rescale, crop, pad, and none.
        # 
        # Default value: none.
        self.adj_dar_method = adj_dar_method
        # Specifies whether to check the audio bitrate. You can set either this parameter or IsCheckAudioBitrateFail. IsCheckAudioBitrateFail takes precedence.
        # 
        # - true: Checks the audio bitrate. If the input audio bitrate is lower than the configured output bitrate, the service uses the input audio bitrate for transcoding.
        # 
        # - false: Does not check the audio bitrate.
        # 
        # Default value:
        # 
        # - false: If this parameter is empty and the output codec is different from the input codec.
        # 
        # - true: If this parameter is empty and the output codec is the same as the input codec.
        self.is_check_audio_bitrate = is_check_audio_bitrate
        # Specifies whether to check the audio bitrate. You can set either IsCheckAudioBitrate or IsCheckAudioBitrateFail. This parameter has a higher priority.
        # 
        # - true: The transcoding job fails if the input audio bitrate is lower than the output bitrate setting.
        # 
        # - false: The audio bitrate is not checked.
        # 
        # Default value: false.
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        # Specifies whether to check the video resolution. The IsCheckReso and IsCheckResoFail parameters are mutually exclusive. IsCheckResoFail takes precedence.
        # 
        # - true: Enables the resolution check. If the resolution (width or height) of the input video is lower than the output resolution, the transcoding job uses the input resolution.
        # 
        # - false: Disables the resolution check.
        # 
        # Default value: false.
        self.is_check_reso = is_check_reso
        # Specifies whether to check the video resolution. You can use either IsCheckReso or IsCheckResoFail, but not both. This parameter has a higher priority.
        # 
        # - true: Checks the resolution. The transcoding job fails if the width or height of the input video is smaller than the output resolution.
        # 
        # - false: Does not check the resolution.
        # 
        # Default value: false.
        self.is_check_reso_fail = is_check_reso_fail
        # Specifies whether to check the video bitrate. You can set either IsCheckVideoBitrate or IsCheckVideoBitrateFail. IsCheckVideoBitrateFail has a higher priority.
        # 
        # - true: Checks the bitrate. If the input video bitrate is lower than the output bitrate, the video is transcoded at the input bitrate.
        # 
        # - false: Does not check the bitrate.
        # 
        # Default value: false.
        self.is_check_video_bitrate = is_check_video_bitrate
        # Specifies whether to check the video bitrate. This parameter and IsCheckVideoBitrate are mutually exclusive. IsCheckVideoBitrateFail has a higher priority.
        # 
        # - true: Enables the check. The transcoding job fails if the input video bitrate is lower than the output bitrate setting.
        # 
        # - false: Disables the check.
        # 
        # Default value: false.
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        # The video transcoding mode. Valid values:
        # 
        # - onepass: Typically used for ABR. The encoding speed is faster than twopass.
        # 
        # - twopass: Typically used for VBR. The encoding speed is slower than onepass.
        # 
        # - CBR: Constant Bitrate mode.
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
        # Segment settings.
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
        # The time points for forced segmentation.
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
        # - Value range: [8, 1000]
        # 
        # - Unit: Kbps
        # 
        # - Default value: 128
        self.bitrate = bitrate
        # The number of sound channels.
        # Default value: 2.
        self.channels = channels
        # The audio codec format. Valid values are AAC, MP3, VORBIS, and FLAC.
        # Default value: AAC
        self.codec = codec
        # The audio encoding preset.
        # When Codec is set to AAC, valid values are aac_low, aac_he, aac_he_v2, aac_ld, and aac_eld.
        self.profile = profile
        # Specifies whether to remove the audio stream.
        self.remove = remove
        # The sample rate.
        # 
        # - Default value: 44100. Valid values: 22050, 32000, 44100, 48000, and 96000.
        # 
        # - Unit: Hz
        self.samplerate = samplerate
        # The volume control settings.
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
        # The target volume.
        self.integrated_loudness_target = integrated_loudness_target
        # The loudness range.
        self.loudness_range_target = loudness_range_target
        # The volume adjustment method.
        self.method = method
        # The true peak.
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
        # The overwrite parameters. If specified, these parameters overwrite the corresponding parameters in the template.
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
        # Adjusts the font size based on the size of the output video.
        # 
        # - Valid values: true, false
        # 
        # - default: false
        self.adaptive = adaptive
        # The outline color.
        # Default: Black
        # For more values, see BorderColor.
        self.border_color = border_color
        # The width of the border.
        # 
        # - Default: 0
        # 
        # - Range: (0, 4096]
        self.border_width = border_width
        # The watermark text. The string must be UTF-8 encoded. Base64 encoding is not required.
        self.content = content
        # The transparency of the font.
        # 
        # - Range: (0, 1].
        # 
        # - Default: 1.0.
        self.font_alpha = font_alpha
        # The font color.
        self.font_color = font_color
        # The font. Default: SimSun.
        self.font_name = font_name
        # The font size.
        # 
        # - Default value: 16
        # 
        # - Range: (4, 120)
        self.font_size = font_size
        # The left margin of the text.
        # 
        # - Default: 0
        # 
        # - Range: [0,4096]
        self.left = left
        # The top margin of the text.
        # 
        # - Default: 0.
        # 
        # - Range: [0,4096].
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
        # The overwrite parameters. If specified, these parameters overwrite the corresponding parameters in the template.
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
        # The caption file format.
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
        # The value of the media asset. If the type is OSS, the value is a URL that supports the OSS and HTTP protocols. If the type is Media, the value is the media asset ID.
        self.media = media
        # The type of the media object.
        # Valid values:
        # 
        # - OSS: an OSS file.
        # 
        # - Media: a media asset ID.
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
        # The parameters that, when specified, overwrite the corresponding parameters in the template.
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
        # The horizontal offset of the watermark image relative to the output video.
        # Default: 0
        # 
        # The value can be specified in two formats:
        # 
        # - An integer that specifies the offset in pixels.
        # 
        #   - Range: [8, 4096]
        # 
        #   - Unit: px
        # 
        # - A decimal that specifies the ratio of the horizontal offset to the width of the output video.
        # 
        #   - Range: (0, 1)
        # 
        #   - The value can have up to four decimal places, such as 0.9999. The system automatically discards any digits beyond the fourth decimal place.
        self.dx = dx
        # The vertical offset of the watermark image relative to the output video.
        # Default value: 0.
        # 
        # The value can be in one of the following two formats:
        # 
        # - An integer that specifies the offset in pixels.
        # 
        #   - Range: [8, 4096].
        # 
        #   - Unit: px.
        # 
        # - A decimal that specifies the ratio of the vertical offset to the output video height.
        # 
        #   - Range: (0, 1).
        # 
        #   - The value supports up to four decimal places, such as 0.9999. Any additional digits are automatically discarded.
        self.dy = dy
        # The image file for the watermark.
        self.file = file
        # The height of the image watermark on the output video.
        # The value can be specified in two ways:
        # 
        # - An integer that represents the watermark height in pixels.
        # 
        #   - Range: [8, 4096].
        # 
        #   - Unit: px.
        # 
        # - A decimal that represents the watermark height as a ratio of the output video\\"s height.
        # 
        #   - Range: (0, 1).
        # 
        #   - The value supports up to four decimal places, such as 0.9999. Digits beyond the fourth decimal place are automatically discarded.
        self.height = height
        # The position of the watermark.
        # 
        # - Valid values: TopRight, TopLeft, BottomRight, and BottomLeft.
        # 
        # - Default value: TopRight.
        self.refer_pos = refer_pos
        # The display time settings for the dynamic watermark.
        self.timeline = timeline
        # The width of the watermark image on the output video.
        # The value can be specified in two formats:
        # 
        # - An integer that specifies the width of the watermark image in pixels.
        # 
        #   - Range: [8, 4096].
        # 
        #   - Unit: px.
        # 
        # - A decimal that represents the width of the watermark relative to the width of the output video.
        # 
        #   - Range: (0, 1).
        # 
        #   - The value supports up to four decimal places, such as 0.9999. Digits beyond the fourth decimal place are automatically discarded.
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
        # The duration of the watermark.
        # 
        # - Valid values: [Number, ToEND]
        # 
        # - Default value: ToEND
        self.duration = duration
        # The time when the watermark appears.
        # 
        # - Unit: seconds
        # 
        # - The value must be numeric.
        # 
        # - Default value: 0
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
        # The value of the media asset:
        # 
        # - If type is OSS, the value is a URL that supports the OSS and HTTP protocols.
        # 
        # - If type is Media, the value is the media asset ID.
        self.media = media
        # The object type of the media asset.
        # Valid values:
        # 
        # - OSS: An OSS file.
        # 
        # - Media: A media asset ID.
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
        # The ciphertext of the key for standard encryption.
        self.cipher_text = cipher_text
        # The decryption endpoint for standard encryption.
        self.decrypt_key_uri = decrypt_key_uri
        # The encryption type.
        self.encrypt_type = encrypt_type
        # The type of the key service. Only KMS and Base64 are supported.
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
        # The index of the audio stream.
        # 
        # This parameter is required.
        self.audio_index = audio_index
        # The duration of the input stream. By default, this is the duration of the video.
        self.duration = duration
        # The start time of the input stream. The default value is 0.
        self.start = start
        # The index of the video stream.
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
        # The value of the media asset:
        # 
        # - If type is set to OSS, the value is a URL. The OSS and HTTP protocols are supported.
        # 
        # - If type is set to Media, the value is the media asset ID.
        self.media = media
        # The media object type.
        # Valid values:
        # 
        # - OSS: An OSS file.
        # 
        # - Media: A media asset ID.
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
        # The value of the media asset:
        # 
        # - If type is OSS, this is a URL. Both the OSS and HTTP protocols are supported.
        # 
        # - If type is Media, this is the media asset ID.
        self.media = media
        # The type of the media object.
        # Valid values:
        # 
        # - OSS: an OSS file.
        # 
        # - Media: a media asset ID.
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

