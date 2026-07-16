# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceRecordRequest(DaraModel):
    def __init__(
        self,
        record_content: str = None,
        record_type: str = None,
    ):
        # The entry content in JSON string format. The format may vary depending on the value of recordType.
        # 
        # This parameter is required.
        self.record_content = record_content
        # The type of the linked entry. Valid values:
        # - logCorrelation: application log association.
        # 
        # This parameter is required.
        self.record_type = record_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_content is not None:
            result['recordContent'] = self.record_content

        if self.record_type is not None:
            result['recordType'] = self.record_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordContent') is not None:
            self.record_content = m.get('recordContent')

        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')

        return self

