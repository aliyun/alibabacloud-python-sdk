# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeHeadersResponseBody(DaraModel):
    def __init__(
        self,
        custom_header: main_models.DescribeHeadersResponseBodyCustomHeader = None,
        request_id: str = None,
    ):
        # The information about the custom header.
        self.custom_header = custom_header
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.custom_header:
            self.custom_header.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_header is not None:
            result['CustomHeader'] = self.custom_header.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHeader') is not None:
            temp_model = main_models.DescribeHeadersResponseBodyCustomHeader()
            self.custom_header = temp_model.from_map(m.get('CustomHeader'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHeadersResponseBodyCustomHeader(DaraModel):
    def __init__(
        self,
        domain: str = None,
        headers: str = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The header of the response.
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.headers is not None:
            result['Headers'] = self.headers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        return self

