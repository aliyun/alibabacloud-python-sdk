# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeLogDeliveryConfigResponseBody(DaraModel):
    def __init__(
        self,
        delivery_config: main_models.DescribeLogDeliveryConfigResponseBodyDeliveryConfig = None,
        request_id: str = None,
    ):
        # The information about the log delivery configuration.
        self.delivery_config = delivery_config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.delivery_config:
            self.delivery_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_config is not None:
            result['DeliveryConfig'] = self.delivery_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryConfig') is not None:
            temp_model = main_models.DescribeLogDeliveryConfigResponseBodyDeliveryConfig()
            self.delivery_config = temp_model.from_map(m.get('DeliveryConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLogDeliveryConfigResponseBodyDeliveryConfig(DaraModel):
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

