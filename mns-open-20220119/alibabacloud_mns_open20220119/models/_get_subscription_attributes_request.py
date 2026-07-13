# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSubscriptionAttributesRequest(DaraModel):
    def __init__(
        self,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The name of the topic to which the subscription belongs.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

