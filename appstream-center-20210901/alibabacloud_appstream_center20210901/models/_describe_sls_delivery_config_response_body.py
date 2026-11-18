# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DescribeSlsDeliveryConfigResponseBody(DaraModel):
    def __init__(
        self,
        delivery_configs: List[main_models.DescribeSlsDeliveryConfigResponseBodyDeliveryConfigs] = None,
        request_id: str = None,
    ):
        # The list of delivery configurations that match the filter conditions. If no configurations match the conditions, an empty list is returned.
        self.delivery_configs = delivery_configs
        # The request ID used to locate the current call.
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
                temp_model = main_models.DescribeSlsDeliveryConfigResponseBodyDeliveryConfigs()
                self.delivery_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSlsDeliveryConfigResponseBodyDeliveryConfigs(DaraModel):
    def __init__(
        self,
        log_stores: List[main_models.DescribeSlsDeliveryConfigResponseBodyDeliveryConfigsLogStores] = None,
        project_name: str = None,
        sls_region_id: str = None,
    ):
        # The list of Logstore delivery configurations under the project.
        self.log_stores = log_stores
        # The name of the destination SLS project.
        self.project_name = project_name
        # The ID of the region where the destination SLS project is located.
        self.sls_region_id = sls_region_id

    def validate(self):
        if self.log_stores:
            for v1 in self.log_stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogStores'] = []
        if self.log_stores is not None:
            for k1 in self.log_stores:
                result['LogStores'].append(k1.to_map() if k1 else None)

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_stores = []
        if m.get('LogStores') is not None:
            for k1 in m.get('LogStores'):
                temp_model = main_models.DescribeSlsDeliveryConfigResponseBodyDeliveryConfigsLogStores()
                self.log_stores.append(temp_model.from_map(k1))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        return self

class DescribeSlsDeliveryConfigResponseBodyDeliveryConfigsLogStores(DaraModel):
    def __init__(
        self,
        delivery_scopes: List[main_models.DescribeSlsDeliveryConfigResponseBodyDeliveryConfigsLogStoresDeliveryScopes] = None,
        log_store_name: str = None,
        ttl: int = None,
    ):
        # The product delivery scopes of the Logstore and the delivery status of each scope.
        self.delivery_scopes = delivery_scopes
        # The name of the destination SLS Logstore.
        self.log_store_name = log_store_name
        # The data retention period configured for the destination Logstore, in days.
        self.ttl = ttl

    def validate(self):
        if self.delivery_scopes:
            for v1 in self.delivery_scopes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeliveryScopes'] = []
        if self.delivery_scopes is not None:
            for k1 in self.delivery_scopes:
                result['DeliveryScopes'].append(k1.to_map() if k1 else None)

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_scopes = []
        if m.get('DeliveryScopes') is not None:
            for k1 in m.get('DeliveryScopes'):
                temp_model = main_models.DescribeSlsDeliveryConfigResponseBodyDeliveryConfigsLogStoresDeliveryScopes()
                self.delivery_scopes.append(temp_model.from_map(k1))

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class DescribeSlsDeliveryConfigResponseBodyDeliveryConfigsLogStoresDeliveryScopes(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        status: str = None,
    ):
        # The product type of the delivery scope. For example, `WuyingServer` indicates Enterprise Edition workstations.
        self.product_type = product_type
        # The current status of the delivery configuration. Valid values:
        # - `Stopped`: Delivery is stopped.
        # - `Enabled`: Delivery is enabled.
        # - `AbnormalLogstoreDeleted`: The destination Logstore is deleted, and delivery is abnormal.
        # - `AbnormalProjectDeleted`: The destination project is deleted, and delivery is abnormal.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

