# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportReversedDeductionHistoryRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        export_uid: int = None,
        language: str = None,
        start_date: str = None,
    ):
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.export_uid = export_uid
        self.language = language
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.export_uid is not None:
            result['ExportUid'] = self.export_uid

        if self.language is not None:
            result['Language'] = self.language

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExportUid') is not None:
            self.export_uid = m.get('ExportUid')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

