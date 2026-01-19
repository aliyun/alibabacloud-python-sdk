# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PocCreateTaskRequest(DaraModel):
    def __init__(
        self,
        date_format: str = None,
        lang: str = None,
        reg_id: str = None,
        task_name: str = None,
        token: str = None,
    ):
        # Date format
        self.date_format = date_format
        # Set the language type for request and response messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Region code.
        self.reg_id = reg_id
        # Task name.
        self.task_name = task_name
        # Task token.
        # 
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_format is not None:
            result['DateFormat'] = self.date_format

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFormat') is not None:
            self.date_format = m.get('DateFormat')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

