# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListVpdsRequest(DaraModel):
    def __init__(
        self,
        enable_page: bool = None,
        filter_er_id: str = None,
        for_select: bool = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[main_models.ListVpdsRequestTag] = None,
        vpd_id: str = None,
        vpd_name: str = None,
        with_dependence: bool = None,
        without_vcc: bool = None,
    ):
        # Specifies whether to enable paged query.
        self.enable_page = enable_page
        # Queries the network segments of Lingjun that are not bound to a specified Lingjun HUB.
        self.filter_er_id = filter_er_id
        # If you select a drop-down list, only the basic information (including the instance ID and instance name) is returned. Possible values:
        # 
        # *   **true**: Select Query Use from the drop-down list.
        # *   **false**: Normal queries are used.
        self.for_select = for_select
        # The page number of the page to return. Start value: 1 Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The status of the CLB instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # The ID of the VPD instance.
        self.vpd_id = vpd_id
        # The name of the VPD instance.
        self.vpd_name = vpd_name
        # Specifies whether to include the dependent resource information. We recommend that you do not query the dependent resource information when you query by page. You can query the dependent resource information separately when you delete it. Possible values:
        # 
        # *   **true**: with dependency information.
        # *   **false**: does not include dependency information.
        self.with_dependence = with_dependence
        # Queries the information about a Lingjun CIDR block that is not bound to a Lingjun connection. Possible values:
        # 
        # *   **true**: filters out VPDs that have been bound to VCC
        # *   **false**: does not filter VPD that has been bound to VCC
        self.without_vcc = without_vcc

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

        if self.filter_er_id is not None:
            result['FilterErId'] = self.filter_er_id

        if self.for_select is not None:
            result['ForSelect'] = self.for_select

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

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name

        if self.with_dependence is not None:
            result['WithDependence'] = self.with_dependence

        if self.without_vcc is not None:
            result['WithoutVcc'] = self.without_vcc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('FilterErId') is not None:
            self.filter_er_id = m.get('FilterErId')

        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')

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
                temp_model = main_models.ListVpdsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')

        if m.get('WithDependence') is not None:
            self.with_dependence = m.get('WithDependence')

        if m.get('WithoutVcc') is not None:
            self.without_vcc = m.get('WithoutVcc')

        return self

class ListVpdsRequestTag(DaraModel):
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

