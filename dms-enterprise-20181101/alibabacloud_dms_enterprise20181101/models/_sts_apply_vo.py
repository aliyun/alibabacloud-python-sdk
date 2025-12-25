# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StsApplyVO(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        duration: int = None,
    ):
        self.aliyun_id = aliyun_id
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

