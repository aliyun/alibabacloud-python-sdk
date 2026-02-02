# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportQos(DaraModel):
    def __init__(
        self,
        max_band_width: int = None,
        max_import_task_qps: int = None,
    ):
        self.max_band_width = max_band_width
        self.max_import_task_qps = max_import_task_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_band_width is not None:
            result['MaxBandWidth'] = self.max_band_width

        if self.max_import_task_qps is not None:
            result['MaxImportTaskQps'] = self.max_import_task_qps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxBandWidth') is not None:
            self.max_band_width = m.get('MaxBandWidth')

        if m.get('MaxImportTaskQps') is not None:
            self.max_import_task_qps = m.get('MaxImportTaskQps')

        return self

