# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAssetScopeRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        match_mode: str = None,
        match_target_ids: List[str] = None,
    ):
        # The asset scope ID.
        # 
        # This parameter is required.
        self.id = id
        # The effective scope mode. Valid values:
        # 
        # - **UserGroupAll**: All user groups.
        # - **UserGroupNormal**: Specified user groups.
        # - **DeviceGroupNormal**: Specified device groups.
        # - **DevTagNormal**: Specified device tags.
        # 
        # This field determines the meaning of MatchTargetIds.
        # 
        # This parameter is required.
        self.match_mode = match_mode
        # The IDs of the user groups, device tags, or tag groups.
        self.match_target_ids = match_target_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.match_target_ids is not None:
            result['MatchTargetIds'] = self.match_target_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('MatchTargetIds') is not None:
            self.match_target_ids = m.get('MatchTargetIds')

        return self

