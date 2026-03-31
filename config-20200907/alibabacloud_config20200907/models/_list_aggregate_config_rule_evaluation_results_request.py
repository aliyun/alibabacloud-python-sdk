# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAggregateConfigRuleEvaluationResultsRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        compliance_type: str = None,
        config_rule_id: str = None,
        max_results: int = None,
        next_token: str = None,
        regions: str = None,
        resource_account_id: int = None,
        resource_group_ids: str = None,
        resource_owner_id: int = None,
        resource_types: str = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The ID of the compliance package.
        # 
        # For more information about how to obtain the ID of a compliance package, see [ListAggregateCompliancePacks](https://help.aliyun.com/document_detail/262059.html).
        self.compliance_pack_id = compliance_pack_id
        # The compliance evaluation result of the resource. Valid values:
        # 
        # *   COMPLIANT: The resource is evaluated as compliant.
        # *   NON_COMPLIANT: The resource is evaluated as non-compliant.
        # *   NOT_APPLICABLE: The rule does not apply to your resource.
        # *   INSUFFICIENT_DATA: No data is available.
        # *   IGNORED: The resource is ignored during compliance evaluation.
        self.compliance_type = compliance_type
        # The rule ID.
        # 
        # For more information about how to query the ID of a rule, see [ListAggregateConfigRules](https://help.aliyun.com/document_detail/264148.html).
        self.config_rule_id = config_rule_id
        # The maximum number of entries to return in a request. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The ID of the region whose resources you want to evaluate. Separate multiple region IDs with commas (,).
        self.regions = regions
        # Member accountId to which the resource to be queried belongs.
        self.resource_account_id = resource_account_id
        # The ID of the resource group whose resources you want to evaluate. Separate multiple resource group IDs with commas (,).
        self.resource_group_ids = resource_group_ids
        self.resource_owner_id = resource_owner_id
        # The type of the resources that you want to evaluate. Separate multiple resource types with commas (,).
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.regions is not None:
            result['Regions'] = self.regions

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Regions') is not None:
            self.regions = m.get('Regions')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        return self

