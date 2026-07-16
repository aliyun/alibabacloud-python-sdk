# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListEnvironmentsResponseBody(DaraModel):
    def __init__(
        self,
        environment_list: List[main_models.ListEnvironmentsResponseBodyEnvironmentList] = None,
        request_id: str = None,
    ):
        # The list of environments.
        self.environment_list = environment_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.environment_list:
            for v1 in self.environment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnvironmentList'] = []
        if self.environment_list is not None:
            for k1 in self.environment_list:
                result['EnvironmentList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.environment_list = []
        if m.get('EnvironmentList') is not None:
            for k1 in m.get('EnvironmentList'):
                temp_model = main_models.ListEnvironmentsResponseBodyEnvironmentList()
                self.environment_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEnvironmentsResponseBodyEnvironmentList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        environment_name: str = None,
        is_default: bool = None,
        pre_site_version: int = None,
        priority: int = None,
        read_only: bool = None,
        rule: str = None,
        site_version: int = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The environment name.
        self.environment_name = environment_name
        # Indicates whether this is the default environment.
        self.is_default = is_default
        # The previous version number.
        self.pre_site_version = pre_site_version
        # The priority.
        self.priority = priority
        # Indicates whether the environment is read-only.
        self.read_only = read_only
        # The environment rule.
        self.rule = rule
        # The site version number.
        self.site_version = site_version
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

        if self.environment_name is not None:
            result['EnvironmentName'] = self.environment_name

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.pre_site_version is not None:
            result['PreSiteVersion'] = self.pre_site_version

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnvironmentName') is not None:
            self.environment_name = m.get('EnvironmentName')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('PreSiteVersion') is not None:
            self.pre_site_version = m.get('PreSiteVersion')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

