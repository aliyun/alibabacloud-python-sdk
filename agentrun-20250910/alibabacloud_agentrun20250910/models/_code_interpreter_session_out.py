# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CodeInterpreterSessionOut(DaraModel):
    def __init__(
        self,
        code_interpreter_id: str = None,
        code_interpreter_name: str = None,
        created_at: str = None,
        last_updated_at: str = None,
        session_id: str = None,
        session_idle_timeout_seconds: int = None,
        status: str = None,
    ):
        # 关联的代码解释器的唯一标识符
        # 
        # This parameter is required.
        self.code_interpreter_id = code_interpreter_id
        # 代码解释器会话的名称
        self.code_interpreter_name = code_interpreter_name
        # 代码解释器会话的创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 代码解释器会话的最后更新时间，采用ISO 8601格式
        self.last_updated_at = last_updated_at
        # 代码解释器会话的唯一标识符
        # 
        # This parameter is required.
        self.session_id = session_id
        # 代码解释器会话的空闲超时时间，单位为秒。实例没有会话请求后处于空闲状态，空闲态为闲置计费模式，超过此超时时间后会话自动过期，不可继续使用
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        # 代码解释器会话的当前状态
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_interpreter_id is not None:
            result['codeInterpreterId'] = self.code_interpreter_id

        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterId') is not None:
            self.code_interpreter_id = m.get('codeInterpreterId')

        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

