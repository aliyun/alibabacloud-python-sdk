# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillReferencesRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        selector_type: str = None,
        selector_value: str = None,
    ):
        # The page number. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. If not specified, the default value on the server is used.
        self.page_size = page_size
        # The reference selector type used for filtering. Valid values: LABEL and VERSION.
        self.selector_type = selector_type
        # The reference selector value used for filtering. Valid values: latest, a named label, HEAD, or a specific version.
        self.selector_value = selector_value

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

        if self.selector_type is not None:
            result['selectorType'] = self.selector_type

        if self.selector_value is not None:
            result['selectorValue'] = self.selector_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('selectorType') is not None:
            self.selector_type = m.get('selectorType')

        if m.get('selectorValue') is not None:
            self.selector_value = m.get('selectorValue')

        return self

