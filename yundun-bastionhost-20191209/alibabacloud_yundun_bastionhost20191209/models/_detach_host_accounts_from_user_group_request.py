# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachHostAccountsFromUserGroupRequest(DaraModel):
    def __init__(
        self,
        hosts: str = None,
        instance_id: str = None,
        project_id: int = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The host IDs and host account IDs that you want to remove from the user group.  
        # You can specify up to 10 host IDs, and each host supports up to 10 host account IDs. You do not need to specify host account IDs. If you do not specify host account IDs, the authorized host and all authorized host accounts of the host are removed from the user group. For the specific structure of this parameter, see the Hosts parameter structure description below the request parameters list.
        # > You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query host IDs and call the [ListHostAccounts](https://help.aliyun.com/document_detail/204372.html) operation to query host account IDs.
        # 
        # This parameter is required.
        self.hosts = hosts
        # The instance ID of the bastion host where the user group from which you want to remove authorization for hosts and host accounts resides.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The project ID.
        self.project_id = project_id
        # The region ID of the bastion host instance where the user group from which you want to remove authorized hosts and host accounts resides.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the user group from which you want to remove authorized hosts and host accounts.
        # > You can call the [ListUserGroups](https://help.aliyun.com/document_detail/204509.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hosts is not None:
            result['Hosts'] = self.hosts

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

