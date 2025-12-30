# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckZoneNameResponseBody(DaraModel):
    def __init__(
        self,
        check: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Indicates whether the zone name can be added. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.check = check
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check is not None:
            result['Check'] = self.check

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check') is not None:
            self.check = m.get('Check')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

