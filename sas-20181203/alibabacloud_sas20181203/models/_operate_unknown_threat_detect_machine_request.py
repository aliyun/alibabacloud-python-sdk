# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperateUnknownThreatDetectMachineRequest(DaraModel):
    def __init__(
        self,
        operate_type: str = None,
        status: str = None,
        uuid_list: List[str] = None,
    ):
        # The operation type. Valid values:
        # 
        # - **restart_study**: Restarts the learning process.
        # 
        # - **increment_study**: Starts incremental learning.
        # 
        # - **change_status**: Changes the status.
        self.operate_type = operate_type
        # The target status. This parameter applies only when `OperateType` is set to `change_status`. Valid values:
        # 
        # - **monitoring**: Monitoring mode.
        # 
        # - **blocking**: Blocking mode.
        self.status = status
        # A list of server UUIDs.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

