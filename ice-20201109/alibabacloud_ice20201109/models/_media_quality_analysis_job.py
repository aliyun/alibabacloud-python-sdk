# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaQualityAnalysisJob(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        input: main_models.MediaQualityAnalysisJobInput = None,
        job_id: str = None,
        name: str = None,
        schedule_config: main_models.MediaQualityAnalysisJobScheduleConfig = None,
        state: str = None,
        template_config: main_models.MediaQualityAnalysisJobTemplateConfig = None,
        user_data: str = None,
        vqa_result: main_models.MediaQualityAnalysisJobVqaResult = None,
    ):
        self.create_time = create_time
        self.finish_time = finish_time
        self.input = input
        self.job_id = job_id
        self.name = name
        self.schedule_config = schedule_config
        self.state = state
        self.template_config = template_config
        self.user_data = user_data
        self.vqa_result = vqa_result

    def validate(self):
        if self.input:
            self.input.validate()
        if self.schedule_config:
            self.schedule_config.validate()
        if self.template_config:
            self.template_config.validate()
        if self.vqa_result:
            self.vqa_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.state is not None:
            result['State'] = self.state

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.vqa_result is not None:
            result['VqaResult'] = self.vqa_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Input') is not None:
            temp_model = main_models.MediaQualityAnalysisJobInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.MediaQualityAnalysisJobScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.MediaQualityAnalysisJobTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VqaResult') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaResult()
            self.vqa_result = temp_model.from_map(m.get('VqaResult'))

        return self

class MediaQualityAnalysisJobTemplateConfig(DaraModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class MediaQualityAnalysisJobScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        self.pipeline_id = pipeline_id
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

class MediaQualityAnalysisJobInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        self.media = media
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

