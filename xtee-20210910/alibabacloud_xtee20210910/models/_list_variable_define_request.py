# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVariableDefineRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        allow_bind: str = None,
        charging_mode: str = None,
        current_page: int = None,
        page_size: int = None,
        paging: str = None,
        query_content: str = None,
        reg_id: str = None,
        role_type: str = None,
        scenes_str: str = None,
        source: str = None,
        status: str = None,
        title: str = None,
        types_str: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Whether binding is allowed, default is ENABLE
        self.allow_bind = allow_bind
        # Charging mode
        self.charging_mode = charging_mode
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10
        self.page_size = page_size
        # Paging identifier
        self.paging = paging
        # Query content
        self.query_content = query_content
        # Region code
        self.reg_id = reg_id
        # Authorization type
        self.role_type = role_type
        # Scenario
        self.scenes_str = scenes_str
        # Source
        self.source = source
        # Status.
        self.status = status
        # Title.
        self.title = title
        # Type
        self.types_str = types_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.allow_bind is not None:
            result['allowBind'] = self.allow_bind

        if self.charging_mode is not None:
            result['chargingMode'] = self.charging_mode

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.paging is not None:
            result['paging'] = self.paging

        if self.query_content is not None:
            result['queryContent'] = self.query_content

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.role_type is not None:
            result['roleType'] = self.role_type

        if self.scenes_str is not None:
            result['scenesStr'] = self.scenes_str

        if self.source is not None:
            result['source'] = self.source

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        if self.types_str is not None:
            result['typesStr'] = self.types_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('allowBind') is not None:
            self.allow_bind = m.get('allowBind')

        if m.get('chargingMode') is not None:
            self.charging_mode = m.get('chargingMode')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('paging') is not None:
            self.paging = m.get('paging')

        if m.get('queryContent') is not None:
            self.query_content = m.get('queryContent')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('roleType') is not None:
            self.role_type = m.get('roleType')

        if m.get('scenesStr') is not None:
            self.scenes_str = m.get('scenesStr')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('typesStr') is not None:
            self.types_str = m.get('typesStr')

        return self

