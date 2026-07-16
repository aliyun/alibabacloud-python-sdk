# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEventRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        product_name: str = None,
        resource_name: str = None,
        rule_name: str = None,
        subscription_shrink: str = None,
        topic_name: str = None,
    ):
        # This parameter is deprecated. Use PageSize for paged queries.
        self.max_results = max_results
        # This parameter is deprecated. Use PageNum for paged queries.
        self.next_token = next_token
        # The page number of the results to return.
        # Valid values: 1 to 100000.
        # If you set this parameter to a value less than 1, the system uses 1. If you set this parameter to a value greater than 100000, the system uses 100000.
        self.page_num = page_num
        # The number of entries to return on each page.
        # Valid values: 10 to 50.
        # If you set this parameter to a value less than 10, the system uses 10. If you set this parameter to a value greater than 50, the system uses 50.
        self.page_size = page_size
        # The name of the Alibaba Cloud service for which event notifications are configured.
        self.product_name = product_name
        # The resource name in the matching rule. This parameter is used to filter rules. For example, for Object Storage Service (OSS), this is the bucket name.
        self.resource_name = resource_name
        # The name of the rule.
        self.rule_name = rule_name
        # The subscriber.
        self.subscription_shrink = subscription_shrink
        # The name of the topic.
        self.topic_name = topic_name

    def validate(self):
        pass

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

        if self.subscription_shrink is not None:
            result['Subscription'] = self.subscription_shrink

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
            self.subscription_shrink = m.get('Subscription')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

