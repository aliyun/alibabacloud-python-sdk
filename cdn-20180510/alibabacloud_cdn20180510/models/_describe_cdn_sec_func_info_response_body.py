# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnSecFuncInfoResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeCdnSecFuncInfoResponseBodyContent] = None,
        description: str = None,
        http_status: str = None,
        request_id: str = None,
        ret_code: str = None,
    ):
        # Queried data.
        self.content = content
        # The description.
        self.description = description
        # The HTTP status code returned.
        self.http_status = http_status
        # The request ID.
        self.request_id = request_id
        # The HTTP request response code.
        # 
        # *   0: OK.
        # *   Values other than 0: an error.
        self.ret_code = ret_code

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.http_status is not None:
            result['HttpStatus'] = self.http_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeCdnSecFuncInfoResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        return self

class DescribeCdnSecFuncInfoResponseBodyContent(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        # The tag.
        self.label = label
        # The value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

