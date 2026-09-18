# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlertRobotRequest(DaraModel):
    def __init__(
        self,
        digital_employee_name: str = None,
        lang: str = None,
        name: str = None,
        robot_id: str = None,
        robot_sign_key: str = None,
        type: str = None,
        url: str = None,
        workspace: str = None,
    ):
        # The name of the digital employee.
        self.digital_employee_name = digital_employee_name
        # The language.
        self.lang = lang
        # The name of the robot.
        self.name = name
        # The unique ID of the robot.
        self.robot_id = robot_id
        # The signature key of the robot.
        self.robot_sign_key = robot_sign_key
        # The type of the robot.
        # 
        # This parameter is required.
        self.type = type
        # The webhook URL of the robot.
        self.url = url
        # The workspace name.
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

        if self.robot_sign_key is not None:
            result['robotSignKey'] = self.robot_sign_key

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

        if m.get('robotSignKey') is not None:
            self.robot_sign_key = m.get('robotSignKey')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

