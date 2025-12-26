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
        charge_type: str = None,
        image_id: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        server_instance_type: str = None,
        status: str = None,
        virtual_node_pool_id: str = None,
        wuying_server_id_list: List[str] = None,
        wuying_server_name_or_id: str = None,
    ):
        self.add_virtual_node_pool_status_list = add_virtual_node_pool_status_list
        # The region ID.
        self.biz_region_id = biz_region_id
        # The billing method of the Internet access package.
        self.charge_type = charge_type
        # The image ID.
        self.image_id = image_id
        # The office network IDs.
        self.office_site_id = office_site_id
        # The page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # Workstation specifications.
        self.server_instance_type = server_instance_type
        # The status of the workstation.
        self.status = status
        self.virtual_node_pool_id = virtual_node_pool_id
        # The list of workstation IDs.
        self.wuying_server_id_list = wuying_server_id_list
        # The workstation name or workstation ID.
        self.wuying_server_name_or_id = wuying_server_name_or_id

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

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.server_instance_type is not None:
            result['ServerInstanceType'] = self.server_instance_type

        if self.status is not None:
            result['Status'] = self.status

        if self.virtual_node_pool_id is not None:
            result['VirtualNodePoolId'] = self.virtual_node_pool_id

        if self.wuying_server_id_list is not None:
            result['WuyingServerIdList'] = self.wuying_server_id_list

        if self.wuying_server_name_or_id is not None:
            result['WuyingServerNameOrId'] = self.wuying_server_name_or_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddVirtualNodePoolStatusList') is not None:
            self.add_virtual_node_pool_status_list = m.get('AddVirtualNodePoolStatusList')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServerInstanceType') is not None:
            self.server_instance_type = m.get('ServerInstanceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VirtualNodePoolId') is not None:
            self.virtual_node_pool_id = m.get('VirtualNodePoolId')

        if m.get('WuyingServerIdList') is not None:
            self.wuying_server_id_list = m.get('WuyingServerIdList')

        if m.get('WuyingServerNameOrId') is not None:
            self.wuying_server_name_or_id = m.get('WuyingServerNameOrId')

        return self

