# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ResourceQuota(DaraModel):
    def __init__(
        self,
        limit: main_models.ResourceSpec = None,
        request: main_models.ResourceSpec = None,
        used: main_models.ResourceSpec = None,
    ):
        self.limit = limit
        self.request = request
        self.used = used

    def validate(self):
        if self.limit:
            self.limit.validate()
        if self.request:
            self.request.validate()
        if self.used:
            self.used.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit.to_map()

        if self.request is not None:
            result['request'] = self.request.to_map()

        if self.used is not None:
            result['used'] = self.used.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            temp_model = main_models.ResourceSpec()
            self.limit = temp_model.from_map(m.get('limit'))

        if m.get('request') is not None:
            temp_model = main_models.ResourceSpec()
            self.request = temp_model.from_map(m.get('request'))

        if m.get('used') is not None:
            temp_model = main_models.ResourceSpec()
            self.used = temp_model.from_map(m.get('used'))

        return self

