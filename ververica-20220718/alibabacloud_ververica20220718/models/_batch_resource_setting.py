# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class BatchResourceSetting(DaraModel):
    def __init__(
        self,
        basic_resource_setting: main_models.BasicResourceSetting = None,
        max_slot: int = None,
    ):
        # The resource parameters in basic mode.
        self.basic_resource_setting = basic_resource_setting
        # The maximum number of slots.
        self.max_slot = max_slot

    def validate(self):
        if self.basic_resource_setting:
            self.basic_resource_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_resource_setting is not None:
            result['basicResourceSetting'] = self.basic_resource_setting.to_map()

        if self.max_slot is not None:
            result['maxSlot'] = self.max_slot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basicResourceSetting') is not None:
            temp_model = main_models.BasicResourceSetting()
            self.basic_resource_setting = temp_model.from_map(m.get('basicResourceSetting'))

        if m.get('maxSlot') is not None:
            self.max_slot = m.get('maxSlot')

        return self

