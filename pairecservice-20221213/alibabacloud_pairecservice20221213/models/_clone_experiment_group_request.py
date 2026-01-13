# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneExperimentGroupRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        layer_id: str = None,
    ):
        # This parameter is required.
        self.environment = environment
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.layer_id = layer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.layer_id is not None:
            result['LayerId'] = self.layer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')

        return self

