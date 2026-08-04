# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateAIDBClusterApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: main_models.CreateAIDBClusterApiKeyResponseBodyApiKey = None,
        request_id: str = None,
    ):
        # The API key.
        self.api_key = api_key
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.api_key:
            self.api_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            temp_model = main_models.CreateAIDBClusterApiKeyResponseBodyApiKey()
            self.api_key = temp_model.from_map(m.get('ApiKey'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAIDBClusterApiKeyResponseBodyApiKey(DaraModel):
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
        # The description.
        self.description = description
        # id
        self.id = id
        # The API key status.
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

