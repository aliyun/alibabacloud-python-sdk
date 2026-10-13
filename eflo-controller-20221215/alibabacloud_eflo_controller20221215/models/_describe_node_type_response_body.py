# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeNodeTypeResponseBody(DaraModel):
    def __init__(
        self,
        disk_quantity: int = None,
        eni_high_dense_quantity: int = None,
        eni_ipv_6address_quantity: int = None,
        eni_private_ip_address_quantity: int = None,
        eni_quantity: int = None,
        eri_quantity: int = None,
        network_card_quantity: int = None,
        network_cards: List[main_models.DescribeNodeTypeResponseBodyNetworkCards] = None,
        primary_eni_queue_number: int = None,
        queue_pair_number: int = None,
        request_id: str = None,
        secondary_eni_queue_number: int = None,
        total_eni_queue_quantity: int = None,
    ):
        # The maximum number of cloud disks that can be mounted.
        self.disk_quantity = disk_quantity
        # The maximum number of network interface controllers (NICs) in high-density mode.
        self.eni_high_dense_quantity = eni_high_dense_quantity
        # The maximum number of IPv6 addresses supported by a NIC.
        self.eni_ipv_6address_quantity = eni_ipv_6address_quantity
        # The maximum number of IPv4 addresses supported by a NIC.
        self.eni_private_ip_address_quantity = eni_private_ip_address_quantity
        # The maximum number of elastic network interfaces (ENIs) supported, including primary and secondary ENIs.
        self.eni_quantity = eni_quantity
        # The number of Elastic RDMA Interfaces (ERIs) for the current specification.
        self.eri_quantity = eri_quantity
        # The number of physical network interface controllers (NICs) supported by the instance type.
        self.network_card_quantity = network_card_quantity
        # The list of physical network interface controllers (NICs), including the details of each physical NIC.
        self.network_cards = network_cards
        # The default number of queues for the primary NIC.
        self.primary_eni_queue_number = primary_eni_queue_number
        # The number of queue pairs (QPs) for all Elastic RDMA Interfaces (ERIs) of the current specification.
        self.queue_pair_number = queue_pair_number
        # The request ID.
        self.request_id = request_id
        # The default number of queues for secondary elastic network interfaces (ENIs).
        self.secondary_eni_queue_number = secondary_eni_queue_number
        # The total queue quota for elastic network interface controllers (NICs) of the current specification.
        self.total_eni_queue_quantity = total_eni_queue_quantity

    def validate(self):
        if self.network_cards:
            for v1 in self.network_cards:
                 if v1:
                    v1.validate()

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

        if self.eri_quantity is not None:
            result['EriQuantity'] = self.eri_quantity

        if self.network_card_quantity is not None:
            result['NetworkCardQuantity'] = self.network_card_quantity

        result['NetworkCards'] = []
        if self.network_cards is not None:
            for k1 in self.network_cards:
                result['NetworkCards'].append(k1.to_map() if k1 else None)

        if self.primary_eni_queue_number is not None:
            result['PrimaryEniQueueNumber'] = self.primary_eni_queue_number

        if self.queue_pair_number is not None:
            result['QueuePairNumber'] = self.queue_pair_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.secondary_eni_queue_number is not None:
            result['SecondaryEniQueueNumber'] = self.secondary_eni_queue_number

        if self.total_eni_queue_quantity is not None:
            result['TotalEniQueueQuantity'] = self.total_eni_queue_quantity

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

        if m.get('EriQuantity') is not None:
            self.eri_quantity = m.get('EriQuantity')

        if m.get('NetworkCardQuantity') is not None:
            self.network_card_quantity = m.get('NetworkCardQuantity')

        self.network_cards = []
        if m.get('NetworkCards') is not None:
            for k1 in m.get('NetworkCards'):
                temp_model = main_models.DescribeNodeTypeResponseBodyNetworkCards()
                self.network_cards.append(temp_model.from_map(k1))

        if m.get('PrimaryEniQueueNumber') is not None:
            self.primary_eni_queue_number = m.get('PrimaryEniQueueNumber')

        if m.get('QueuePairNumber') is not None:
            self.queue_pair_number = m.get('QueuePairNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecondaryEniQueueNumber') is not None:
            self.secondary_eni_queue_number = m.get('SecondaryEniQueueNumber')

        if m.get('TotalEniQueueQuantity') is not None:
            self.total_eni_queue_quantity = m.get('TotalEniQueueQuantity')

        return self

class DescribeNodeTypeResponseBodyNetworkCards(DaraModel):
    def __init__(
        self,
        network_card_index: int = None,
    ):
        # The index of the physical network interface controller (NIC), starting from 0. You can specify this index to attach elastic network interfaces (ENIs) to different underlying physical network interface controllers (NICs).
        self.network_card_index = network_card_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_card_index is not None:
            result['NetworkCardIndex'] = self.network_card_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkCardIndex') is not None:
            self.network_card_index = m.get('NetworkCardIndex')

        return self

