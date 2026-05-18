# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMountPointsVscAttachInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        input_region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        query_infos_shrink: str = None,
        use_assume_role_chk_server_perm: bool = None,
    ):
        # This parameter is required.
        self.input_region_id = input_region_id
        self.max_results = max_results
        self.next_token = next_token
        self.query_infos_shrink = query_infos_shrink
        self.use_assume_role_chk_server_perm = use_assume_role_chk_server_perm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.query_infos_shrink is not None:
            result['QueryInfos'] = self.query_infos_shrink

        if self.use_assume_role_chk_server_perm is not None:
            result['UseAssumeRoleChkServerPerm'] = self.use_assume_role_chk_server_perm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('QueryInfos') is not None:
            self.query_infos_shrink = m.get('QueryInfos')

        if m.get('UseAssumeRoleChkServerPerm') is not None:
            self.use_assume_role_chk_server_perm = m.get('UseAssumeRoleChkServerPerm')

        return self

