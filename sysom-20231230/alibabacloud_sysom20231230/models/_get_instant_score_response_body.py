# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetInstantScoreResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInstantScoreResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # - `code == Success` indicates that the authorization is successful.
        # - Other status codes indicate that the authorization has failed. If the authorization has failed, check the `message` field for the detailed fault information.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code == Success`, this field is empty.
        # - Otherwise, this field contains the error information of the request.
        self.message = message
        # Id of the request
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
            temp_model = main_models.GetInstantScoreResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetInstantScoreResponseBodyData(DaraModel):
    def __init__(
        self,
        error: float = None,
        latency: float = None,
        load: float = None,
        saturation: float = None,
        total: float = None,
    ):
        # The error score.
        self.error = error
        # The latency score.
        self.latency = latency
        # The load score.
        self.load = load
        # The saturation score.
        self.saturation = saturation
        # The total score.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['error'] = self.error

        if self.latency is not None:
            result['latency'] = self.latency

        if self.load is not None:
            result['load'] = self.load

        if self.saturation is not None:
            result['saturation'] = self.saturation

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('latency') is not None:
            self.latency = m.get('latency')

        if m.get('load') is not None:
            self.load = m.get('load')

        if m.get('saturation') is not None:
            self.saturation = m.get('saturation')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

