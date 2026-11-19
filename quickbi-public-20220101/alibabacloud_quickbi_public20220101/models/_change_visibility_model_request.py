# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeVisibilityModelRequest(DaraModel):
    def __init__(
        self,
        data_portal_id: str = None,
        menu_ids: str = None,
        show_only_with_access: bool = None,
    ):
        # The ID of the data portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id
        # The IDs of the leaf node menus in the data portal.
        # 
        # - You can specify multiple IDs. Separate multiple IDs with commas (,). A maximum of 100 IDs can be modified at a time.
        # 
        # This parameter is required.
        self.menu_ids = menu_ids
        # Specifies whether the menus are visible only to authorized users. Valid values:
        # 
        # - true: The menus are visible only to authorized users.
        # - false: The menus are visible to all users.
        # 
        # This parameter is required.
        self.show_only_with_access = show_only_with_access

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id

        if self.menu_ids is not None:
            result['MenuIds'] = self.menu_ids

        if self.show_only_with_access is not None:
            result['ShowOnlyWithAccess'] = self.show_only_with_access

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')

        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')

        if m.get('ShowOnlyWithAccess') is not None:
            self.show_only_with_access = m.get('ShowOnlyWithAccess')

        return self

