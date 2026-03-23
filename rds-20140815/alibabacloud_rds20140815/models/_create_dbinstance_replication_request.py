# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBInstanceReplicationRequest(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        db_instance_id: str = None,
        master_host: str = None,
        master_password: str = None,
        master_port: int = None,
        master_user: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The name of the replication channel, used to identify the replication link.
        self.channel_name = channel_name
        # The instance ID. You can obtain it by invoking DescribeDBInstances.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # The host address of the master database, which can be an IP address or a domain name.
        # 
        # This parameter is required.
        self.master_host = master_host
        # The password of the master database, used to authenticate the replication user. It must be Base64-encoded in advance.
        # 
        # This parameter is required.
        self.master_password = master_password
        # The port number of the master database, typically 3306 for MySQL.
        # 
        # This parameter is required.
        self.master_port = master_port
        # The username of the master database, used to establish the replication connection.
        # 
        # This parameter is required.
        self.master_user = master_user
        # 阿里云账号ID，用于指定资源的所有者
        self.owner_id = owner_id
        # The ID of the Region where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.master_host is not None:
            result['MasterHost'] = self.master_host

        if self.master_password is not None:
            result['MasterPassword'] = self.master_password

        if self.master_port is not None:
            result['MasterPort'] = self.master_port

        if self.master_user is not None:
            result['MasterUser'] = self.master_user

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('MasterHost') is not None:
            self.master_host = m.get('MasterHost')

        if m.get('MasterPassword') is not None:
            self.master_password = m.get('MasterPassword')

        if m.get('MasterPort') is not None:
            self.master_port = m.get('MasterPort')

        if m.get('MasterUser') is not None:
            self.master_user = m.get('MasterUser')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

