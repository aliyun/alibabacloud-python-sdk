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
        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self.end_time = end_time
        self.latest_version_only = latest_version_only
        self.page_number = page_number
        self.page_size = page_size
        self.pkg_label = pkg_label
        self.pkg_type = pkg_type
        self.start_time = start_time
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

