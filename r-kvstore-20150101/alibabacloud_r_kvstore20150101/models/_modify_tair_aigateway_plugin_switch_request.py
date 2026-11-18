# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTairAIGatewayPluginSwitchRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        parameters: str = None,
        region_id: str = None,
        security_token: str = None,
    ):
        # The Tair AI gateway instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The plug-in switch parameters for the Tair AI gateway instance. Format: {"PluginName1":"true/false","PluginName2":"true/false",...}. The specified values overwrite the existing values.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

