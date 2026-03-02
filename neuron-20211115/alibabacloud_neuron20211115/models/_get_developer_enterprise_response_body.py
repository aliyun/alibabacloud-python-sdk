# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class GetDeveloperEnterpriseResponseBody(DaraModel):
    def __init__(
        self,
        enterprise: main_models.Enterprise = None,
        request_id: str = None,
    ):
        self.enterprise = enterprise
        self.request_id = request_id

    def validate(self):
        if self.enterprise:
            self.enterprise.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise is not None:
            result['enterprise'] = self.enterprise.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enterprise') is not None:
            temp_model = main_models.Enterprise()
            self.enterprise = temp_model.from_map(m.get('enterprise'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

