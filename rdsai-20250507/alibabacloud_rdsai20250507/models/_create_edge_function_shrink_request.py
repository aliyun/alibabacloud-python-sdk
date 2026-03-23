# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEdgeFunctionShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        code_shrink: str = None,
        custom_config_shrink: str = None,
        edge_function_name: str = None,
        envs_shrink: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The code parameters.
        self.code_shrink = code_shrink
        # The configuration parameters of the edge function.
        self.custom_config_shrink = custom_config_shrink
        # The name of the function.
        self.edge_function_name = edge_function_name
        # The environment variables.
        self.envs_shrink = envs_shrink
        # The ID of the RDS Supabase instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.code_shrink is not None:
            result['Code'] = self.code_shrink

        if self.custom_config_shrink is not None:
            result['CustomConfig'] = self.custom_config_shrink

        if self.edge_function_name is not None:
            result['EdgeFunctionName'] = self.edge_function_name

        if self.envs_shrink is not None:
            result['Envs'] = self.envs_shrink

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Code') is not None:
            self.code_shrink = m.get('Code')

        if m.get('CustomConfig') is not None:
            self.custom_config_shrink = m.get('CustomConfig')

        if m.get('EdgeFunctionName') is not None:
            self.edge_function_name = m.get('EdgeFunctionName')

        if m.get('Envs') is not None:
            self.envs_shrink = m.get('Envs')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

