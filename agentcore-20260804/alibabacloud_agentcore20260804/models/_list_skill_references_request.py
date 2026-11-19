# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillReferencesRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        ref_type: str = None,
        selector_type: str = None,
        selector_value: str = None,
        source_id: str = None,
    ):
        # The page number, starting from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. If not specified, the server default value is used.
        self.page_size = page_size
        # Filters by reference strength. Valid values: STRONG, WEAK.
        self.ref_type = ref_type
        # Filters by reference selector type. Valid values: LABEL, VERSION.
        self.selector_type = selector_type
        # Filters by reference selector value. Valid values: latest, a named label, HEAD, or a specific version.
        self.selector_value = selector_value
        # Filters by reference source identifier. The value must be agentcore or a configured source.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['pageNo'] = self.page_no

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.ref_type is not None:
            result['refType'] = self.ref_type

        if self.selector_type is not None:
            result['selectorType'] = self.selector_type

        if self.selector_value is not None:
            result['selectorValue'] = self.selector_value

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('refType') is not None:
            self.ref_type = m.get('refType')

        if m.get('selectorType') is not None:
            self.selector_type = m.get('selectorType')

        if m.get('selectorValue') is not None:
            self.selector_value = m.get('selectorValue')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        return self

