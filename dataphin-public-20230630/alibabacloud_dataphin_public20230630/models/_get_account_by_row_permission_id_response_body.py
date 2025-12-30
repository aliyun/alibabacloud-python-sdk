# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetAccountByRowPermissionIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetAccountByRowPermissionIdResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetAccountByRowPermissionIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAccountByRowPermissionIdResponseBodyData(DaraModel):
    def __init__(
        self,
        id: int = None,
        user_mapping_list: List[main_models.GetAccountByRowPermissionIdResponseBodyDataUserMappingList] = None,
    ):
        self.id = id
        self.user_mapping_list = user_mapping_list

    def validate(self):
        if self.user_mapping_list:
            for v1 in self.user_mapping_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        result['UserMappingList'] = []
        if self.user_mapping_list is not None:
            for k1 in self.user_mapping_list:
                result['UserMappingList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.user_mapping_list = []
        if m.get('UserMappingList') is not None:
            for k1 in m.get('UserMappingList'):
                temp_model = main_models.GetAccountByRowPermissionIdResponseBodyDataUserMappingList()
                self.user_mapping_list.append(temp_model.from_map(k1))

        return self

class GetAccountByRowPermissionIdResponseBodyDataUserMappingList(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        accounts: List[main_models.GetAccountByRowPermissionIdResponseBodyDataUserMappingListAccounts] = None,
    ):
        self.account_type = account_type
        self.accounts = accounts

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.GetAccountByRowPermissionIdResponseBodyDataUserMappingListAccounts()
                self.accounts.append(temp_model.from_map(k1))

        return self

class GetAccountByRowPermissionIdResponseBodyDataUserMappingListAccounts(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        return self

