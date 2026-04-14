# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210903 import models as main_models
from darabonba.model import DaraModel

class ListRunningAppsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        running_cloud_apps: List[main_models.ListRunningAppsResponseBodyRunningCloudApps] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.running_cloud_apps = running_cloud_apps

    def validate(self):
        if self.running_cloud_apps:
            for v1 in self.running_cloud_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RunningCloudApps'] = []
        if self.running_cloud_apps is not None:
            for k1 in self.running_cloud_apps:
                result['RunningCloudApps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.running_cloud_apps = []
        if m.get('RunningCloudApps') is not None:
            for k1 in m.get('RunningCloudApps'):
                temp_model = main_models.ListRunningAppsResponseBodyRunningCloudApps()
                self.running_cloud_apps.append(temp_model.from_map(k1))

        return self

class ListRunningAppsResponseBodyRunningCloudApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_name: str = None,
        app_version: str = None,
        app_version_name: str = None,
        duration: int = None,
        icon_url: str = None,
        os_type: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.app_id = app_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_name = app_name
        self.app_version = app_version
        self.app_version_name = app_version_name
        self.duration = duration
        self.icon_url = icon_url
        self.os_type = os_type
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

