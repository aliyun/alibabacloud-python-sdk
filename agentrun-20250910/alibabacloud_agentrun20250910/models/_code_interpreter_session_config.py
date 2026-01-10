# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CodeInterpreterSessionConfig(DaraModel):
    def __init__(
        self,
        environment: Dict[str, str] = None,
        timeout: int = None,
        working_directory: str = None,
    ):
        # 代码解释器会话的环境变量配置
        self.environment = environment
        # 代码解释器会话的超时时间，单位为秒
        self.timeout = timeout
        # 代码解释器会话的工作目录路径
        self.working_directory = working_directory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['environment'] = self.environment

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.working_directory is not None:
            result['workingDirectory'] = self.working_directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environment') is not None:
            self.environment = m.get('environment')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('workingDirectory') is not None:
            self.working_directory = m.get('workingDirectory')

        return self

