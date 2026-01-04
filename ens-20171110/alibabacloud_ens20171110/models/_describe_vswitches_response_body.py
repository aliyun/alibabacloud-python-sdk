# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeVSwitchesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        v_switches: main_models.DescribeVSwitchesResponseBodyVSwitches = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the vSwitches. For more information, see the array of vSwitches in the response examples in the JSON format.
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VSwitches') is not None:
            temp_model = main_models.DescribeVSwitchesResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m.get('VSwitches'))

        return self

class DescribeVSwitchesResponseBodyVSwitches(DaraModel):
    def __init__(
        self,
        v_switch: List[main_models.DescribeVSwitchesResponseBodyVSwitchesVSwitch] = None,
    ):
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for v1 in self.v_switch:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k1 in self.v_switch:
                result['VSwitch'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k1 in m.get('VSwitch'):
                temp_model = main_models.DescribeVSwitchesResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k1))

        return self

class DescribeVSwitchesResponseBodyVSwitchesVSwitch(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        created_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        free_ip_count: int = None,
        network_id: str = None,
        status: str = None,
        tags: main_models.DescribeVSwitchesResponseBodyVSwitchesVSwitchTags = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        # The IPv4 CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The time when the VPC was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.created_time = created_time
        # The description of the vSwitch.
        self.description = description
        # The ID of the ENS node.
        self.ens_region_id = ens_region_id
        # The number of available IP addresses.
        self.free_ip_count = free_ip_count
        # The ID of the virtual private cloud (VPC).
        self.network_id = network_id
        # The status of the vSwitch. Valid values:
        # 
        # *   Pending
        # *   Available
        self.status = status
        self.tags = tags
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The name of the vSwitch.
        self.v_switch_name = v_switch_name

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.free_ip_count is not None:
            result['FreeIpCount'] = self.free_ip_count

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('FreeIpCount') is not None:
            self.free_ip_count = m.get('FreeIpCount')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVSwitchesResponseBodyVSwitchesVSwitchTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        return self

class DescribeVSwitchesResponseBodyVSwitchesVSwitchTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeVSwitchesResponseBodyVSwitchesVSwitchTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVSwitchesResponseBodyVSwitchesVSwitchTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVSwitchesResponseBodyVSwitchesVSwitchTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        self.tag_key = tag_key
        self.tag_value = tag_value
        # The request error rate.
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

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

