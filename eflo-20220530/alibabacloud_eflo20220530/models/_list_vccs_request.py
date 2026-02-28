# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListVccsRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        cen_id: str = None,
        enable_page: bool = None,
        ex_status: str = None,
        filter_er_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[main_models.ListVccsRequestTag] = None,
        vcc_id: str = None,
        vpc_id: str = None,
        vpd_id: str = None,
    ):
        # The peak bandwidth of the Lingjun connection instance. Unit: Mbit/s. Valid values: 1000 to 400000
        self.bandwidth = bandwidth
        # The ID of the CEN instance; [What is the CEN?](https://help.aliyun.com/document_detail/181681.html)
        # 
        # You can call the [DescribeCens](https://help.aliyun.com/document_detail/468215.htm) to query the information of CEN instances under the current Alibaba Cloud account.
        self.cen_id = cen_id
        # Specifies whether to enable paged query. Optional values:
        # 
        # *   **true**: Enable pagination query
        # *   **false**: Pagination query is disabled
        self.enable_page = enable_page
        # Excludes all data in the specified status. If the status parameter exists, ExStatus does not take effect.
        self.ex_status = ex_status
        # Filter queries by Lingjun HUB instance ID
        self.filter_er_id = filter_er_id
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The instance status.
        self.status = status
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # Virtual Private Cloud IDs; [What is Virtual Private Cloud](https://help.aliyun.com/document_detail/34217.html)
        # 
        # You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html#demo-0) operation to query the specified VPC.
        self.vpc_id = vpc_id
        # Lingjun CIDR block instance ID
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
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page

        if self.ex_status is not None:
            result['ExStatus'] = self.ex_status

        if self.filter_er_id is not None:
            result['FilterErId'] = self.filter_er_id

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('ExStatus') is not None:
            self.ex_status = m.get('ExStatus')

        if m.get('FilterErId') is not None:
            self.filter_er_id = m.get('FilterErId')

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListVccsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        return self

class ListVccsRequestTag(DaraModel):
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

