# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgUserGroupQueryUserListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DsgUserGroupQueryUserListResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DsgUserGroupQueryUserListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DsgUserGroupQueryUserListResponseBodyData(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: int = None,
        base_id: str = None,
        parent_account_id: str = None,
        yun_account: str = None,
    ):
        # The name of the user.
        self.account_name = account_name
        # The type of the user. Valid values:
        # 
        # *   1 to 5: Alibaba Cloud account
        # *   6: RAM role
        self.account_type = account_type
        # The user ID or role ID.
        self.base_id = base_id
        # The parent user ID. This parameter is required if a RAM user is used.
        self.parent_account_id = parent_account_id
        # The name of the Alibaba Cloud account or RAM role. The return value of this parameter must be used if the user group is created by using an Alibaba Cloud account or a RAM role.
        self.yun_account = yun_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.base_id is not None:
            result['BaseId'] = self.base_id

        if self.parent_account_id is not None:
            result['ParentAccountId'] = self.parent_account_id

        if self.yun_account is not None:
            result['YunAccount'] = self.yun_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        if m.get('ParentAccountId') is not None:
            self.parent_account_id = m.get('ParentAccountId')

        if m.get('YunAccount') is not None:
            self.yun_account = m.get('YunAccount')

        return self

