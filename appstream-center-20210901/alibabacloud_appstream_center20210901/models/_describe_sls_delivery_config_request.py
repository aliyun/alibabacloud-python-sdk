# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DescribeSlsDeliveryConfigRequest(DaraModel):
    def __init__(
        self,
        delivery_scopes: List[main_models.DescribeSlsDeliveryConfigRequestDeliveryScopes] = None,
        log_store_name: str = None,
        project_name: str = None,
        sls_region_id: str = None,
    ):
        # Filters delivery scopes by the product type to which the logs belong. If this parameter is omitted or an empty list is passed, delivery scopes are not filtered by product type.
        self.delivery_scopes = delivery_scopes
        # The name of the SLS Logstore. Exact match is used. If this parameter is omitted, delivery scopes are not filtered by Logstore name.
        self.log_store_name = log_store_name
        # The name of the SLS project. Exact match is used. If this parameter is omitted, delivery scopes are not filtered by project name.
        self.project_name = project_name
        # The ID of the region where the SLS project is located. Exact match is used. If this parameter is omitted, delivery scopes are not filtered by region.
        self.sls_region_id = sls_region_id

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

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_scopes = []
        if m.get('DeliveryScopes') is not None:
            for k1 in m.get('DeliveryScopes'):
                temp_model = main_models.DescribeSlsDeliveryConfigRequestDeliveryScopes()
                self.delivery_scopes.append(temp_model.from_map(k1))

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        return self

class DescribeSlsDeliveryConfigRequestDeliveryScopes(DaraModel):
    def __init__(
        self,
        product_type: str = None,
    ):
        # The query condition for the product type to which the logs belong. If you specify this parameter, delivery scopes are filtered by the specified product type. The value must be consistent with the existing delivery configurations. For example, `WuyingServer` indicates Enterprise Edition workstations.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

