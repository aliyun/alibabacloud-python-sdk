# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSubscriptionRequest(DaraModel):
    def __init__(
        self,
        access_point: str = None,
        aliyun_uid: int = None,
        default_topic: str = None,
        event_subscriptions_json: str = None,
        instance_id: str = None,
        mq_instance_id: str = None,
        mq_type: str = None,
        password: str = None,
        producer_id: str = None,
        username: str = None,
    ):
        # This parameter is required.
        self.access_point = access_point
        self.aliyun_uid = aliyun_uid
        self.default_topic = default_topic
        # This parameter is required.
        self.event_subscriptions_json = event_subscriptions_json
        # This parameter is required.
        self.instance_id = instance_id
        self.mq_instance_id = mq_instance_id
        self.mq_type = mq_type
        self.password = password
        self.producer_id = producer_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point is not None:
            result['AccessPoint'] = self.access_point

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.default_topic is not None:
            result['DefaultTopic'] = self.default_topic

        if self.event_subscriptions_json is not None:
            result['EventSubscriptionsJson'] = self.event_subscriptions_json

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mq_instance_id is not None:
            result['MqInstanceId'] = self.mq_instance_id

        if self.mq_type is not None:
            result['MqType'] = self.mq_type

        if self.password is not None:
            result['Password'] = self.password

        if self.producer_id is not None:
            result['ProducerId'] = self.producer_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPoint') is not None:
            self.access_point = m.get('AccessPoint')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('DefaultTopic') is not None:
            self.default_topic = m.get('DefaultTopic')

        if m.get('EventSubscriptionsJson') is not None:
            self.event_subscriptions_json = m.get('EventSubscriptionsJson')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MqInstanceId') is not None:
            self.mq_instance_id = m.get('MqInstanceId')

        if m.get('MqType') is not None:
            self.mq_type = m.get('MqType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProducerId') is not None:
            self.producer_id = m.get('ProducerId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

