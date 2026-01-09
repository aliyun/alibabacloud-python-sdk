# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class LogGroupList(DaraModel):
    def __init__(
        self,
        log_group_list: List[main_models.LogGroup] = None,
    ):
        # This parameter is required.
        self.log_group_list = log_group_list

    def validate(self):
        if self.log_group_list:
            for v1 in self.log_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['logGroupList'] = []
        if self.log_group_list is not None:
            for k1 in self.log_group_list:
                result['logGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_group_list = []
        if m.get('logGroupList') is not None:
            for k1 in m.get('logGroupList'):
                temp_model = main_models.LogGroup()
                self.log_group_list.append(temp_model.from_map(k1))

        return self

