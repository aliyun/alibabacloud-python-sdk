# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DescribeWuyingServerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeWuyingServerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeWuyingServerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWuyingServerResponseBodyData(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        biz_region_id: str = None,
        charge_type: str = None,
        create_time: str = None,
        eni_private_ip_address_quantity: int = None,
        expired_time: str = None,
        image_id: str = None,
        image_name: str = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        os_type: str = None,
        private_ip_sets: List[main_models.DescribeWuyingServerResponseBodyDataPrivateIpSets] = None,
        status: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        wuying_server_id: str = None,
        wuying_server_name: str = None,
    ):
        self.bandwidth = bandwidth
        self.biz_region_id = biz_region_id
        self.charge_type = charge_type
        self.create_time = create_time
        self.eni_private_ip_address_quantity = eni_private_ip_address_quantity
        self.expired_time = expired_time
        self.image_id = image_id
        self.image_name = image_name
        self.network_interface_ip = network_interface_ip
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.office_site_type = office_site_type
        self.os_type = os_type
        self.private_ip_sets = private_ip_sets
        self.status = status
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size
        self.wuying_server_id = wuying_server_id
        self.wuying_server_name = wuying_server_name

    def validate(self):
        if self.private_ip_sets:
            for v1 in self.private_ip_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.eni_private_ip_address_quantity is not None:
            result['EniPrivateIpAddressQuantity'] = self.eni_private_ip_address_quantity

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        result['PrivateIpSets'] = []
        if self.private_ip_sets is not None:
            for k1 in self.private_ip_sets:
                result['PrivateIpSets'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        if self.wuying_server_name is not None:
            result['WuyingServerName'] = self.wuying_server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EniPrivateIpAddressQuantity') is not None:
            self.eni_private_ip_address_quantity = m.get('EniPrivateIpAddressQuantity')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        self.private_ip_sets = []
        if m.get('PrivateIpSets') is not None:
            for k1 in m.get('PrivateIpSets'):
                temp_model = main_models.DescribeWuyingServerResponseBodyDataPrivateIpSets()
                self.private_ip_sets.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        if m.get('WuyingServerName') is not None:
            self.wuying_server_name = m.get('WuyingServerName')

        return self

class DescribeWuyingServerResponseBodyDataPrivateIpSets(DaraModel):
    def __init__(
        self,
        primary: bool = None,
        private_ip_address: str = None,
    ):
        self.primary = primary
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary is not None:
            result['Primary'] = self.primary

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

