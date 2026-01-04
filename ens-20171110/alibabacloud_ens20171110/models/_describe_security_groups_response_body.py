# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        security_groups: main_models.DescribeSecurityGroupsResponseBodySecurityGroups = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Details about security groups.
        self.security_groups = security_groups
        # The total number of returned pages.
        self.total_count = total_count

    def validate(self):
        if self.security_groups:
            self.security_groups.validate()

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

        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroups') is not None:
            temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroups()
            self.security_groups = temp_model.from_map(m.get('SecurityGroups'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSecurityGroupsResponseBodySecurityGroups(DaraModel):
    def __init__(
        self,
        security_group: List[main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup] = None,
    ):
        self.security_group = security_group

    def validate(self):
        if self.security_group:
            for v1 in self.security_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecurityGroup'] = []
        if self.security_group is not None:
            for k1 in self.security_group:
                result['SecurityGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_group = []
        if m.get('SecurityGroup') is not None:
            for k1 in m.get('SecurityGroup'):
                temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup()
                self.security_group.append(temp_model.from_map(k1))

        return self

class DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        instance_count: int = None,
        instance_ids: main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupInstanceIds = None,
        network_interface_ids: main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupNetworkInterfaceIds = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        # The creation time. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the security group.
        self.description = description
        # The number of associated instances.
        self.instance_count = instance_count
        # The IDs of the instances that are associated with the security group.
        self.instance_ids = instance_ids
        # The IDs of the ENIs that are associated with the security group.
        self.network_interface_ids = network_interface_ids
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The name of the security group.
        self.security_group_name = security_group_name

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()
        if self.network_interface_ids:
            self.network_interface_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()

        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceIds') is not None:
            temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupInstanceIds()
            self.instance_ids = temp_model.from_map(m.get('InstanceIds'))

        if m.get('NetworkInterfaceIds') is not None:
            temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupNetworkInterfaceIds()
            self.network_interface_ids = temp_model.from_map(m.get('NetworkInterfaceIds'))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

class DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupNetworkInterfaceIds(DaraModel):
    def __init__(
        self,
        network_interface_id: List[str] = None,
    ):
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        return self

class DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupInstanceIds(DaraModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

