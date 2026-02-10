# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetFileProtectDashboardResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileProtectDashboardResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFileProtectDashboardResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileProtectDashboardResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_rule_count: int = None,
        plugin_count: int = None,
        plugin_offline_count: int = None,
        plugin_online_count: int = None,
    ):
        # The total number of enabled rules.
        self.enable_rule_count = enable_rule_count
        # The total number of servers on which the Security Center agent is installed.
        self.plugin_count = plugin_count
        # The total number of servers on which the Security Center agent is offline.
        self.plugin_offline_count = plugin_offline_count
        # The total number of servers on which the Security Center agent is online.
        self.plugin_online_count = plugin_online_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_rule_count is not None:
            result['EnableRuleCount'] = self.enable_rule_count

        if self.plugin_count is not None:
            result['PluginCount'] = self.plugin_count

        if self.plugin_offline_count is not None:
            result['PluginOfflineCount'] = self.plugin_offline_count

        if self.plugin_online_count is not None:
            result['PluginOnlineCount'] = self.plugin_online_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableRuleCount') is not None:
            self.enable_rule_count = m.get('EnableRuleCount')

        if m.get('PluginCount') is not None:
            self.plugin_count = m.get('PluginCount')

        if m.get('PluginOfflineCount') is not None:
            self.plugin_offline_count = m.get('PluginOfflineCount')

        if m.get('PluginOnlineCount') is not None:
            self.plugin_online_count = m.get('PluginOnlineCount')

        return self

