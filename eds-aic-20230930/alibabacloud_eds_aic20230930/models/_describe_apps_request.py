# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAppsRequest(DaraModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        app_name: str = None,
        app_type: str = None,
        biz_region_id: str = None,
        installation_status: str = None,
        md5: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        # The IDs of the applications.
        self.app_id_list = app_id_list
        # The name of the application.
        self.app_name = app_name
        self.app_type = app_type
        # Region id.
        self.biz_region_id = biz_region_id
        # The installation/uninstallation status of the application.
        # 
        # Valid values:
        # 
        # *   INSTALLFAILED: The application failed to be installed.
        # *   UNINSTALLING: The application is being uninstalled.
        # *   INSTALLING: The application is being installed.
        # *   UNINSTALLED: The application is uninstalled.
        # *   INSTALLED: The application is installed.
        # *   UNINSTALLFAILED: The application failed to be uninstalled.
        self.installation_status = installation_status
        # The value of MD5.
        self.md5 = md5
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The status of the application.
        # 
        # Valid values:
        # 
        # *   FAILED: The application failed to be created.
        # *   NORMAL: The application is available.
        # *   CREATING: The application is being created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.installation_status is not None:
            result['InstallationStatus'] = self.installation_status

        if self.md5 is not None:
            result['MD5'] = self.md5

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('InstallationStatus') is not None:
            self.installation_status = m.get('InstallationStatus')

        if m.get('MD5') is not None:
            self.md5 = m.get('MD5')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

