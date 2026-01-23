# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoBuildRuleResponseBody(DaraModel):
    def __init__(
        self,
        build_rule_id: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The ID of the building rule.
        self.build_rule_id = build_rule_id
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

