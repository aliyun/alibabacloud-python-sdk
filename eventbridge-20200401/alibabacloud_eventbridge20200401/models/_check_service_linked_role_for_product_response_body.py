# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CheckServiceLinkedRoleForProductResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CheckServiceLinkedRoleForProductResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # The returned data.
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
            temp_model = main_models.CheckServiceLinkedRoleForProductResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CheckServiceLinkedRoleForProductResponseBodyData(DaraModel):
    def __init__(
        self,
        check_pass: bool = None,
        sts_role_name: str = None,
    ):
        # Indicates whether the service-linked role exists.
        self.check_pass = check_pass
        # The name of the service-linked role.
        self.sts_role_name = sts_role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_pass is not None:
            result['CheckPass'] = self.check_pass

        if self.sts_role_name is not None:
            result['StsRoleName'] = self.sts_role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckPass') is not None:
            self.check_pass = m.get('CheckPass')

        if m.get('StsRoleName') is not None:
            self.sts_role_name = m.get('StsRoleName')

        return self

