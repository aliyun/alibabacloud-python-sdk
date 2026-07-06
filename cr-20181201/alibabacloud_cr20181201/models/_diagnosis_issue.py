# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class DiagnosisIssue(DaraModel):
    def __init__(
        self,
        code: str = None,
        extra: Dict[str, str] = None,
        first_occurrence: str = None,
        last_occurrence: str = None,
        level: str = None,
        occurrence_count: int = None,
        solution: str = None,
    ):
        # A unique code that identifies the issue type.
        self.code = code
        # An object that contains additional, unstructured key-value information about the issue.
        self.extra = extra
        # The time, in ISO 8601 format, when the issue was first detected.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.first_occurrence = first_occurrence
        # The time, in ISO 8601 format, when the issue was last detected.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.last_occurrence = last_occurrence
        # Specifies the severity of the issue. Valid values are `INFO`, `WARN`, and `ERROR`.
        self.level = level
        # The total number of times the issue has occurred.
        self.occurrence_count = occurrence_count
        # The recommended action to resolve the issue.
        self.solution = solution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.first_occurrence is not None:
            result['FirstOccurrence'] = self.first_occurrence

        if self.last_occurrence is not None:
            result['LastOccurrence'] = self.last_occurrence

        if self.level is not None:
            result['Level'] = self.level

        if self.occurrence_count is not None:
            result['OccurrenceCount'] = self.occurrence_count

        if self.solution is not None:
            result['Solution'] = self.solution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('FirstOccurrence') is not None:
            self.first_occurrence = m.get('FirstOccurrence')

        if m.get('LastOccurrence') is not None:
            self.last_occurrence = m.get('LastOccurrence')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('OccurrenceCount') is not None:
            self.occurrence_count = m.get('OccurrenceCount')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        return self

