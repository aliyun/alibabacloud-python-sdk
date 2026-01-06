# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetTemplateListByUserIdResponseBody(DaraModel):
    def __init__(
        self,
        next_cursor: int = None,
        request_id: str = None,
        template_list: List[main_models.GetTemplateListByUserIdResponseBodyTemplateList] = None,
    ):
        self.next_cursor = next_cursor
        # requestId
        self.request_id = request_id
        self.template_list = template_list

    def validate(self):
        if self.template_list:
            for v1 in self.template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['templateList'] = []
        if self.template_list is not None:
            for k1 in self.template_list:
                result['templateList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.template_list = []
        if m.get('templateList') is not None:
            for k1 in m.get('templateList'):
                temp_model = main_models.GetTemplateListByUserIdResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k1))

        return self

class GetTemplateListByUserIdResponseBodyTemplateList(DaraModel):
    def __init__(
        self,
        icon_url: str = None,
        name: str = None,
        report_code: str = None,
        url: str = None,
    ):
        self.icon_url = icon_url
        self.name = name
        self.report_code = report_code
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.name is not None:
            result['Name'] = self.name

        if self.report_code is not None:
            result['ReportCode'] = self.report_code

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReportCode') is not None:
            self.report_code = m.get('ReportCode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

