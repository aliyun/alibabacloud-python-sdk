# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class PaChatCompletionStreamHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_qiagent_api_key: str = None,
        x_qiinstance_id: str = None,
        x_qisession_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.x_qiagent_api_key = x_qiagent_api_key
        # This parameter is required.
        self.x_qiinstance_id = x_qiinstance_id
        self.x_qisession_id = x_qisession_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_qiagent_api_key is not None:
            result['X-QI-Agent-Api-Key'] = self.x_qiagent_api_key

        if self.x_qiinstance_id is not None:
            result['X-QI-Instance-Id'] = self.x_qiinstance_id

        if self.x_qisession_id is not None:
            result['X-QI-Session-Id'] = self.x_qisession_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('X-QI-Agent-Api-Key') is not None:
            self.x_qiagent_api_key = m.get('X-QI-Agent-Api-Key')

        if m.get('X-QI-Instance-Id') is not None:
            self.x_qiinstance_id = m.get('X-QI-Instance-Id')

        if m.get('X-QI-Session-Id') is not None:
            self.x_qisession_id = m.get('X-QI-Session-Id')

        return self

