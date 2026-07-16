# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class CreateLivyComputeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateLivyComputeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code of the request. A value of 1000000 indicates that the request was successful. Other values indicate that the request failed. For more information, see the message parameter.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateLivyComputeResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateLivyComputeResponseBodyData(DaraModel):
    def __init__(
        self,
        livy_compute_id: str = None,
    ):
        # The ID of the Livy Gateway.
        self.livy_compute_id = livy_compute_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.livy_compute_id is not None:
            result['livyComputeId'] = self.livy_compute_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('livyComputeId') is not None:
            self.livy_compute_id = m.get('livyComputeId')

        return self

