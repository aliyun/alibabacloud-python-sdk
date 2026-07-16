# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class ResetUserPasswordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ResetUserPasswordResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.ResetUserPasswordResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ResetUserPasswordResponseBodyData(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        password: str = None,
        subject: str = None,
        user_pool_id: str = None,
    ):
        self.instance_id = instance_id
        self.name = name
        self.password = password
        self.subject = subject
        self.user_pool_id = user_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.password is not None:
            result['Password'] = self.password

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.user_pool_id is not None:
            result['UserPoolId'] = self.user_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('UserPoolId') is not None:
            self.user_pool_id = m.get('UserPoolId')

        return self

