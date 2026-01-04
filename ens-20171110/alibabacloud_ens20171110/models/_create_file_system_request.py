# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateFileSystemRequest(DaraModel):
    def __init__(
        self,
        order_details: List[main_models.CreateFileSystemRequestOrderDetails] = None,
    ):
        # The information about the orders.
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
                temp_model = main_models.CreateFileSystemRequestOrderDetails()
                self.order_details.append(temp_model.from_map(k1))

        return self

class CreateFileSystemRequestOrderDetails(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        ens_region_id: str = None,
        file_system_name: str = None,
        mount_target_domain: str = None,
        network_id: str = None,
        order_type: str = None,
        protocol_type: str = None,
        storge_type: str = None,
    ):
        # The billing method of the NAS file system. Valid values:
        # 
        # *   PrePaid: subscription. This billing method is not supported.
        # *   PostPaid: pay-as-you-go.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The ID of the edge node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The name of the file system. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.file_system_name = file_system_name
        # The name of the mount target. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.mount_target_domain = mount_target_domain
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.network_id = network_id
        # The type of the order. Set the value to BUY.
        # 
        # This parameter is required.
        self.order_type = order_type
        # The storage protocol. Set the value to nfs.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The storage type. Valid values:
        # 
        # *   Capacity.
        # *   Performance.
        # 
        # This parameter is required.
        self.storge_type = storge_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.storge_type is not None:
            result['StorgeType'] = self.storge_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('StorgeType') is not None:
            self.storge_type = m.get('StorgeType')

        return self

