# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListWuyingServerRequest(DaraModel):
    def __init__(
        self,
        add_virtual_node_pool_status_list: List[str] = None,
        biz_region_id: str = None,
        biz_type: int = None,
        charge_type: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        expired_time_end: str = None,
        expired_time_start: str = None,
        image_id: str = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        server_instance_type: str = None,
        status: str = None,
        users: List[str] = None,
        virtual_node_pool_id: str = None,
        wuying_server_id_list: List[str] = None,
        wuying_server_name_or_id: str = None,
        zone_id: str = None,
    ):
        # The list of statuses for joining a virtual node pool.
        self.add_virtual_node_pool_status_list = add_virtual_node_pool_status_list
        # The region ID.
        self.biz_region_id = biz_region_id
        # The business type.
        self.biz_type = biz_type
        # The billing type.
        self.charge_type = charge_type
        # The end time of the creation time range, in ISO 8601 format. This time point is exclusive.
        self.create_time_end = create_time_end
        # The start time of the creation time range, in ISO 8601 format. This time point is inclusive.
        self.create_time_start = create_time_start
        # The end time of the expiration time range, in ISO 8601 format. This time point is exclusive.
        self.expired_time_end = expired_time_end
        # The start time of the expiration time range, in ISO 8601 format. This time point is inclusive.
        self.expired_time_start = expired_time_start
        # The image ID.
        self.image_id = image_id
        # The internal IP address.
        self.network_interface_ip = network_interface_ip
        # The office network ID.
        self.office_site_id = office_site_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The product type.
        self.product_type = product_type
        # The workstation instance type.
        self.server_instance_type = server_instance_type
        # The workstation status.
        self.status = status
        # The list of authorized users.
        self.users = users
        # The virtual node pool ID.
        self.virtual_node_pool_id = virtual_node_pool_id
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list
        # The workstation name or workstation ID.
        self.wuying_server_name_or_id = wuying_server_name_or_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_virtual_node_pool_status_list is not None:
            result['AddVirtualNodePoolStatusList'] = self.add_virtual_node_pool_status_list

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.expired_time_end is not None:
            result['ExpiredTimeEnd'] = self.expired_time_end

        if self.expired_time_start is not None:
            result['ExpiredTimeStart'] = self.expired_time_start

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.server_instance_type is not None:
            result['ServerInstanceType'] = self.server_instance_type

        if self.status is not None:
            result['Status'] = self.status

        if self.users is not None:
            result['Users'] = self.users

        if self.virtual_node_pool_id is not None:
            result['VirtualNodePoolId'] = self.virtual_node_pool_id

        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list

        if self.wuying_server_name_or_id is not None:
            result['WuyingServerNameOrId'] = self.wuying_server_name_or_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddVirtualNodePoolStatusList') is not None:
            self.add_virtual_node_pool_status_list = m.get('AddVirtualNodePoolStatusList')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('ExpiredTimeEnd') is not None:
            self.expired_time_end = m.get('ExpiredTimeEnd')

        if m.get('ExpiredTimeStart') is not None:
            self.expired_time_start = m.get('ExpiredTimeStart')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ServerInstanceType') is not None:
            self.server_instance_type = m.get('ServerInstanceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        if m.get('VirtualNodePoolId') is not None:
            self.virtual_node_pool_id = m.get('VirtualNodePoolId')

        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')

        if m.get('WuyingServerNameOrId') is not None:
            self.wuying_server_name_or_id = m.get('WuyingServerNameOrId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

