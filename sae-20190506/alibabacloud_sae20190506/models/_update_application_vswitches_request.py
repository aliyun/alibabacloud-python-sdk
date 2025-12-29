# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationVswitchesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        deploy: bool = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        v_switch_id: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        self.deploy = deploy
        self.min_ready_instance_ratio = min_ready_instance_ratio
        self.min_ready_instances = min_ready_instances
        # The ID of the vSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.deploy is not None:
            result['Deploy'] = self.deploy

        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')

        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')

        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

