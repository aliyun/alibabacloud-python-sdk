# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListSubnetsRequest(DaraModel):
    def __init__(
        self,
        enable_page: bool = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        subnet_id: str = None,
        subnet_name: str = None,
        tag: List[main_models.ListSubnetsRequestTag] = None,
        type: str = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to query by page. Optional values:
        # 
        # *   **true**: Enable pagination query
        # *   **false**: Pagination query is disabled
        self.enable_page = enable_page
        # The number of the page to return. The value must be greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The region ID of the disk.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The status of the CLB instance. Valid values:
        # 
        # *   **Available**: Normal
        # *   **Not Available**: Unavailable
        # *   **Executing**: Executing
        # *   **Deleting**: The node is being deleted.
        self.status = status
        # Lingjun subnet instance ID
        self.subnet_id = subnet_id
        # Lingjun subnet instance name
        self.subnet_name = subnet_name
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # Lingjun Subnet Usage Type; optional; optional. Valid values:
        # 
        # *   **If you do not set this field for a common type**
        # *   **OOB** :OOB type
        # *   **LB**: LB type
        self.type = type
        # The ID of the Lingjun CIDR block.
        self.vpd_id = vpd_id
        # The zone ID of the disk.
        self.zone_id = zone_id

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListSubnetsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListSubnetsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the VPN attachment.
        # 
        # You cannot specify an empty string as a tag key. It can be up to 64 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # You can specify at most 20 tag keys in each call.
        self.key = key
        # The tag value of the VPN connection.
        # 
        # The tag value can be empty or a string of up to 128 characters. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        # 
        # Each key-value pair must be unique. You can specify values for at most 20 tag keys in each call.
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

