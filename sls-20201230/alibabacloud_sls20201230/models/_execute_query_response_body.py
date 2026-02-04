# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ExecuteQueryResponseBody(DaraModel):
    def __init__(
        self,
        meta: main_models.ExecuteQueryResponseBodyMeta = None,
    ):
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meta') is not None:
            temp_model = main_models.ExecuteQueryResponseBodyMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        return self

class ExecuteQueryResponseBodyMeta(DaraModel):
    def __init__(
        self,
        affected_rows: int = None,
        elapsed_millisecond: int = None,
    ):
        self.affected_rows = affected_rows
        self.elapsed_millisecond = elapsed_millisecond

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_rows is not None:
            result['affectedRows'] = self.affected_rows

        if self.elapsed_millisecond is not None:
            result['elapsedMillisecond'] = self.elapsed_millisecond

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('affectedRows') is not None:
            self.affected_rows = m.get('affectedRows')

        if m.get('elapsedMillisecond') is not None:
            self.elapsed_millisecond = m.get('elapsedMillisecond')

        return self

