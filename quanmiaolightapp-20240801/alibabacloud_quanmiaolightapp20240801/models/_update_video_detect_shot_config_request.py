# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVideoDetectShotConfigRequest(DaraModel):
    def __init__(
        self,
        async_concurrency: int = None,
    ):
        # This parameter is required.
        self.async_concurrency = async_concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_concurrency is not None:
            result['asyncConcurrency'] = self.async_concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncConcurrency') is not None:
            self.async_concurrency = m.get('asyncConcurrency')

        return self

