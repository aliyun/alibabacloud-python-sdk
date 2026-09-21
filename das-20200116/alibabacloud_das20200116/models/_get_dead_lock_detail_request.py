# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeadLockDetailRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
        source: str = None,
        text_id: str = None,
    ):
        # The ID of the database instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # > Required for PolarDB for MySQL cluster instances.
        self.node_id = node_id
        # The source of the analysis task:
        # 
        # - **MANUAL** or **not specified**: queries the recent deadlock analysis task.
        # 
        # - **AUTO**: queries the full deadlock analysis task.
        self.source = source
        # The ID of the deadlock text. This value is returned from the GetDeadLockHistory operation.
        # 
        # This parameter is required.
        self.text_id = text_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.source is not None:
            result['Source'] = self.source

        if self.text_id is not None:
            result['TextId'] = self.text_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TextId') is not None:
            self.text_id = m.get('TextId')

        return self

