# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateAgentVersionRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateAgentVersionRequestBody = None,
        client_token: str = None,
    ):
        # 保存版本的请求体。
        self.body = body
        # 客户端生成的幂等令牌，当前为预留参数，后端暂不提供持久化幂等保证。
        self.client_token = client_token

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

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateAgentVersionRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateAgentVersionRequestBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        version_name: str = None,
    ):
        # 版本描述，最多 1024 个字符，保存后不可修改。
        self.description = description
        # 用户自定义的展示名称，去除首尾空白后为 1 至 128 个字符，可包含中文、大小写字母、空格和标点，不能包含控制字符。同一 Agent 下未删除的版本名称唯一，区分大小写，保存后不可修改。版本号 agentVersion 由系统生成，不由此字段决定。
        # 
        # This parameter is required.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.version_name is not None:
            result['versionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('versionName') is not None:
            self.version_name = m.get('versionName')

        return self

