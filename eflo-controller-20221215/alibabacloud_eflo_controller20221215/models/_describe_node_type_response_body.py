# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNodeTypeResponseBody(DaraModel):
    def __init__(
        self,
        disk_quantity: int = None,
        eni_high_dense_quantity: int = None,
        eni_ipv_6address_quantity: int = None,
        eni_private_ip_address_quantity: int = None,
        eni_quantity: int = None,
        request_id: str = None,
    ):
        # The maximum number of disks that can be attached.
        self.disk_quantity = disk_quantity
        # The maximum number of network interfaces for high-density mode.
        self.eni_high_dense_quantity = eni_high_dense_quantity
        # The maximum number of IPv6 addresses that an ENI can have.
        self.eni_ipv_6address_quantity = eni_ipv_6address_quantity
        # The maximum number of IPv4 addresses that an ENI can have.
        self.eni_private_ip_address_quantity = eni_private_ip_address_quantity
        # The maximum number of supported elastic network interfaces (ENIs), including primary and secondary ENIs.
        self.eni_quantity = eni_quantity
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_quantity is not None:
            result['DiskQuantity'] = self.disk_quantity

        if self.eni_high_dense_quantity is not None:
            result['EniHighDenseQuantity'] = self.eni_high_dense_quantity

        if self.eni_ipv_6address_quantity is not None:
            result['EniIpv6AddressQuantity'] = self.eni_ipv_6address_quantity

        if self.eni_private_ip_address_quantity is not None:
            result['EniPrivateIpAddressQuantity'] = self.eni_private_ip_address_quantity

        if self.eni_quantity is not None:
            result['EniQuantity'] = self.eni_quantity

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskQuantity') is not None:
            self.disk_quantity = m.get('DiskQuantity')

        if m.get('EniHighDenseQuantity') is not None:
            self.eni_high_dense_quantity = m.get('EniHighDenseQuantity')

        if m.get('EniIpv6AddressQuantity') is not None:
            self.eni_ipv_6address_quantity = m.get('EniIpv6AddressQuantity')

        if m.get('EniPrivateIpAddressQuantity') is not None:
            self.eni_private_ip_address_quantity = m.get('EniPrivateIpAddressQuantity')

        if m.get('EniQuantity') is not None:
            self.eni_quantity = m.get('EniQuantity')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

