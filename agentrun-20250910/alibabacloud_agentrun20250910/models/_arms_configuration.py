# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ArmsConfiguration(DaraModel):
    def __init__(
        self,
        arms_license_key: str = None,
        enable_arms: bool = None,
    ):
        # 应用实时监控服务（ARMS）的许可证密钥
        self.arms_license_key = arms_license_key
        # 是否启用应用实时监控服务（ARMS）
        self.enable_arms = enable_arms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arms_license_key is not None:
            result['armsLicenseKey'] = self.arms_license_key

        if self.enable_arms is not None:
            result['enableArms'] = self.enable_arms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsLicenseKey') is not None:
            self.arms_license_key = m.get('armsLicenseKey')

        if m.get('enableArms') is not None:
            self.enable_arms = m.get('enableArms')

        return self

