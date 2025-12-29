# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class QueryControlStrategyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: List[main_models.QueryControlStrategyResponseBodyResultObject] = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Processing result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.QueryControlStrategyResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class QueryControlStrategyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        biz_type: str = None,
        id: int = None,
        status: str = None,
        threshold: float = None,
        user_id: int = None,
    ):
        # API name, same as the **ProductCode** of the authentication interface.
        self.api_name = api_name
        # Rule configuration type:
        # - **QPS**: QPS greater than
        # - **SUCCESS_RATE_5_MIN**: Success rate in the last 5 minutes less than
        # - **RESP_TIME_5_MIN**: Average response time in the last 5 minutes greater than
        # - **AMOUNT_RISE**: Call volume growth ratio greater than
        # - **AMOUNT_FALL**: Call volume decline ratio less than
        # - **PASSED_RATE_1_HOUR**: Verification consistency rate in the last hour less than
        # - **PARAM_ERROR_RATE_1_HOUR**: Parameter error rate in the last hour greater than
        self.biz_type = biz_type
        # Rule ID.
        self.id = id
        # Status:
        # - **disabled**: Disabled
        # - **normal**: Enabled
        self.status = status
        # Alarm threshold for rule configuration.
        self.threshold = threshold
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

