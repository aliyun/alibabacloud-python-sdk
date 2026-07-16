# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class CrossAccountVerifyTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CrossAccountVerifyTokenResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

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

        if self.result is not None:
            result['Result'] = self.result.to_map()

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

        if m.get('Result') is not None:
            temp_model = main_models.CrossAccountVerifyTokenResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CrossAccountVerifyTokenResponseBodyResult(DaraModel):
    def __init__(
        self,
        auth_roles: List[str] = None,
        auth_time: int = None,
        name: str = None,
        uid: str = None,
    ):
        self.auth_roles = auth_roles
        self.auth_time = auth_time
        self.name = name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_roles is not None:
            result['AuthRoles'] = self.auth_roles

        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time

        if self.name is not None:
            result['Name'] = self.name

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthRoles') is not None:
            self.auth_roles = m.get('AuthRoles')

        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

