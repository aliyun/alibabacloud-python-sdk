# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class ListEventRulesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        product_name: str = None,
        resource_name: str = None,
        rule_name: str = None,
        subscription: main_models.ListEventRulesRequestSubscription = None,
        topic_name: str = None,
    ):
        # **[Deprecated]** Use PageSize for paging.
        self.max_results = max_results
        # **[Deprecated]** Use PageNum for paging.
        self.next_token = next_token
        # The page number of the returned results. Valid values: 1 to 100000. If the specified value is less than 1, the system defaults to 1. If the specified value is greater than 100000, the system defaults to 100000.
        self.page_num = page_num
        # The number of entries to return on each page. Valid values: 10 to 50. If the specified value is less than 10, the system defaults to 10. If the specified value is greater than 50, the system defaults to 50.
        self.page_size = page_size
        # The name of the cloud service for event notifications.
        self.product_name = product_name
        # The resource name in the matching rules, used to filter rules. For example, in OSS, this is the OSS bucket name.
        self.resource_name = resource_name
        # The filter condition for the rule name.
        self.rule_name = rule_name
        # The subscription endpoint.
        self.subscription = subscription
        # The name of the topic.
        self.topic_name = topic_name

    def validate(self):
        if self.subscription:
            self.subscription.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.subscription is not None:
            result['Subscription'] = self.subscription.to_map()

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Subscription') is not None:
            temp_model = main_models.ListEventRulesRequestSubscription()
            self.subscription = temp_model.from_map(m.get('Subscription'))

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

class ListEventRulesRequestSubscription(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_value: str = None,
    ):
        # The endpoint type. Valid values:
        # - **topic**: The topic type. A topic supports delivery to multiple subscription endpoints. You can add or remove subscription endpoints later.
        # - **queue**: The queue type. Messages are delivered directly to a queue. This reduces the link path, but you cannot add new subscription endpoints later.
        self.endpoint_type = endpoint_type
        # The actual value of the receiving endpoint. When EndpointType is set to topic, this is the topic name. When EndpointType is set to queue, this is the queue name.
        self.endpoint_value = endpoint_value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('EndpointValue') is not None:
            self.endpoint_value = m.get('EndpointValue')

        return self

