# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterApiKeysResponseBody(DaraModel):
    def __init__(
        self,
        api_keys: List[main_models.DescribeAIDBClusterApiKeysResponseBodyApiKeys] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
    ):
        # API Keys。
        self.api_keys = api_keys
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.api_keys:
            for v1 in self.api_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiKeys'] = []
        if self.api_keys is not None:
            for k1 in self.api_keys:
                result['ApiKeys'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_keys = []
        if m.get('ApiKeys') is not None:
            for k1 in m.get('ApiKeys'):
                temp_model = main_models.DescribeAIDBClusterApiKeysResponseBodyApiKeys()
                self.api_keys.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAIDBClusterApiKeysResponseBodyApiKeys(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        status: str = None,
    ):
        # The API key of the model service.
        self.api_key = api_key
        # The creation time.
        self.create_time = create_time
        # The description of the API key.
        self.description = description
        # ApiKey ID
        self.id = id
        # The status of the API key.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

