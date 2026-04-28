# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConsumerRequest(DaraModel):
    def __init__(
        self,
        consumer_group_name: str = None,
        gw_cluster_id: str = None,
        key_type: str = None,
        name: str = None,
        nick_name: str = None,
        region_id: str = None,
    ):
        self.consumer_group_name = consumer_group_name
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.key_type = key_type
        # This parameter is required.
        self.name = name
        self.nick_name = nick_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.name is not None:
            result['Name'] = self.name

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

