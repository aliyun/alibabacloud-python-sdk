# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group_order: main_models.CreateResourceGroupResponseBodyResourceGroupOrder = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the order that is used to create the serverless resource group.
        self.resource_group_order = resource_group_order
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.resource_group_order:
            self.resource_group_order.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_order is not None:
            result['ResourceGroupOrder'] = self.resource_group_order.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupOrder') is not None:
            temp_model = main_models.CreateResourceGroupResponseBodyResourceGroupOrder()
            self.resource_group_order = temp_model.from_map(m.get('ResourceGroupOrder'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateResourceGroupResponseBodyResourceGroupOrder(DaraModel):
    def __init__(
        self,
        id: str = None,
        order_id: int = None,
        order_instance_id: str = None,
    ):
        # The ID of the serverless resource group.
        self.id = id
        # The ID of the order that is used to create the serverless resource group.
        self.order_id = order_id
        # The instance ID of the order that is used to create the serverless resource group.
        self.order_instance_id = order_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')

        return self

