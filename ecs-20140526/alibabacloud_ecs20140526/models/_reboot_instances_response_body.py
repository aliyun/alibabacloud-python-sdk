# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class RebootInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_responses: main_models.RebootInstancesResponseBodyInstanceResponses = None,
        request_id: str = None,
    ):
        # Details about instance-specific responses, which contain the status of each instance before and after the operation is called and the results of the operation.
        self.instance_responses = instance_responses
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_responses:
            self.instance_responses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_responses is not None:
            result['InstanceResponses'] = self.instance_responses.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceResponses') is not None:
            temp_model = main_models.RebootInstancesResponseBodyInstanceResponses()
            self.instance_responses = temp_model.from_map(m.get('InstanceResponses'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RebootInstancesResponseBodyInstanceResponses(DaraModel):
    def __init__(
        self,
        instance_response: List[main_models.RebootInstancesResponseBodyInstanceResponsesInstanceResponse] = None,
    ):
        self.instance_response = instance_response

    def validate(self):
        if self.instance_response:
            for v1 in self.instance_response:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceResponse'] = []
        if self.instance_response is not None:
            for k1 in self.instance_response:
                result['InstanceResponse'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_response = []
        if m.get('InstanceResponse') is not None:
            for k1 in m.get('InstanceResponse'):
                temp_model = main_models.RebootInstancesResponseBodyInstanceResponsesInstanceResponse()
                self.instance_response.append(temp_model.from_map(k1))

        return self

class RebootInstancesResponseBodyInstanceResponsesInstanceResponse(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_status: str = None,
        instance_id: str = None,
        message: str = None,
        previous_status: str = None,
    ):
        # The error code returned for the instance. A return value of 200 indicates that the operation is successful. For more information, see the "Error codes" section of this topic.
        self.code = code
        # The current state of the instance.
        self.current_status = current_status
        # The ID of the instance.
        self.instance_id = instance_id
        # The error message that is returned for the operation on the instance. The return value Success indicates that the operation is successful. For more information, see the "Error codes" section of this topic.
        self.message = message
        # The state of the instance before the operation is called.
        self.previous_status = previous_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        if self.previous_status is not None:
            result['PreviousStatus'] = self.previous_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PreviousStatus') is not None:
            self.previous_status = m.get('PreviousStatus')

        return self

