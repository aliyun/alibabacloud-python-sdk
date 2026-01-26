# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class QueryCommercialUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryCommercialUsageResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response status. Valid values: 2XX: The request is successful. 3XX: A redirection message is returned. 4XX: The request is invalid. 5XX: A server error occurs.
        self.code = code
        # The returned struct.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.QueryCommercialUsageResponseBodyData()
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

class QueryCommercialUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        complete: bool = None,
        items: List[Dict[str, Any]] = None,
    ):
        # Indicates whether a multi-region query is complete. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.complete = complete
        # The returned struct.
        self.items = items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete is not None:
            result['Complete'] = self.complete

        if self.items is not None:
            result['Items'] = self.items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')

        if m.get('Items') is not None:
            self.items = m.get('Items')

        return self

