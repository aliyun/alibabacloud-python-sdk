# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceLinkedRoleStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeServiceLinkedRoleStatusResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.DescribeServiceLinkedRoleStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeServiceLinkedRoleStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        body: main_models.DescribeServiceLinkedRoleStatusResponseBodyDataBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.DescribeServiceLinkedRoleStatusResponseBodyDataBody()
            self.body = temp_model.from_map(m.get('Body'))

        return self

class DescribeServiceLinkedRoleStatusResponseBodyDataBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        role_status: main_models.DescribeServiceLinkedRoleStatusResponseBodyDataBodyRoleStatus = None,
    ):
        self.request_id = request_id
        self.role_status = role_status

    def validate(self):
        if self.role_status:
            self.role_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_status is not None:
            result['RoleStatus'] = self.role_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleStatus') is not None:
            temp_model = main_models.DescribeServiceLinkedRoleStatusResponseBodyDataBodyRoleStatus()
            self.role_status = temp_model.from_map(m.get('RoleStatus'))

        return self

class DescribeServiceLinkedRoleStatusResponseBodyDataBodyRoleStatus(DaraModel):
    def __init__(
        self,
        status: bool = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

