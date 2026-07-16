# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateOnceTaskRequest(DaraModel):
    def __init__(
        self,
        param: str = None,
        source: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # A JSON string that contains additional parameters for the task.
        # 
        # This parameter is required.
        self.param = param
        # The source that initiated the task.
        self.source = source
        # The name of the scan task.
        # 
        # -
        # 
        # -
        # 
        # -
        # 
        # -
        # 
        # -
        # 
        # -
        # 
        # -
        # 
        # -
        # 
        # -
        # 
        # -
        # 
        # This parameter is required.
        self.task_name = task_name
        # The type of the scan task. Valid values:
        # 
        # - **CLIENT_PROBLEM_CHECK**: a client troubleshooting task
        # 
        # - **CLIENT_DEV_OPS**: a cloud DevOps task
        # 
        # - **ASSET_SECURITY_CHECK**: an asset collection task
        # 
        # - **ASSETS_COLLECTION**: an asset fingerprinting task
        # 
        # - **IMAGE_SCAN**: a container image scan task
        # 
        # - **AI_SECURITY_CHECK**: an AI asset synchronization task
        # 
        # - **IDC_PROBE_SCAN**: an IDC probe scan task
        # 
        # - **ATTACK_SURFACE_SCAN**: an attack surface scan task
        # 
        # - **ASSET_EXPOSURE_SCAN**: an asset exposure scan task
        # 
        # - **VUL_CHECK_TASK**: a vulnerability scan task
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param is not None:
            result['Param'] = self.param

        if self.source is not None:
            result['Source'] = self.source

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

