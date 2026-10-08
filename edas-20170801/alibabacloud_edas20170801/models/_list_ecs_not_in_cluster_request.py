# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEcsNotInClusterRequest(DaraModel):
    def __init__(
        self,
        network_mode: int = None,
        vpc_id: str = None,
    ):
        # The network type. Valid values:
        # 
        # - 1: classic network
        # 
        # - 2: virtual private cloud (VPC)
        # 
        # This parameter is required.
        self.network_mode = network_mode
        # The ID of the VPC. This parameter is required if the NetworkMode parameter is set to 2.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

