# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSandboxesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # 当前页码，从1开始计数
        self.max_results = max_results
        self.next_token = next_token
        self.status = status
        # 按模板名称过滤
        self.template_name = template_name
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.status is not None:
            result['status'] = self.status

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.template_type is not None:
            result['templateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        return self

