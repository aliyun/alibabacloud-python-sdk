# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        error_lines_shrink: str = None,
        import_sequence: str = None,
        language: str = None,
        status: str = None,
        system_token: str = None,
    ):
        self.app_type = app_type
        self.error_lines_shrink = error_lines_shrink
        self.import_sequence = import_sequence
        self.language = language
        self.status = status
        self.system_token = system_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.error_lines_shrink is not None:
            result['ErrorLines'] = self.error_lines_shrink

        if self.import_sequence is not None:
            result['ImportSequence'] = self.import_sequence

        if self.language is not None:
            result['Language'] = self.language

        if self.status is not None:
            result['Status'] = self.status

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ErrorLines') is not None:
            self.error_lines_shrink = m.get('ErrorLines')

        if m.get('ImportSequence') is not None:
            self.import_sequence = m.get('ImportSequence')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

