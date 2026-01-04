# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomerGatewayResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        customer_gateway_id: str = None,
        description: str = None,
        ip_address: str = None,
        name: str = None,
        request_id: str = None,
    ):
        # The timestamp generated when the customer gateway was created. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The ID of the customer gateway.
        self.customer_gateway_id = customer_gateway_id
        # The description of the customer gateway.
        self.description = description
        # The static IP address of the gateway device in the on-premises data center.
        self.ip_address = ip_address
        # The name of the customer gateway.
        self.name = name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.customer_gateway_id is not None:
            result['CustomerGatewayId'] = self.customer_gateway_id

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomerGatewayId') is not None:
            self.customer_gateway_id = m.get('CustomerGatewayId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

