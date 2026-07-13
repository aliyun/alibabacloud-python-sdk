# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class ListEventRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListEventRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status of the response.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListEventRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEventRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_data: List[main_models.ListEventRulesResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        size: int = None,
        total: int = None,
    ):
        # This parameter is deprecated. The maximum number of entries is based on Total.
        self.max_results = max_results
        # This parameter is deprecated. Paged queries are based on PageNum.
        self.next_token = next_token
        # The data entries.
        self.page_data = page_data
        # The page number of the returned results.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of pages.
        self.pages = pages
        # The number of entries on the current page.
        self.size = size
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.page_data:
            for v1 in self.page_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PageData'] = []
        if self.page_data is not None:
            for k1 in self.page_data:
                result['PageData'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pages is not None:
            result['Pages'] = self.pages

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.page_data = []
        if m.get('PageData') is not None:
            for k1 in m.get('PageData'):
                temp_model = main_models.ListEventRulesResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pages') is not None:
            self.pages = m.get('Pages')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEventRulesResponseBodyDataPageData(DaraModel):
    def __init__(
        self,
        delivery_mode: str = None,
        endpoint: main_models.ListEventRulesResponseBodyDataPageDataEndpoint = None,
        event_types: List[str] = None,
        match_rules: List[List[main_models.EventMatchRule]] = None,
        rule_name: str = None,
        subscriptions: List[main_models.ListEventRulesResponseBodyDataPageDataSubscriptions] = None,
        topic_name: str = None,
    ):
        # This parameter is deprecated.
        self.delivery_mode = delivery_mode
        # The endpoint of the subscription.
        self.endpoint = endpoint
        # The list of event types.
        self.event_types = event_types
        # The event matching rules. The rules have an OR relationship.
        self.match_rules = match_rules
        # The name of the event notification rule.
        self.rule_name = rule_name
        # The subscribers. A maximum of 20 entries are returned. If there are more subscribers, see [List Subscriptions](https://help.aliyun.com/document_detail/2804757.html).
        self.subscriptions = subscriptions
        # The name of the topic.
        self.topic_name = topic_name

    def validate(self):
        if self.endpoint:
            self.endpoint.validate()
        if self.match_rules:
            for v1 in self.match_rules:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.subscriptions:
            for v1 in self.subscriptions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_mode is not None:
            result['DeliveryMode'] = self.delivery_mode

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint.to_map()

        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        result['MatchRules'] = []
        if self.match_rules is not None:
            for k1 in self.match_rules:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['MatchRules'].append(l1)

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        result['Subscriptions'] = []
        if self.subscriptions is not None:
            for k1 in self.subscriptions:
                result['Subscriptions'].append(k1.to_map() if k1 else None)

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryMode') is not None:
            self.delivery_mode = m.get('DeliveryMode')

        if m.get('Endpoint') is not None:
            temp_model = main_models.ListEventRulesResponseBodyDataPageDataEndpoint()
            self.endpoint = temp_model.from_map(m.get('Endpoint'))

        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        self.match_rules = []
        if m.get('MatchRules') is not None:
            for k1 in m.get('MatchRules'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.EventMatchRule()
                    l1.append(temp_model.from_map(k2))
                self.match_rules.append(l1)

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        self.subscriptions = []
        if m.get('Subscriptions') is not None:
            for k1 in m.get('Subscriptions'):
                temp_model = main_models.ListEventRulesResponseBodyDataPageDataSubscriptions()
                self.subscriptions.append(temp_model.from_map(k1))

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

class ListEventRulesResponseBodyDataPageDataSubscriptions(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_value: str = None,
    ):
        # The endpoint type.
        self.endpoint_type = endpoint_type
        # The actual value of the endpoint.
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

class ListEventRulesResponseBodyDataPageDataEndpoint(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_value: str = None,
    ):
        # The endpoint type. Valid values:
        # 
        # - **topic**: A topic can deliver messages to multiple subscribers. You can add or remove subscribers later.
        # 
        # - **queue**: Messages are delivered directly to a queue. This simplifies the delivery path, but you cannot add new subscribers later.
        self.endpoint_type = endpoint_type
        # The actual value of the endpoint.
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

