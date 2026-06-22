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
        # The type of file to export. Valid values:
        # 
        # - **virusScanExport**: Exports details of a virus scan task. This parameter is required when ExportType is set to virusScanExport.
        self.export_file_type = export_file_type
        # The type of records to export. Valid values:
        # 
        # - **assetInstance**: The list of servers in Asset Center
        # 
        # - **user**: The list of account asset fingerprints
        # 
        # - **port**: The list of port asset fingerprints
        # 
        # - **process**: The list of process asset fingerprints
        # 
        # - **sca**: The list of middleware asset fingerprints
        # 
        # - **database**: The list of database asset fingerprints
        # 
        # - **web**: The list of web service asset fingerprints
        # 
        # - **software**: The list of software asset fingerprints
        # 
        # - **cron**: The list of scheduled task (cron) asset fingerprints
        # 
        # - **autorun**: The list of startup item asset fingerprints
        # 
        # - **lkm**: The list of kernel module asset fingerprints
        # 
        # - **webserver**: The list of website asset fingerprints
        # 
        # - **virusScanExport**: The list of virus scan task details
        # 
        # - **imageVulExport**: The list of system vulnerabilities in images
        # 
        # - imageVulExport: The list of system vulnerabilities in images
        # 
        # - **imageBaseLineExport**: The list of image baseline check results
        # 
        # - **imageAffectedMaliciousExport**: The list of malicious sample check results for images
        # 
        # - **baselineCspm**: The list of cloud platform configuration check results
        # 
        # - **attack**: The list of attack analysis alerts
        # 
        # - **accessKey**: The list of AK leakage detection alerts
        # 
        # - **exportObjectScanEvents**: The list of malicious file detection alerts
        # 
        # - **domainDetail**: Website assets
        # 
        # - **assetsPropertyScaProcessDetail**: RASP-protected processes
        # 
        # - **exportHcWarning**: The list of system baseline risks
        # 
        # - **raspAttackAlert**: The list of RASP attack alerts
        # 
        # - **raspApplicationConfiguration**: The list of RASP application configurations
        # 
        # - **raspWeaknessDetection**: The list of RASP weakness detection results
        # 
        # - **raspInMemoryWebshellDetection**: The list of RASP alerts for in-memory webshell detection
        # 
        # - **raspInMemoryWebshellInsertion**: The list of RASP alerts for in-memory webshell insertion
        # 
        # - **listAgentExport**: The list of agents
        # 
        # - **listSkillExport**: The list of skills
        # 
        # - **listModelExport**: The list of models
        # 
        # This parameter is required.
        self.export_type = export_type
        # The language of the content in the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The filter conditions for the exported content.
        # 
        # > This is a general-purpose operation for exporting various detection lists from Cloud Security Center. As parameter configurations vary by feature, we recommend that you omit this parameter to export the complete list. You can then filter the data in the exported Excel file.
        self.params = params
        # The ID of the management account for a member in Resource Directory.
        # 
        # > You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
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

