# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListSubAccountResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        sub_account_list: main_models.ListSubAccountResponseBodySubAccountList = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.sub_account_list = sub_account_list

    def validate(self):
        if self.sub_account_list:
            self.sub_account_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sub_account_list is not None:
            result['SubAccountList'] = self.sub_account_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubAccountList') is not None:
            temp_model = main_models.ListSubAccountResponseBodySubAccountList()
            self.sub_account_list = temp_model.from_map(m.get('SubAccountList'))

        return self

class ListSubAccountResponseBodySubAccountList(DaraModel):
    def __init__(
        self,
        sub_account: List[main_models.ListSubAccountResponseBodySubAccountListSubAccount] = None,
    ):
        self.sub_account = sub_account

    def validate(self):
        if self.sub_account:
            for v1 in self.sub_account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubAccount'] = []
        if self.sub_account is not None:
            for k1 in self.sub_account:
                result['SubAccount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_account = []
        if m.get('SubAccount') is not None:
            for k1 in m.get('SubAccount'):
                temp_model = main_models.ListSubAccountResponseBodySubAccountListSubAccount()
                self.sub_account.append(temp_model.from_map(k1))

        return self

class ListSubAccountResponseBodySubAccountListSubAccount(DaraModel):
    def __init__(
        self,
        admin_edas_id: str = None,
        admin_user_id: str = None,
        admin_user_kp: str = None,
        email: str = None,
        phone: str = None,
        sub_edas_id: str = None,
        sub_user_id: str = None,
        sub_user_kp: str = None,
    ):
        self.admin_edas_id = admin_edas_id
        self.admin_user_id = admin_user_id
        self.admin_user_kp = admin_user_kp
        self.email = email
        self.phone = phone
        self.sub_edas_id = sub_edas_id
        self.sub_user_id = sub_user_id
        self.sub_user_kp = sub_user_kp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_edas_id is not None:
            result['AdminEdasId'] = self.admin_edas_id

        if self.admin_user_id is not None:
            result['AdminUserId'] = self.admin_user_id

        if self.admin_user_kp is not None:
            result['AdminUserKp'] = self.admin_user_kp

        if self.email is not None:
            result['Email'] = self.email

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.sub_edas_id is not None:
            result['SubEdasId'] = self.sub_edas_id

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.sub_user_kp is not None:
            result['SubUserKp'] = self.sub_user_kp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminEdasId') is not None:
            self.admin_edas_id = m.get('AdminEdasId')

        if m.get('AdminUserId') is not None:
            self.admin_user_id = m.get('AdminUserId')

        if m.get('AdminUserKp') is not None:
            self.admin_user_kp = m.get('AdminUserKp')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('SubEdasId') is not None:
            self.sub_edas_id = m.get('SubEdasId')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('SubUserKp') is not None:
            self.sub_user_kp = m.get('SubUserKp')

        return self

