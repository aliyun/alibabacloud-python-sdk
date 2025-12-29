# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ImageConfig(DaraModel):
    def __init__(
        self,
        acceleration_type: str = None,
        image: str = None,
        instance_id: str = None,
        registry_config: main_models.RegistryConfig = None,
    ):
        self.acceleration_type = acceleration_type
        self.image = image
        self.instance_id = instance_id
        self.registry_config = registry_config

    def validate(self):
        if self.registry_config:
            self.registry_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type

        if self.image is not None:
            result['image'] = self.image

        if self.instance_id is not None:
            result['instanceID'] = self.instance_id

        if self.registry_config is not None:
            result['registryConfig'] = self.registry_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')

        if m.get('registryConfig') is not None:
            temp_model = main_models.RegistryConfig()
            self.registry_config = temp_model.from_map(m.get('registryConfig'))

        return self

