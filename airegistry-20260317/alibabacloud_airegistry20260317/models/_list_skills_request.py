# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillsRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        order_by: str = None,
        owner: str = None,
        page_no: int = None,
        page_size: int = None,
        scope: str = None,
        search: str = None,
        skill_name: str = None,
    ):
        # This parameter is required.
        self.namespace_id = namespace_id
        self.order_by = order_by
        self.owner = owner
        self.page_no = page_no
        self.page_size = page_size
        self.scope = scope
        self.search = search
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.search is not None:
            result['Search'] = self.search

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

