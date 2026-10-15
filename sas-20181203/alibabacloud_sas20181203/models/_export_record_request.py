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
        # Specifies the type of the file to be exported. Valid values:
        # 
        # - **virusScanExport**: Exports the virus scan task details. This value is required and can only be used when ExportType is set to virusScanExport.
        self.export_file_type = export_file_type
        # Specifies the type of the detection result list to be exported. Valid values:
        # 
        # - **assetInstance**: the server list in the Asset Center
        # - **user**: the Asset Fingerprints list of accounts
        # - **port**: the Asset Fingerprints list of ports
        # - **process**: the Asset Fingerprints list of processes
        # - **sca**: the Asset Fingerprints list of middleware
        # - **database**: the Asset Fingerprints list of databases
        # - **web**: the Asset Fingerprints list of web services
        # - **software**: the Asset Fingerprints list of software
        # - **cron**: the Asset Fingerprints list of scheduled nodes
        # - **autorun**: the Asset Fingerprints list of startup items
        # - **lkm**: the Asset Fingerprints list of kernel modules
        # - **webserver**: the Asset Fingerprints list of websites
        # - **virusScanExport**: the virus scan node details list
        # - **imageVulExport**: the image system vulnerability list
        # - **imageBaseLineExport**: the image baseline check result list
        # - **imageAffectedMaliciousExport**: the image malicious sample check result list
        # - **baselineCspm**: the cloud platform configuration check result list
        # - **attack**: the attack analysis alerting event list
        # - **accessKey**: the AccessKey leak detection alerting event list
        # - **exportObjectScanEvents**: the malicious file detection alerting event list
        # - **domainDetail**: the website assets
        # - **assetsPropertyScaProcessDetail**: the RASP-protected processes in Application Protection
        # - **exportHcWarning**: the system baseline risk list
        # - **raspAttackAlert**: the Application Protection attack alerting list
        # - **raspApplicationConfiguration**: the Application Protection application configuration list
        # - **raspWeaknessDetection**: the Application Protection weakness detection list
        # - **raspInMemoryWebshellDetection**: the Application Protection in-memory webshell detection alerting list
        # - **raspInMemoryWebshellInsertion**: the Application Protection in-memory webshell injection alerting list
        # - **listAgentExport**: the agent list
        # - **listSkillExport**: the skill list
        # - **listModelExport**: the model list
        # - **listAiAgentEventExport**: the agent risk list
        # 
        # This parameter is required.
        self.export_type = export_type
        # Specifies the language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Specifies the filter conditions for the exported content.
        # 
        # > This operation is a general export operation for exporting detection lists of multiple features in Security Center. The configuration fields of this parameter vary based on the feature. Do not specify this parameter when you call the operation. You can export the information list without specifying this parameter and then filter the target data in the exported Excel file.
        self.params = params
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # > You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
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

