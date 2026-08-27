# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserResponseBody(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        code: str = None,
        display_name: str = None,
        is_new_user: bool = None,
        message: str = None,
        request_id: str = None,
        wn_user_id: str = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # The error code.
        self.code = code
        # The cluster name.
        self.display_name = display_name
        # Indicates whether the user is newly created. A value of false indicates that an existing user is added to the tenant.
        self.is_new_user = is_new_user
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The WINNEXO platform user ID.
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.code is not None:
            result['code'] = self.code

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_new_user is not None:
            result['isNewUser'] = self.is_new_user

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isNewUser') is not None:
            self.is_new_user = m.get('isNewUser')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

