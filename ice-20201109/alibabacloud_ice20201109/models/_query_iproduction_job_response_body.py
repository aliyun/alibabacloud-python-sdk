# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryIProductionJobResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        function_name: str = None,
        input: main_models.QueryIProductionJobResponseBodyInput = None,
        job_id: str = None,
        job_params: str = None,
        name: str = None,
        output: main_models.QueryIProductionJobResponseBodyOutput = None,
        output_files: List[str] = None,
        output_media_ids: List[str] = None,
        output_urls: List[str] = None,
        request_id: str = None,
        result: str = None,
        schedule_config: main_models.QueryIProductionJobResponseBodyScheduleConfig = None,
        status: str = None,
        template_id: str = None,
        user_data: str = None,
    ):
        # The time when the job was created, in UTC.
        self.create_time = create_time
        # The time when the job was completed, in UTC.
        self.finish_time = finish_time
        # The name of the algorithm to use. Valid values:
        # 
        # - **Cover**: smart cover
        # 
        # - **VideoClip**: video summary
        # 
        # - **VideoDelogo**: video logo removal
        # 
        # - **VideoDetext**: video text removal
        # 
        # - **CaptionExtraction**: caption extraction
        # 
        # - **VideoGreenScreenMatting**: green screen matting
        # 
        # - **FaceBeauty**: video beautification
        # 
        # - **VideoH2V**: horizontal-to-vertical video conversion
        # 
        # - **MusicSegmentDetect**: chorus detection
        # 
        # - **AudioBeatDetection**: beat detection
        # 
        # - **AudioQualityAssessment**: audio quality assessment
        # 
        # - **SpeechDenoise**: speech denoising
        # 
        # - **AudioMixing**: audio mixing
        # 
        # - **MusicDemix**: music source separation
        self.function_name = function_name
        # The input media.
        self.input = input
        # The job ID.
        self.job_id = job_id
        # A JSON object that contains the parameters for the algorithm job. The specific parameters vary depending on the selected algorithm.
        self.job_params = job_params
        # The job name.
        self.name = name
        # The output media.
        self.output = output
        # An array of output file paths.
        self.output_files = output_files
        # The output media asset IDs.
        self.output_media_ids = output_media_ids
        # An array of output file URLs.
        self.output_urls = output_urls
        # The request ID.
        self.request_id = request_id
        # The algorithm output, returned as a JSON string. The structure of the output varies based on the `FunctionName`. For more information, see the additional notes below.
        self.result = result
        # The job configuration.
        self.schedule_config = schedule_config
        # The job status. Valid values:
        # 
        # - Queuing: The job is awaiting processing.
        # 
        # - Analyzing: The job is being processed.
        # 
        # - Fail: The job failed to complete.
        # 
        # - Success: The job completed successfully.
        self.status = status
        # The template ID.
        self.template_id = template_id
        # The user data. The system returns this value unchanged.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.output:
            self.output.validate()
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

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.output_files is not None:
            result['OutputFiles'] = self.output_files

        if self.output_media_ids is not None:
            result['OutputMediaIds'] = self.output_media_ids

        if self.output_urls is not None:
            result['OutputUrls'] = self.output_urls

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Input') is not None:
            temp_model = main_models.QueryIProductionJobResponseBodyInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            temp_model = main_models.QueryIProductionJobResponseBodyOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('OutputFiles') is not None:
            self.output_files = m.get('OutputFiles')

        if m.get('OutputMediaIds') is not None:
            self.output_media_ids = m.get('OutputMediaIds')

        if m.get('OutputUrls') is not None:
            self.output_urls = m.get('OutputUrls')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.QueryIProductionJobResponseBodyScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class QueryIProductionJobResponseBodyScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # The pipeline ID.
        self.pipeline_id = pipeline_id
        # The job\\"s priority within the pipeline.
        # 
        # - A larger value indicates a higher priority. The highest priority is 10.
        # 
        # - Default: **6**.
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

class QueryIProductionJobResponseBodyOutput(DaraModel):
    def __init__(
        self,
        biz: str = None,
        media: str = None,
        output_url: str = None,
        type: str = None,
    ):
        # The service that the media asset belongs to.
        self.biz = biz
        # The destination for the output. If the output `Type` is `OSS`, this parameter returns an OSS file URL. If the output `Type` is `Media`, it returns the specified or a newly generated media asset ID.
        # 
        # Valid OSS URL formats:
        # 
        # 1. oss\\://bucket/object
        # 
        # 2. http(s)://bucket.oss-[RegionId].aliyuncs.com/object
        #    In these formats, `bucket` is the name of the OSS bucket in the same region as the current project, and `object` is the file path.
        self.media = media
        # The OSS URL of the output file. This value is returned only when `Type` is `Media`.
        self.output_url = output_url
        # The media type. Valid values:
        # 
        # - OSS: An OSS file URL.
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
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.media is not None:
            result['Media'] = self.media

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QueryIProductionJobResponseBodyInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The source file for the job. Set this to an OSS file URL if `Type` is `OSS`, or a media asset ID if `Type` is `Media`.
        # Valid OSS URL formats:
        # 
        # 1. oss\\://bucket/object
        # 
        # 2. http(s)://bucket.oss-[RegionId].aliyuncs.com/object
        #    In these formats, `bucket` is the name of the OSS bucket in the same region as the current project, and `object` is the file path.
        self.media = media
        # The input type. Valid values:
        # 
        # 1. OSS: An OSS file URL.
        # 
        # 2. Media: A media asset ID.
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

