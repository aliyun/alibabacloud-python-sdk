# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelArtifactBuildTaskRequest(DaraModel):
    def __init__(
        self,
        build_task_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the artifact building task.
        # 
        # This parameter is required.
        self.build_task_id = build_task_id
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
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

