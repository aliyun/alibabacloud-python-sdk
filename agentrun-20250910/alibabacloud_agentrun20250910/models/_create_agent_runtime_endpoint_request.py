# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateAgentRuntimeEndpointRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateAgentRuntimeEndpointInput = None,
    ):
        # 包含要创建的智能体运行时端点配置信息的请求体
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateAgentRuntimeEndpointInput()
            self.body = temp_model.from_map(m.get('body'))

        return self

