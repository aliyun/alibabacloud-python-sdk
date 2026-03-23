# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeParameterTimedScheduleTaskRequest(DaraModel):
    def __init__(
        self,
        db_instance_name: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.db_instance_name = db_instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        return self

