# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class CreateUsersResponseBody(DaraModel):
    def __init__(
        self,
        all_succeed: bool = None,
        create_result: main_models.CreateUsersResponseBodyCreateResult = None,
        request_id: str = None,
    ):
        self.all_succeed = all_succeed
        # The result of user creation.
        self.create_result = create_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.create_result:
            self.create_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_succeed is not None:
            result['AllSucceed'] = self.all_succeed

        if self.create_result is not None:
            result['CreateResult'] = self.create_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllSucceed') is not None:
            self.all_succeed = m.get('AllSucceed')

        if m.get('CreateResult') is not None:
            temp_model = main_models.CreateUsersResponseBodyCreateResult()
            self.create_result = temp_model.from_map(m.get('CreateResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateUsersResponseBodyCreateResult(DaraModel):
    def __init__(
        self,
        created_users: List[main_models.CreateUsersResponseBodyCreateResultCreatedUsers] = None,
        failed_users: List[main_models.CreateUsersResponseBodyCreateResultFailedUsers] = None,
    ):
        # Details of the created convenience users.
        self.created_users = created_users
        # Details of the convenience users that failed to be created.
        self.failed_users = failed_users

    def validate(self):
        if self.created_users:
            for v1 in self.created_users:
                 if v1:
                    v1.validate()
        if self.failed_users:
            for v1 in self.failed_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CreatedUsers'] = []
        if self.created_users is not None:
            for k1 in self.created_users:
                result['CreatedUsers'].append(k1.to_map() if k1 else None)

        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k1 in self.failed_users:
                result['FailedUsers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.created_users = []
        if m.get('CreatedUsers') is not None:
            for k1 in m.get('CreatedUsers'):
                temp_model = main_models.CreateUsersResponseBodyCreateResultCreatedUsers()
                self.created_users.append(temp_model.from_map(k1))

        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k1 in m.get('FailedUsers'):
                temp_model = main_models.CreateUsersResponseBodyCreateResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k1))

        return self

class CreateUsersResponseBodyCreateResultFailedUsers(DaraModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        error_code: str = None,
        error_message: str = None,
        phone: str = None,
    ):
        # The email address of the end user.
        self.email = email
        # The name of the end user.
        self.end_user_id = end_user_id
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The mobile number of the end user.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.phone is not None:
            result['Phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        return self

class CreateUsersResponseBodyCreateResultCreatedUsers(DaraModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        phone: str = None,
        real_nick_name: str = None,
        remark: str = None,
    ):
        # The email address of the end user.
        self.email = email
        # The name of the end user.
        self.end_user_id = end_user_id
        # The mobile number of the end user.
        self.phone = phone
        # The display name of the end user.
        self.real_nick_name = real_nick_name
        # The remarks of the end user.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

