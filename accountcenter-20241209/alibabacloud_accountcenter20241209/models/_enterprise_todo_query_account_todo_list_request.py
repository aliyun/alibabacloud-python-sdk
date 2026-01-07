# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseTodoQueryAccountTodoListRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        max_results: int = None,
        next_token: str = None,
        operate_pk: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        page: int = None,
        page_size: int = None,
        show_complete_info: bool = None,
        status: str = None,
        todo_type: str = None,
    ):
        self.app_name = app_name
        self.max_results = max_results
        self.next_token = next_token
        self.operate_pk = operate_pk
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.page = page
        self.page_size = page_size
        self.show_complete_info = show_complete_info
        self.status = status
        self.todo_type = todo_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.operate_pk is not None:
            result['OperatePk'] = self.operate_pk

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info

        if self.status is not None:
            result['Status'] = self.status

        if self.todo_type is not None:
            result['TodoType'] = self.todo_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OperatePk') is not None:
            self.operate_pk = m.get('OperatePk')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TodoType') is not None:
            self.todo_type = m.get('TodoType')

        return self

