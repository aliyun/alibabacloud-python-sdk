# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceEvaluationResultsRequest(DaraModel):
    def __init__(
        self,
        compliance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
        risk_level: int = None,
        sort_by: str = None,
    ):
        # The compliance evaluation result. Valid values:
        # 
        # - COMPLIANT: The resource is compliant.
        # 
        # - NON_COMPLIANT: The resource is non-compliant.
        # 
        # - NOT_APPLICABLE: The rule does not apply to the resource.
        # 
        # - INSUFFICIENT_DATA: No data is available for the resource.
        # 
        # - IGNORED: The evaluation result is ignored.
        self.compliance_type = compliance_type
        # The maximum number of entries to return for a single request. Valid values: 1 to 100.
        self.max_results = max_results
        # If the response is truncated, pass the `NextToken` value in a subsequent request to retrieve the remaining results.
        self.next_token = next_token
        # The ID of the region where the resource resides. For example, `global` indicates Global, and `cn-hangzhou` indicates China (Hangzhou).
        # 
        # For more information, see [ListDiscoveredResources](https://help.aliyun.com/document_detail/169620.html).
        self.region = region
        # The resource ID.
        # 
        # For more information, see [ListDiscoveredResources](https://help.aliyun.com/document_detail/169620.html).
        self.resource_id = resource_id
        # The resource type.
        # 
        # For more information, see [ListDiscoveredResources](https://help.aliyun.com/document_detail/169620.html).
        self.resource_type = resource_type
        # The risk level of the rule. Valid values:
        # 
        # - 1: High risk.
        # 
        # - 2: Medium risk.
        # 
        # - 3: Low risk.
        self.risk_level = risk_level
        # This parameter is optional. The only supported value is `LastNonCompliantRecordTimestamp-Asc`. This value sorts resources based on when they first became non-compliant, with the earliest appearing first. Use this parameter only when you set the `ComplianceType` parameter to `NON_COMPLIANT`.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

