# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachHostGroupAccountsToUserRequest(DaraModel):
    def __init__(
        self,
        host_groups: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The IDs of the host groups and the names of the host accounts to which you want to grant the user access. You can specify up to 10 host group IDs and up to 10 host account names for each host group. If you do not specify host account names, the user is granted access only to the host groups. For more information about the structure of this parameter, see the HostGroups parameter structure description in the request parameter list.
        # > You can call the [ListHostGroups](https://help.aliyun.com/document_detail/201307.html) operation to obtain host group IDs and call the [ListHostAccounts](https://help.aliyun.com/document_detail/204372.html) operation to obtain host account names.
        # 
        # This parameter is required.
        self.host_groups = host_groups
        # The instance ID of the Bastionhost instance to which the user to be granted authorization on host groups and host accounts belongs.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies the region ID of the Bastionhost instance where the user to be granted permissions on host groups and host accounts is located.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the user to be granted permissions on host groups and host accounts.
        # > You can call the [ListUsers](https://help.aliyun.com/document_detail/204522.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

