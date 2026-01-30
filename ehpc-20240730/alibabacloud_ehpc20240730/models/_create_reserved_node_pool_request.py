# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReservedNodePoolRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        count: int = None,
        description: str = None,
        host_postfix: str = None,
        host_prefix: str = None,
        name: str = None,
        v_switch_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.count = count
        self.description = description
        self.host_postfix = host_postfix
        self.host_prefix = host_prefix
        self.name = name
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.count is not None:
            result['Count'] = self.count

        if self.description is not None:
            result['Description'] = self.description

        if self.host_postfix is not None:
            result['HostPostfix'] = self.host_postfix

        if self.host_prefix is not None:
            result['HostPrefix'] = self.host_prefix

        if self.name is not None:
            result['Name'] = self.name

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HostPostfix') is not None:
            self.host_postfix = m.get('HostPostfix')

        if m.get('HostPrefix') is not None:
            self.host_prefix = m.get('HostPrefix')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

