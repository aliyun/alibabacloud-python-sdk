# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListAlertRobotsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        robots: List[main_models.ListAlertRobotsResponseBodyRobots] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.robots = robots
        self.total = total

    def validate(self):
        if self.robots:
            for v1 in self.robots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['robots'] = []
        if self.robots is not None:
            for k1 in self.robots:
                result['robots'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.robots = []
        if m.get('robots') is not None:
            for k1 in m.get('robots'):
                temp_model = main_models.ListAlertRobotsResponseBodyRobots()
                self.robots.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAlertRobotsResponseBodyRobots(DaraModel):
    def __init__(
        self,
        digital_employee_name: str = None,
        lang: str = None,
        name: str = None,
        robot_id: str = None,
        type: str = None,
        url: str = None,
        workspace: str = None,
    ):
        self.digital_employee_name = digital_employee_name
        self.lang = lang
        self.name = name
        self.robot_id = robot_id
        self.type = type
        self.url = url
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.lang is not None:
            result['lang'] = self.lang

        if self.name is not None:
            result['name'] = self.name

        if self.robot_id is not None:
            result['robotId'] = self.robot_id

        if self.type is not None:
            result['type'] = self.type

        if self.url is not None:
            result['url'] = self.url

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('robotId') is not None:
            self.robot_id = m.get('robotId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

