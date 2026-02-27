# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResourceGroupAdminSettingRequest(DaraModel):
    def __init__(
        self,
        creator_as_admin: bool = None,
    ):
        # Specifies whether to enable the Use Creator as Administrator feature.
        # 
        # This parameter is required.
        self.creator_as_admin = creator_as_admin

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_as_admin is not None:
            result['CreatorAsAdmin'] = self.creator_as_admin

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorAsAdmin') is not None:
            self.creator_as_admin = m.get('CreatorAsAdmin')

        return self

