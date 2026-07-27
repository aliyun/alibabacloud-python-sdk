# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        client_token: str = None,
        components_shrink: str = None,
        dbinstance_name: str = None,
        instance_class: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.branch_name = branch_name
        self.client_token = client_token
        self.components_shrink = components_shrink
        self.dbinstance_name = dbinstance_name
        self.instance_class = instance_class
        self.instance_name = instance_name
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

        if self.components_shrink is not None:
            result['Components'] = self.components_shrink

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

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

        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

