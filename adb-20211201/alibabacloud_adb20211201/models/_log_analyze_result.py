# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LogAnalyzeResult(DaraModel):
    def __init__(
        self,
        app_error_advice: str = None,
        app_error_code: str = None,
        app_error_log: str = None,
    ):
        self.app_error_advice = app_error_advice
        self.app_error_code = app_error_code
        self.app_error_log = app_error_log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_error_advice is not None:
            result['AppErrorAdvice'] = self.app_error_advice

        if self.app_error_code is not None:
            result['AppErrorCode'] = self.app_error_code

        if self.app_error_log is not None:
            result['AppErrorLog'] = self.app_error_log

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppErrorAdvice') is not None:
            self.app_error_advice = m.get('AppErrorAdvice')

        if m.get('AppErrorCode') is not None:
            self.app_error_code = m.get('AppErrorCode')

        if m.get('AppErrorLog') is not None:
            self.app_error_log = m.get('AppErrorLog')

        return self

