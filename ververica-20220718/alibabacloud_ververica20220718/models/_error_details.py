# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ErrorDetails(DaraModel):
    def __init__(
        self,
        column_number: str = None,
        end_column_number: str = None,
        end_line_number: str = None,
        invalidflink_conf: List[str] = None,
        line_number: str = None,
        message: str = None,
    ):
        # The number of the column at which the error starts.
        self.column_number = column_number
        # The number of the column at which the error ends.
        self.end_column_number = end_column_number
        # The number of the row at which the error ends.
        self.end_line_number = end_line_number
        # The list of invalid configurations of Realtime Compute for Apache Flink.
        self.invalidflink_conf = invalidflink_conf
        # The number the row at which the error starts.
        self.line_number = line_number
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_number is not None:
            result['columnNumber'] = self.column_number

        if self.end_column_number is not None:
            result['endColumnNumber'] = self.end_column_number

        if self.end_line_number is not None:
            result['endLineNumber'] = self.end_line_number

        if self.invalidflink_conf is not None:
            result['invalidflinkConf'] = self.invalidflink_conf

        if self.line_number is not None:
            result['lineNumber'] = self.line_number

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnNumber') is not None:
            self.column_number = m.get('columnNumber')

        if m.get('endColumnNumber') is not None:
            self.end_column_number = m.get('endColumnNumber')

        if m.get('endLineNumber') is not None:
            self.end_line_number = m.get('endLineNumber')

        if m.get('invalidflinkConf') is not None:
            self.invalidflink_conf = m.get('invalidflinkConf')

        if m.get('lineNumber') is not None:
            self.line_number = m.get('lineNumber')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

