# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecRulesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecRulesResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The policies.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApisecRulesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisecRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        id: int = None,
        rule: str = None,
        status: int = None,
        type: str = None,
        update_time: int = None,
    ):
        # The ID of the policy.
        self.id = id
        # The details of the policy. The value is a string that consists of multiple parameters in the JSON format.
        self.rule = rule
        # The status of the policy. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.status = status
        # The type of the policy. Valid values:
        # 
        # *   **risk**: risk detection
        # *   **event**: security event
        # *   **sensitive_word**: sensitive data
        # *   **auth_flag**: authentication credential
        # *   **api_tag**: business purpose
        # *   **desensitization**: data masking
        # *   **whitelist**: whitelist
        # *   **recognition**: API recognition
        # *   **offline_api**: lifecycle management
        self.type = type
        # The time when the policy was updated. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

