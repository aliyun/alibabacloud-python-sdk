# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class UpdateAutoThrottleRulesAsyncResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.UpdateAutoThrottleRulesAsyncResponseBodyData = None,
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
            temp_model = main_models.UpdateAutoThrottleRulesAsyncResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateAutoThrottleRulesAsyncResponseBodyData(DaraModel):
    def __init__(
        self,
        complete: bool = None,
        config_response: main_models.UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponse = None,
        fail: bool = None,
        is_finish: bool = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        # Indicates whether the asynchronous request was complete. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.complete = complete
        # The returned data of the configuration.
        # 
        # >  The data is returned only if the value of isFinish is **true**. This value indicates that the asynchronous request is complete.
        self.config_response = config_response
        # Indicates whether the asynchronous request failed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fail = fail
        # Indicates whether the asynchronous request was complete. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_finish = is_finish
        # The ID of the asynchronous request.
        self.result_id = result_id
        # The state of the asynchronous request. Valid values:
        # 
        # *   **RUNNING**
        # *   **SUCCESS**
        # *   **FAIL**
        self.state = state
        # The time when the asynchronous request was made. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp

    def validate(self):
        if self.config_response:
            self.config_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete is not None:
            result['Complete'] = self.complete

        if self.config_response is not None:
            result['ConfigResponse'] = self.config_response.to_map()

        if self.fail is not None:
            result['Fail'] = self.fail

        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        if self.state is not None:
            result['State'] = self.state

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')

        if m.get('ConfigResponse') is not None:
            temp_model = main_models.UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponse()
            self.config_response = temp_model.from_map(m.get('ConfigResponse'))

        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponse(DaraModel):
    def __init__(
        self,
        config_fail_instance_count: int = None,
        config_fail_instance_list: List[main_models.UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList] = None,
        config_success_instance_count: int = None,
        config_success_instance_list: List[main_models.UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList] = None,
        total_instance_count: int = None,
    ):
        # The number of database instances for which the parameters failed to be configured.
        self.config_fail_instance_count = config_fail_instance_count
        # The database instances for which the parameters failed to be configured.
        self.config_fail_instance_list = config_fail_instance_list
        # The number of database instances for which the parameters are configured.
        self.config_success_instance_count = config_success_instance_count
        # The database instances for which the parameters are configured.
        self.config_success_instance_list = config_success_instance_list
        # The total number of database instances.
        self.total_instance_count = total_instance_count

    def validate(self):
        if self.config_fail_instance_list:
            for v1 in self.config_fail_instance_list:
                 if v1:
                    v1.validate()
        if self.config_success_instance_list:
            for v1 in self.config_success_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_fail_instance_count is not None:
            result['ConfigFailInstanceCount'] = self.config_fail_instance_count

        result['ConfigFailInstanceList'] = []
        if self.config_fail_instance_list is not None:
            for k1 in self.config_fail_instance_list:
                result['ConfigFailInstanceList'].append(k1.to_map() if k1 else None)

        if self.config_success_instance_count is not None:
            result['ConfigSuccessInstanceCount'] = self.config_success_instance_count

        result['ConfigSuccessInstanceList'] = []
        if self.config_success_instance_list is not None:
            for k1 in self.config_success_instance_list:
                result['ConfigSuccessInstanceList'].append(k1.to_map() if k1 else None)

        if self.total_instance_count is not None:
            result['TotalInstanceCount'] = self.total_instance_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFailInstanceCount') is not None:
            self.config_fail_instance_count = m.get('ConfigFailInstanceCount')

        self.config_fail_instance_list = []
        if m.get('ConfigFailInstanceList') is not None:
            for k1 in m.get('ConfigFailInstanceList'):
                temp_model = main_models.UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList()
                self.config_fail_instance_list.append(temp_model.from_map(k1))

        if m.get('ConfigSuccessInstanceCount') is not None:
            self.config_success_instance_count = m.get('ConfigSuccessInstanceCount')

        self.config_success_instance_list = []
        if m.get('ConfigSuccessInstanceList') is not None:
            for k1 in m.get('ConfigSuccessInstanceList'):
                temp_model = main_models.UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList()
                self.config_success_instance_list.append(temp_model.from_map(k1))

        if m.get('TotalInstanceCount') is not None:
            self.total_instance_count = m.get('TotalInstanceCount')

        return self

class UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList(DaraModel):
    def __init__(
        self,
        config_success: bool = None,
        instance_id: str = None,
    ):
        # Indicates whether the parameters are configured. Valid values:
        # 
        # * **true**
        # 
        # * **false**
        self.config_success = config_success
        # The database instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList(DaraModel):
    def __init__(
        self,
        config_success: bool = None,
        error_message: str = None,
        instance_id: str = None,
    ):
        # Indicates whether the parameters are configured. Valid values:
        # 
        # * **true**
        # 
        # * **false**
        self.config_success = config_success
        # The error message returned.
        self.error_message = error_message
        # The database instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

