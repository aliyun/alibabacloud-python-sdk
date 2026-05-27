# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class BatchGetUserIdByOpenDingtalkIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.BatchGetUserIdByOpenDingtalkIdResponseBodyResults] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.results = results
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.BatchGetUserIdByOpenDingtalkIdResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class BatchGetUserIdByOpenDingtalkIdResponseBodyResults(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        open_dingtalk_id: str = None,
        user_id: str = None,
    ):
        self.error_message = error_message
        self.open_dingtalk_id = open_dingtalk_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.open_dingtalk_id is not None:
            result['OpenDingtalkId'] = self.open_dingtalk_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('OpenDingtalkId') is not None:
            self.open_dingtalk_id = m.get('OpenDingtalkId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

