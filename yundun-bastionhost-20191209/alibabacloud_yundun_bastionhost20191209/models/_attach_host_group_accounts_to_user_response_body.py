# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class AttachHostGroupAccountsToUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.AttachHostGroupAccountsToUserResponseBodyResults] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.AttachHostGroupAccountsToUserResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class AttachHostGroupAccountsToUserResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        host_account_names: List[main_models.AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames] = None,
        host_group_id: str = None,
        message: str = None,
        user_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of authorizing the user to manage the host accounts.
        self.host_account_names = host_account_names
        # The ID of the host group.
        self.host_group_id = host_group_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        if self.host_account_names:
            for v1 in self.host_account_names:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k1 in self.host_account_names:
                result['HostAccountNames'].append(k1.to_map() if k1 else None)

        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id

        if self.message is not None:
            result['Message'] = self.message

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k1 in m.get('HostAccountNames'):
                temp_model = main_models.AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k1))

        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames(DaraModel):
    def __init__(
        self,
        code: str = None,
        host_account_name: str = None,
        message: str = None,
    ):
        # The return code that indicates whether the user was authorized to manage the host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The name of the host account.
        self.host_account_name = host_account_name
        # This parameter is deprecated.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

