# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class AddUsersToGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.AddUsersToGroupResponseBodyResults] = None,
    ):
        # The request ID. Alibaba Cloud generates a unique ID for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The result information of the operation.
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
                temp_model = main_models.AddUsersToGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class AddUsersToGroupResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        user_group_id: str = None,
        user_id: str = None,
    ):
        # The result of the operation. Valid values:
        # - **OK**: The operation was successful.
        # - **UNEXPECTED**: An unknown error occurred.
        # - **INVALID_ARGUMENT**: The request parameters are invalid.
        # 
        #     > Check the request parameters and call the operation again.
        # 
        # - **OBJECT_NOT_FOUND**: The specified object does not exist.
        # 
        #     > Check whether the bastion host instance ID exists, whether the host exists, and whether the host ID is correct, and then call the operation again.
        # 
        # - **OBJECT_AlREADY_EXISTS**: The specified object already exists.
        self.code = code
        # This parameter is deprecated and can be ignored.
        self.message = message
        # The user group ID.
        self.user_group_id = user_group_id
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

