# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_companyreg20200306 import models as main_models
from darabonba.model import DaraModel

class BindProduceAuthorizationResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.BindProduceAuthorizationResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.BindProduceAuthorizationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BindProduceAuthorizationResponseBodyData(DaraModel):
    def __init__(
        self,
        authorized_user_list: List[main_models.BindProduceAuthorizationResponseBodyDataAuthorizedUserList] = None,
        message: str = None,
        success: bool = None,
    ):
        self.authorized_user_list = authorized_user_list
        self.message = message
        self.success = success

    def validate(self):
        if self.authorized_user_list:
            for v1 in self.authorized_user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizedUserList'] = []
        if self.authorized_user_list is not None:
            for k1 in self.authorized_user_list:
                result['AuthorizedUserList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_user_list = []
        if m.get('AuthorizedUserList') is not None:
            for k1 in m.get('AuthorizedUserList'):
                temp_model = main_models.BindProduceAuthorizationResponseBodyDataAuthorizedUserList()
                self.authorized_user_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class BindProduceAuthorizationResponseBodyDataAuthorizedUserList(DaraModel):
    def __init__(
        self,
        account_valid_type: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.account_valid_type = account_valid_type
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_valid_type is not None:
            result['AccountValidType'] = self.account_valid_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountValidType') is not None:
            self.account_valid_type = m.get('AccountValidType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

