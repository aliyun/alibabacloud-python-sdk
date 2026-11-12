# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudAccountResourcesRequest(DaraModel):
    def __init__(
        self,
        cloud_account_id: str = None,
        cloud_account_resource_entity_type: str = None,
        cloud_account_resource_name_contains: str = None,
        cloud_account_resource_name_prefix: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the cloud account.
        # 
        # This parameter is required.
        self.cloud_account_id = cloud_account_id
        # Filters resources by entity type. Valid values: ram_policy.
        self.cloud_account_resource_entity_type = cloud_account_resource_entity_type
        # The keyword used for fuzzy matching of the resource name. This is equivalent to LIKE \\"%value%\\".
        self.cloud_account_resource_name_contains = cloud_account_resource_name_contains
        # The prefix of the resource name used for matching.
        self.cloud_account_resource_name_prefix = cloud_account_resource_name_prefix
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of entries to return per page during paging in a paged query. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The query token. Set the value to the NextToken value returned by the previous API call.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_account_resource_entity_type is not None:
            result['CloudAccountResourceEntityType'] = self.cloud_account_resource_entity_type

        if self.cloud_account_resource_name_contains is not None:
            result['CloudAccountResourceNameContains'] = self.cloud_account_resource_name_contains

        if self.cloud_account_resource_name_prefix is not None:
            result['CloudAccountResourceNamePrefix'] = self.cloud_account_resource_name_prefix

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudAccountResourceEntityType') is not None:
            self.cloud_account_resource_entity_type = m.get('CloudAccountResourceEntityType')

        if m.get('CloudAccountResourceNameContains') is not None:
            self.cloud_account_resource_name_contains = m.get('CloudAccountResourceNameContains')

        if m.get('CloudAccountResourceNamePrefix') is not None:
            self.cloud_account_resource_name_prefix = m.get('CloudAccountResourceNamePrefix')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

