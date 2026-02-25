# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class SearchPipelineResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pipeline_list: main_models.SearchPipelineResponseBodyPipelineList = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        self.pipeline_list = pipeline_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.pipeline_list:
            self.pipeline_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pipeline_list is not None:
            result['PipelineList'] = self.pipeline_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PipelineList') is not None:
            temp_model = main_models.SearchPipelineResponseBodyPipelineList()
            self.pipeline_list = temp_model.from_map(m.get('PipelineList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchPipelineResponseBodyPipelineList(DaraModel):
    def __init__(
        self,
        pipeline: List[main_models.SearchPipelineResponseBodyPipelineListPipeline] = None,
    ):
        self.pipeline = pipeline

    def validate(self):
        if self.pipeline:
            for v1 in self.pipeline:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Pipeline'] = []
        if self.pipeline is not None:
            for k1 in self.pipeline:
                result['Pipeline'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pipeline = []
        if m.get('Pipeline') is not None:
            for k1 in m.get('Pipeline'):
                temp_model = main_models.SearchPipelineResponseBodyPipelineListPipeline()
                self.pipeline.append(temp_model.from_map(k1))

        return self

class SearchPipelineResponseBodyPipelineListPipeline(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        id: str = None,
        name: str = None,
        notify_config: main_models.SearchPipelineResponseBodyPipelineListPipelineNotifyConfig = None,
        quota_allocate: int = None,
        role: str = None,
        speed: str = None,
        speed_level: int = None,
        state: str = None,
    ):
        self.creation_time = creation_time
        self.id = id
        self.name = name
        self.notify_config = notify_config
        self.quota_allocate = quota_allocate
        self.role = role
        self.speed = speed
        self.speed_level = speed_level
        self.state = state

    def validate(self):
        if self.notify_config:
            self.notify_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.notify_config is not None:
            result['NotifyConfig'] = self.notify_config.to_map()

        if self.quota_allocate is not None:
            result['QuotaAllocate'] = self.quota_allocate

        if self.role is not None:
            result['Role'] = self.role

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.speed_level is not None:
            result['SpeedLevel'] = self.speed_level

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyConfig') is not None:
            temp_model = main_models.SearchPipelineResponseBodyPipelineListPipelineNotifyConfig()
            self.notify_config = temp_model.from_map(m.get('NotifyConfig'))

        if m.get('QuotaAllocate') is not None:
            self.quota_allocate = m.get('QuotaAllocate')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('SpeedLevel') is not None:
            self.speed_level = m.get('SpeedLevel')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class SearchPipelineResponseBodyPipelineListPipelineNotifyConfig(DaraModel):
    def __init__(
        self,
        mq_tag: str = None,
        mq_topic: str = None,
        queue_name: str = None,
        topic: str = None,
    ):
        self.mq_tag = mq_tag
        self.mq_topic = mq_topic
        self.queue_name = queue_name
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mq_tag is not None:
            result['MqTag'] = self.mq_tag

        if self.mq_topic is not None:
            result['MqTopic'] = self.mq_topic

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqTag') is not None:
            self.mq_tag = m.get('MqTag')

        if m.get('MqTopic') is not None:
            self.mq_topic = m.get('MqTopic')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

