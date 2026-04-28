# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConsumerGroupRequest(DaraModel):
    def __init__(
        self,
        consumer_group_name: str = None,
        gw_cluster_id: str = None,
        is_default: str = None,
        nick_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.consumer_group_name = consumer_group_name
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.is_default = is_default
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

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

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

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

