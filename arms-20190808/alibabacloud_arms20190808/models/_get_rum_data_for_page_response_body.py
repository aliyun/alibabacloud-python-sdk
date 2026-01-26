# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetRumDataForPageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRumDataForPageResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The responses code. The status code 200 indicates that the request was successful.
        self.code = code
        # The result of the operation.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
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
            temp_model = main_models.GetRumDataForPageResponseBodyData()
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

class GetRumDataForPageResponseBodyData(DaraModel):
    def __init__(
        self,
        authentication: str = None,
        completion: str = None,
        items: List[Dict[str, Any]] = None,
        page: str = None,
        page_size: str = None,
        preference: str = None,
        total: str = None,
    ):
        # A reserved parameter. Ignore this parameter.
        self.authentication = authentication
        # Indicates whether the query ends. Valid values: true and false.
        self.completion = completion
        # The queried data.
        self.items = items
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # A reserved parameter. Ignore this parameter.
        self.preference = preference
        # The total number of entries returned.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication is not None:
            result['Authentication'] = self.authentication

        if self.completion is not None:
            result['Completion'] = self.completion

        if self.items is not None:
            result['Items'] = self.items

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.preference is not None:
            result['Preference'] = self.preference

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authentication') is not None:
            self.authentication = m.get('Authentication')

        if m.get('Completion') is not None:
            self.completion = m.get('Completion')

        if m.get('Items') is not None:
            self.items = m.get('Items')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Preference') is not None:
            self.preference = m.get('Preference')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

