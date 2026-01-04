# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        from_app_version: str = None,
        timeout: int = None,
        to_app_version: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The current version number.
        # 
        # This parameter is required.
        self.from_app_version = from_app_version
        # The timeout period of the asynchronous rollback operation. Unit: seconds. Default value: 300.
        self.timeout = timeout
        # The target version number. By default, the system automatically rolls back the container version to the previous version.
        self.to_app_version = to_app_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.from_app_version is not None:
            result['FromAppVersion'] = self.from_app_version

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.to_app_version is not None:
            result['ToAppVersion'] = self.to_app_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('FromAppVersion') is not None:
            self.from_app_version = m.get('FromAppVersion')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('ToAppVersion') is not None:
            self.to_app_version = m.get('ToAppVersion')

        return self

