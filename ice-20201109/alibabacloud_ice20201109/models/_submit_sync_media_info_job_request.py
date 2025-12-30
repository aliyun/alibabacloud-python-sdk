# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitSyncMediaInfoJobRequest(DaraModel):
    def __init__(
        self,
        input: main_models.SubmitSyncMediaInfoJobRequestInput = None,
        name: str = None,
        schedule_config: main_models.SubmitSyncMediaInfoJobRequestScheduleConfig = None,
        user_data: str = None,
    ):
        # The input of the job.
        # 
        # This parameter is required.
        self.input = input
        # The job name.
        self.name = name
        # The scheduling parameters. This parameter is optional.
        self.schedule_config = schedule_config
        # The user data.
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
            temp_model = main_models.SubmitSyncMediaInfoJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitSyncMediaInfoJobRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitSyncMediaInfoJobRequestScheduleConfig(DaraModel):
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

class SubmitSyncMediaInfoJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
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
        # The type of the media object.
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

