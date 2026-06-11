# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionForSNSModify(DaraModel):
    def __init__(
        self,
        filter_setting: main_models.FilterSetting = None,
        workspace_filter_setting: main_models.WorkspaceFilterSetting = None,
    ):
        self.filter_setting = filter_setting
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

        if self.workspace_filter_setting is not None:
            result['workspaceFilterSetting'] = self.workspace_filter_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('workspaceFilterSetting') is not None:
            temp_model = main_models.WorkspaceFilterSetting()
            self.workspace_filter_setting = temp_model.from_map(m.get('workspaceFilterSetting'))

        return self

