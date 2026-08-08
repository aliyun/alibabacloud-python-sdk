# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCrossAccountsRequest(DaraModel):
    def __init__(
        self,
        cross_account_owner_id: int = None,
        management_mode: str = None,
        max_results: int = None,
        next_token: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.cross_account_owner_id = cross_account_owner_id
        self.management_mode = management_mode
        self.max_results = max_results
        self.next_token = next_token
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account_owner_id is not None:
            result['CrossAccountOwnerId'] = self.cross_account_owner_id

        if self.management_mode is not None:
            result['ManagementMode'] = self.management_mode

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountOwnerId') is not None:
            self.cross_account_owner_id = m.get('CrossAccountOwnerId')

        if m.get('ManagementMode') is not None:
            self.management_mode = m.get('ManagementMode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

