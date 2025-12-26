# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class GetTrainingJobErrorInfoResponseBody(DaraModel):
    def __init__(
        self,
        error_info: main_models.GetTrainingJobErrorInfoResponseBodyErrorInfo = None,
        request_id: str = None,
    ):
        self.error_info = error_info
        self.request_id = request_id

    def validate(self):
        if self.error_info:
            self.error_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorInfo') is not None:
            temp_model = main_models.GetTrainingJobErrorInfoResponseBodyErrorInfo()
            self.error_info = temp_model.from_map(m.get('ErrorInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTrainingJobErrorInfoResponseBodyErrorInfo(DaraModel):
    def __init__(
        self,
        additional_info: str = None,
        code: str = None,
        message: str = None,
    ):
        self.additional_info = additional_info
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_info is not None:
            result['AdditionalInfo'] = self.additional_info

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalInfo') is not None:
            self.additional_info = m.get('AdditionalInfo')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

