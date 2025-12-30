# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeSupportLinesResponseBody(DaraModel):
    def __init__(
        self,
        record_lines: main_models.DescribeSupportLinesResponseBodyRecordLines = None,
        request_id: str = None,
    ):
        # The Alibaba Cloud DNS lines.
        self.record_lines = record_lines
        self.request_id = request_id

    def validate(self):
        if self.record_lines:
            self.record_lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_lines is not None:
            result['RecordLines'] = self.record_lines.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordLines') is not None:
            temp_model = main_models.DescribeSupportLinesResponseBodyRecordLines()
            self.record_lines = temp_model.from_map(m.get('RecordLines'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSupportLinesResponseBodyRecordLines(DaraModel):
    def __init__(
        self,
        record_line: List[main_models.DescribeSupportLinesResponseBodyRecordLinesRecordLine] = None,
    ):
        self.record_line = record_line

    def validate(self):
        if self.record_line:
            for v1 in self.record_line:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordLine'] = []
        if self.record_line is not None:
            for k1 in self.record_line:
                result['RecordLine'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_line = []
        if m.get('RecordLine') is not None:
            for k1 in m.get('RecordLine'):
                temp_model = main_models.DescribeSupportLinesResponseBodyRecordLinesRecordLine()
                self.record_line.append(temp_model.from_map(k1))

        return self

class DescribeSupportLinesResponseBodyRecordLinesRecordLine(DaraModel):
    def __init__(
        self,
        father_code: str = None,
        line_code: str = None,
        line_display_name: str = None,
        line_name: str = None,
    ):
        # The code of the parent line. Currently, no data is returned.
        self.father_code = father_code
        # The code of the child line.
        self.line_code = line_code
        # The display name of the line.
        self.line_display_name = line_display_name
        # The name of the child line.
        self.line_name = line_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.father_code is not None:
            result['FatherCode'] = self.father_code

        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.line_display_name is not None:
            result['LineDisplayName'] = self.line_display_name

        if self.line_name is not None:
            result['LineName'] = self.line_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')

        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('LineDisplayName') is not None:
            self.line_display_name = m.get('LineDisplayName')

        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')

        return self

