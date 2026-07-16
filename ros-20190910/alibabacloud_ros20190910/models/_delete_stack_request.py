# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteStackRequest(DaraModel):
    def __init__(
        self,
        delete_options: List[str] = None,
        parallelism: int = None,
        ram_role_name: str = None,
        region_id: str = None,
        retain_all_resources: bool = None,
        retain_resources: List[str] = None,
        stack_id: str = None,
    ):
        # The options for deleting the stack.
        self.delete_options = delete_options
        # The maximum number of concurrent operations that can be performed on resources.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # 
        # 
        # > -  If you set this parameter to an integer that is greater than 0, the integer is used. If you set this parameter to 0 or leave this parameter empty, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > -  If you set this parameter to a specific value, ROS associates the value with the stack. The value affects subsequent operations on the stack, such as an update operation.
        self.parallelism = parallelism
        # The name of the RAM role. Resource Orchestration Service (ROS) assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\\
        # ROS assumes the role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.\\
        # If you leave this parameter empty when you call the DeleteStack operation, ROS cannot assume the existing RAM role that is associated with the stack. If you want ROS to assume a RAM role, you must specify this parameter. If no RAM roles are available, ROS uses a temporary credential that is generated from the credentials of your account.\\
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to retain all resources in the stack.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.retain_all_resources = retain_all_resources
        # The resources that you want to retain.
        self.retain_resources = retain_resources
        # The ID of the stack.
        # 
        # This parameter is required.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_options is not None:
            result['DeleteOptions'] = self.delete_options

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retain_all_resources is not None:
            result['RetainAllResources'] = self.retain_all_resources

        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteOptions') is not None:
            self.delete_options = m.get('DeleteOptions')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RetainAllResources') is not None:
            self.retain_all_resources = m.get('RetainAllResources')

        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

