# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomizedListHeadersResponseBody(DaraModel):
    def __init__(
        self,
        headers: List[main_models.DescribeCustomizedListHeadersResponseBodyHeaders] = None,
        request_id: str = None,
    ):
        self.headers = headers
        self.request_id = request_id

    def validate(self):
        if self.headers:
            for v1 in self.headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Headers'] = []
        if self.headers is not None:
            for k1 in self.headers:
                result['Headers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k1 in m.get('Headers'):
                temp_model = main_models.DescribeCustomizedListHeadersResponseBodyHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCustomizedListHeadersResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        display_type: str = None,
        header_key: str = None,
        header_name: str = None,
    ):
        self.display_type = display_type
        self.header_key = header_key
        self.header_name = header_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_type is not None:
            result['DisplayType'] = self.display_type

        if self.header_key is not None:
            result['HeaderKey'] = self.header_key

        if self.header_name is not None:
            result['HeaderName'] = self.header_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayType') is not None:
            self.display_type = m.get('DisplayType')

        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')

        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')

        return self

