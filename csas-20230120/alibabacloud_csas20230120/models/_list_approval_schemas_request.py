# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApprovalSchemasRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        policy_type: str = None,
        schema_ids: List[str] = None,
        schema_name: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.page_size = page_size
        self.policy_type = policy_type
        self.schema_ids = schema_ids
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.schema_ids is not None:
            result['SchemaIds'] = self.schema_ids

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('SchemaIds') is not None:
            self.schema_ids = m.get('SchemaIds')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        return self

