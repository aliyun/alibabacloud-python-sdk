# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiFallbackServiceConfig(DaraModel):
    def __init__(
        self,
        pass_through_model_name: bool = None,
        service_id: str = None,
        target_model_name: str = None,
    ):
        self.pass_through_model_name = pass_through_model_name
        self.service_id = service_id
        self.target_model_name = target_model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pass_through_model_name is not None:
            result['passThroughModelName'] = self.pass_through_model_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.target_model_name is not None:
            result['targetModelName'] = self.target_model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passThroughModelName') is not None:
            self.pass_through_model_name = m.get('passThroughModelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('targetModelName') is not None:
            self.target_model_name = m.get('targetModelName')

        return self

