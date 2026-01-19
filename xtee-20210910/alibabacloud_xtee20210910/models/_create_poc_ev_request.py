# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePocEvRequest(DaraModel):
    def __init__(
        self,
        date_format: str = None,
        file_name: str = None,
        file_type: str = None,
        file_url: str = None,
        lang: str = None,
        reg_id: str = None,
        service_code: str = None,
        service_name: str = None,
        tab: str = None,
        task_name: str = None,
        type: str = None,
    ):
        # Date format type
        self.date_format = date_format
        # File name.
        # > The file name must end with txt or sql. For example, test.txt, test.sql.
        self.file_name = file_name
        # File type
        self.file_type = file_type
        # File URL.
        self.file_url = file_url
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Region code
        self.reg_id = reg_id
        # Service code.
        self.service_code = service_code
        # Service name.
        self.service_name = service_name
        # Scenario.
        self.tab = tab
        # Task name.
        self.task_name = task_name
        # Access type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_format is not None:
            result['DateFormat'] = self.date_format

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFormat') is not None:
            self.date_format = m.get('DateFormat')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

