# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDirectorySsoStatusRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        enable_sso: bool = None,
        region_id: str = None,
    ):
        # The AD directory ID.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # Specifies whether to enable SSO. Valid values:
        # 
        # *   true: enables SSO.
        # *   false: disables SSO.
        # 
        # This parameter is required.
        self.enable_sso = enable_sso
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.enable_sso is not None:
            result['EnableSso'] = self.enable_sso

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EnableSso') is not None:
            self.enable_sso = m.get('EnableSso')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

