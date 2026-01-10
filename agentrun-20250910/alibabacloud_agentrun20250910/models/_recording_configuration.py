# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class RecordingConfiguration(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        oss_location: main_models.OssConfiguration = None,
    ):
        # 是否启用录制
        # 
        # This parameter is required.
        self.enabled = enabled
        self.oss_location = oss_location

    def validate(self):
        if self.oss_location:
            self.oss_location.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.oss_location is not None:
            result['ossLocation'] = self.oss_location.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('ossLocation') is not None:
            temp_model = main_models.OssConfiguration()
            self.oss_location = temp_model.from_map(m.get('ossLocation'))

        return self

