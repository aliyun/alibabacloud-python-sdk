# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFileDetectReportRequest(DaraModel):
    def __init__(
        self,
        event_id: int = None,
        field: str = None,
        file_hash: str = None,
        lang: str = None,
        source_type: str = None,
    ):
        self.event_id = event_id
        self.field = field
        self.file_hash = file_hash
        self.lang = lang
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.field is not None:
            result['Field'] = self.field

        if self.file_hash is not None:
            result['FileHash'] = self.file_hash

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

