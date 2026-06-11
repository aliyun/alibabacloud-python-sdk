# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDataLevelPermissionRuleUsersRequest(DaraModel):
    def __init__(
        self,
        delete_user_model: str = None,
    ):
        # {
        # "ruleId": "a5bb24da-***-a891683e14da", // The ID of the row-level permission rule.
        # "cubeId": "7c7223ae-***-3c744528014b", // The ID of the dataset.
        # "delModel": {
        # "userGroups": [
        # "0d5fb19b-***-1248fc27ca51", // The ID of the user group to remove.
        # "3d2c23d4-***-f6390f325c2d"
        # ],
        # "users": [
        # "433&#x34;***358", // The ID of the user to remove.
        # "Huang***&#x33;fa822"
        # ]
        # }
        # }
        # 
        # This parameter is required.
        self.delete_user_model = delete_user_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_user_model is not None:
            result['DeleteUserModel'] = self.delete_user_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteUserModel') is not None:
            self.delete_user_model = m.get('DeleteUserModel')

        return self

