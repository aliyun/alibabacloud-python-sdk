# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeNotifyTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeNotifyTemplateListResponseBodyData] = None,
        page: main_models.DescribeNotifyTemplateListResponseBodyPage = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The pagination information.
        self.page = page
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeNotifyTemplateListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            temp_model = main_models.DescribeNotifyTemplateListResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNotifyTemplateListResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNotifyTemplateListResponseBodyData(DaraModel):
    def __init__(
        self,
        content: str = None,
        event_id: str = None,
        params: str = None,
        subject: str = None,
        template_name: str = None,
    ):
        # The body of the template.
        self.content = content
        # The ID of the message event corresponding to the template.
        self.event_id = event_id
        # The parameters of the template.
        self.params = params
        # The title of the template.
        self.subject = subject
        # The name of the template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.params is not None:
            result['Params'] = self.params

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

