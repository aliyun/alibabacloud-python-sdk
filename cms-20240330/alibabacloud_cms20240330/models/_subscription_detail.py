# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionDetail(DaraModel):
    def __init__(
        self,
        filter_setting: main_models.FilterSetting = None,
        subscribe_legacy_event: bool = None,
        workspace_filter_setting: main_models.WorkspaceFilterSetting = None,
    ):
        # The filter conditions for event content.
        self.filter_setting = filter_setting
        # Specifies whether to subscribe to legacy product events (events with an empty workspace from CMS 1.0, ARMS, or SLS).
        self.subscribe_legacy_event = subscribe_legacy_event
        # The cross-workspace event routing (global subscription) settings.
        self.workspace_filter_setting = workspace_filter_setting

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()
        if self.workspace_filter_setting:
            self.workspace_filter_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.subscribe_legacy_event is not None:
            result['subscribeLegacyEvent'] = self.subscribe_legacy_event

        if self.workspace_filter_setting is not None:
            result['workspaceFilterSetting'] = self.workspace_filter_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('subscribeLegacyEvent') is not None:
            self.subscribe_legacy_event = m.get('subscribeLegacyEvent')

        if m.get('workspaceFilterSetting') is not None:
            temp_model = main_models.WorkspaceFilterSetting()
            self.workspace_filter_setting = temp_model.from_map(m.get('workspaceFilterSetting'))

        return self

