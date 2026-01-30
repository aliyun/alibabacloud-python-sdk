# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListCloudAppsResponseBody(DaraModel):
    def __init__(
        self,
        cloud_apps: List[main_models.ListCloudAppsResponseBodyCloudApps] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cloud_apps = cloud_apps
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.cloud_apps:
            for v1 in self.cloud_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudApps'] = []
        if self.cloud_apps is not None:
            for k1 in self.cloud_apps:
                result['CloudApps'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_apps = []
        if m.get('CloudApps') is not None:
            for k1 in m.get('CloudApps'):
                temp_model = main_models.ListCloudAppsResponseBodyCloudApps()
                self.cloud_apps.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloudAppsResponseBodyCloudApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_version: str = None,
        description: str = None,
        pkg_format: str = None,
        pkg_type: str = None,
        stable_patch_id: str = None,
        status: str = None,
        status_description: str = None,
        update_time: str = None,
        upload_time: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self.description = description
        self.pkg_format = pkg_format
        self.pkg_type = pkg_type
        self.stable_patch_id = stable_patch_id
        self.status = status
        self.status_description = status_description
        self.update_time = update_time
        self.upload_time = upload_time

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

        if self.description is not None:
            result['Description'] = self.description

        if self.pkg_format is not None:
            result['PkgFormat'] = self.pkg_format

        if self.pkg_type is not None:
            result['PkgType'] = self.pkg_type

        if self.stable_patch_id is not None:
            result['StablePatchId'] = self.stable_patch_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_description is not None:
            result['StatusDescription'] = self.status_description

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PkgFormat') is not None:
            self.pkg_format = m.get('PkgFormat')

        if m.get('PkgType') is not None:
            self.pkg_type = m.get('PkgType')

        if m.get('StablePatchId') is not None:
            self.stable_patch_id = m.get('StablePatchId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDescription') is not None:
            self.status_description = m.get('StatusDescription')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        return self

