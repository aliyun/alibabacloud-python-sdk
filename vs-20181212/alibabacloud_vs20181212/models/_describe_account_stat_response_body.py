# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccountStatResponseBody(DaraModel):
    def __init__(
        self,
        group_limit: int = None,
        group_num: int = None,
        id: str = None,
        request_id: str = None,
        template_limit: int = None,
        template_num: int = None,
    ):
        self.group_limit = group_limit
        self.group_num = group_num
        # ID
        self.id = id
        self.request_id = request_id
        self.template_limit = template_limit
        self.template_num = template_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_limit is not None:
            result['GroupLimit'] = self.group_limit

        if self.group_num is not None:
            result['GroupNum'] = self.group_num

        if self.id is not None:
            result['Id'] = self.id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_limit is not None:
            result['TemplateLimit'] = self.template_limit

        if self.template_num is not None:
            result['TemplateNum'] = self.template_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupLimit') is not None:
            self.group_limit = m.get('GroupLimit')

        if m.get('GroupNum') is not None:
            self.group_num = m.get('GroupNum')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateLimit') is not None:
            self.template_limit = m.get('TemplateLimit')

        if m.get('TemplateNum') is not None:
            self.template_num = m.get('TemplateNum')

        return self

