# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class DescribeSaslUsersResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        sasl_user_list: main_models.DescribeSaslUsersResponseBodySaslUserList = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.sasl_user_list = sasl_user_list
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.sasl_user_list:
            self.sasl_user_list.validate()

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

        if self.sasl_user_list is not None:
            result['SaslUserList'] = self.sasl_user_list.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SaslUserList') is not None:
            temp_model = main_models.DescribeSaslUsersResponseBodySaslUserList()
            self.sasl_user_list = temp_model.from_map(m.get('SaslUserList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSaslUsersResponseBodySaslUserList(DaraModel):
    def __init__(
        self,
        sasl_user_vo: List[main_models.DescribeSaslUsersResponseBodySaslUserListSaslUserVO] = None,
    ):
        self.sasl_user_vo = sasl_user_vo

    def validate(self):
        if self.sasl_user_vo:
            for v1 in self.sasl_user_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SaslUserVO'] = []
        if self.sasl_user_vo is not None:
            for k1 in self.sasl_user_vo:
                result['SaslUserVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sasl_user_vo = []
        if m.get('SaslUserVO') is not None:
            for k1 in m.get('SaslUserVO'):
                temp_model = main_models.DescribeSaslUsersResponseBodySaslUserListSaslUserVO()
                self.sasl_user_vo.append(temp_model.from_map(k1))

        return self

class DescribeSaslUsersResponseBodySaslUserListSaslUserVO(DaraModel):
    def __init__(
        self,
        mechanism: str = None,
        password: str = None,
        type: str = None,
        username: str = None,
    ):
        self.mechanism = mechanism
        self.password = password
        self.type = type
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mechanism is not None:
            result['Mechanism'] = self.mechanism

        if self.password is not None:
            result['Password'] = self.password

        if self.type is not None:
            result['Type'] = self.type

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mechanism') is not None:
            self.mechanism = m.get('Mechanism')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

