# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteComponentAssetRequest(DaraModel):
    def __init__(
        self,
        component_asset_uuid: str = None,
        lang: str = None,
        role_for: int = None,
    ):
        # Asset UUID.
        # 
        # This parameter is required.
        self.component_asset_uuid = component_asset_uuid
        # Set the language type for requests and received messages, default is **zh**. Values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Resource directory member account ID.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

