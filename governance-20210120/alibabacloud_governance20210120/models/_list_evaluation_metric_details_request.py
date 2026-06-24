# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEvaluationMetricDetailsRequest(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        date: str = None,
        evaluation_domain: str = None,
        id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        scope: str = None,
        snapshot_id: str = None,
    ):
        # The ID of the member account. This parameter is applicable only to the multi-account check pattern.
        self.account_id = account_id
        # The date to query.
        self.date = date
        self.evaluation_domain = evaluation_domain
        # The ID of the check item for which you want to retrieve non-compliant resources.
        # 
        # You can call the [ListEvaluationMetadata](https://help.aliyun.com/document_detail/2841889.html) operation to obtain the check item ID.
        self.id = id
        # The maximum number of entries to return in a single request. Default value: 5.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The scope of the governance maturity check. Valid values:
        # 
        # - Account (default): queries the check item details for the current account.
        # - ResourceDirectory: queries the check item details for all member accounts in the resource directory. Before using this value, upgrade to multi-account governance maturity check.
        self.scope = scope
        # The check snapshot ID.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.date is not None:
            result['Date'] = self.date

        if self.evaluation_domain is not None:
            result['EvaluationDomain'] = self.evaluation_domain

        if self.id is not None:
            result['Id'] = self.id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('EvaluationDomain') is not None:
            self.evaluation_domain = m.get('EvaluationDomain')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

