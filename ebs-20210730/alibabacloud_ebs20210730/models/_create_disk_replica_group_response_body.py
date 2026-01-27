# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDiskReplicaGroupResponseBody(DaraModel):
    def __init__(
        self,
        replica_group_id: str = None,
        request_id: str = None,
    ):
        # The ID of the replication pair-consistent group.
        self.replica_group_id = replica_group_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

