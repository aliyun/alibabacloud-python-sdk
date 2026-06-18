# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRoutineRouteResponseBody(DaraModel):
    def __init__(
        self,
        bypass: str = None,
        config_id: int = None,
        config_type: str = None,
        fallback: str = None,
        mode: str = None,
        request_id: str = None,
        route_enable: str = None,
        route_name: str = None,
        routine_name: str = None,
        rule: str = None,
        sequence: int = None,
        site_version: int = None,
        timeout: str = None,
    ):
        # The bypass mode. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.bypass = bypass
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. Valid values:
        # 
        # - `global`: Queries the global configuration.
        # 
        # - `rule`: Queries the rule configuration.
        self.config_type = config_type
        # Specifies whether to enable fallback to origin. If this feature is enabled, requests are sent to the origin server when the function encounters an exception, such as exceeding its CPU limit. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.fallback = fallback
        # The configuration mode. Valid values:
        # 
        # - `simple`: simple mode.
        # 
        # - `custom`: custom mode.
        self.mode = mode
        # The request ID.
        self.request_id = request_id
        # The route status. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.route_enable = route_enable
        # The route name.
        self.route_name = route_name
        # The name of the edge function routine.
        self.routine_name = routine_name
        # The rule expression.
        self.rule = rule
        # The rule execution order.
        self.sequence = sequence
        # The version number of the site.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

