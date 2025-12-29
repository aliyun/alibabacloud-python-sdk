# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ApplicationStatus(DaraModel):
    def __init__(
        self,
        instance_count: int = None,
        scale_config: main_models.ScaleConfig = None,
    ):
        self.instance_count = instance_count
        self.scale_config = scale_config

    def validate(self):
        if self.scale_config:
            self.scale_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count

        if self.scale_config is not None:
            result['scaleConfig'] = self.scale_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')

        if m.get('scaleConfig') is not None:
            temp_model = main_models.ScaleConfig()
            self.scale_config = temp_model.from_map(m.get('scaleConfig'))

        return self

