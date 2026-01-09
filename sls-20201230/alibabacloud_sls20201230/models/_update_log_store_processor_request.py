# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLogStoreProcessorRequest(DaraModel):
    def __init__(
        self,
        processor_name: str = None,
    ):
        # The identifier of the ingest processor.
        # 
        # This parameter is required.
        self.processor_name = processor_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.processor_name is not None:
            result['processorName'] = self.processor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processorName') is not None:
            self.processor_name = m.get('processorName')

        return self

