# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobRequest(DaraModel):
    def __init__(
        self,
        need_detail: bool = None,
    ):
        # Specifies whether to return the job details. Default value: true.
        self.need_detail = need_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_detail is not None:
            result['NeedDetail'] = self.need_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedDetail') is not None:
            self.need_detail = m.get('NeedDetail')

        return self

