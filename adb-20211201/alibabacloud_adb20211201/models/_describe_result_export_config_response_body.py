# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeResultExportConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeResultExportConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API status or POP error code.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP response status code. A value of 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The returned message. Valid values:
        # 
        # *   The request succeeded, and the server returns **OK**.
        # *   The request failed, and the server returns an error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values: Valid values:
        # 
        # *   **True: Succeeded.**
        # *   **False: Failed.
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
            temp_model = main_models.DescribeResultExportConfigResponseBodyData()
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

class DescribeResultExportConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        export_type: str = None,
        oss_info: main_models.DescribeResultExportConfigResponseBodyDataOssInfo = None,
        sls_info: main_models.DescribeResultExportConfigResponseBodyDataSlsInfo = None,
    ):
        # The export type. Valid values:
        # 
        # *   SLS: Indicates that the export destination is SLS.
        # *   OSS: Indicates that the export destination is OSS.
        self.export_type = export_type
        # The configured OSS export settings, returned when the export destination is OSS.
        self.oss_info = oss_info
        # The configured SLS export settings, returned when the export destination is SLS.
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
            temp_model = main_models.DescribeResultExportConfigResponseBodyDataOssInfo()
            self.oss_info = temp_model.from_map(m.get('OssInfo'))

        if m.get('SlsInfo') is not None:
            temp_model = main_models.DescribeResultExportConfigResponseBodyDataSlsInfo()
            self.sls_info = temp_model.from_map(m.get('SlsInfo'))

        return self

class DescribeResultExportConfigResponseBodyDataSlsInfo(DaraModel):
    def __init__(
        self,
        logstore_ttl: int = None,
        resource_group: str = None,
        sls_project: str = None,
    ):
        # The expiration period (in days) for the temporary Logstore automatically created during result set export. The Logstore is automatically deleted after expiration. The returned value is between 1 and 30 days (inclusive).
        self.logstore_ttl = logstore_ttl
        # The name of the resource group that runs the export SQL.
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

class DescribeResultExportConfigResponseBodyDataOssInfo(DaraModel):
    def __init__(
        self,
        export_base_path: str = None,
        resource_group: str = None,
        result_file_ttl: int = None,
    ):
        # The path of the OSS bucket to which the result sets are exported.
        self.export_base_path = export_base_path
        # The name of the resource group that runs the export SQL.
        self.resource_group = resource_group
        # The expiration period (in days) for the OSS file. The returned value is between 1 and 30 days (inclusive).
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

