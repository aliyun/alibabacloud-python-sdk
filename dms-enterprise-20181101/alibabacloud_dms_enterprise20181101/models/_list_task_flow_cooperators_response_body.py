# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTaskFlowCooperatorsResponseBody(DaraModel):
    def __init__(
        self,
        cooperator_list: main_models.ListTaskFlowCooperatorsResponseBodyCooperatorList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The users that are involved in the task flow.
        self.cooperator_list = cooperator_list
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.cooperator_list:
            self.cooperator_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cooperator_list is not None:
            result['CooperatorList'] = self.cooperator_list.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CooperatorList') is not None:
            temp_model = main_models.ListTaskFlowCooperatorsResponseBodyCooperatorList()
            self.cooperator_list = temp_model.from_map(m.get('CooperatorList'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTaskFlowCooperatorsResponseBodyCooperatorList(DaraModel):
    def __init__(
        self,
        cooperator: List[main_models.ListTaskFlowCooperatorsResponseBodyCooperatorListCooperator] = None,
    ):
        self.cooperator = cooperator

    def validate(self):
        if self.cooperator:
            for v1 in self.cooperator:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cooperator'] = []
        if self.cooperator is not None:
            for k1 in self.cooperator:
                result['Cooperator'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cooperator = []
        if m.get('Cooperator') is not None:
            for k1 in m.get('Cooperator'):
                temp_model = main_models.ListTaskFlowCooperatorsResponseBodyCooperatorListCooperator()
                self.cooperator.append(temp_model.from_map(k1))

        return self

class ListTaskFlowCooperatorsResponseBodyCooperatorListCooperator(DaraModel):
    def __init__(
        self,
        email: str = None,
        login_name: str = None,
        nick_name: str = None,
        user_id: str = None,
    ):
        # The email address of the user.
        self.email = email
        # The username.
        self.login_name = login_name
        # The alias of the user.
        self.nick_name = nick_name
        # userId.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

