# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPortalMenusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # A JSON string that levels the details of the portal menu list. Valid values:
        # 
        # *   menuType: the type of the menu.
        # 
        #     *   0: dashboard
        #     *   1: outer chain
        #     *   2: workbook
        #     *   4: directory folder
        #     *   5: form filling
        #     *   6: self-service data retrieval
        # 
        # *   menuId: menu ID
        # 
        # *   uri: ID or URL of the resource associated with the menu
        # 
        # *   showOnlyWithAccess: Authorized Only Visible
        # 
        # *   menuName: menu display name
        # 
        # *   dependentPermisson: whether the report resource associated with the menu has permissions
        # 
        # *   children: submenu
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

