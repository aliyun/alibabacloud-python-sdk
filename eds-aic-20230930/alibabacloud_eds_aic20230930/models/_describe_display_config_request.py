# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDisplayConfigRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
    ):
        self.android_instance_ids = android_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        return self

