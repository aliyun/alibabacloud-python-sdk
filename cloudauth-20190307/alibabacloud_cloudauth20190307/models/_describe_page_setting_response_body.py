# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DescribePageSettingResponseBody(DaraModel):
    def __init__(
        self,
        fail_reasons: Dict[str, Any] = None,
        request_id: str = None,
    ):
        # Failure reasons.
        self.fail_reasons = fail_reasons
        # The ID of this request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_reasons is not None:
            result['FailReasons'] = self.fail_reasons

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailReasons') is not None:
            self.fail_reasons = m.get('FailReasons')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

