# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeHaVipsResponseBody(DaraModel):
    def __init__(
        self,
        ha_vips: List[main_models.DescribeHaVipsResponseBodyHaVips] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # Details of the HAVIPs.
        self.ha_vips = ha_vips
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ha_vips:
            for v1 in self.ha_vips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HaVips'] = []
        if self.ha_vips is not None:
            for k1 in self.ha_vips:
                result['HaVips'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ha_vips = []
        if m.get('HaVips') is not None:
            for k1 in m.get('HaVips'):
                temp_model = main_models.DescribeHaVipsResponseBodyHaVips()
                self.ha_vips.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHaVipsResponseBodyHaVips(DaraModel):
    def __init__(
        self,
        associated_eip_addresses: List[main_models.DescribeHaVipsResponseBodyHaVipsAssociatedEipAddresses] = None,
        associated_instances: List[main_models.DescribeHaVipsResponseBodyHaVipsAssociatedInstances] = None,
        creation_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        ha_vip_id: str = None,
        ip_address: str = None,
        name: str = None,
        network_id: str = None,
        status: str = None,
        v_switch_id: str = None,
    ):
        # The elastic IP addresses (EIPs) that are associated with the HAVIP.
        self.associated_eip_addresses = associated_eip_addresses
        # The information about instances that are associated with the HAVIP.
        self.associated_instances = associated_instances
        # The time when the HAVIP was created.
        self.creation_time = creation_time
        # The description of the HAVIP.
        self.description = description
        # The ID of the region.
        self.ens_region_id = ens_region_id
        # The ID of the HAVIP.
        self.ha_vip_id = ha_vip_id
        # The IP address of the HAVIP.
        self.ip_address = ip_address
        # The name of the HAVIP.
        self.name = name
        # The ID of the network.
        self.network_id = network_id
        # The status of the HAVIP. Valid values:
        # 
        # *   Creating
        # *   Available
        # *   InUse
        # *   Deleting
        self.status = status
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.associated_eip_addresses:
            for v1 in self.associated_eip_addresses:
                 if v1:
                    v1.validate()
        if self.associated_instances:
            for v1 in self.associated_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociatedEipAddresses'] = []
        if self.associated_eip_addresses is not None:
            for k1 in self.associated_eip_addresses:
                result['AssociatedEipAddresses'].append(k1.to_map() if k1 else None)

        result['AssociatedInstances'] = []
        if self.associated_instances is not None:
            for k1 in self.associated_instances:
                result['AssociatedInstances'].append(k1.to_map() if k1 else None)

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.name is not None:
            result['Name'] = self.name

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_eip_addresses = []
        if m.get('AssociatedEipAddresses') is not None:
            for k1 in m.get('AssociatedEipAddresses'):
                temp_model = main_models.DescribeHaVipsResponseBodyHaVipsAssociatedEipAddresses()
                self.associated_eip_addresses.append(temp_model.from_map(k1))

        self.associated_instances = []
        if m.get('AssociatedInstances') is not None:
            for k1 in m.get('AssociatedInstances'):
                temp_model = main_models.DescribeHaVipsResponseBodyHaVipsAssociatedInstances()
                self.associated_instances.append(temp_model.from_map(k1))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeHaVipsResponseBodyHaVipsAssociatedInstances(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip_address: str = None,
        status: str = None,
    ):
        # The time when the instance was created.
        self.creation_time = creation_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The type of the instance that is associated with the HAVIP. Valid values:
        # 
        # *   EnsInstance: ENS instance
        # *   NetworkInterface: elastic network interface (ENI)
        self.instance_type = instance_type
        # The private IP address of the instance that is associated with the HAVIP. Valid values:
        self.ip_address = ip_address
        # The association status of the HAVIP. Valid values:
        # 
        # *   Associating
        # *   InUse
        # *   Unassociating
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeHaVipsResponseBodyHaVipsAssociatedEipAddresses(DaraModel):
    def __init__(
        self,
        eip: str = None,
        eip_id: str = None,
    ):
        # The EIP.
        self.eip = eip
        # The ID of the EIP.
        self.eip_id = eip_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip is not None:
            result['Eip'] = self.eip

        if self.eip_id is not None:
            result['EipId'] = self.eip_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')

        return self

