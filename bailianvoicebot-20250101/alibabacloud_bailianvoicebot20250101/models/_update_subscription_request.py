# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateSubscriptionRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        endpoint: str = None,
        event_subscriptions: List[str] = None,
        mq_instance_id: str = None,
        mq_type: str = None,
        password: str = None,
        producer_id: str = None,
        topic: str = None,
        user_name: str = None,
    ):
        self.business_unit_id = business_unit_id
        self.endpoint = endpoint
        self.event_subscriptions = event_subscriptions
        self.mq_instance_id = mq_instance_id
        self.mq_type = mq_type
        self.password = password
        self.producer_id = producer_id
        self.topic = topic
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.event_subscriptions is not None:
            result['EventSubscriptions'] = self.event_subscriptions

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
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EventSubscriptions') is not None:
            self.event_subscriptions = m.get('EventSubscriptions')

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

