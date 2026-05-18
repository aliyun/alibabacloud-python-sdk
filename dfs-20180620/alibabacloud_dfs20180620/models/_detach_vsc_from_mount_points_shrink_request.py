# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachVscFromMountPointsShrinkRequest(DaraModel):
    def __init__(
        self,
        detach_infos_shrink: str = None,
        input_region_id: str = None,
        use_assume_role_chk_server_perm: bool = None,
    ):
        self.detach_infos_shrink = detach_infos_shrink
        # This parameter is required.
        self.input_region_id = input_region_id
        self.use_assume_role_chk_server_perm = use_assume_role_chk_server_perm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detach_infos_shrink is not None:
            result['DetachInfos'] = self.detach_infos_shrink

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.use_assume_role_chk_server_perm is not None:
            result['UseAssumeRoleChkServerPerm'] = self.use_assume_role_chk_server_perm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetachInfos') is not None:
            self.detach_infos_shrink = m.get('DetachInfos')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('UseAssumeRoleChkServerPerm') is not None:
            self.use_assume_role_chk_server_perm = m.get('UseAssumeRoleChkServerPerm')

        return self

