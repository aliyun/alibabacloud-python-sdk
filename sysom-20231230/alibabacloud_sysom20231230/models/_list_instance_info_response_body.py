# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListInstanceInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListInstanceInfoResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListInstanceInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListInstanceInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        info_key: str = None,
        info_type: str = None,
        info_value: str = None,
    ):
        self.info_key = info_key
        self.info_type = info_type
        self.info_value = info_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_key is not None:
            result['infoKey'] = self.info_key

        if self.info_type is not None:
            result['infoType'] = self.info_type

        if self.info_value is not None:
            result['infoValue'] = self.info_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('infoKey') is not None:
            self.info_key = m.get('infoKey')

        if m.get('infoType') is not None:
            self.info_type = m.get('infoType')

        if m.get('infoValue') is not None:
            self.info_value = m.get('infoValue')

        return self

