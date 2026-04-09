# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListParametersRequest(DaraModel):
    def __init__(
        self,
        ids: List[int] = None,
        names: List[str] = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        scope: str = None,
        sort_by: str = None,
        type: str = None,
    ):
        self.ids = ids
        self.names = names
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.scope = scope
        self.sort_by = sort_by
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.names is not None:
            result['Names'] = self.names

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

