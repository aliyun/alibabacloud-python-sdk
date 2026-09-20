# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMultiZoneClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        immediate_delete_flag: bool = None,
    ):
        # The ID of the multi-zone cluster to delete.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to immediately delete the instance. By default, the instance is moved to the recycle bin and permanently deleted after 7 days. Valid values:
        # - true: Immediately deletes the instance without moving it to the recycle bin. Use this option with caution.
        # - false: Moves the instance to the recycle bin. This is the default value.
        self.immediate_delete_flag = immediate_delete_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.immediate_delete_flag is not None:
            result['ImmediateDeleteFlag'] = self.immediate_delete_flag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ImmediateDeleteFlag') is not None:
            self.immediate_delete_flag = m.get('ImmediateDeleteFlag')

        return self

