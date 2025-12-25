# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RedeployRCInstanceRequest(DaraModel):
    def __init__(
        self,
        force_stop: bool = None,
        instance_id: str = None,
    ):
        # Specifies whether to forcefully stop the instance that is in the Running state. Default value: false.
        # 
        # >  A forced stop is equivalent to the shutdown operation for a physical database server and can result in loss of data that is not written to storage devices. We recommend that you redeploy instances when they are in the Stopped state.
        self.force_stop = force_stop
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

