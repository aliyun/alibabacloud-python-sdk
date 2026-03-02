# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Resource(DaraModel):
    def __init__(
        self,
        elastic_resource: main_models.ResourceSpec = None,
        fixed_resource: main_models.ResourceSpec = None,
    ):
        self.elastic_resource = elastic_resource
        # This parameter is required.
        self.fixed_resource = fixed_resource

    def validate(self):
        if self.elastic_resource:
            self.elastic_resource.validate()
        if self.fixed_resource:
            self.fixed_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_resource is not None:
            result['elasticResource'] = self.elastic_resource.to_map()

        if self.fixed_resource is not None:
            result['fixedResource'] = self.fixed_resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticResource') is not None:
            temp_model = main_models.ResourceSpec()
            self.elastic_resource = temp_model.from_map(m.get('elasticResource'))

        if m.get('fixedResource') is not None:
            temp_model = main_models.ResourceSpec()
            self.fixed_resource = temp_model.from_map(m.get('fixedResource'))

        return self

