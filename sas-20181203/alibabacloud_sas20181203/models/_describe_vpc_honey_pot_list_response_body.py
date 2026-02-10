# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcHoneyPotListResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeVpcHoneyPotListResponseBodyPageInfo = None,
        request_id: str = None,
        vpc_honey_pot_dtolist: List[main_models.DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOList] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the honeypots.
        self.vpc_honey_pot_dtolist = vpc_honey_pot_dtolist

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.vpc_honey_pot_dtolist:
            for v1 in self.vpc_honey_pot_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VpcHoneyPotDTOList'] = []
        if self.vpc_honey_pot_dtolist is not None:
            for k1 in self.vpc_honey_pot_dtolist:
                result['VpcHoneyPotDTOList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeVpcHoneyPotListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vpc_honey_pot_dtolist = []
        if m.get('VpcHoneyPotDTOList') is not None:
            for k1 in m.get('VpcHoneyPotDTOList'):
                temp_model = main_models.DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOList()
                self.vpc_honey_pot_dtolist.append(temp_model.from_map(k1))

        return self

class DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOList(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        create_time: int = None,
        honey_pot_ecs_instance_status: str = None,
        honey_pot_eni_instance_id: str = None,
        honey_pot_existence: bool = None,
        honey_pot_instance_status: str = None,
        honey_pot_vpc_switch_id: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_region_id: str = None,
        vpc_status: str = None,
        vpc_switch_id_list: List[main_models.DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOListVpcSwitchIdList] = None,
    ):
        # The CIDR block of the VPC.
        self.cidr_block = cidr_block
        # The time at which the VPC was created. Unit: milliseconds.
        self.create_time = create_time
        # The status of the server on which the honeypot is deployed. Valid values:
        # 
        # *   **Pending**: The server is being created.
        # *   **Running**: The server is running.
        # *   **Starting**: The server is being started.
        # *   **Stopping**: The server is being stopped.
        # *   **Stopped**: The server is stopped.
        self.honey_pot_ecs_instance_status = honey_pot_ecs_instance_status
        # The ID of the elastic network interface (ENI) used by the honeypot in the VPC.
        self.honey_pot_eni_instance_id = honey_pot_eni_instance_id
        # Indicates whether the cloud honeypot feature is enabled for the VPC. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.honey_pot_existence = honey_pot_existence
        # The status of the honeypot. Valid values:
        # 
        # *   **pending**: The honeypot is being created.
        # *   **deleting**: The honeypot is being deleted.
        # *   **off**: The honeypot is disabled.
        # *   **suspending**: The honeypot is suspended.
        # *   **on**: The honeypot is enabled.
        self.honey_pot_instance_status = honey_pot_instance_status
        # The ID of the vSwitch to which the ENI used by the honeypot is connected.
        self.honey_pot_vpc_switch_id = honey_pot_vpc_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name
        # The region ID of the VPC.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.vpc_region_id = vpc_region_id
        # The status of the VPC. Valid values:
        # 
        # *   **Available**: The VPC is normal and available.
        # *   **Pending**: The VPC is being configured.
        self.vpc_status = vpc_status
        # An array that consists of the vSwitches in the VPC.
        self.vpc_switch_id_list = vpc_switch_id_list

    def validate(self):
        if self.vpc_switch_id_list:
            for v1 in self.vpc_switch_id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.honey_pot_ecs_instance_status is not None:
            result['HoneyPotEcsInstanceStatus'] = self.honey_pot_ecs_instance_status

        if self.honey_pot_eni_instance_id is not None:
            result['HoneyPotEniInstanceId'] = self.honey_pot_eni_instance_id

        if self.honey_pot_existence is not None:
            result['HoneyPotExistence'] = self.honey_pot_existence

        if self.honey_pot_instance_status is not None:
            result['HoneyPotInstanceStatus'] = self.honey_pot_instance_status

        if self.honey_pot_vpc_switch_id is not None:
            result['HoneyPotVpcSwitchId'] = self.honey_pot_vpc_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        if self.vpc_status is not None:
            result['VpcStatus'] = self.vpc_status

        result['VpcSwitchIdList'] = []
        if self.vpc_switch_id_list is not None:
            for k1 in self.vpc_switch_id_list:
                result['VpcSwitchIdList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('HoneyPotEcsInstanceStatus') is not None:
            self.honey_pot_ecs_instance_status = m.get('HoneyPotEcsInstanceStatus')

        if m.get('HoneyPotEniInstanceId') is not None:
            self.honey_pot_eni_instance_id = m.get('HoneyPotEniInstanceId')

        if m.get('HoneyPotExistence') is not None:
            self.honey_pot_existence = m.get('HoneyPotExistence')

        if m.get('HoneyPotInstanceStatus') is not None:
            self.honey_pot_instance_status = m.get('HoneyPotInstanceStatus')

        if m.get('HoneyPotVpcSwitchId') is not None:
            self.honey_pot_vpc_switch_id = m.get('HoneyPotVpcSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        if m.get('VpcStatus') is not None:
            self.vpc_status = m.get('VpcStatus')

        self.vpc_switch_id_list = []
        if m.get('VpcSwitchIdList') is not None:
            for k1 in m.get('VpcSwitchIdList'):
                temp_model = main_models.DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOListVpcSwitchIdList()
                self.vpc_switch_id_list.append(temp_model.from_map(k1))

        return self

class DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOListVpcSwitchIdList(DaraModel):
    def __init__(
        self,
        vpc_switch_id: str = None,
        vpc_switch_name: str = None,
        zone_id: str = None,
    ):
        # The ID of the vSwitch.
        self.vpc_switch_id = vpc_switch_id
        # The name of the vSwitch.
        self.vpc_switch_name = vpc_switch_name
        # The zone ID of the vSwitch.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_switch_id is not None:
            result['VpcSwitchId'] = self.vpc_switch_id

        if self.vpc_switch_name is not None:
            result['VpcSwitchName'] = self.vpc_switch_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcSwitchId') is not None:
            self.vpc_switch_id = m.get('VpcSwitchId')

        if m.get('VpcSwitchName') is not None:
            self.vpc_switch_name = m.get('VpcSwitchName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeVpcHoneyPotListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

