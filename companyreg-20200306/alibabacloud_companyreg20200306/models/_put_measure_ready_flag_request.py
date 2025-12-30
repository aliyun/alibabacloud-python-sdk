# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutMeasureReadyFlagRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        data_type: str = None,
        end_time: str = None,
        ready_flag: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.data_type = data_type
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.ready_flag = ready_flag
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ready_flag is not None:
            result['ReadyFlag'] = self.ready_flag

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ReadyFlag') is not None:
            self.ready_flag = m.get('ReadyFlag')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

