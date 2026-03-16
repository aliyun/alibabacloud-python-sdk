# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetServiceEstimateCostResponseBody(DaraModel):
    def __init__(
        self,
        commodity: Dict[str, main_models.CommodityValue] = None,
        request_id: str = None,
        resources: Dict[str, Any] = None,
    ):
        # Alibaba Cloud Marketplace purchase order information.
        self.commodity = commodity
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resources = resources

    def validate(self):
        if self.commodity:
            for v1 in self.commodity.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Commodity'] = {}
        if self.commodity is not None:
            for k1, v1 in self.commodity.items():
                result['Commodity'][k1] = v1.to_map() if v1 else None

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodity = {}
        if m.get('Commodity') is not None:
            for k1, v1 in m.get('Commodity').items():
                temp_model = main_models.CommodityValue()
                self.commodity[k1] = temp_model.from_map(v1)

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        return self

