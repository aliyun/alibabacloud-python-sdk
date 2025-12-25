# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateDomainResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateDomainResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID. You can use this value to trace the API call.
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
            temp_model = main_models.UpdateDomainResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class UpdateDomainResponseBodyData(DaraModel):
    def __init__(
        self,
        deploy_revision_id: str = None,
    ):
        # The released version ID.
        self.deploy_revision_id = deploy_revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy_revision_id is not None:
            result['deployRevisionId'] = self.deploy_revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deployRevisionId') is not None:
            self.deploy_revision_id = m.get('deployRevisionId')

        return self

