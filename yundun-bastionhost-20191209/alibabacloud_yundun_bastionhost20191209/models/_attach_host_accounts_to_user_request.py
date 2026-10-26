# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachHostAccountsToUserRequest(DaraModel):
    def __init__(
        self,
        hosts: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The IDs of the hosts and host accounts to be authorized for the user. You can specify up to 10 host IDs, and up to 9 host account IDs for each host. If you do not specify host account IDs, only the hosts are authorized for the user. For more information about the structure of this parameter, see the Hosts parameter structure description in the request parameters section.
        # > You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query host IDs and call the [ListHostAccounts](https://help.aliyun.com/document_detail/204372.html) operation to query host account IDs.
        # 
        # This parameter is required.
        self.hosts = hosts
        # The instance ID of the Bastionhost instance to which the user to be granted authorization for hosts and host accounts belongs.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the Bastionhost instance where the user to be authorized for hosts and host accounts resides.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the user to whom you want to authorize hosts and host accounts.
        # > You can call the [ListUsers](https://help.aliyun.com/document_detail/204522.html) operation to query the value of this parameter.
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
        if self.hosts is not None:
            result['Hosts'] = self.hosts

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

