# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetAsyncErrorRequestStatResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAsyncErrorRequestStatResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetAsyncErrorRequestStatResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAsyncErrorRequestStatResultResponseBodyData(DaraModel):
    def __init__(
        self,
        complete: bool = None,
        fail: bool = None,
        is_finish: bool = None,
        result: Dict[str, main_models.DataResultValue] = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        # Indicates whether the asynchronous request was complete.
        # 
        # *   **true**
        # *   **false**
        self.complete = complete
        # Indicates whether the request failed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fail = fail
        # Indicates whether the asynchronous request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_finish = is_finish
        # The returned data of the asynchronous request.
        self.result = result
        # The ID of the asynchronous request.
        self.result_id = result_id
        # The state of the asynchronous request. Valid values:
        # 
        # *   **RUNNING**: The asynchronous request is running.
        # *   **SUCCESS**: The asynchronous request is successful.
        # *   **FAIL**: The asynchronous request fails.
        self.state = state
        # The time when the asynchronous request was made. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp

    def validate(self):
        if self.result:
            for v1 in self.result.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete is not None:
            result['complete'] = self.complete

        if self.fail is not None:
            result['fail'] = self.fail

        if self.is_finish is not None:
            result['isFinish'] = self.is_finish

        result['result'] = {}
        if self.result is not None:
            for k1, v1 in self.result.items():
                result['result'][k1] = v1.to_map() if v1 else None

        if self.result_id is not None:
            result['resultId'] = self.result_id

        if self.state is not None:
            result['state'] = self.state

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('complete') is not None:
            self.complete = m.get('complete')

        if m.get('fail') is not None:
            self.fail = m.get('fail')

        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')

        self.result = {}
        if m.get('result') is not None:
            for k1, v1 in m.get('result').items():
                temp_model = main_models.DataResultValue()
                self.result[k1] = temp_model.from_map(v1)

        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

