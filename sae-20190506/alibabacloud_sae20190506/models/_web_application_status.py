# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class WebApplicationStatus(DaraModel):
    def __init__(
        self,
        instance_count: int = None,
        web_scaling_config: main_models.WebScalingConfig = None,
    ):
        self.instance_count = instance_count
        self.web_scaling_config = web_scaling_config

    def validate(self):
        if self.web_scaling_config:
            self.web_scaling_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.web_scaling_config is not None:
            result['WebScalingConfig'] = self.web_scaling_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('WebScalingConfig') is not None:
            temp_model = main_models.WebScalingConfig()
            self.web_scaling_config = temp_model.from_map(m.get('WebScalingConfig'))

        return self

