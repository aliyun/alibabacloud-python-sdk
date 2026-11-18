# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DeliverToUserSlsRequest(DaraModel):
    def __init__(
        self,
        delivery_scopes: List[main_models.DeliverToUserSlsRequestDeliveryScopes] = None,
        existed_project_name: str = None,
        log_store_name: str = None,
        project_name: str = None,
        sls_region_id: str = None,
        ttl: int = None,
    ):
        # The list of product scopes for which delivery needs to be configured. Specify at least one item. You cannot create duplicate enabled delivery configurations for the same account and product type.
        # 
        # This parameter is required.
        self.delivery_scopes = delivery_scopes
        # The name of an existing SLS project. The name must start with `elastic-desktop-` and the project must already exist in the specified SLS region of the current account.
        # 
        # Specify either this parameter or `ProjectName`.
        self.existed_project_name = existed_project_name
        # The name of the destination Logstore. The name must start with `elastic_desktop_`. If the Logstore does not exist, it is created. If the Logstore already exists, it is reused.
        # 
        # If this parameter is not specified, the part after `elastic-desktop-` in the selected project name is used as a suffix to generate a name that starts with `elastic_desktop_`. For example, if the project name is `elastic-desktop-audit`, the default Logstore name is `elastic_desktop_audit`.
        self.log_store_name = log_store_name
        # The name of the SLS project to be created or reused. The name must start with `elastic-desktop-`.
        # 
        # Specify either this parameter or `ExistedProjectName`. If the project does not exist, it is created. If the project already exists, it is reused.
        self.project_name = project_name
        # The ID of the region where the destination SLS project is located. This parameter is required.
        # 
        # This parameter is required.
        self.sls_region_id = sls_region_id
        # The data retention period of the new Logstore. Unit: days.
        # 
        # **Valid values:** 1 to 3650.
        # 
        # **Default value:** 30.
        # 
        # If an existing Logstore is reused, this operation does not update its data retention period.
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

        if self.existed_project_name is not None:
            result['ExistedProjectName'] = self.existed_project_name

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_scopes = []
        if m.get('DeliveryScopes') is not None:
            for k1 in m.get('DeliveryScopes'):
                temp_model = main_models.DeliverToUserSlsRequestDeliveryScopes()
                self.delivery_scopes.append(temp_model.from_map(k1))

        if m.get('ExistedProjectName') is not None:
            self.existed_project_name = m.get('ExistedProjectName')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class DeliverToUserSlsRequestDeliveryScopes(DaraModel):
    def __init__(
        self,
        product_type: str = None,
    ):
        # The product type to which the logs belong. Specify the product type for which you want to enable log delivery. For example, `CloudBrowser` indicates Cloud Browser.
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

