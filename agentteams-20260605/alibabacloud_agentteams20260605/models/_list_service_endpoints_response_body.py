# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class ListServiceEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListServiceEndpointsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.items = items
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListServiceEndpointsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServiceEndpointsResponseBodyItems(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        component: str = None,
        create_time: str = None,
        domain: str = None,
        domain_type: str = None,
        endpoint_config: main_models.ListServiceEndpointsResponseBodyItemsEndpointConfig = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        instance_id: str = None,
        network_type: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.component = component
        self.create_time = create_time
        self.domain = domain
        self.domain_type = domain_type
        self.endpoint_config = endpoint_config
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.instance_id = instance_id
        self.network_type = network_type
        self.status = status
        self.update_time = update_time

    def validate(self):
        if self.endpoint_config:
            self.endpoint_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.component is not None:
            result['Component'] = self.component

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.endpoint_config is not None:
            result['EndpointConfig'] = self.endpoint_config.to_map()

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('Component') is not None:
            self.component = m.get('Component')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('EndpointConfig') is not None:
            temp_model = main_models.ListServiceEndpointsResponseBodyItemsEndpointConfig()
            self.endpoint_config = temp_model.from_map(m.get('EndpointConfig'))

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListServiceEndpointsResponseBodyItemsEndpointConfig(DaraModel):
    def __init__(
        self,
        auth: main_models.ListServiceEndpointsResponseBodyItemsEndpointConfigAuth = None,
    ):
        self.auth = auth

    def validate(self):
        if self.auth:
            self.auth.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            temp_model = main_models.ListServiceEndpointsResponseBodyItemsEndpointConfigAuth()
            self.auth = temp_model.from_map(m.get('Auth'))

        return self

class ListServiceEndpointsResponseBodyItemsEndpointConfigAuth(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        api_key_name: str = None,
    ):
        self.api_key = api_key
        self.api_key_name = api_key_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_key_name is not None:
            result['ApiKeyName'] = self.api_key_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiKeyName') is not None:
            self.api_key_name = m.get('ApiKeyName')

        return self

