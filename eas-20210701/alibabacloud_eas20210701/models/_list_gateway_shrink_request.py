# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayShrinkRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        gateway_type: str = None,
        internet_enabled: bool = None,
        label_shrink: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_name: str = None,
        sort: str = None,
        status: str = None,
    ):
        # The billing method.
        self.charge_type = charge_type
        # The ID of the private gateway. You can obtain the ID from the private_gateway_id field in the response of the ListResources operation.
        self.gateway_id = gateway_id
        # The alias of the private gateway.
        self.gateway_name = gateway_name
        # The type of the gateway.
        self.gateway_type = gateway_type
        # Specifies whether to enable access over the public network.
        self.internet_enabled = internet_enabled
        # Filter by tag.
        self.label_shrink = label_shrink
        # The sort order.
        self.order = order
        # The page number of the gateway list to return. The default value is 1.
        self.page_number = page_number
        # The number of gateways to return on each page. The default value is 100.
        self.page_size = page_size
        # The ID of the resource group. You can obtain the ID from the ResourceId field in the response of the [ListResources](https://help.aliyun.com/document_detail/412133.html) operation.
        self.resource_name = resource_name
        # The field to sort by.
        self.sort = sort
        # The status of the gateway.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.internet_enabled is not None:
            result['InternetEnabled'] = self.internet_enabled

        if self.label_shrink is not None:
            result['Label'] = self.label_shrink

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('InternetEnabled') is not None:
            self.internet_enabled = m.get('InternetEnabled')

        if m.get('Label') is not None:
            self.label_shrink = m.get('Label')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

