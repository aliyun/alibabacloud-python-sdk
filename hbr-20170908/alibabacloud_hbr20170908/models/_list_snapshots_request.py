# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSnapshotsRequest(DaraModel):
    def __init__(
        self,
        complete_time_end: int = None,
        complete_time_start: int = None,
        max_results: int = None,
        next_token: str = None,
        plan_id: str = None,
        protected_resource_id: str = None,
        skip: int = None,
        source_type: str = None,
        vault_id: str = None,
    ):
        # The end completion time. The value is a UNIX timestamp in seconds. Only backup points whose completion time is less than this value are returned.
        self.complete_time_end = complete_time_end
        # The start completion time. The value is a UNIX timestamp in seconds. Only backup points whose completion time is greater than or equal to this value are returned.
        self.complete_time_start = complete_time_start
        # The maximum number of results to return for a paged query. Default value: 10. The value must be greater than 1.
        self.max_results = max_results
        # The pagination token. You do not need to specify this parameter for the first query. When you query the next page, set this parameter to the **NextToken** value returned from the previous page. If **NextToken** is empty, no more pages exist. This parameter cannot be used together with **Skip**.
        self.next_token = next_token
        # The ID of the backup plan. This is an optional filter. If you specify this parameter, only the backup points under the specified backup plan are returned.
        self.plan_id = plan_id
        # The ID of the protected resource. The protected resource must exist, and its data source type must be the same as the value of the **SourceType** parameter.
        # 
        # This parameter is required.
        self.protected_resource_id = protected_resource_id
        # The number of entries to skip. The value must be a non-negative integer and a multiple of **MaxResults**. This parameter cannot be used together with **NextToken**.
        self.skip = skip
        # The data source type. It must be the same as the data source type of the protected resource specified by ProtectedResourceId. Valid values:
        # 
        # This parameter is required.
        self.source_type = source_type
        # The ID of the vault. This is an optional filter. If you specify this parameter, only the backup points in the specified vault are returned.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time_end is not None:
            result['CompleteTimeEnd'] = self.complete_time_end

        if self.complete_time_start is not None:
            result['CompleteTimeStart'] = self.complete_time_start

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.protected_resource_id is not None:
            result['ProtectedResourceId'] = self.protected_resource_id

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTimeEnd') is not None:
            self.complete_time_end = m.get('CompleteTimeEnd')

        if m.get('CompleteTimeStart') is not None:
            self.complete_time_start = m.get('CompleteTimeStart')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('ProtectedResourceId') is not None:
            self.protected_resource_id = m.get('ProtectedResourceId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

