# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteModelServiceRequest(DaraModel):
    def __init__(
        self,
        model_service_name: str = None,
    ):
        self.model_service_name = model_service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_service_name is not None:
            result['modelServiceName'] = self.model_service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelServiceName') is not None:
            self.model_service_name = m.get('modelServiceName')

        return self

