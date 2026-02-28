# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListNetworkInterfacesRequest(DaraModel):
    def __init__(
        self,
        enable_page: bool = None,
        ip: str = None,
        network_interface_id: str = None,
        node_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        subnet_id: str = None,
        tag: List[main_models.ListNetworkInterfacesRequestTag] = None,
        vpd_id: str = None,
    ):
        # Specifies whether pagination is required.
        self.enable_page = enable_page
        # network interface controller the IP address.
        self.ip = ip
        # Lingjun network interface controller ID.
        self.network_interface_id = network_interface_id
        # The ID of the machine to which the instance belongs.
        self.node_id = node_id
        # The number of the page to return.
        self.page_number = page_number
        # The current number of pages.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the instance to which the Lingjun subnet belongs.
        self.subnet_id = subnet_id
        # The list of tags
        self.tag = tag
        # The ID of the VPD.
        self.vpd_id = vpd_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListNetworkInterfacesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        return self

class ListNetworkInterfacesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

