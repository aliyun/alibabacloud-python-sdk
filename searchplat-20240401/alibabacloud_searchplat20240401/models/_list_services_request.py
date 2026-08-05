# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServicesRequest(DaraModel):
    def __init__(
        self,
        model_type: str = None,
        name: str = None,
        service_id: str = None,
        service_type: str = None,
    ):
        # The model type. Valid values:
        # 
        # - system: built-in model
        # - deployment: custom deployment model.
        self.model_type = model_type
        # The service name.
        self.name = name
        # The service ID.
        self.service_id = service_id
        # The service type.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.name is not None:
            result['name'] = self.name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        return self

