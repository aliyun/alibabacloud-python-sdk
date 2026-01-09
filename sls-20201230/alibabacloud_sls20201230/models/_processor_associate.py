# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProcessorAssociate(DaraModel):
    def __init__(
        self,
        processor_id: str = None,
    ):
        # This parameter is required.
        self.processor_id = processor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.processor_id is not None:
            result['processorId'] = self.processor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')

        return self

