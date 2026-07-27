# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceStorageConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        client_token: str = None,
        config_list_shrink: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.branch_name = branch_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, which ensures that the request is not repeated.
        self.client_token = client_token
        # The list of storage configurations.
        self.config_list_shrink = config_list_shrink
        # The instance ID of the AI application.
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
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_list_shrink is not None:
            result['ConfigList'] = self.config_list_shrink

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigList') is not None:
            self.config_list_shrink = m.get('ConfigList')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

