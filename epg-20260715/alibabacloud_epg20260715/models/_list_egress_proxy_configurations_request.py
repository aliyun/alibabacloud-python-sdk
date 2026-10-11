# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class ListEgressProxyConfigurationsRequest(DaraModel):
    def __init__(
        self,
        egress_proxy_configuration_ids: List[str] = None,
        egress_proxy_configuration_names: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        skip: int = None,
        status: str = None,
        tag: List[main_models.ListEgressProxyConfigurationsRequestTag] = None,
    ):
        # The list of egress proxy configuration IDs.
        self.egress_proxy_configuration_ids = egress_proxy_configuration_ids
        # The list of egress proxy configuration names.
        self.egress_proxy_configuration_names = egress_proxy_configuration_names
        # The maximum number of entries to return per page during paging in a paged query. Valid values: 0 to 1000. Default value: 20.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - Leave this parameter empty for the first query or when no next query is required.
        # - If a next query is required, set this parameter to the value of NextToken returned from the previous API call.
        self.next_token = next_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The number of entries to skip during paging in a paged query. The value must be greater than or equal to 0. Default value: 0.
        self.skip = skip
        # Filters egress proxy configurations by status. Valid values:
        # 
        # - **Provisioning**: The egress proxy configuration is being created.
        # 
        # - **Available**: The egress proxy configuration is available.
        # 
        # - **Configuring**: The specifications of the egress proxy configuration are being changed.
        self.status = status
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_configuration_ids is not None:
            result['EgressProxyConfigurationIds'] = self.egress_proxy_configuration_ids

        if self.egress_proxy_configuration_names is not None:
            result['EgressProxyConfigurationNames'] = self.egress_proxy_configuration_names

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyConfigurationIds') is not None:
            self.egress_proxy_configuration_ids = m.get('EgressProxyConfigurationIds')

        if m.get('EgressProxyConfigurationNames') is not None:
            self.egress_proxy_configuration_names = m.get('EgressProxyConfigurationNames')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListEgressProxyConfigurationsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListEgressProxyConfigurationsRequestTag(DaraModel):
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

