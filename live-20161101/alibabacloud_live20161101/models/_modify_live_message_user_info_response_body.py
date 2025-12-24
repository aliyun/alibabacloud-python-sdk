# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ModifyLiveMessageUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        fail_list: List[main_models.ModifyLiveMessageUserInfoResponseBodyFailList] = None,
        request_id: str = None,
        success_list: List[main_models.ModifyLiveMessageUserInfoResponseBodySuccessList] = None,
    ):
        # The users whose information failed to be modified.
        self.fail_list = fail_list
        # The request ID.
        self.request_id = request_id
        # The users whose information was modified.
        self.success_list = success_list

    def validate(self):
        if self.fail_list:
            for v1 in self.fail_list:
                 if v1:
                    v1.validate()
        if self.success_list:
            for v1 in self.success_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailList'] = []
        if self.fail_list is not None:
            for k1 in self.fail_list:
                result['FailList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SuccessList'] = []
        if self.success_list is not None:
            for k1 in self.success_list:
                result['SuccessList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_list = []
        if m.get('FailList') is not None:
            for k1 in m.get('FailList'):
                temp_model = main_models.ModifyLiveMessageUserInfoResponseBodyFailList()
                self.fail_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.success_list = []
        if m.get('SuccessList') is not None:
            for k1 in m.get('SuccessList'):
                temp_model = main_models.ModifyLiveMessageUserInfoResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k1))

        return self

class ModifyLiveMessageUserInfoResponseBodySuccessList(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        success: bool = None,
    ):
        # The ID of the group to which the user belongs. For successful modification, the information of the user is updated when you query the users in the group.
        self.group_id = group_id
        # Indicates whether the group to which the user belongs is modified. In this case, the group is modified.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifyLiveMessageUserInfoResponseBodyFailList(DaraModel):
    def __init__(
        self,
        code: int = None,
        group_id: str = None,
        reason: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The ID of the group to which the user belongs. For failed modification, the information of the user is not updated when you query the users in the group. You can try again after you check the failure reason and fix the issue.
        self.group_id = group_id
        # The reason why the information of the user failed to be modified.
        self.reason = reason
        # Indicates whether the group to which the user belongs is modified. In this case, the group is not modified.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

