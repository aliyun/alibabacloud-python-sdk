# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreatePipelineNodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreatePipelineNodeResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.CreatePipelineNodeResponseBodyData()
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

class CreatePipelineNodeResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code_list: List[str] = None,
        error_message_list: List[str] = None,
        pipeline_id: int = None,
    ):
        self.error_code_list = error_code_list
        self.error_message_list = error_message_list
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code_list is not None:
            result['ErrorCodeList'] = self.error_code_list

        if self.error_message_list is not None:
            result['ErrorMessageList'] = self.error_message_list

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCodeList') is not None:
            self.error_code_list = m.get('ErrorCodeList')

        if m.get('ErrorMessageList') is not None:
            self.error_message_list = m.get('ErrorMessageList')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        return self

