# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListIntegrationPoliciesRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        bind_resource_id: str = None,
        entity_group_ids: str = None,
        filter_region_ids: str = None,
        max_results: int = None,
        next_token: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        prometheus_instance_id: str = None,
        query: str = None,
        resource_group_id: str = None,
        tag: List[main_models.ListIntegrationPoliciesRequestTag] = None,
        workspace: str = None,
    ):
        # The add-on name.
        self.addon_name = addon_name
        # The ID of the attached resource.
        self.bind_resource_id = bind_resource_id
        # The IDs of the entity groups to filter by. Separate multiple IDs with commas.
        self.entity_group_ids = entity_group_ids
        # The IDs of the regions to query. Separate multiple region IDs with commas.
        self.filter_region_ids = filter_region_ids
        # The maximum number of entries to return on each page. The default value is 30. The maximum value is 100.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. You do not need to specify this parameter for the first request. You can obtain the token from the response to the previous request.
        self.next_token = next_token
        # The policy ID.
        self.policy_id = policy_id
        # The policy name.
        self.policy_name = policy_name
        # The policy type.
        self.policy_type = policy_type
        # The instance ID.
        self.prometheus_instance_id = prometheus_instance_id
        # A general-purpose query string.
        self.query = query
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tag = tag
        # The workspace.
        self.workspace = workspace

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
        if self.addon_name is not None:
            result['addonName'] = self.addon_name

        if self.bind_resource_id is not None:
            result['bindResourceId'] = self.bind_resource_id

        if self.entity_group_ids is not None:
            result['entityGroupIds'] = self.entity_group_ids

        if self.filter_region_ids is not None:
            result['filterRegionIds'] = self.filter_region_ids

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.policy_type is not None:
            result['policyType'] = self.policy_type

        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id

        if self.query is not None:
            result['query'] = self.query

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['tag'].append(k1.to_map() if k1 else None)

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('bindResourceId') is not None:
            self.bind_resource_id = m.get('bindResourceId')

        if m.get('entityGroupIds') is not None:
            self.entity_group_ids = m.get('entityGroupIds')

        if m.get('filterRegionIds') is not None:
            self.filter_region_ids = m.get('filterRegionIds')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')

        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tag = []
        if m.get('tag') is not None:
            for k1 in m.get('tag'):
                temp_model = main_models.ListIntegrationPoliciesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListIntegrationPoliciesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

