# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetUserInRecycleBinResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.GetUserInRecycleBinResponseBodyUser = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the RAM user.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('User') is not None:
            temp_model = main_models.GetUserInRecycleBinResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class GetUserInRecycleBinResponseBodyUser(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        delete_date: str = None,
        display_name: str = None,
        recycle_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The time when the RAM user was created.
        self.create_date = create_date
        # The time when the RAM user will be permanently deleted from the recycle bin.
        self.delete_date = delete_date
        # The display name of the RAM user.
        self.display_name = display_name
        # The time when the RAM user was deleted and moved to the recycle bin.
        self.recycle_date = recycle_date
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.recycle_date is not None:
            result['RecycleDate'] = self.recycle_date

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('RecycleDate') is not None:
            self.recycle_date = m.get('RecycleDate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

