# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class BuildAICoachScriptRecordResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.BuildAICoachScriptRecordResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        script_record_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.script_record_id = script_record_id
        self.success = success

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

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.BuildAICoachScriptRecordResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class BuildAICoachScriptRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        script_id: str = None,
    ):
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script_id is not None:
            result['scriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scriptId') is not None:
            self.script_id = m.get('scriptId')

        return self

