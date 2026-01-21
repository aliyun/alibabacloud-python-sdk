# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DeleteSiteMonitorsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DeleteSiteMonitorsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the call was successful.
        self.code = code
        # The information about the site monitoring tasks that were deleted.
        self.data = data
        # The returned message. If the call was successful, the value success is returned. If the call failed, an error message such as `TaskId not found` is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. The value true indicates success. The value false indicates failure.
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
            temp_model = main_models.DeleteSiteMonitorsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteSiteMonitorsResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
    ):
        # The number of the site monitoring tasks that were deleted.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        return self

