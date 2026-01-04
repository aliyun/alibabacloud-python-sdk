# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JoinVSwitchesToEpnInstanceRequest(DaraModel):
    def __init__(
        self,
        epninstance_id: str = None,
        v_switches_info: str = None,
    ):
        # The ID of the edge network instance.
        # 
        # This parameter is required.
        self.epninstance_id = epninstance_id
        # The information about the internal networking to which you want to add the edge network instance.
        # 
        # This parameter is required.
        self.v_switches_info = v_switches_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id

        if self.v_switches_info is not None:
            result['VSwitchesInfo'] = self.v_switches_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')

        if m.get('VSwitchesInfo') is not None:
            self.v_switches_info = m.get('VSwitchesInfo')

        return self

