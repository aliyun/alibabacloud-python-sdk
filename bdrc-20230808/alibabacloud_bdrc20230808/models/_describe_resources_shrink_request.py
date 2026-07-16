# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        data_redundancy_type: str = None,
        failed_rule_template: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_arn: str = None,
        resource_category_id: str = None,
        resource_id: str = None,
        resource_owner_ids_shrink: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
        sort_by: str = None,
        sort_order: str = None,
        storage_class: str = None,
    ):
        # The data redundancy type.
        self.data_redundancy_type = data_redundancy_type
        # A filter for rules that failed the scoring.
        self.failed_rule_template = failed_rule_template
        # The page size. Default: 10. Maximum: 100. Values less than 10 are set to 10, and values greater than 100 are set to 100.
        self.max_results = max_results
        # The pagination token. The service returns a token if the response is truncated. To retrieve the next page of results, include this token in your next request. If no token is returned, all results have been retrieved.
        self.next_token = next_token
        # The Resource ARN.
        self.resource_arn = resource_arn
        # The ID of the resource category.
        self.resource_category_id = resource_category_id
        # The resource ID. For example, for an instance, this is the instance ID.
        self.resource_id = resource_id
        # A list of resource owner IDs. Use this parameter for cross-account scenarios. If you omit this parameter, the service returns data for the current account by default.
        self.resource_owner_ids_shrink = resource_owner_ids_shrink
        # The resource region ID.
        self.resource_region_id = resource_region_id
        # The resource type.
        self.resource_type = resource_type
        # The sort key.
        self.sort_by = sort_by
        # The sort order.
        self.sort_order = sort_order
        # The storage class.
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type

        if self.failed_rule_template is not None:
            result['FailedRuleTemplate'] = self.failed_rule_template

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_category_id is not None:
            result['ResourceCategoryId'] = self.resource_category_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_ids_shrink is not None:
            result['ResourceOwnerIds'] = self.resource_owner_ids_shrink

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')

        if m.get('FailedRuleTemplate') is not None:
            self.failed_rule_template = m.get('FailedRuleTemplate')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerIds') is not None:
            self.resource_owner_ids_shrink = m.get('ResourceOwnerIds')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        return self

