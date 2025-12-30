# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RejectSolutionRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        note: str = None,
        solution_biz_id: str = None,
    ):
        self.biz_type = biz_type
        # This parameter is required.
        self.note = note
        # This parameter is required.
        self.solution_biz_id = solution_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.note is not None:
            result['Note'] = self.note

        if self.solution_biz_id is not None:
            result['SolutionBizId'] = self.solution_biz_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('SolutionBizId') is not None:
            self.solution_biz_id = m.get('SolutionBizId')

        return self

