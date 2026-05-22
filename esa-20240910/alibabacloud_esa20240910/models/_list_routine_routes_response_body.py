# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListRoutineRoutesResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListRoutineRoutesResponseBodyConfigs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.configs = configs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListRoutineRoutesResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListRoutineRoutesResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        bypass: str = None,
        config_id: int = None,
        config_type: str = None,
        fallback: str = None,
        mode: str = None,
        route_enable: str = None,
        route_name: str = None,
        routine_name: str = None,
        rule: str = None,
        sequence: int = None,
        site_id: int = None,
        site_name: str = None,
        site_version: int = None,
        timeout: str = None,
    ):
        self.bypass = bypass
        self.config_id = config_id
        self.config_type = config_type
        self.fallback = fallback
        self.mode = mode
        self.route_enable = route_enable
        self.route_name = route_name
        self.routine_name = routine_name
        self.rule = rule
        self.sequence = sequence
        self.site_id = site_id
        self.site_name = site_name
        self.site_version = site_version
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bypass is not None:
            result['Bypass'] = self.bypass

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.fallback is not None:
            result['Fallback'] = self.fallback

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.route_enable is not None:
            result['RouteEnable'] = self.route_enable

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bypass') is not None:
            self.bypass = m.get('Bypass')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Fallback') is not None:
            self.fallback = m.get('Fallback')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RouteEnable') is not None:
            self.route_enable = m.get('RouteEnable')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

