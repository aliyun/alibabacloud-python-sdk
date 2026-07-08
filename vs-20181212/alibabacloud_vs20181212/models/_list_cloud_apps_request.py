# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudAppsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_version: str = None,
        end_time: str = None,
        latest_version_only: bool = None,
        page_number: int = None,
        page_size: int = None,
        pkg_label: str = None,
        pkg_type: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The ID of the cloud application. This ID corresponds to a unique application package.
        self.app_id = app_id
        # Application name.
        self.app_name = app_name
        # Application version.
        self.app_version = app_version
        # The time range filter parameter. Express it in ISO8601 standard format, using UTC time: yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # Return only the latest submitted version of the application. Default value: false.
        self.latest_version_only = latest_version_only
        # The page number for the query list. The starting value is 1. Default value: 1.
        self.page_number = page_number
        # The number of rows per page for paged queries. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # Valid values:
        # 
        # 1. Valid values:
        #    a. hot
        #    b. game
        #    c. app
        # 
        # 2. Special case:a. To list applications that have no tags, enter NULL.
        self.pkg_label = pkg_label
        # The package type. Valid values:
        # 
        # 1. android
        # 
        # 2. win
        # 
        # 3. android_appmarket
        self.pkg_type = pkg_type
        # The time range filter parameter. Express it in ISO8601 standard format, using UTC time: yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time
        # The application upload status. Valid values:
        # 
        # 1. Success: The desired state, indicating success.
        # 
        # 2. Failed: The desired state, indicating failure.
        # 
        # 3. Created
        # 
        # 4. Doing
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.latest_version_only is not None:
            result['LatestVersionOnly'] = self.latest_version_only

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pkg_label is not None:
            result['PkgLabel'] = self.pkg_label

        if self.pkg_type is not None:
            result['PkgType'] = self.pkg_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LatestVersionOnly') is not None:
            self.latest_version_only = m.get('LatestVersionOnly')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PkgLabel') is not None:
            self.pkg_label = m.get('PkgLabel')

        if m.get('PkgType') is not None:
            self.pkg_type = m.get('PkgType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

