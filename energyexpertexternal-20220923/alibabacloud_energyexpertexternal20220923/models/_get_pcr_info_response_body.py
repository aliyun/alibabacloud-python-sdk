# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetPcrInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetPcrInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetPcrInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPcrInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        url: str = None,
    ):
        # The timestamp when the report was created. The timestamp is in milliseconds.
        self.create_time = create_time
        # Report name
        self.name = name
        # Download url link.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.name is not None:
            result['name'] = self.name

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

