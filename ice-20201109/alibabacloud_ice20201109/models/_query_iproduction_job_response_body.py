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
        # The time when the job was created.
        self.create_time = create_time
        # The time when the job was complete.
        self.finish_time = finish_time
        # The name of the algorithm that you want to use for the job. Valid values:
        # 
        # *   **Cover**: This algorithm intelligently generates a thumbnail image for a video.
        # *   **VideoClip**: This algorithm intelligently generates a summary for a video.
        # *   **VideoDelogo**: This algorithm removes logos from a video.
        # *   **VideoDetext**: This algorithm removes captions from a video.
        self.function_name = function_name
        # The input file.
        self.input = input
        # The ID of the intelligent production job.
        self.job_id = job_id
        # The algorithm-specific parameters. The parameters are specified as JSON objects and vary based on the algorithm.
        self.job_params = job_params
        # The name of the intelligent production job.
        self.name = name
        # The output file.
        self.output = output
        # The output files.
        self.output_files = output_files
        self.output_media_ids = output_media_ids
        # The URLs of the output files.
        self.output_urls = output_urls
        # The ID of the request.
        self.request_id = request_id
        # The output of the algorithm. The output is in JSON format and varies based on the algorithm. For more information, see the "Parameters of Result" section of this topic.
        self.result = result
        # The scheduling configuration.
        self.schedule_config = schedule_config
        # The status of the job. Valid values:
        # 
        # *   Queuing: The job is waiting in the queue.
        # *   Analysing: The job is in progress.
        # *   Fail: The job failed.
        # *   Success: The job was successful.
        self.status = status
        # The template ID.
        self.template_id = template_id
        # The user-defined data that is returned in the response.
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
        # The ID of the ApsaraVideo Media Processing (MPS) queue.
        self.pipeline_id = pipeline_id
        # The priority of the job in the MPS queue to which the job is added.
        # 
        # *   A value of 10 indicates the highest priority.
        # *   Default value: **6**.
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
        self.biz = biz
        # The output file. If Type is set to OSS, set this parameter to the path of an OSS object. If Type is set to Media, set this parameter to the ID of a media asset. You can specify the path of an OSS object in one of the following formats:
        # 
        # 1.  oss://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object bucket in the path specifies an OSS bucket that resides in the same region as the intelligent production job. object in the path specifies the object path in OSS.
        self.media = media
        self.output_url = output_url
        # The media type. Valid values:
        # 
        # *   OSS: OSS object
        # *   Media: media asset
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
        # The input file. If Type is set to OSS, set this parameter to the path of an OSS object. If Type is set to Media, set this parameter to the ID of a media asset. You can specify the path of an OSS object in one of the following formats:
        # 
        # 1.  oss://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object bucket in the path specifies an OSS bucket that resides in the same region as the intelligent production job. object in the path specifies the object path in OSS.
        self.media = media
        # The media type. Valid values:
        # 
        # 1.  OSS: Object Storage Service (OSS) object
        # 2.  Media: media asset
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

