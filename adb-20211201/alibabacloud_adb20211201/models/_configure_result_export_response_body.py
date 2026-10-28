# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ConfigureResultExportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ConfigureResultExportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend error code.
        self.code = code
        # The configured result set export information.
        self.data = data
        # The HTTP status code. A status code of 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The additional information about the call result. Description:
        # 
        # - If the request is normal, OK is returned.
        # - If the request is abnormal, a specific error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
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
            temp_model = main_models.ConfigureResultExportResponseBodyData()
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

class ConfigureResultExportResponseBodyData(DaraModel):
    def __init__(
        self,
        export_type: str = None,
        oss_info: main_models.ConfigureResultExportResponseBodyDataOssInfo = None,
        sls_info: main_models.ConfigureResultExportResponseBodyDataSlsInfo = None,
    ):
        # The export type. Valid values:
        # 
        # - SLS: Exports data to SLS.
        # - OSS: Exports data to OSS.
        self.export_type = export_type
        # The OSS export information configured when the export destination is OSS.
        self.oss_info = oss_info
        # The SLS configuration information when the export destination is SLS.
        self.sls_info = sls_info

    def validate(self):
        if self.oss_info:
            self.oss_info.validate()
        if self.sls_info:
            self.sls_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.oss_info is not None:
            result['OssInfo'] = self.oss_info.to_map()

        if self.sls_info is not None:
            result['SlsInfo'] = self.sls_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('OssInfo') is not None:
            temp_model = main_models.ConfigureResultExportResponseBodyDataOssInfo()
            self.oss_info = temp_model.from_map(m.get('OssInfo'))

        if m.get('SlsInfo') is not None:
            temp_model = main_models.ConfigureResultExportResponseBodyDataSlsInfo()
            self.sls_info = temp_model.from_map(m.get('SlsInfo'))

        return self

class ConfigureResultExportResponseBodyDataSlsInfo(DaraModel):
    def __init__(
        self,
        logstore_ttl: int = None,
        resource_group: str = None,
        sls_project: str = None,
    ):
        # The expiration time of the temporary Logstore generated for result set export. Unit: days. The Logstore is automatically deleted after expiration. The minimum value is 1 day and the maximum value is 30 days.
        self.logstore_ttl = logstore_ttl
        # The name of the resource group in which the export SQL statement is executed.
        self.resource_group = resource_group
        # The name of the SLS project.
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore_ttl is not None:
            result['LogstoreTtl'] = self.logstore_ttl

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogstoreTtl') is not None:
            self.logstore_ttl = m.get('LogstoreTtl')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        return self

class ConfigureResultExportResponseBodyDataOssInfo(DaraModel):
    def __init__(
        self,
        export_base_path: str = None,
        resource_group: str = None,
        result_file_ttl: int = None,
    ):
        # The OSS path where the export results are stored.
        self.export_base_path = export_base_path
        # The name of the resource group in which the export SQL statement is executed.
        self.resource_group = resource_group
        # The expiration time of the OSS file. Unit: days. The minimum value is 1 day and the maximum value is 30 days.
        self.result_file_ttl = result_file_ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_base_path is not None:
            result['ExportBasePath'] = self.export_base_path

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.result_file_ttl is not None:
            result['ResultFileTtl'] = self.result_file_ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportBasePath') is not None:
            self.export_base_path = m.get('ExportBasePath')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('ResultFileTtl') is not None:
            self.result_file_ttl = m.get('ResultFileTtl')

        return self

