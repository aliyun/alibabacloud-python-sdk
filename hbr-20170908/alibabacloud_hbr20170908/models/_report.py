# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Report(DaraModel):
    def __init__(
        self,
        failed_files: str = None,
        skipped_files: str = None,
        success_files: str = None,
        total_files: str = None,
    ):
        self.failed_files = failed_files
        self.skipped_files = skipped_files
        self.success_files = success_files
        self.total_files = total_files

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_files is not None:
            result['FailedFiles'] = self.failed_files

        if self.skipped_files is not None:
            result['SkippedFiles'] = self.skipped_files

        if self.success_files is not None:
            result['SuccessFiles'] = self.success_files

        if self.total_files is not None:
            result['TotalFiles'] = self.total_files

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedFiles') is not None:
            self.failed_files = m.get('FailedFiles')

        if m.get('SkippedFiles') is not None:
            self.skipped_files = m.get('SkippedFiles')

        if m.get('SuccessFiles') is not None:
            self.success_files = m.get('SuccessFiles')

        if m.get('TotalFiles') is not None:
            self.total_files = m.get('TotalFiles')

        return self

