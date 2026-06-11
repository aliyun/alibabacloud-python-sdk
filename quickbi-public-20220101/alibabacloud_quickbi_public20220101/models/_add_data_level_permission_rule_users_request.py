# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataLevelPermissionRuleUsersRequest(DaraModel):
    def __init__(
        self,
        add_user_model: str = None,
    ):
        # {
        # "ruleId": "a5bb24da-***-a891683e14da", // The ID of the row-level permission rule.
        # "cubeId": "7c7223ae-***-3c744528014b", // The ID of the dataset.
        # "addModel": {
        # "userGroups": [
        # "0d5fb19b-***-1248fc27ca51", // The IDs of the user groups to add.
        # "3d2c23d4-***-f6390f325c2d"
        # ],
        # "users": [
        # "433&#x34;***358", // The user IDs of the users to add.
        # "Huang***&#x33;fa822"
        # ]
        # }
        # }
        # 
        # This parameter is required.
        self.add_user_model = add_user_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_user_model is not None:
            result['AddUserModel'] = self.add_user_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddUserModel') is not None:
            self.add_user_model = m.get('AddUserModel')

        return self

