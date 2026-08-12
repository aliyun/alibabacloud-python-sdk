# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class ListTeamsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        teams: List[main_models.E2BTeam] = None,
        total: int = None,
    ):
        # The error code.
        self.code = code
        # The response message.
        self.message = message
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Minimum value: 1. Maximum value: 50.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The list of teams.
        self.teams = teams
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.teams:
            for v1 in self.teams:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['teams'] = []
        if self.teams is not None:
            for k1 in self.teams:
                result['teams'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.teams = []
        if m.get('teams') is not None:
            for k1 in m.get('teams'):
                temp_model = main_models.E2BTeam()
                self.teams.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

