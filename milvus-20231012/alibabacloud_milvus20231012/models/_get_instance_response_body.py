# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        instance: main_models.InstanceDetail = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.instance = instance
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.instance is not None:
            result['instance'] = self.instance.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('instance') is not None:
            temp_model = main_models.InstanceDetail()
            self.instance = temp_model.from_map(m.get('instance'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

