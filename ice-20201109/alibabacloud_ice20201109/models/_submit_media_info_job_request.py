# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitMediaInfoJobRequest(DaraModel):
    def __init__(
        self,
        input: main_models.SubmitMediaInfoJobRequestInput = None,
        name: str = None,
        schedule_config: main_models.SubmitMediaInfoJobRequestScheduleConfig = None,
        user_data: str = None,
    ):
        # The input for the job.
        # 
        # This parameter is required.
        self.input = input
        # The job name.
        self.name = name
        # The scheduling settings.
        self.schedule_config = schedule_config
        # The custom user data.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.schedule_config:
            self.schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.SubmitMediaInfoJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitMediaInfoJobRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitMediaInfoJobRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # The pipeline ID.
        self.pipeline_id = pipeline_id
        # The job priority. A higher value means a higher priority. Valid values range from 1 to 10.
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

class SubmitMediaInfoJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The source of the input media:
        # 
        # - If `Type` is `OSS`, set this parameter to the URL of the input file. You can use OSS (`oss://`), HTTP, or HTTPS URLs.
        # 
        # > You must first add the OSS bucket specified in the URL to Intelligent Media Management Service (IMS) by using [Storage Management](https://help.aliyun.com/document_detail/609918.html).
        # 
        # - If `Type` is `Media`, set this parameter to the media asset ID.
        # 
        # This parameter is required.
        self.media = media
        # The type of the input media.
        # 
        # - `OSS`: The input is an OSS file.
        # 
        # - `Media`: The input is a media asset ID.
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

