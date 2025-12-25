# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class QueryConsumerAuthorizationRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryConsumerAuthorizationRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.QueryConsumerAuthorizationRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryConsumerAuthorizationRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.QueryConsumerAuthorizationRulesResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: str = None,
    ):
        # The rules.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.QueryConsumerAuthorizationRulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class QueryConsumerAuthorizationRulesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        api_info: main_models.HttpApiApiInfo = None,
        consumer_authorization_rule_id: str = None,
        consumer_id: str = None,
        consumer_info: main_models.ConsumerInfo = None,
        create_timestamp: int = None,
        deploy_status: str = None,
        environment_info: main_models.EnvironmentInfo = None,
        expire_mode: str = None,
        expire_status: str = None,
        expire_timestamp: int = None,
        gateway_info: main_models.GatewayInfo = None,
        resource_id: str = None,
        resource_info: main_models.QueryConsumerAuthorizationRulesResponseBodyDataItemsResourceInfo = None,
        resource_type: str = None,
        update_timestamp: int = None,
    ):
        # The API details.
        self.api_info = api_info
        # The rule ID.
        self.consumer_authorization_rule_id = consumer_authorization_rule_id
        # The consumer ID.
        self.consumer_id = consumer_id
        # The consumer information.
        self.consumer_info = consumer_info
        # The creation timestamp. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The deployment status of the API in the current environment.
        self.deploy_status = deploy_status
        # The environment information.
        self.environment_info = environment_info
        # The expiry mode. Valid values: LongTerm and ShortTerm.
        self.expire_mode = expire_mode
        # The rule status.
        self.expire_status = expire_status
        # The time when the rule expires.
        self.expire_timestamp = expire_timestamp
        # The instance information.
        self.gateway_info = gateway_info
        # The resource IDs.
        self.resource_id = resource_id
        # The resource information.
        self.resource_info = resource_info
        # The resource type.
        self.resource_type = resource_type
        # The update timestamp. Unit: milliseconds.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.api_info:
            self.api_info.validate()
        if self.consumer_info:
            self.consumer_info.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.resource_info:
            self.resource_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_info is not None:
            result['apiInfo'] = self.api_info.to_map()

        if self.consumer_authorization_rule_id is not None:
            result['consumerAuthorizationRuleId'] = self.consumer_authorization_rule_id

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.consumer_info is not None:
            result['consumerInfo'] = self.consumer_info.to_map()

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status

        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.expire_mode is not None:
            result['expireMode'] = self.expire_mode

        if self.expire_status is not None:
            result['expireStatus'] = self.expire_status

        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_info is not None:
            result['resourceInfo'] = self.resource_info.to_map()

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiInfo') is not None:
            temp_model = main_models.HttpApiApiInfo()
            self.api_info = temp_model.from_map(m.get('apiInfo'))

        if m.get('consumerAuthorizationRuleId') is not None:
            self.consumer_authorization_rule_id = m.get('consumerAuthorizationRuleId')

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('consumerInfo') is not None:
            temp_model = main_models.ConsumerInfo()
            self.consumer_info = temp_model.from_map(m.get('consumerInfo'))

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')

        if m.get('environmentInfo') is not None:
            temp_model = main_models.EnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('expireMode') is not None:
            self.expire_mode = m.get('expireMode')

        if m.get('expireStatus') is not None:
            self.expire_status = m.get('expireStatus')

        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceInfo') is not None:
            temp_model = main_models.QueryConsumerAuthorizationRulesResponseBodyDataItemsResourceInfo()
            self.resource_info = temp_model.from_map(m.get('resourceInfo'))

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

class QueryConsumerAuthorizationRulesResponseBodyDataItemsResourceInfo(DaraModel):
    def __init__(
        self,
        operation_info: main_models.HttpApiOperationInfo = None,
        route: main_models.HttpRoute = None,
    ):
        # The operation information.
        self.operation_info = operation_info
        # The route.
        self.route = route

    def validate(self):
        if self.operation_info:
            self.operation_info.validate()
        if self.route:
            self.route.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_info is not None:
            result['operationInfo'] = self.operation_info.to_map()

        if self.route is not None:
            result['route'] = self.route.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationInfo') is not None:
            temp_model = main_models.HttpApiOperationInfo()
            self.operation_info = temp_model.from_map(m.get('operationInfo'))

        if m.get('route') is not None:
            temp_model = main_models.HttpRoute()
            self.route = temp_model.from_map(m.get('route'))

        return self

