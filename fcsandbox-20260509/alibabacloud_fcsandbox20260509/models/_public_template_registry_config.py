# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class PublicTemplateRegistryConfig(DaraModel):
    def __init__(
        self,
        network_config: main_models.PublicTemplateRegistryNetworkConfig = None,
    ):
        self.network_config = network_config

    def validate(self):
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('networkConfig') is not None:
            temp_model = main_models.PublicTemplateRegistryNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        return self

