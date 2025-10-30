# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListInstanceExtensionsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListInstanceExtensionsResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The queried extensions.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListInstanceExtensionsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListInstanceExtensionsResponseBodyItems(DaraModel):
    def __init__(
        self,
        current_version: str = None,
        description: str = None,
        extension_id: str = None,
        installed_databases: str = None,
        is_install_need_restart: bool = None,
        latest_version: str = None,
        name: str = None,
        status: str = None,
    ):
        # The current version.
        self.current_version = current_version
        # The description of the extension.
        self.description = description
        # The extension ID.
        self.extension_id = extension_id
        # The names of the databases in which the extension is installed.
        self.installed_databases = installed_databases
        # Indicates whether an instance restart is required after you install the extension for the extension to take effect.
        self.is_install_need_restart = is_install_need_restart
        # The latest version.
        self.latest_version = latest_version
        # The name of the extension.
        self.name = name
        # The status of the extension.
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

        if self.installed_databases is not None:
            result['InstalledDatabases'] = self.installed_databases

        if self.is_install_need_restart is not None:
            result['IsInstallNeedRestart'] = self.is_install_need_restart

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('InstalledDatabases') is not None:
            self.installed_databases = m.get('InstalledDatabases')

        if m.get('IsInstallNeedRestart') is not None:
            self.is_install_need_restart = m.get('IsInstallNeedRestart')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

