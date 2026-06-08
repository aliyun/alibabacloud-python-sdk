# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackInstanceRequest(DaraModel):
    def __init__(
        self,
        output_option: str = None,
        region_id: str = None,
        stack_group_name: str = None,
        stack_instance_account_id: str = None,
        stack_instance_region_id: str = None,
    ):
        # Specifies whether to return the Outputs parameter. The Outputs parameter specifies the outputs of the stack. Valid values:
        # 
        # *   Enabled: returns the Outputs parameter.
        # *   Disabled (default): does not return the Outputs parameter.
        # 
        # >  The Outputs parameter requires a long period of time to calculate. If you do not require the outputs of the stack, we recommend that you set OutputOption to Disabled to improve the response speed of the API operation.
        self.output_option = output_option
        # The region ID of the stack group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the stack group. The name must be unique within a region.\\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or letter.
        # 
        # This parameter is required.
        self.stack_group_name = stack_group_name
        # The ID of the destination account to which the stack belongs.
        # 
        # *   If the stack group is granted self-managed permissions, the stack belongs to an Alibaba Cloud account.
        # *   If the stack group is granted service-managed permissions, the stack belongs to a member in a resource directory.
        # 
        # > For more information about the destination account, see [Overview](https://help.aliyun.com/document_detail/154578.html).
        # 
        # This parameter is required.
        self.stack_instance_account_id = stack_instance_account_id
        # The region ID of the stack.
        # 
        # This parameter is required.
        self.stack_instance_region_id = stack_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_option is not None:
            result['OutputOption'] = self.output_option

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.stack_instance_account_id is not None:
            result['StackInstanceAccountId'] = self.stack_instance_account_id

        if self.stack_instance_region_id is not None:
            result['StackInstanceRegionId'] = self.stack_instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputOption') is not None:
            self.output_option = m.get('OutputOption')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = m.get('StackInstanceAccountId')

        if m.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = m.get('StackInstanceRegionId')

        return self

