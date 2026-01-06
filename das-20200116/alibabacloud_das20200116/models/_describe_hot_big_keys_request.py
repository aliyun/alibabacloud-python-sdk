# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHotBigKeysRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        node_id: str = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The ID of the ApsaraDB for Redis instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the data shard on the ApsaraDB for Redis instance.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

