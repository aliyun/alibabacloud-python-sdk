# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAclAppsRequest(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        lang: str = None,
        page_no: int = None,
        page_size: int = None,
        popular: int = None,
        protocols: List[str] = None,
    ):
        # This parameter is required.
        self.acl_type = acl_type
        self.lang = lang
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.popular = popular
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.popular is not None:
            result['Popular'] = self.popular

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Popular') is not None:
            self.popular = m.get('Popular')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        return self

