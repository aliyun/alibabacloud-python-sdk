# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListAiccsRobotResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAiccsRobotResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = main_models.ListAiccsRobotResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAiccsRobotResponseBodyData(DaraModel):
    def __init__(
        self,
        at_profession: str = None,
        at_sence: str = None,
        id: int = None,
        robot_name: str = None,
        robot_type: str = None,
    ):
        self.at_profession = at_profession
        self.at_sence = at_sence
        self.id = id
        self.robot_name = robot_name
        self.robot_type = robot_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.at_profession is not None:
            result['AtProfession'] = self.at_profession

        if self.at_sence is not None:
            result['AtSence'] = self.at_sence

        if self.id is not None:
            result['Id'] = self.id

        if self.robot_name is not None:
            result['RobotName'] = self.robot_name

        if self.robot_type is not None:
            result['RobotType'] = self.robot_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtProfession') is not None:
            self.at_profession = m.get('AtProfession')

        if m.get('AtSence') is not None:
            self.at_sence = m.get('AtSence')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')

        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')

        return self

