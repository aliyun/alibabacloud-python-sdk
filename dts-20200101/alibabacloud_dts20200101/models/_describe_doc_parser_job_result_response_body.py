# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDocParserJobResultResponseBody(DaraModel):
    def __init__(
        self,
        content_list: List[main_models.DescribeDocParserJobResultResponseBodyContentList] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        file_url: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.content_list = content_list
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.file_url = file_url
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.content_list:
            for v1 in self.content_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContentList'] = []
        if self.content_list is not None:
            for k1 in self.content_list:
                result['ContentList'].append(k1.to_map() if k1 else None)

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content_list = []
        if m.get('ContentList') is not None:
            for k1 in m.get('ContentList'):
                temp_model = main_models.DescribeDocParserJobResultResponseBodyContentList()
                self.content_list.append(temp_model.from_map(k1))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDocParserJobResultResponseBodyContentList(DaraModel):
    def __init__(
        self,
        content: str = None,
        page_number: int = None,
    ):
        self.content = content
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        return self

