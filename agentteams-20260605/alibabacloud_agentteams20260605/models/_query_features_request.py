# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryFeaturesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_name: str = None,
        target_scope: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.resource_name = resource_name
        # This parameter is required.
        self.target_scope = target_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.target_scope is not None:
            result['TargetScope'] = self.target_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('TargetScope') is not None:
            self.target_scope = m.get('TargetScope')

        return self

