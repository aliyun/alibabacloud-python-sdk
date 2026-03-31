# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecLogDeliveriesResponseBody(DaraModel):
    def __init__(
        self,
        delivery_configs: List[main_models.DescribeApisecLogDeliveriesResponseBodyDeliveryConfigs] = None,
        request_id: str = None,
    ):
        # The configurations of API security log subscription.
        self.delivery_configs = delivery_configs
        # The ID of the request.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_configs = []
        if m.get('DeliveryConfigs') is not None:
            for k1 in m.get('DeliveryConfigs'):
                temp_model = main_models.DescribeApisecLogDeliveriesResponseBodyDeliveryConfigs()
                self.delivery_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApisecLogDeliveriesResponseBodyDeliveryConfigs(DaraModel):
    def __init__(
        self,
        assert_key: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        project_name: str = None,
        status: bool = None,
    ):
        # The type of the log subscription. Valid values:
        # 
        # *   **risk**: risk information.
        # *   **event**: attack event information.
        # *   **asset**: asset information.
        self.assert_key = assert_key
        # The ID of the region where logs are stored.
        self.log_region_id = log_region_id
        # The name of the Logstore in Simple Log Service.
        self.log_store_name = log_store_name
        # The name of the project in Simple Log Service.
        self.project_name = project_name
        # The status of API security log subscription. Valid values:
        # 
        # *   **true**: enabled.
        # *   **false**: disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assert_key is not None:
            result['AssertKey'] = self.assert_key

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssertKey') is not None:
            self.assert_key = m.get('AssertKey')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

