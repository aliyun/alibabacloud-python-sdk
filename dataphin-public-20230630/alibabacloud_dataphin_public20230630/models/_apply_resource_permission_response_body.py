# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ApplyResourcePermissionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ApplyResourcePermissionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code of the request. A value of OK indicates that the request is successful.
        self.code = code
        # The application result.
        self.data = data
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message of the request.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ApplyResourcePermissionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ApplyResourcePermissionResponseBodyData(DaraModel):
    def __init__(
        self,
        apply_ids: List[str] = None,
        bpms_ids: List[str] = None,
    ):
        # The list of application IDs.
        self.apply_ids = apply_ids
        # The list of approval IDs.
        self.bpms_ids = bpms_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_ids is not None:
            result['ApplyIds'] = self.apply_ids

        if self.bpms_ids is not None:
            result['BpmsIds'] = self.bpms_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyIds') is not None:
            self.apply_ids = m.get('ApplyIds')

        if m.get('BpmsIds') is not None:
            self.bpms_ids = m.get('BpmsIds')

        return self

