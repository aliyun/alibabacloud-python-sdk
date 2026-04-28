# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        # The state of the task.
        # 
        # Valid values:
        # 
        # *   running
        # 
        #     <!-- -->
        # 
        #     : The task is
        # 
        #     <!-- -->
        # 
        #     running
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   failed
        # 
        #     <!-- -->
        # 
        #     : The task
        # 
        #     <!-- -->
        # 
        #     fails
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   succeeded
        # 
        #     <!-- -->
        # 
        #     : The task is
        # 
        #     <!-- -->
        # 
        #     successful
        # 
        #     <!-- -->
        # 
        #     .
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        return self

