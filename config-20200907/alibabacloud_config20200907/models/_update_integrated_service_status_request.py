# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIntegratedServiceStatusRequest(DaraModel):
    def __init__(
        self,
        aggregator_delivery_data_type: str = None,
        integrated_types: str = None,
        service_code: str = None,
        status: bool = None,
    ):
        self.aggregator_delivery_data_type = aggregator_delivery_data_type
        self.integrated_types = integrated_types
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_delivery_data_type is not None:
            result['AggregatorDeliveryDataType'] = self.aggregator_delivery_data_type

        if self.integrated_types is not None:
            result['IntegratedTypes'] = self.integrated_types

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorDeliveryDataType') is not None:
            self.aggregator_delivery_data_type = m.get('AggregatorDeliveryDataType')

        if m.get('IntegratedTypes') is not None:
            self.integrated_types = m.get('IntegratedTypes')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

