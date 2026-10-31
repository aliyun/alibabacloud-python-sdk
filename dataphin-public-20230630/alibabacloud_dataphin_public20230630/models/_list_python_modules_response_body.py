# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListPythonModulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListPythonModulesResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The paged query result with paging details.
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListPythonModulesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListPythonModulesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        python_module_list: List[main_models.ListPythonModulesResponseBodyPageResultPythonModuleList] = None,
        total_count: int = None,
    ):
        # The paginated list of Python third-party packages.
        self.python_module_list = python_module_list
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.python_module_list:
            for v1 in self.python_module_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PythonModuleList'] = []
        if self.python_module_list is not None:
            for k1 in self.python_module_list:
                result['PythonModuleList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.python_module_list = []
        if m.get('PythonModuleList') is not None:
            for k1 in m.get('PythonModuleList'):
                temp_model = main_models.ListPythonModulesResponseBodyPageResultPythonModuleList()
                self.python_module_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPythonModulesResponseBodyPageResultPythonModuleList(DaraModel):
    def __init__(
        self,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        install_time: str = None,
        install_type: str = None,
        installer: str = None,
        name: str = None,
        python_version: str = None,
        status: str = None,
        version: str = None,
    ):
        # The creation time.
        self.gmt_created = gmt_created
        # The last update time.
        self.gmt_modified = gmt_modified
        # The ID of the Python third-party package.
        self.id = id
        # The installation time.
        self.install_time = install_time
        # The installation method. Valid values:
        # - UPLOAD_INSTALL: upload installation package
        # - ONLINE_INSTALL: online installation
        self.install_type = install_type
        # The installer.
        self.installer = installer
        # The name of the Python third-party package.
        self.name = name
        # The Python version. Valid values: PYTHON_2_7, PYTHON_3_7, and PYTHON_3_11.
        self.python_version = python_version
        # The status of the third-party package. Valid values:
        # - INSTALL_SUCCESS: installation succeeded
        # - INSTALL_FAILED: installation failed
        # - INSTALLING: installing
        # - UPGRADE_SUCCESS: upgrade succeeded
        # - UPGRADE_FAILED: upgrade failed
        # - UPGRADING: upgrading
        self.status = status
        # The version of the third-party package.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.install_time is not None:
            result['InstallTime'] = self.install_time

        if self.install_type is not None:
            result['InstallType'] = self.install_type

        if self.installer is not None:
            result['Installer'] = self.installer

        if self.name is not None:
            result['Name'] = self.name

        if self.python_version is not None:
            result['PythonVersion'] = self.python_version

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')

        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')

        if m.get('Installer') is not None:
            self.installer = m.get('Installer')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PythonVersion') is not None:
            self.python_version = m.get('PythonVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

