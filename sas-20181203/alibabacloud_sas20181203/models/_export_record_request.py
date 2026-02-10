# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportRecordRequest(DaraModel):
    def __init__(
        self,
        export_file_type: str = None,
        export_type: str = None,
        lang: str = None,
        params: str = None,
        resource_directory_account_id: int = None,
    ):
        # The type of the file to export. Valid values:
        # 
        # *   **virusScanExport**: The details of the virus scan tasks are exported. This parameter is available and required when ExportType is set to virusScanExport.
        self.export_file_type = export_file_type
        # The type of detection result list to be exported. Values:
        # - **assetInstance**: List of servers in the asset center 
        # - **user**: List of asset fingerprints for accounts 
        # - **port**: List of asset fingerprints for ports 
        # - **process**: List of asset fingerprints for processes 
        # - **sca**: List of asset fingerprints for middleware 
        # - **database**: List of asset fingerprints for databases 
        # - **web**: List of asset fingerprints for web services 
        # - **software**: List of asset fingerprints for software 
        # - **cron**: List of asset fingerprints for scheduled tasks 
        # - **autorun**: List of asset fingerprints for startup items 
        # - **lkm**: List of asset fingerprints for kernel modules 
        # - **webserver**: List of asset fingerprints for web sites 
        # - **virusScanExport**: List of details for virus scan tasks 
        # - **imageVulExport**: List of system vulnerabilities in images 
        # - **imageBaseLineExport**: List of baseline check results in images 
        # - **imageAffectedMaliciousExport**: List of malicious sample check results in images 
        # - **baselineCspm**: List of detection results for cloud platform configuration checks 
        # - **attack**: List of alert events for attack analysis 
        # - **accessKey**: List of alert events for AK leak detection 
        # - **exportObjectScanEvents**: List of alert events for malicious file detection 
        # - **domainDetail**: Website assets 
        # - **assetsPropertyScaProcessDetail**: RASP protection process for application protection 
        # - **exportHcWarning**: List of system baseline risks 
        # - **raspAttackAlert**: List of attack alerts for Application Protection
        # - **raspApplicationConfiguration**: List of application configurations for Application Protection
        # - **raspWeaknessDetection**: List of weakness detections for Application Protection
        # - **raspInMemoryWebshellDetection**: List of in-memory webshell detection alerts for Application Protection
        # - **raspInMemoryWebshellInsertion**: List of in-memory webshell insertion alerts for Application Protection
        # 
        # This parameter is required.
        self.export_type = export_type
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The conditions that are used to filter check results.
        # 
        # > This operation is a common export operation for multiple features of Security Center. The available configuration fields of this parameter vary based on the features. We recommend that you do not specify this parameter when you call the operation. You can export an information list without specifying this parameter, and then filter data in the exported Excel file.
        self.params = params
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the ID.
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_file_type is not None:
            result['ExportFileType'] = self.export_file_type

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.params is not None:
            result['Params'] = self.params

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportFileType') is not None:
            self.export_file_type = m.get('ExportFileType')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self

