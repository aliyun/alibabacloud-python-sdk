# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class CategoryMatchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CategoryMatchResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. The value "success" is returned for a successful call.
        self.code = code
        # The product category matching result.
        self.data = data
        # The error message. The value "Success" is returned for a successful call.
        self.message = message
        # The request ID, which uniquely identifies the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values: true and false.
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
            temp_model = main_models.CategoryMatchResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CategoryMatchResponseBodyData(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
        category_path: str = None,
        confidence: int = None,
        match_successful: bool = None,
        reason: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The ID of the matched category.
        self.category_id = category_id
        # The name of the matched category.
        self.category_name = category_name
        # The full path of the category, separated by forward slashes (/).
        self.category_path = category_path
        # The matching confidence score, ranging from 0 to 100.
        self.confidence = confidence
        # Indicates whether the match is successful.
        self.match_successful = match_successful
        # The reason for the match.
        self.reason = reason
        # The usage information.
        self.usage_map = usage_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.category_path is not None:
            result['CategoryPath'] = self.category_path

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.match_successful is not None:
            result['MatchSuccessful'] = self.match_successful

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CategoryPath') is not None:
            self.category_path = m.get('CategoryPath')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('MatchSuccessful') is not None:
            self.match_successful = m.get('MatchSuccessful')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

