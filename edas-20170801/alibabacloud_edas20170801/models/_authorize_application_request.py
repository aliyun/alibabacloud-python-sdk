# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeApplicationRequest(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
        target_user_id: str = None,
    ):
        # The ID of the application. You can specify multiple IDs. Separate multiple IDs with semicolons (;). If you leave this parameter empty, the permissions on the application are revoked.
        # 
        # This parameter is required.
        self.app_ids = app_ids
        # The ID of the RAM user to be authorized. The value of the parameter is in the `sub-account name@primary account UID` format.
        # 
        # This parameter is required.
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

