# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class RunInstanceInspectionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        item_overrides: List[main_models.RunInstanceInspectionRequestItemOverrides] = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.item_overrides = item_overrides
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.item_overrides:
            for v1 in self.item_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        result['itemOverrides'] = []
        if self.item_overrides is not None:
            for k1 in self.item_overrides:
                result['itemOverrides'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        self.item_overrides = []
        if m.get('itemOverrides') is not None:
            for k1 in m.get('itemOverrides'):
                temp_model = main_models.RunInstanceInspectionRequestItemOverrides()
                self.item_overrides.append(temp_model.from_map(k1))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class RunInstanceInspectionRequestItemOverrides(DaraModel):
    def __init__(
        self,
        parameters: Any = None,
        template_code: str = None,
    ):
        # This parameter is required.
        self.parameters = parameters
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

