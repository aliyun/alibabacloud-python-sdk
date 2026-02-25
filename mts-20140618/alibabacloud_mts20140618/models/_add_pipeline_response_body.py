# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class AddPipelineResponseBody(DaraModel):
    def __init__(
        self,
        pipeline: main_models.AddPipelineResponseBodyPipeline = None,
        request_id: str = None,
    ):
        # The MPS queue.
        self.pipeline = pipeline
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.pipeline:
            self.pipeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline is not None:
            result['Pipeline'] = self.pipeline.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pipeline') is not None:
            temp_model = main_models.AddPipelineResponseBodyPipeline()
            self.pipeline = temp_model.from_map(m.get('Pipeline'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddPipelineResponseBodyPipeline(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        notify_config: main_models.AddPipelineResponseBodyPipelineNotifyConfig = None,
        quota_allocate: int = None,
        role: str = None,
        speed: str = None,
        speed_level: int = None,
        state: str = None,
    ):
        # The ID of the MPS queue.
        self.id = id
        # The name of the MPS queue.
        self.name = name
        # The MNS configuration.
        self.notify_config = notify_config
        # The quota that is allocated to the MPS queue.
        self.quota_allocate = quota_allocate
        # The role.
        self.role = role
        # The type of the MPS queue.
        self.speed = speed
        # The level of the MPS queue.
        self.speed_level = speed_level
        # The state of the MPS queue.
        # 
        # *   Active: The MPS queue is active. The jobs in the MPS queue are scheduled and transcoded by MPS.
        # *   Paused: The MPS queue is paused. Jobs in the MPS queue are no longer scheduled for transcoding by MPS. All of the jobs in the MPS queue remain in the Submitted state. Jobs that are being transcoded are not affected.
        self.state = state

    def validate(self):
        if self.notify_config:
            self.notify_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyConfig') is not None:
            temp_model = main_models.AddPipelineResponseBodyPipelineNotifyConfig()
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

class AddPipelineResponseBodyPipelineNotifyConfig(DaraModel):
    def __init__(
        self,
        mq_tag: str = None,
        mq_topic: str = None,
        queue_name: str = None,
        topic: str = None,
    ):
        # The tag string.
        self.mq_tag = mq_tag
        # The queue of messages that are received.
        self.mq_topic = mq_topic
        # The name of the queue.
        self.queue_name = queue_name
        # The name of the topic.
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

