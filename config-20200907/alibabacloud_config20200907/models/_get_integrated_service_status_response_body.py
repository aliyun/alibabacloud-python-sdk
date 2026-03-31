# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIntegratedServiceStatusResponseBody(DaraModel):
    def __init__(
        self,
        aggregator_delivery_data_type: str = None,
        data: bool = None,
        integrated_types: str = None,
        request_id: str = None,
    ):
        # The type of the event that is integrated across accounts. Valid values:
        # 
        # *   NonCompliantNotification: non-compliance event
        self.aggregator_delivery_data_type = aggregator_delivery_data_type
        # Indicates whether the product has been integrated. Valid values:
        # 
        # *   true
        # *   false
        self.data = data
        # The types of the integrated events. Separate multiple event types with commas (,). Valid values:
        # 
        # *   ConfigurationItemChangeNotification: resource change event
        # *   NonCompliantNotification: non-compliance event
        self.integrated_types = integrated_types
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_delivery_data_type is not None:
            result['AggregatorDeliveryDataType'] = self.aggregator_delivery_data_type

        if self.data is not None:
            result['Data'] = self.data

        if self.integrated_types is not None:
            result['IntegratedTypes'] = self.integrated_types

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorDeliveryDataType') is not None:
            self.aggregator_delivery_data_type = m.get('AggregatorDeliveryDataType')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('IntegratedTypes') is not None:
            self.integrated_types = m.get('IntegratedTypes')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

