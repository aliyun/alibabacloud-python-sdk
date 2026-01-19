# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeBackendListRequest(DaraModel):
    def __init__(
        self,
        backend_name: str = None,
        backend_type: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        tag: List[main_models.DescribeBackendListRequestTag] = None,
    ):
        # The name of the backend service. You can use \\* to perform fuzzy queries.
        self.backend_name = backend_name
        # The type of the backend service.
        self.backend_type = backend_type
        # The number of the current page.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        self.security_token = security_token
        # The list of the tag.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_name is not None:
            result['BackendName'] = self.backend_name

        if self.backend_type is not None:
            result['BackendType'] = self.backend_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendName') is not None:
            self.backend_name = m.get('BackendName')

        if m.get('BackendType') is not None:
            self.backend_type = m.get('BackendType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeBackendListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeBackendListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

