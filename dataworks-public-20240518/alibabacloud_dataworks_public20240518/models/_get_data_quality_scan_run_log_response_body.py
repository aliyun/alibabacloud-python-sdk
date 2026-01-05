# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDataQualityScanRunLogResponseBody(DaraModel):
    def __init__(
        self,
        log_segment: main_models.GetDataQualityScanRunLogResponseBodyLogSegment = None,
        request_id: str = None,
    ):
        # The task log information.
        self.log_segment = log_segment
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.log_segment:
            self.log_segment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_segment is not None:
            result['LogSegment'] = self.log_segment.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogSegment') is not None:
            temp_model = main_models.GetDataQualityScanRunLogResponseBodyLogSegment()
            self.log_segment = temp_model.from_map(m.get('LogSegment'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataQualityScanRunLogResponseBodyLogSegment(DaraModel):
    def __init__(
        self,
        log: str = None,
        next_offset: int = None,
    ):
        # The task log.
        self.log = log
        # The starting offset of the next log segment. A value of -1 indicates that all logs have been read.
        self.next_offset = next_offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log is not None:
            result['Log'] = self.log

        if self.next_offset is not None:
            result['NextOffset'] = self.next_offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Log') is not None:
            self.log = m.get('Log')

        if m.get('NextOffset') is not None:
            self.next_offset = m.get('NextOffset')

        return self

