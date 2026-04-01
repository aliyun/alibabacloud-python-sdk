# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeVSwitchesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        v_switchs: List[main_models.DescribeVSwitchesResponseBodyVSwitchs] = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page. The value of this parameter is the same as the value of the **PageSize** parameter in the request parameters.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count
        # Details of the vSwitches.
        self.v_switchs = v_switchs

    def validate(self):
        if self.v_switchs:
            for v1 in self.v_switchs:
                 if v1:
                    v1.validate()

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

        result['VSwitchs'] = []
        if self.v_switchs is not None:
            for k1 in self.v_switchs:
                result['VSwitchs'].append(k1.to_map() if k1 else None)

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

        self.v_switchs = []
        if m.get('VSwitchs') is not None:
            for k1 in m.get('VSwitchs'):
                temp_model = main_models.DescribeVSwitchesResponseBodyVSwitchs()
                self.v_switchs.append(temp_model.from_map(k1))

        return self

class DescribeVSwitchesResponseBodyVSwitchs(DaraModel):
    def __init__(
        self,
        available_ip_address_count: str = None,
        cidr_block: str = None,
        description: str = None,
        is_default: bool = None,
        iz_no: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        # The number of available IP addresses in the vSwitch.
        # 
        # This parameter is required.
        self.available_ip_address_count = available_ip_address_count
        # The CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The description of the vSwitch.
        self.description = description
        # Indicates whether the vSwitch is the default vSwitch. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_default = is_default
        # The ID of the zone to which the vSwitch belongs.
        self.iz_no = iz_no
        # The status of the vSwitch. Valid values:
        # 
        # *   **Pending**: The vSwitch is being specified.
        # *   **Available**: The vSwitch is available.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The vSwitch name.
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.iz_no is not None:
            result['IzNo'] = self.iz_no

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        return self

