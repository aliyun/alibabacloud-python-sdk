# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDataLevelPermissionWhiteListRequest(DaraModel):
    def __init__(
        self,
        white_list_model: str = None,
    ):
        # { "ruleType": "ROW_LEVEL", // The row-level permission type. "usersModel": { "userGroups": [ "0d5fb19b- ***-1248 fc27ca51", // The ID of the user group. "3d2c23d4-***-f6390f325c2d" ], "users": [ "4334 ***358", // Quick BI the UserID of the user. "Huang***3fa822" ] }, "cubeId": "7c7223ae-31d1-4d2f-b11f-3c744528014b" }
        # 
        # This parameter is required.
        self.white_list_model = white_list_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.white_list_model is not None:
            result['WhiteListModel'] = self.white_list_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteListModel') is not None:
            self.white_list_model = m.get('WhiteListModel')

        return self

