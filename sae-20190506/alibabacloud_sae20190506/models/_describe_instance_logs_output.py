# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceLogsOutput(DaraModel):
    def __init__(
        self,
        web_log_entrys: List[main_models.WebLogEntry] = None,
    ):
        self.web_log_entrys = web_log_entrys

    def validate(self):
        if self.web_log_entrys:
            for v1 in self.web_log_entrys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WebLogEntrys'] = []
        if self.web_log_entrys is not None:
            for k1 in self.web_log_entrys:
                result['WebLogEntrys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.web_log_entrys = []
        if m.get('WebLogEntrys') is not None:
            for k1 in m.get('WebLogEntrys'):
                temp_model = main_models.WebLogEntry()
                self.web_log_entrys.append(temp_model.from_map(k1))

        return self

