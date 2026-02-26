# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDBInstanceReplicationRequest(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        db_instance_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # 复制通道名称，用于标识需要删除的复制链路
        self.channel_name = channel_name
        # 目标RDS实例ID，复制链路将从此实例上删除
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # 阿里云账号ID，用于指定资源的所有者
        self.owner_id = owner_id
        # 地域ID，表示RDS实例所在的地域
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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

