# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListIntegratedServiceResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListIntegratedServiceResponseBodyData] = None,
        request_id: str = None,
    ):
        # The information about the cloud service that can be integrated.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListIntegratedServiceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListIntegratedServiceResponseBodyData(DaraModel):
    def __init__(
        self,
        aggregator_delivery_data_type: str = None,
        integrated_types: str = None,
        service_code: str = None,
        service_name: str = None,
        status: bool = None,
    ):
        # The type of the event that is integrated across accounts. Valid values:
        # 
        # *   NonCompliantNotification: non-compliance event
        self.aggregator_delivery_data_type = aggregator_delivery_data_type
        # The types of the integrated events. Separate multiple event types with commas (,). Valid values:
        # 
        # *   ConfigurationItemChangeNotification: resource change event
        # *   NonCompliantNotification: non-compliance event
        self.integrated_types = integrated_types
        # The identifier of the cloud service. Valid values:
        # 
        # *   eventbridge: EventBridge
        # *   cms: CloudMonitor
        # *   bpstudio: Cloud Architect Design Tools
        self.service_code = service_code
        # The name of the cloud service.
        self.service_name = service_name
        # The integration status of the cloud service. Valid values:
        # 
        # *   true
        # *   false
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

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

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

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

