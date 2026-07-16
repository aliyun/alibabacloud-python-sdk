# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTaskDetailHistoryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_name_cursor: str = None,
        lang: str = None,
        page_size: int = None,
        task_detail_no_cursor: str = None,
        task_no: str = None,
        task_status: int = None,
        user_client_ip: str = None,
    ):
        self.domain_name = domain_name
        self.domain_name_cursor = domain_name_cursor
        self.lang = lang
        # This parameter is required.
        self.page_size = page_size
        self.task_detail_no_cursor = task_detail_no_cursor
        # This parameter is required.
        self.task_no = task_no
        self.task_status = task_status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_name_cursor is not None:
            result['DomainNameCursor'] = self.domain_name_cursor

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_detail_no_cursor is not None:
            result['TaskDetailNoCursor'] = self.task_detail_no_cursor

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameCursor') is not None:
            self.domain_name_cursor = m.get('DomainNameCursor')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskDetailNoCursor') is not None:
            self.task_detail_no_cursor = m.get('TaskDetailNoCursor')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

