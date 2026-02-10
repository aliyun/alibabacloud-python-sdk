# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSuspEventUserSettingResponseBody(DaraModel):
    def __init__(
        self,
        levels_on: List[str] = None,
        request_id: str = None,
    ):
        # An array that consists of the risk levels of alert notifications. Valid values:
        # 
        # *   **remind**
        # *   **suspicious**
        # *   **serious**
        self.levels_on = levels_on
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

