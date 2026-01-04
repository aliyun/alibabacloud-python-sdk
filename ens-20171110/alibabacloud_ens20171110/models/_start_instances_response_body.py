# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class StartInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_responses: List[main_models.InstanceOperateResponse] = None,
        request_id: str = None,
    ):
        self.instance_responses = instance_responses
        self.request_id = request_id

    def validate(self):
        if self.instance_responses:
            for v1 in self.instance_responses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceResponses'] = []
        if self.instance_responses is not None:
            for k1 in self.instance_responses:
                result['InstanceResponses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_responses = []
        if m.get('InstanceResponses') is not None:
            for k1 in m.get('InstanceResponses'):
                temp_model = main_models.InstanceOperateResponse()
                self.instance_responses.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

