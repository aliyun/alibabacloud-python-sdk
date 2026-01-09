# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class LogItem(DaraModel):
    def __init__(
        self,
        contents: List[main_models.LogContent] = None,
        time: int = None,
        time_ns: int = None,
    ):
        # This parameter is required.
        self.contents = contents
        # This parameter is required.
        self.time = time
        self.time_ns = time_ns

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['Contents'].append(k1.to_map() if k1 else None)

        if self.time is not None:
            result['Time'] = self.time

        if self.time_ns is not None:
            result['TimeNs'] = self.time_ns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k1 in m.get('Contents'):
                temp_model = main_models.LogContent()
                self.contents.append(temp_model.from_map(k1))

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TimeNs') is not None:
            self.time_ns = m.get('TimeNs')

        return self

