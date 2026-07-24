# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartComputeInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
        selected_zones: str = None,
        service_version: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_name = instance_name
        # This parameter is required.
        self.region_id = region_id
        self.selected_zones = selected_zones
        self.service_version = service_version
        # This parameter is required.
        self.v_switch_ids = v_switch_ids
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.selected_zones is not None:
            result['SelectedZones'] = self.selected_zones

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SelectedZones') is not None:
            self.selected_zones = m.get('SelectedZones')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

