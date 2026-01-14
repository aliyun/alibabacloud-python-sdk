# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateVideoClipTaskRequest(DaraModel):
    def __init__(
        self,
        aliyun_main_id: str = None,
        description: str = None,
        oss_keys: List[str] = None,
        requirement: str = None,
    ):
        self.aliyun_main_id = aliyun_main_id
        self.description = description
        self.oss_keys = oss_keys
        self.requirement = requirement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_main_id is not None:
            result['aliyunMainId'] = self.aliyun_main_id

        if self.description is not None:
            result['description'] = self.description

        if self.oss_keys is not None:
            result['ossKeys'] = self.oss_keys

        if self.requirement is not None:
            result['requirement'] = self.requirement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunMainId') is not None:
            self.aliyun_main_id = m.get('aliyunMainId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('ossKeys') is not None:
            self.oss_keys = m.get('ossKeys')

        if m.get('requirement') is not None:
            self.requirement = m.get('requirement')

        return self

