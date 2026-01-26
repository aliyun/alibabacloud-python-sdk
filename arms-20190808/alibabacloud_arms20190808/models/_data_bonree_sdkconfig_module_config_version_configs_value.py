# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DataBonreeSDKConfigModuleConfigVersionConfigsValue(DaraModel):
    def __init__(
        self,
        use_custom: bool = None,
        custom_config: Dict[str, main_models.DataBonreeSDKConfigModuleConfigVersionConfigsValueCustomConfigValue] = None,
        description: str = None,
        update_time: int = None,
    ):
        # Indicates whether the custom configuration is used.
        self.use_custom = use_custom
        # The custom configuration.
        self.custom_config = custom_config
        # The description of the version configuration.
        self.description = description
        # The time when the version configuration was updated.
        self.update_time = update_time

    def validate(self):
        if self.custom_config:
            for v1 in self.custom_config.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.use_custom is not None:
            result['useCustom'] = self.use_custom

        result['customConfig'] = {}
        if self.custom_config is not None:
            for k1, v1 in self.custom_config.items():
                result['customConfig'][k1] = v1.to_map() if v1 else None

        if self.description is not None:
            result['description'] = self.description

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('useCustom') is not None:
            self.use_custom = m.get('useCustom')

        self.custom_config = {}
        if m.get('customConfig') is not None:
            for k1, v1 in m.get('customConfig').items():
                temp_model = main_models.DataBonreeSDKConfigModuleConfigVersionConfigsValueCustomConfigValue()
                self.custom_config[k1] = temp_model.from_map(v1)

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

