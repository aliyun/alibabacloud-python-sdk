# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class GetTemplateQuestionsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        error_code: str = None,
        message: str = None,
        question_configs: List[main_models.QuestionPlugin] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Total amount of data under the current request conditions. This parameter is optional and does not need to be returned by default.
        self.code = code
        # Details
        self.details = details
        # error code
        self.error_code = error_code
        # Return message of the request
        # 
        # This parameter is required.
        self.message = message
        # List of question configurations
        self.question_configs = question_configs
        # Request ID
        self.request_id = request_id
        # is succeeded
        self.success = success

    def validate(self):
        if self.question_configs:
            for v1 in self.question_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.details is not None:
            result['Details'] = self.details

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k1 in self.question_configs:
                result['QuestionConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k1 in m.get('QuestionConfigs'):
                temp_model = main_models.QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

