# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeLogDeliveryConfigsResponseBody(DaraModel):
    def __init__(
        self,
        delivery_configs: List[main_models.DescribeLogDeliveryConfigsResponseBodyDeliveryConfigs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the log delivery configuration.
        self.delivery_configs = delivery_configs
        self.max_results = max_results
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.delivery_configs:
            for v1 in self.delivery_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeliveryConfigs'] = []
        if self.delivery_configs is not None:
            for k1 in self.delivery_configs:
                result['DeliveryConfigs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_configs = []
        if m.get('DeliveryConfigs') is not None:
            for k1 in m.get('DeliveryConfigs'):
                temp_model = main_models.DescribeLogDeliveryConfigsResponseBodyDeliveryConfigs()
                self.delivery_configs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLogDeliveryConfigsResponseBodyDeliveryConfigs(DaraModel):
    def __init__(
        self,
        delivery_detail: str = None,
        delivery_name: str = None,
        delivery_type: str = None,
    ):
        # The content of the log delivery configuration. The value is a JSON string that contains multiple parameters.
        # 
        # >  This parameter is the same as the **DeliveryDetail** parameter of the **CreateLogDeliveryConfig** operation. For more information, see **Parameter description for log delivery configuration** of the [CreateLogDeliveryConfig](~~CreateLogDeliveryConfig~~) operation.
        self.delivery_detail = delivery_detail
        # The name of the log delivery configuration.
        self.delivery_name = delivery_name
        # The type of the log delivery configuration. Valid values:
        # 
        # *   **syslog**: Logs are delivered to a syslog service.
        # *   **kafka**: Logs are delivered to a Kafka service.
        self.delivery_type = delivery_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_detail is not None:
            result['DeliveryDetail'] = self.delivery_detail

        if self.delivery_name is not None:
            result['DeliveryName'] = self.delivery_name

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryDetail') is not None:
            self.delivery_detail = m.get('DeliveryDetail')

        if m.get('DeliveryName') is not None:
            self.delivery_name = m.get('DeliveryName')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        return self

