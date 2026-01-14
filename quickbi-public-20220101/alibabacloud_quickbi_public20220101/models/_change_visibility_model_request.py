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
        # The ID of the BI portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id
        # The menu ID of the BI portal leaf node.
        # 
        # *   The directory menu cannot be authorized.
        # *   You can upload multiple parameters at a time. Separate multiple IDs with commas (,). The maximum number of parameters that can be modified at a time is 100.
        # 
        # This parameter is required.
        self.menu_ids = menu_ids
        # Whether only authorization is visible. Valid values:
        # 
        # *   true: Only the authorization is visible.
        # *   false: Both are visible.
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

