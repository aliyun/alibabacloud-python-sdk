# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchUserRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        limit: int = None,
        marker: str = None,
        nick_name: str = None,
        nick_name_for_fuzzy: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        user_name: str = None,
    ):
        # The email address of the user.
        self.email = email
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The nickname of the user. The nickname can be up to 128 characters in length.
        self.nick_name = nick_name
        # The nickname used for fuzzy searches. The nickname can be up to 128 characters in length.
        self.nick_name_for_fuzzy = nick_name_for_fuzzy
        # The mobile number of the user.
        self.phone = phone
        # The role of the user. Valid values:
        # 
        # *   superadmin
        # *   admin
        # *   user
        self.role = role
        # The state of the user. Valid values:
        # 
        # *   disabled: The user is prohibited from logon.
        # *   enabled: The user is in a normal state.
        self.status = status
        # The name of the user. The name can be up to 128 characters in length.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.nick_name is not None:
            result['nick_name'] = self.nick_name

        if self.nick_name_for_fuzzy is not None:
            result['nick_name_for_fuzzy'] = self.nick_name_for_fuzzy

        if self.phone is not None:
            result['phone'] = self.phone

        if self.role is not None:
            result['role'] = self.role

        if self.status is not None:
            result['status'] = self.status

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')

        if m.get('nick_name_for_fuzzy') is not None:
            self.nick_name_for_fuzzy = m.get('nick_name_for_fuzzy')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

