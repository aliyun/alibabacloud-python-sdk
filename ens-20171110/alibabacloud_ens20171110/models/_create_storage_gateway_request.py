# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateStorageGatewayRequest(DaraModel):
    def __init__(
        self,
        order_details: List[main_models.CreateStorageGatewayRequestOrderDetails] = None,
    ):
        # The array of orders.
        # 
        # This parameter is required.
        self.order_details = order_details

    def validate(self):
        if self.order_details:
            for v1 in self.order_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OrderDetails'] = []
        if self.order_details is not None:
            for k1 in self.order_details:
                result['OrderDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_details = []
        if m.get('OrderDetails') is not None:
            for k1 in m.get('OrderDetails'):
                temp_model = main_models.CreateStorageGatewayRequestOrderDetails()
                self.order_details.append(temp_model.from_map(k1))

        return self

class CreateStorageGatewayRequestOrderDetails(DaraModel):
    def __init__(
        self,
        description: str = None,
        ens_region_id: str = None,
        gateway_name: str = None,
        gateway_type: str = None,
        vpc_id: str = None,
    ):
        # The description of the gateway. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The ID of the node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The name of the gateway. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, colons (.), underscores (_), and hyphens (-).
        self.gateway_name = gateway_name
        # The type of the gateway. Set this parameter to **1**. **1** indicates iSCSI.
        # 
        # This parameter is required.
        self.gateway_type = gateway_type
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

