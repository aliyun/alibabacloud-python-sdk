# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyStrategyTargetRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        source_ip: str = None,
        target: str = None,
        type: str = None,
    ):
        # The ID of the baseline check policy. The ID is returned after the policy is created. The value of this parameter is in the JSON format and contains the following field:
        # 
        # *   **strategyId**: the ID of the policy
        # 
        # This parameter is required.
        self.config = config
        # The source IP address of the request.
        self.source_ip = source_ip
        # The information about the asset group to which the policy is applied. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **TargetType**: the type of the asset to which the policy is applied. Set the value to **groupId**, which indicates that the policy is applied to an asset group.
        # *   **BindUuidCount**: the number of servers to which the policy is applied.
        # *   **Target**: the ID of the asset group.
        # 
        # This parameter is required.
        self.target = target
        # The type of the configuration. Set the value to **hc_strategy**.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

