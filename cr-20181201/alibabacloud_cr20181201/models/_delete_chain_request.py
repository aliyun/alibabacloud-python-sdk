# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteChainRequest(DaraModel):
    def __init__(
        self,
        chain_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the delivery pipeline.
        # 
        # This parameter is required.
        self.chain_id = chain_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

