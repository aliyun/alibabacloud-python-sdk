# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListVersionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        site_version_list: List[main_models.ListVersionsResponseBodySiteVersionList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The version list of the site.
        self.site_version_list = site_version_list

    def validate(self):
        if self.site_version_list:
            for v1 in self.site_version_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SiteVersionList'] = []
        if self.site_version_list is not None:
            for k1 in self.site_version_list:
                result['SiteVersionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.site_version_list = []
        if m.get('SiteVersionList') is not None:
            for k1 in m.get('SiteVersionList'):
                temp_model = main_models.ListVersionsResponseBodySiteVersionList()
                self.site_version_list.append(temp_model.from_map(k1))

        return self

class ListVersionsResponseBodySiteVersionList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        environment_name_list: List[str] = None,
        parent_site_version: int = None,
        read_only: bool = None,
        site_version: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # The environment list of the site version. The version may have no environment or one or more environments configured, such as the default environment or environment 2.
        self.environment_name_list = environment_name_list
        # The parent version of the site version.
        self.parent_site_version = parent_site_version
        # Indicates whether the version is read-only. Default value: false.
        self.read_only = read_only
        # The site version.
        self.site_version = site_version
        # The status. Valid values:
        # 
        # - **online**: active.
        # 
        # - **configuring**: being configured.
        # 
        # - **configure_faild**: configuration failed.
        self.status = status
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.environment_name_list is not None:
            result['EnvironmentNameList'] = self.environment_name_list

        if self.parent_site_version is not None:
            result['ParentSiteVersion'] = self.parent_site_version

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvironmentNameList') is not None:
            self.environment_name_list = m.get('EnvironmentNameList')

        if m.get('ParentSiteVersion') is not None:
            self.parent_site_version = m.get('ParentSiteVersion')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

