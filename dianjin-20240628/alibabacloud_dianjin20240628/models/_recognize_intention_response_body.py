# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RecognizeIntentionResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.RecognizeIntentionResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        # Processing time in milliseconds.
        self.cost = cost
        # Response data.
        self.data = data
        # Data type.
        self.data_type = data_type
        # Error code.
        self.err_code = err_code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        self.success = success
        # Timestamp.
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('data') is not None:
            temp_model = main_models.RecognizeIntentionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class RecognizeIntentionResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis_process: str = None,
        intention_code: str = None,
        intention_name: str = None,
        intention_script: str = None,
        recommend_intention: str = None,
        recommend_script: str = None,
    ):
        # Analysis process.
        self.analysis_process = analysis_process
        # Intent code.
        self.intention_code = intention_code
        # Intent name.
        self.intention_name = intention_name
        # Intent script.
        self.intention_script = intention_script
        # Recommended intent.
        self.recommend_intention = recommend_intention
        # Recommended script.
        self.recommend_script = recommend_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process

        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code

        if self.intention_name is not None:
            result['intentionName'] = self.intention_name

        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script

        if self.recommend_intention is not None:
            result['recommendIntention'] = self.recommend_intention

        if self.recommend_script is not None:
            result['recommendScript'] = self.recommend_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')

        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')

        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')

        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')

        if m.get('recommendIntention') is not None:
            self.recommend_intention = m.get('recommendIntention')

        if m.get('recommendScript') is not None:
            self.recommend_script = m.get('recommendScript')

        return self

