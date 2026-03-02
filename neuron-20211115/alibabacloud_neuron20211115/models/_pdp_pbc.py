# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpPbc(DaraModel):
    def __init__(
        self,
        alias: str = None,
        company: str = None,
        company_id: int = None,
        description: str = None,
        developer_id: str = None,
        git_group: str = None,
        git_group_info: str = None,
        gmt_create: str = None,
        id: int = None,
        name: str = None,
        request_id: str = None,
        snowberg_display: bool = None,
        type: str = None,
    ):
        # This parameter is required.
        self.alias = alias
        # This parameter is required.
        self.company = company
        # This parameter is required.
        self.company_id = company_id
        self.description = description
        self.developer_id = developer_id
        self.git_group = git_group
        self.git_group_info = git_group_info
        self.gmt_create = gmt_create
        self.id = id
        # This parameter is required.
        self.name = name
        self.request_id = request_id
        self.snowberg_display = snowberg_display
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.company is not None:
            result['company'] = self.company

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.description is not None:
            result['description'] = self.description

        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.git_group is not None:
            result['gitGroup'] = self.git_group

        if self.git_group_info is not None:
            result['gitGroupInfo'] = self.git_group_info

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.snowberg_display is not None:
            result['snowbergDisplay'] = self.snowberg_display

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('company') is not None:
            self.company = m.get('company')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('gitGroup') is not None:
            self.git_group = m.get('gitGroup')

        if m.get('gitGroupInfo') is not None:
            self.git_group_info = m.get('gitGroupInfo')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('snowbergDisplay') is not None:
            self.snowberg_display = m.get('snowbergDisplay')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

