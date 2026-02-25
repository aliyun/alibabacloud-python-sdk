# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class UpdatePipelineResponseBody(DaraModel):
    def __init__(
        self,
        pipeline: main_models.UpdatePipelineResponseBodyPipeline = None,
        request_id: str = None,
    ):
        # The details of the MPS queue.
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
            temp_model = main_models.UpdatePipelineResponseBodyPipeline()
            self.pipeline = temp_model.from_map(m.get('Pipeline'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdatePipelineResponseBodyPipeline(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        notify_config: main_models.UpdatePipelineResponseBodyPipelineNotifyConfig = None,
        quota_allocate: int = None,
        role: str = None,
        speed: str = None,
        state: str = None,
    ):
        # The ID of the MPS queue.
        self.id = id
        # The new name of the MPS queue.
        self.name = name
        # The MNS configuration.
        self.notify_config = notify_config
        # The quota that is allocated to the MPS queue.
        self.quota_allocate = quota_allocate
        # The role that is assigned to the current RAM user.
        self.role = role
        # The type of the MPS queue. Default value: **Standard**. Valid values:
        # 
        # *   **Boost**: MPS queue with transcoding speed boosted
        # *   **Standard**: standard MPS queue
        # *   **NarrowBandHDV2**: MPS queue that supports Narrowband HD 2.0
        # *   **AIVideoCover**: MPS queue for intelligent snapshot capture
        # *   **AIVideoFPShot**: MPS queue for media fingerprinting
        # *   **AIVideoCensor**: MPS queue for automated review
        # *   **AIVideoMCU**: MPS queue for smart tagging
        # *   **AIVideoSummary**: MPS queue for video synopsis
        # *   **AIVideoPorn**: MPS queue for pornography detection in videos
        # *   **AIAudioKWS**: MPS queue for keyword recognition in audio
        # *   **AIAudioASR**: MPS queue for speech-to-text conversion
        self.speed = speed
        # The state of the MPS queue. Valid values:
        # 
        # *   **Active**: The MPS queue is active.
        # *   **Paused**: The MPS queue is paused.
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
            temp_model = main_models.UpdatePipelineResponseBodyPipelineNotifyConfig()
            self.notify_config = temp_model.from_map(m.get('NotifyConfig'))

        if m.get('QuotaAllocate') is not None:
            self.quota_allocate = m.get('QuotaAllocate')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class UpdatePipelineResponseBodyPipelineNotifyConfig(DaraModel):
    def __init__(
        self,
        mq_tag: str = None,
        mq_topic: str = None,
        queue_name: str = None,
        topic: str = None,
    ):
        # The tags of the messages.
        self.mq_tag = mq_tag
        # The queue of messages that are received.
        self.mq_topic = mq_topic
        # The queue that is created in MNS.
        self.queue_name = queue_name
        # The topic that is created in MNS.
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

