# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryPipelineListResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_pids: main_models.QueryPipelineListResponseBodyNonExistPids = None,
        pipeline_list: main_models.QueryPipelineListResponseBodyPipelineList = None,
        request_id: str = None,
    ):
        self.non_exist_pids = non_exist_pids
        self.pipeline_list = pipeline_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.non_exist_pids:
            self.non_exist_pids.validate()
        if self.pipeline_list:
            self.pipeline_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_pids is not None:
            result['NonExistPids'] = self.non_exist_pids.to_map()

        if self.pipeline_list is not None:
            result['PipelineList'] = self.pipeline_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistPids') is not None:
            temp_model = main_models.QueryPipelineListResponseBodyNonExistPids()
            self.non_exist_pids = temp_model.from_map(m.get('NonExistPids'))

        if m.get('PipelineList') is not None:
            temp_model = main_models.QueryPipelineListResponseBodyPipelineList()
            self.pipeline_list = temp_model.from_map(m.get('PipelineList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryPipelineListResponseBodyPipelineList(DaraModel):
    def __init__(
        self,
        pipeline: List[main_models.QueryPipelineListResponseBodyPipelineListPipeline] = None,
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
                temp_model = main_models.QueryPipelineListResponseBodyPipelineListPipeline()
                self.pipeline.append(temp_model.from_map(k1))

        return self

class QueryPipelineListResponseBodyPipelineListPipeline(DaraModel):
    def __init__(
        self,
        extend_config: main_models.QueryPipelineListResponseBodyPipelineListPipelineExtendConfig = None,
        id: str = None,
        name: str = None,
        notify_config: main_models.QueryPipelineListResponseBodyPipelineListPipelineNotifyConfig = None,
        quota_allocate: int = None,
        role: str = None,
        speed: str = None,
        speed_level: int = None,
        state: str = None,
    ):
        self.extend_config = extend_config
        self.id = id
        self.name = name
        self.notify_config = notify_config
        self.quota_allocate = quota_allocate
        self.role = role
        self.speed = speed
        self.speed_level = speed_level
        self.state = state

    def validate(self):
        if self.extend_config:
            self.extend_config.validate()
        if self.notify_config:
            self.notify_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_config is not None:
            result['ExtendConfig'] = self.extend_config.to_map()

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
        if m.get('ExtendConfig') is not None:
            temp_model = main_models.QueryPipelineListResponseBodyPipelineListPipelineExtendConfig()
            self.extend_config = temp_model.from_map(m.get('ExtendConfig'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyConfig') is not None:
            temp_model = main_models.QueryPipelineListResponseBodyPipelineListPipelineNotifyConfig()
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

class QueryPipelineListResponseBodyPipelineListPipelineNotifyConfig(DaraModel):
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

class QueryPipelineListResponseBodyPipelineListPipelineExtendConfig(DaraModel):
    def __init__(
        self,
        is_boost_new: bool = None,
        max_multi_speed: int = None,
        multi_speed_downgrade_policy: str = None,
    ):
        self.is_boost_new = is_boost_new
        self.max_multi_speed = max_multi_speed
        self.multi_speed_downgrade_policy = multi_speed_downgrade_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_boost_new is not None:
            result['IsBoostNew'] = self.is_boost_new

        if self.max_multi_speed is not None:
            result['MaxMultiSpeed'] = self.max_multi_speed

        if self.multi_speed_downgrade_policy is not None:
            result['MultiSpeedDowngradePolicy'] = self.multi_speed_downgrade_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBoostNew') is not None:
            self.is_boost_new = m.get('IsBoostNew')

        if m.get('MaxMultiSpeed') is not None:
            self.max_multi_speed = m.get('MaxMultiSpeed')

        if m.get('MultiSpeedDowngradePolicy') is not None:
            self.multi_speed_downgrade_policy = m.get('MultiSpeedDowngradePolicy')

        return self

class QueryPipelineListResponseBodyNonExistPids(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

