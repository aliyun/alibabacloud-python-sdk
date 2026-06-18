# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRoutineRouteRequest(DaraModel):
    def __init__(
        self,
        bypass: str = None,
        config_id: int = None,
        fallback: str = None,
        route_enable: str = None,
        route_name: str = None,
        routine_name: str = None,
        rule: str = None,
        sequence: int = None,
        site_id: int = None,
        timeout: str = None,
    ):
        # Specifies whether to enable bypass mode. Valid values:
        # 
        # - on: Enabled
        # 
        # - off: Disabled
        self.bypass = bypass
        # The configuration ID.
        # 
        # This parameter is required.
        self.config_id = config_id
        # Specifies whether to enable fallback. If enabled, requests fall back to the origin server if the function encounters an exception, such as exceeding the CPU usage limit. Valid values:
        # 
        # - on: Enabled
        # 
        # - off: Disabled
        self.fallback = fallback
        # Specifies whether to enable the route. Valid values:
        # 
        # - on: Enabled
        # 
        # - off: Disabled
        self.route_enable = route_enable
        # The route name.
        self.route_name = route_name
        # The name of the Routine.
        self.routine_name = routine_name
        # The content of the rule.
        self.rule = rule
        # The execution sequence of the rule.
        self.sequence = sequence
        # The ID of the site. You can obtain this ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
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

        if self.fallback is not None:
            result['Fallback'] = self.fallback

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

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bypass') is not None:
            self.bypass = m.get('Bypass')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Fallback') is not None:
            self.fallback = m.get('Fallback')

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

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

