# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class DivisionPageResult(DaraModel):
    def __init__(
        self,
        division_list: List[main_models.Division] = None,
        request_id: str = None,
    ):
        self.division_list = division_list
        self.request_id = request_id

    def validate(self):
        if self.division_list:
            for v1 in self.division_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['divisionList'] = []
        if self.division_list is not None:
            for k1 in self.division_list:
                result['divisionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.division_list = []
        if m.get('divisionList') is not None:
            for k1 in m.get('divisionList'):
                temp_model = main_models.Division()
                self.division_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

