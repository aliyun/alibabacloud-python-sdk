# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeAppsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeAppsResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The objects that are returned.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAppsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAppsResponseBodyData(DaraModel):
    def __init__(
        self,
        android_app_version: str = None,
        apk_size: str = None,
        app_id: int = None,
        app_name: str = None,
        app_type: str = None,
        biz_region_id: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon_url: str = None,
        installation_status: str = None,
        instance_group_list: List[str] = None,
        md5: str = None,
        package_name: str = None,
        status: str = None,
    ):
        # The version of the application.
        self.android_app_version = android_app_version
        # Apk size.
        self.apk_size = apk_size
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        self.app_type = app_type
        # Region id.
        self.biz_region_id = biz_region_id
        # The description of the application.
        self.description = description
        # The time when the application was created.
        self.gmt_create = gmt_create
        # The time when the application was last modified.
        self.gmt_modified = gmt_modified
        # The icon URL of the application.
        self.icon_url = icon_url
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
        # The list of instance groups where the application is installed.
        self.instance_group_list = instance_group_list
        # The value of MD5.
        self.md5 = md5
        # The name of the application package.
        self.package_name = package_name
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
        if self.android_app_version is not None:
            result['AndroidAppVersion'] = self.android_app_version

        if self.apk_size is not None:
            result['ApkSize'] = self.apk_size

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.installation_status is not None:
            result['InstallationStatus'] = self.installation_status

        if self.instance_group_list is not None:
            result['InstanceGroupList'] = self.instance_group_list

        if self.md5 is not None:
            result['MD5'] = self.md5

        if self.package_name is not None:
            result['PackageName'] = self.package_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidAppVersion') is not None:
            self.android_app_version = m.get('AndroidAppVersion')

        if m.get('ApkSize') is not None:
            self.apk_size = m.get('ApkSize')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('InstallationStatus') is not None:
            self.installation_status = m.get('InstallationStatus')

        if m.get('InstanceGroupList') is not None:
            self.instance_group_list = m.get('InstanceGroupList')

        if m.get('MD5') is not None:
            self.md5 = m.get('MD5')

        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

