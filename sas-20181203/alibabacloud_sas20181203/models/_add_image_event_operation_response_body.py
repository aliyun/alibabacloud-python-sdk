# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddImageEventOperationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddImageEventOperationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
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
            temp_model = main_models.AddImageEventOperationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddImageEventOperationResponseBodyData(DaraModel):
    def __init__(
        self,
        conditions: str = None,
        event_key: str = None,
        event_name: str = None,
        event_type: str = None,
        id: int = None,
        operation_code: str = None,
        scenarios: str = None,
    ):
        # The rule conditions. The value is in the JSON format. Valid values of keys:
        # 
        # *   **condition**: the matching condition.
        # *   **type**: the matching type.
        # *   **value**: the matching value.
        self.conditions = conditions
        # The keyword of the alert item.
        self.event_key = event_key
        # The name of the alert item.
        self.event_name = event_name
        # The alert type.
        # 
        # *   Only **sensitiveFile** may be returned.
        self.event_type = event_type
        # The primary key of the alert handling rule.
        self.id = id
        # The operation code.
        # 
        # *   Only **whitelist** may be returned, which indicates that the alert item is added to the whitelist.
        self.operation_code = operation_code
        # The application scope of the rule. The value is in the JSON format. Valid values of keys:
        # 
        # *   **type**
        # *   **value**
        self.scenarios = scenarios

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditions is not None:
            result['Conditions'] = self.conditions

        if self.event_key is not None:
            result['EventKey'] = self.event_key

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.id is not None:
            result['Id'] = self.id

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.scenarios is not None:
            result['Scenarios'] = self.scenarios

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')

        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('Scenarios') is not None:
            self.scenarios = m.get('Scenarios')

        return self

