# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceActiveOpsTaskResponseBody(DaraModel):
    def __init__(
        self,
        instance_active_ops_task: main_models.InstanceActiveOpsTask = None,
        request_id: str = None,
    ):
        self.instance_active_ops_task = instance_active_ops_task
        self.request_id = request_id

    def validate(self):
        if self.instance_active_ops_task:
            self.instance_active_ops_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_active_ops_task is not None:
            result['InstanceActiveOpsTask'] = self.instance_active_ops_task.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceActiveOpsTask') is not None:
            temp_model = main_models.InstanceActiveOpsTask()
            self.instance_active_ops_task = temp_model.from_map(m.get('InstanceActiveOpsTask'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

