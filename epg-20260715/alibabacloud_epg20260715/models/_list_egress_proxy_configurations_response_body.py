# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class ListEgressProxyConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        egress_proxy_configurations: List[main_models.ListEgressProxyConfigurationsResponseBodyEgressProxyConfigurations] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of egress proxy configurations.
        self.egress_proxy_configurations = egress_proxy_configurations
        # The maximum number of entries returned for the current request.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If NextToken is empty, no next query is required.
        # - If NextToken is returned, the value indicates the token for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of egress proxy configurations that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.egress_proxy_configurations:
            for v1 in self.egress_proxy_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EgressProxyConfigurations'] = []
        if self.egress_proxy_configurations is not None:
            for k1 in self.egress_proxy_configurations:
                result['EgressProxyConfigurations'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.egress_proxy_configurations = []
        if m.get('EgressProxyConfigurations') is not None:
            for k1 in m.get('EgressProxyConfigurations'):
                temp_model = main_models.ListEgressProxyConfigurationsResponseBodyEgressProxyConfigurations()
                self.egress_proxy_configurations.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEgressProxyConfigurationsResponseBodyEgressProxyConfigurations(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        egress_proxy_configuration_id: str = None,
        egress_proxy_configuration_name: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListEgressProxyConfigurationsResponseBodyEgressProxyConfigurationsTags] = None,
    ):
        # The time when the egress proxy configuration was created. The time is displayed in UTC in the yyyy-MM-ddTHH:mm:ssZ format.
        self.create_time = create_time
        # The description of the egress proxy configuration. The description must be 2 to 256 characters in length, and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # The ID of the egress proxy configuration.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id
        # The name of the egress proxy configuration. The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        self.egress_proxy_configuration_name = egress_proxy_configuration_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the egress proxy configuration. Valid values:
        # 
        # - **Provisioning**: The egress proxy configuration is being created.
        # 
        # - **Available**: The egress proxy configuration is available.
        # 
        # - **Configuring**: The specifications of the egress proxy configuration are being changed.
        self.status = status
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        if self.egress_proxy_configuration_name is not None:
            result['EgressProxyConfigurationName'] = self.egress_proxy_configuration_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        if m.get('EgressProxyConfigurationName') is not None:
            self.egress_proxy_configuration_name = m.get('EgressProxyConfigurationName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListEgressProxyConfigurationsResponseBodyEgressProxyConfigurationsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListEgressProxyConfigurationsResponseBodyEgressProxyConfigurationsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The value can be up to 256 characters in length and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

