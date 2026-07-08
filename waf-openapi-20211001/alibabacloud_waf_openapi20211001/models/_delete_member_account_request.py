# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMemberAccountRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        member_account_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        source_ip: str = None,
    ):
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the member account that you want to delete from WAF.
        # 
        # This parameter is required.
        self.member_account_id = member_account_id
        # The region in which the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the resource group to which the WAF instance belongs.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The source IP address of the request. You do not need to specify this parameter. The system automatically obtains this value.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_account_id is not None:
            result['MemberAccountId'] = self.member_account_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberAccountId') is not None:
            self.member_account_id = m.get('MemberAccountId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

