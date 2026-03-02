# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class StreamingResourceSetting(DaraModel):
    def __init__(
        self,
        basic_resource_setting: main_models.BasicResourceSetting = None,
        expert_resource_setting: main_models.ExpertResourceSetting = None,
        resource_setting_mode: str = None,
    ):
        # The resource parameters in basic mode.
        self.basic_resource_setting = basic_resource_setting
        # The resource parameters in expert mode.
        self.expert_resource_setting = expert_resource_setting
        # The resource configuration mode used by a deployment that runs in streaming mode. Valid values:
        # 
        # *   EXPERT
        # *   BASIC
        self.resource_setting_mode = resource_setting_mode

    def validate(self):
        if self.basic_resource_setting:
            self.basic_resource_setting.validate()
        if self.expert_resource_setting:
            self.expert_resource_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_resource_setting is not None:
            result['basicResourceSetting'] = self.basic_resource_setting.to_map()

        if self.expert_resource_setting is not None:
            result['expertResourceSetting'] = self.expert_resource_setting.to_map()

        if self.resource_setting_mode is not None:
            result['resourceSettingMode'] = self.resource_setting_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basicResourceSetting') is not None:
            temp_model = main_models.BasicResourceSetting()
            self.basic_resource_setting = temp_model.from_map(m.get('basicResourceSetting'))

        if m.get('expertResourceSetting') is not None:
            temp_model = main_models.ExpertResourceSetting()
            self.expert_resource_setting = temp_model.from_map(m.get('expertResourceSetting'))

        if m.get('resourceSettingMode') is not None:
            self.resource_setting_mode = m.get('resourceSettingMode')

        return self

