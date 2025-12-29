# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifyResultRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
    ):
        # Authentication ID. A unique ID that identifies an authentication task, not exceeding 64 characters. For a single authentication task, the system supports an unlimited number of submissions until the final authentication is successful and the task is completed. > You need to use a different BizId for each new authentication task.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # Business scenario identifier for real-person authentication service
        # 
        # This parameter is required.
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        return self

