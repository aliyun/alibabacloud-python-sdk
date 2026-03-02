# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class SearchTracesByPageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trace_infos: List[main_models.TraceInfo] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.trace_infos = trace_infos

    def validate(self):
        if self.trace_infos:
            for v1 in self.trace_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['traceInfos'] = []
        if self.trace_infos is not None:
            for k1 in self.trace_infos:
                result['traceInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.trace_infos = []
        if m.get('traceInfos') is not None:
            for k1 in m.get('traceInfos'):
                temp_model = main_models.TraceInfo()
                self.trace_infos.append(temp_model.from_map(k1))

        return self

