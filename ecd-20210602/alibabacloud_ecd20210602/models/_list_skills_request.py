# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSkillsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        skill_channel: str = None,
        skill_ids: List[str] = None,
        supplier_type: str = None,
    ):
        # The page number of the current page in a paged query.
        self.page_number = page_number
        # The maximum number of rows per page in a paged query. Default value: 20.
        self.page_size = page_size
        # The skill channel.
        # 
        # This parameter is required.
        self.skill_channel = skill_channel
        # The list of skill IDs.
        self.skill_ids = skill_ids
        # The supply type.
        self.supplier_type = supplier_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.skill_channel is not None:
            result['SkillChannel'] = self.skill_channel

        if self.skill_ids is not None:
            result['SkillIds'] = self.skill_ids

        if self.supplier_type is not None:
            result['SupplierType'] = self.supplier_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SkillChannel') is not None:
            self.skill_channel = m.get('SkillChannel')

        if m.get('SkillIds') is not None:
            self.skill_ids = m.get('SkillIds')

        if m.get('SupplierType') is not None:
            self.supplier_type = m.get('SupplierType')

        return self

