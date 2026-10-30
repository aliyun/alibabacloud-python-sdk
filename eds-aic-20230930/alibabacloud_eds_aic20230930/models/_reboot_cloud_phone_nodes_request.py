# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RebootCloudPhoneNodesRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        node_ids: List[str] = None,
    ):
        # Specifies whether to force a restart. Valid values:
        # - true: Forces a restart without waiting for the instances to gracefully exit.
        # - false: Performs a graceful restart.
        # Default value: false.
        self.force = force
        # The IDs of the cloud phone matrices. Valid values of N: 1 to 100.
        self.node_ids = node_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        return self

