# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetCustomerListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCustomerListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call failed.
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
            temp_model = main_models.GetCustomerListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCustomerListResponseBodyData(DaraModel):
    def __init__(
        self,
        uid_list: List[str] = None,
    ):
        # The list of customer IDs.
        self.uid_list = uid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uid_list is not None:
            result['UidList'] = self.uid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UidList') is not None:
            self.uid_list = m.get('UidList')

        return self

