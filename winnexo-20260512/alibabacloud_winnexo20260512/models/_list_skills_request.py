# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSkillsRequest(DaraModel):
    def __init__(
        self,
        bind_status: str = None,
        filter_type: str = None,
        keyword: str = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        tags: List[str] = None,
        tenant_id: str = None,
    ):
        # The binding status. Valid values: BOUND (bound) and UNBOUND (unbound global skills). Must be specified together with operatingObjectName.
        self.bind_status = bind_status
        # The filter expression type.
        # 
        # - SQL: SQL-based filtering.
        # - TAG: Tag-based filtering.
        self.filter_type = filter_type
        # The search keyword. Supports fuzzy search by API name or exact search by API ID.
        self.keyword = keyword
        # The digital employee name. Used to calculate the CodeAgent allowedSkills whitelist based on binding relationships.
        self.operating_object_name = operating_object_name
        # The current page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The tag filtering parameter.
        self.tags = tags
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_status is not None:
            result['bindStatus'] = self.bind_status

        if self.filter_type is not None:
            result['filterType'] = self.filter_type

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tags is not None:
            result['tags'] = self.tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindStatus') is not None:
            self.bind_status = m.get('bindStatus')

        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

