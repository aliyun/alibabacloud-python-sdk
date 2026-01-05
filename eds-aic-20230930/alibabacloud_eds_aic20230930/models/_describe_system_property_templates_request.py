# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSystemPropertyTemplatesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        template_ids: List[str] = None,
        template_name: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.template_ids = template_ids
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

