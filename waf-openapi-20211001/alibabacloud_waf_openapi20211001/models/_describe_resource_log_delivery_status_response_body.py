# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceLogDeliveryStatusResponseBody(DaraModel):
    def __init__(
        self,
        log_configs: List[main_models.DescribeResourceLogDeliveryStatusResponseBodyLogConfigs] = None,
        request_id: str = None,
    ):
        self.log_configs = log_configs
        self.request_id = request_id

    def validate(self):
        if self.log_configs:
            for v1 in self.log_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogConfigs'] = []
        if self.log_configs is not None:
            for k1 in self.log_configs:
                result['LogConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_configs = []
        if m.get('LogConfigs') is not None:
            for k1 in m.get('LogConfigs'):
                temp_model = main_models.DescribeResourceLogDeliveryStatusResponseBodyLogConfigs()
                self.log_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeResourceLogDeliveryStatusResponseBodyLogConfigs(DaraModel):
    def __init__(
        self,
        delivery_name: str = None,
        delivery_type: str = None,
        resource: str = None,
        status: bool = None,
    ):
        self.delivery_name = delivery_name
        self.delivery_type = delivery_type
        self.resource = resource
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_name is not None:
            result['DeliveryName'] = self.delivery_name

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryName') is not None:
            self.delivery_name = m.get('DeliveryName')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

