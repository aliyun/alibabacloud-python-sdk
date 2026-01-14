# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDataLevelPermissionRuleUsersRequest(DaraModel):
    def __init__(
        self,
        delete_user_model: str = None,
    ):
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

