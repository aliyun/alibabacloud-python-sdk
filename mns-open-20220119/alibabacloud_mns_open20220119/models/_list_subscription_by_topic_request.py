# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSubscriptionByTopicRequest(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_value: str = None,
        page_num: int = None,
        page_size: int = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        self.endpoint_type = endpoint_type
        self.endpoint_value = endpoint_value
        # The page number of the results to return.
        # Valid values: 1 to 100000000.
        # If the value is less than 1, the system uses 1. If the value is greater than 100000000, the system uses 100000000.
        self.page_num = page_num
        # The number of entries to return on each page.
        # Valid values: 10 to 50.
        # If the value is less than 10, the system uses 10. If the value is greater than 50, the system uses 50.
        self.page_size = page_size
        # The subscription name.
        self.subscription_name = subscription_name
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.endpoint_value is not None:
            result['EndpointValue'] = self.endpoint_value

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('EndpointValue') is not None:
            self.endpoint_value = m.get('EndpointValue')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

