# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTaskOperationLogsRequest(DaraModel):
    def __init__(
        self,
        date: int = None,
        id: int = None,
        page_number: int = None,
        page_size: int = None,
        project_env: str = None,
    ):
        # The operation date, accurate to the day. The default value is the current day. You can query only the operation logs generated within the previous 31 days.
        self.date = date
        # The task ID.
        # 
        # This parameter is required.
        self.id = id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The environment of the workspace. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.project_env = project_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.id is not None:
            result['Id'] = self.id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        return self

