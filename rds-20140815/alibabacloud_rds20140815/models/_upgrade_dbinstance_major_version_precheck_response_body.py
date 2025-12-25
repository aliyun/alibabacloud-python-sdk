# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBInstanceMajorVersionPrecheckResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        request_id: str = None,
        target_major_version: str = None,
        task_id: str = None,
    ):
        # The instance name.
        self.dbinstance_name = dbinstance_name
        # The request ID.
        self.request_id = request_id
        # The new major engine version of the instance.
        self.target_major_version = target_major_version
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.target_major_version is not None:
            result['TargetMajorVersion'] = self.target_major_version

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TargetMajorVersion') is not None:
            self.target_major_version = m.get('TargetMajorVersion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

