# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ConfigureResultExportRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        export_type: str = None,
        oss_info: main_models.ConfigureResultExportRequestOssInfo = None,
        region_id: str = None,
        sls_info: main_models.ConfigureResultExportRequestSlsInfo = None,
    ):
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to view the cluster IDs of all AnalyticDB for MySQL clusters in the destination region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The export type. Valid values:
        # 
        # - SLS: Exports data to SLS.
        # - OSS: Exports data to OSS.
        self.export_type = export_type
        # The OSS configuration information when the export destination is OSS.
        self.oss_info = oss_info
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.oss_info is not None:
            result['OssInfo'] = self.oss_info.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_info is not None:
            result['SlsInfo'] = self.sls_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('OssInfo') is not None:
            temp_model = main_models.ConfigureResultExportRequestOssInfo()
            self.oss_info = temp_model.from_map(m.get('OssInfo'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsInfo') is not None:
            temp_model = main_models.ConfigureResultExportRequestSlsInfo()
            self.sls_info = temp_model.from_map(m.get('SlsInfo'))

        return self

class ConfigureResultExportRequestSlsInfo(DaraModel):
    def __init__(
        self,
        logstore_ttl: int = None,
        resource_group: str = None,
        sls_project: str = None,
    ):
        # The expiration time of the temporary Logstore generated for result set export. Unit: days. The Logstore is automatically deleted after expiration. The minimum value is 1 day and the maximum value is 30 days. An error is returned if the value is out of range.
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

class ConfigureResultExportRequestOssInfo(DaraModel):
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
        # The expiration time of the OSS file. Unit: days. The minimum value is 1 day and the maximum value is 30 days. An error is returned if the value is out of range.
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

