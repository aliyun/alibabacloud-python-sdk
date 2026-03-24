# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchFaqShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        category_ids_shrink: str = None,
        create_time_begin: str = None,
        create_time_end: str = None,
        create_user_name: str = None,
        end_time_begin: str = None,
        end_time_end: str = None,
        keyword: str = None,
        modify_time_begin: str = None,
        modify_time_end: str = None,
        modify_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_scope: int = None,
        start_time_begin: str = None,
        start_time_end: str = None,
        status: int = None,
    ):
        self.agent_key = agent_key
        self.category_ids_shrink = category_ids_shrink
        self.create_time_begin = create_time_begin
        self.create_time_end = create_time_end
        self.create_user_name = create_user_name
        self.end_time_begin = end_time_begin
        self.end_time_end = end_time_end
        self.keyword = keyword
        self.modify_time_begin = modify_time_begin
        self.modify_time_end = modify_time_end
        self.modify_user_name = modify_user_name
        self.page_number = page_number
        self.page_size = page_size
        self.search_scope = search_scope
        self.start_time_begin = start_time_begin
        self.start_time_end = start_time_end
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink

        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin

        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.modify_time_begin is not None:
            result['ModifyTimeBegin'] = self.modify_time_begin

        if self.modify_time_end is not None:
            result['ModifyTimeEnd'] = self.modify_time_end

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_scope is not None:
            result['SearchScope'] = self.search_scope

        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin

        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')

        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')

        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ModifyTimeBegin') is not None:
            self.modify_time_begin = m.get('ModifyTimeBegin')

        if m.get('ModifyTimeEnd') is not None:
            self.modify_time_end = m.get('ModifyTimeEnd')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchScope') is not None:
            self.search_scope = m.get('SearchScope')

        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')

        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

