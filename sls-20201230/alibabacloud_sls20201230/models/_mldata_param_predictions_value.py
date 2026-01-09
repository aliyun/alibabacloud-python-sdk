# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class MLDataParamPredictionsValue(DaraModel):
    def __init__(
        self,
        annotated_by: str = None,
        update_time: int = None,
        results: List[Dict[str, str]] = None,
    ):
        self.annotated_by = annotated_by
        self.update_time = update_time
        self.results = results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotated_by is not None:
            result['annotatedBy'] = self.annotated_by

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.results is not None:
            result['results'] = self.results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotatedBy') is not None:
            self.annotated_by = m.get('annotatedBy')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('results') is not None:
            self.results = m.get('results')

        return self

