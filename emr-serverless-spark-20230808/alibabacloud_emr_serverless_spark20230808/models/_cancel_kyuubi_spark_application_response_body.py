# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class CancelKyuubiSparkApplicationResponseBody(DaraModel):
    def __init__(
        self,
        body: main_models.CancelKyuubiSparkApplicationResponseBodyBody = None,
        request_id: str = None,
    ):
        self.body = body
        self.request_id = request_id

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CancelKyuubiSparkApplicationResponseBodyBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CancelKyuubiSparkApplicationResponseBodyBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        success: bool = None,
    ):
        self.application_id = application_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['applicationId'] = self.application_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationId') is not None:
            self.application_id = m.get('applicationId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

