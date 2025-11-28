# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExtensionResponseBody(DaraModel):
    def __init__(
        self,
        current_version: str = None,
        description: str = None,
        extension_id: str = None,
        extension_name: str = None,
        is_install_need_restart: bool = None,
        is_latest_version: bool = None,
        latest_version: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.current_version = current_version
        self.description = description
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.is_install_need_restart = is_install_need_restart
        self.is_latest_version = is_latest_version
        self.latest_version = latest_version
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.description is not None:
            result['Description'] = self.description

        if self.extension_id is not None:
            result['ExtensionId'] = self.extension_id

        if self.extension_name is not None:
            result['ExtensionName'] = self.extension_name

        if self.is_install_need_restart is not None:
            result['IsInstallNeedRestart'] = self.is_install_need_restart

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExtensionId') is not None:
            self.extension_id = m.get('ExtensionId')

        if m.get('ExtensionName') is not None:
            self.extension_name = m.get('ExtensionName')

        if m.get('IsInstallNeedRestart') is not None:
            self.is_install_need_restart = m.get('IsInstallNeedRestart')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

