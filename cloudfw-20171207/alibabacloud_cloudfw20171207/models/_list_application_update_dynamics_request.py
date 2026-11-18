# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationUpdateDynamicsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The language of the returned information. Valid values:
        # - **zh**: Chinese. This is the default value.
        # - **en**: English.
        # This parameter determines whether the update description and application name are returned in Chinese or English.
        self.lang = lang
        # The page number. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. The value must be greater than or equal to 1. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

