# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class QueryAttackCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.QueryAttackCountResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The number of entries returned on the current page.
        self.count = count
        # An array that consists of the numbers of alert events in different attack phases.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether exceptions are handled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryAttackCountResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAttackCountResponseBodyData(DaraModel):
    def __init__(
        self,
        event_count: int = None,
        tactic_id: str = None,
        tactic_type: str = None,
    ):
        # The number of times that the alert is triggered.
        self.event_count = event_count
        # The stage ID of the ATT\\&CK attack.
        self.tactic_id = tactic_id
        # The type of stage of the ATT\\&CK attack.
        self.tactic_type = tactic_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.tactic_id is not None:
            result['TacticId'] = self.tactic_id

        if self.tactic_type is not None:
            result['TacticType'] = self.tactic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('TacticId') is not None:
            self.tactic_id = m.get('TacticId')

        if m.get('TacticType') is not None:
            self.tactic_type = m.get('TacticType')

        return self

