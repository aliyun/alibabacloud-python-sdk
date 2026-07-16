# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class OpenDatasetProxyAppendDataRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        data_meta: List[Dict[str, str]] = None,
        task_id: str = None,
        trace_id: str = None,
        uuid: str = None,
    ):
        self.biz_code = biz_code
        # A list of data records. A single invocation can contain up to 100 records. Each element in the array is a map.
        self.data_meta = data_meta
        # Task ID, indicating the task to which data is appended.
        self.task_id = task_id
        # TraceId
        self.trace_id = trace_id
        # Unique identifier ID, controlled by the business side.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.data_meta is not None:
            result['DataMeta'] = self.data_meta

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.uuid is not None:
            result['UUID'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('DataMeta') is not None:
            self.data_meta = m.get('DataMeta')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')

        return self

