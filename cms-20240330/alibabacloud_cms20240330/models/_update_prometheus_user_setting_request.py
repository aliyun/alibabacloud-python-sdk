# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePrometheusUserSettingRequest(DaraModel):
    def __init__(
        self,
        setting_value: str = None,
    ):
        # This parameter is required.
        self.setting_value = setting_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.setting_value is not None:
            result['settingValue'] = self.setting_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('settingValue') is not None:
            self.setting_value = m.get('settingValue')

        return self

