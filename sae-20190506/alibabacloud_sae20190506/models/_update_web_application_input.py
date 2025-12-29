# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class UpdateWebApplicationInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        web_network_config: main_models.WebNetworkConfig = None,
    ):
        self.description = description
        self.web_network_config = web_network_config

    def validate(self):
        if self.web_network_config:
            self.web_network_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.web_network_config is not None:
            result['WebNetworkConfig'] = self.web_network_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('WebNetworkConfig') is not None:
            temp_model = main_models.WebNetworkConfig()
            self.web_network_config = temp_model.from_map(m.get('WebNetworkConfig'))

        return self

