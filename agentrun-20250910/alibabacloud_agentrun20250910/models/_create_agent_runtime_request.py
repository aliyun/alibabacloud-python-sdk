# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateAgentRuntimeRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateAgentRuntimeInput = None,
    ):
        # 创建智能体运行时所需的完整配置信息，包括运行时名称、资源规格、网络配置、协议配置等
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
            temp_model = main_models.CreateAgentRuntimeInput()
            self.body = temp_model.from_map(m.get('body'))

        return self

