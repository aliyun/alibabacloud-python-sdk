# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRecommendManagedRulesRequest(DaraModel):
    def __init__(
        self,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        max_results: int = None,
        next_token: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        selected_managed_rule_identifiers: str = None,
    ):
        # The rule does not take effect on resources in the specified regions. The resources in the specified regions are not evaluated. Separate multiple region IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The rule does not take effect on resources in the specified resource groups. The resources in the specified resource groups are not evaluated. Separate multiple resource group IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The rule does not take effect on the specified resources. The specified resources are not evaluated. Separate multiple resource IDs with commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The maximum number of entries to return on each page. Default value: 200.
        self.max_results = max_results
        # The token that specifies the position from which to start the query. If this parameter is left empty, the query starts from the beginning.
        self.next_token = next_token
        # The scope of region IDs. Separate multiple region IDs with commas (,).
        self.region_ids_scope = region_ids_scope
        # The rule takes effect only on resources in the specified resource groups. Separate multiple resource group IDs with commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The rule takes effect on the specified resources. Separate multiple resource IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The managed rules that have been selected. Separate multiple rule identifiers with commas (,).
        # The system does not recommend managed rules that are of the same resource type as the selected managed rules.
        self.selected_managed_rule_identifiers = selected_managed_rule_identifiers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_region_ids_scope is not None:
            result['ExcludeRegionIdsScope'] = self.exclude_region_ids_scope

        if self.exclude_resource_group_ids_scope is not None:
            result['ExcludeResourceGroupIdsScope'] = self.exclude_resource_group_ids_scope

        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope

        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope

        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope

        if self.selected_managed_rule_identifiers is not None:
            result['SelectedManagedRuleIdentifiers'] = self.selected_managed_rule_identifiers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')

        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')

        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')

        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')

        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')

        if m.get('SelectedManagedRuleIdentifiers') is not None:
            self.selected_managed_rule_identifiers = m.get('SelectedManagedRuleIdentifiers')

        return self

