# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class NeuronAppPluginUpdateCmd(DaraModel):
    def __init__(
        self,
        config: main_models.MobiPluginConfig = None,
        id: int = None,
    ):
        # This parameter is required.
        self.config = config
        # This parameter is required.
        self.id = id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.MobiPluginConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

