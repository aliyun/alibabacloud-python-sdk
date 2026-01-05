# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class BatchUpdateTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success_info: Dict[str, main_models.SuccessInfoValue] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result of the batch operation, which is in the MAP structure. The task ID serves as a key, and the result serves as a value.
        self.success_info = success_info

    def validate(self):
        if self.success_info:
            for v1 in self.success_info.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SuccessInfo'] = {}
        if self.success_info is not None:
            for k1, v1 in self.success_info.items():
                result['SuccessInfo'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.success_info = {}
        if m.get('SuccessInfo') is not None:
            for k1, v1 in m.get('SuccessInfo').items():
                temp_model = main_models.SuccessInfoValue()
                self.success_info[k1] = temp_model.from_map(v1)

        return self

