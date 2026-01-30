# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ManageLoginResponseBody(DaraModel):
    def __init__(
        self,
        login_info: main_models.ManageLoginResponseBodyLoginInfo = None,
        request_id: str = None,
    ):
        self.login_info = login_info
        self.request_id = request_id

    def validate(self):
        if self.login_info:
            self.login_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_info is not None:
            result['LoginInfo'] = self.login_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginInfo') is not None:
            temp_model = main_models.ManageLoginResponseBodyLoginInfo()
            self.login_info = temp_model.from_map(m.get('LoginInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ManageLoginResponseBodyLoginInfo(DaraModel):
    def __init__(
        self,
        adb_login_port: int = None,
        login_hostname: str = None,
        login_port: int = None,
    ):
        self.adb_login_port = adb_login_port
        self.login_hostname = login_hostname
        self.login_port = login_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adb_login_port is not None:
            result['AdbLoginPort'] = self.adb_login_port

        if self.login_hostname is not None:
            result['LoginHostname'] = self.login_hostname

        if self.login_port is not None:
            result['LoginPort'] = self.login_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdbLoginPort') is not None:
            self.adb_login_port = m.get('AdbLoginPort')

        if m.get('LoginHostname') is not None:
            self.login_hostname = m.get('LoginHostname')

        if m.get('LoginPort') is not None:
            self.login_port = m.get('LoginPort')

        return self

