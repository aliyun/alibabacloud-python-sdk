# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSubscriptionShrinkRequest(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        event_subscriptions_shrink: str = None,
        instance_id: str = None,
        mq_instance_id: str = None,
        mq_type: str = None,
        password: str = None,
        producer_id: str = None,
        topic: str = None,
        user_name: str = None,
    ):
        # The endpoint.
        self.endpoint = endpoint
        # The list of subscription items.
        self.event_subscriptions_shrink = event_subscriptions_shrink
        # The instance ID.
        self.instance_id = instance_id
        # The instance ID of the message queue.
        self.mq_instance_id = mq_instance_id
        # The MSMQ type.
        self.mq_type = mq_type
        # The password.
        self.password = password
        # The producer ID.
        self.producer_id = producer_id
        # The topic.
        self.topic = topic
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.event_subscriptions_shrink is not None:
            result['EventSubscriptions'] = self.event_subscriptions_shrink

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

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EventSubscriptions') is not None:
            self.event_subscriptions_shrink = m.get('EventSubscriptions')

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

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

