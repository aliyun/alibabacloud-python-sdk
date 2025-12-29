# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateVerifySettingResponseBody(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        biz_type: str = None,
        request_id: str = None,
        solution: str = None,
        step_list: List[str] = None,
    ):
        # Verification scenario name.
        self.biz_name = biz_name
        # Verification scenario identifier.
        self.biz_type = biz_type
        # ID of this request.
        self.request_id = request_id
        # Authentication solution name.
        self.solution = solution
        # Authentication steps
        self.step_list = step_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.step_list is not None:
            result['StepList'] = self.step_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')

        return self

