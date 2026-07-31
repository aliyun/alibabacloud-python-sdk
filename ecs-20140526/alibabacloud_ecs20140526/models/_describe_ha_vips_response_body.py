# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeHaVipsResponseBody(DaraModel):
    def __init__(
        self,
        ha_vips: main_models.DescribeHaVipsResponseBodyHaVips = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ha_vips = ha_vips
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ha_vips:
            self.ha_vips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vips is not None:
            result['HaVips'] = self.ha_vips.to_map()

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
        if m.get('HaVips') is not None:
            temp_model = main_models.DescribeHaVipsResponseBodyHaVips()
            self.ha_vips = temp_model.from_map(m.get('HaVips'))

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
        ha_vip: List[main_models.DescribeHaVipsResponseBodyHaVipsHaVip] = None,
    ):
        self.ha_vip = ha_vip

    def validate(self):
        if self.ha_vip:
            for v1 in self.ha_vip:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HaVip'] = []
        if self.ha_vip is not None:
            for k1 in self.ha_vip:
                result['HaVip'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ha_vip = []
        if m.get('HaVip') is not None:
            for k1 in m.get('HaVip'):
                temp_model = main_models.DescribeHaVipsResponseBodyHaVipsHaVip()
                self.ha_vip.append(temp_model.from_map(k1))

        return self

class DescribeHaVipsResponseBodyHaVipsHaVip(DaraModel):
    def __init__(
        self,
        associated_eip_addresses: main_models.DescribeHaVipsResponseBodyHaVipsHaVipAssociatedEipAddresses = None,
        associated_instances: main_models.DescribeHaVipsResponseBodyHaVipsHaVipAssociatedInstances = None,
        create_time: str = None,
        description: str = None,
        ha_vip_id: str = None,
        ip_address: str = None,
        master_instance_id: str = None,
        region_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.associated_eip_addresses = associated_eip_addresses
        self.associated_instances = associated_instances
        self.create_time = create_time
        self.description = description
        self.ha_vip_id = ha_vip_id
        self.ip_address = ip_address
        self.master_instance_id = master_instance_id
        self.region_id = region_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.associated_eip_addresses:
            self.associated_eip_addresses.validate()
        if self.associated_instances:
            self.associated_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_eip_addresses is not None:
            result['AssociatedEipAddresses'] = self.associated_eip_addresses.to_map()

        if self.associated_instances is not None:
            result['AssociatedInstances'] = self.associated_instances.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedEipAddresses') is not None:
            temp_model = main_models.DescribeHaVipsResponseBodyHaVipsHaVipAssociatedEipAddresses()
            self.associated_eip_addresses = temp_model.from_map(m.get('AssociatedEipAddresses'))

        if m.get('AssociatedInstances') is not None:
            temp_model = main_models.DescribeHaVipsResponseBodyHaVipsHaVipAssociatedInstances()
            self.associated_instances = temp_model.from_map(m.get('AssociatedInstances'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeHaVipsResponseBodyHaVipsHaVipAssociatedInstances(DaraModel):
    def __init__(
        self,
        associated_instance: List[str] = None,
    ):
        self.associated_instance = associated_instance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_instance is not None:
            result['associatedInstance'] = self.associated_instance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('associatedInstance') is not None:
            self.associated_instance = m.get('associatedInstance')

        return self

class DescribeHaVipsResponseBodyHaVipsHaVipAssociatedEipAddresses(DaraModel):
    def __init__(
        self,
        associated_eip_addresse: List[str] = None,
    ):
        self.associated_eip_addresse = associated_eip_addresse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_eip_addresse is not None:
            result['associatedEipAddresse'] = self.associated_eip_addresse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('associatedEipAddresse') is not None:
            self.associated_eip_addresse = m.get('associatedEipAddresse')

        return self

