# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeAndroidInstanceRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        authorize_user_id: str = None,
        un_authorize_user_id: str = None,
    ):
        # List of instance IDs.
        self.android_instance_ids = android_instance_ids
        # User ID to be assigned.
        self.authorize_user_id = authorize_user_id
        # User ID to be unassigned.
        self.un_authorize_user_id = un_authorize_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.authorize_user_id is not None:
            result['AuthorizeUserId'] = self.authorize_user_id

        if self.un_authorize_user_id is not None:
            result['UnAuthorizeUserId'] = self.un_authorize_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('AuthorizeUserId') is not None:
            self.authorize_user_id = m.get('AuthorizeUserId')

        if m.get('UnAuthorizeUserId') is not None:
            self.un_authorize_user_id = m.get('UnAuthorizeUserId')

        return self

