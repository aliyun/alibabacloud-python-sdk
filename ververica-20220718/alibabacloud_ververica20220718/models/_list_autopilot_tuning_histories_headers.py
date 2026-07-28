# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ListAutopilotTuningHistoriesHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        accept_language: str = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The language type. Default value: en-US. Set this to zh-CN for Chinese.
        self.accept_language = accept_language
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.accept_language is not None:
            result['Accept-Language'] = self.accept_language

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('Accept-Language') is not None:
            self.accept_language = m.get('Accept-Language')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

