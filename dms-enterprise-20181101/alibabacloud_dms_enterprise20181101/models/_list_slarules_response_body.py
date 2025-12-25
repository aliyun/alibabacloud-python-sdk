# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSLARulesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        slarule_list: main_models.ListSLARulesResponseBodySLARuleList = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # The list of SLA rules.
        self.slarule_list = slarule_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.slarule_list:
            self.slarule_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slarule_list is not None:
            result['SLARuleList'] = self.slarule_list.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SLARuleList') is not None:
            temp_model = main_models.ListSLARulesResponseBodySLARuleList()
            self.slarule_list = temp_model.from_map(m.get('SLARuleList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSLARulesResponseBodySLARuleList(DaraModel):
    def __init__(
        self,
        slarule: List[main_models.ListSLARulesResponseBodySLARuleListSLARule] = None,
    ):
        self.slarule = slarule

    def validate(self):
        if self.slarule:
            for v1 in self.slarule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SLARule'] = []
        if self.slarule is not None:
            for k1 in self.slarule:
                result['SLARule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slarule = []
        if m.get('SLARule') is not None:
            for k1 in m.get('SLARule'):
                temp_model = main_models.ListSLARulesResponseBodySLARuleListSLARule()
                self.slarule.append(temp_model.from_map(k1))

        return self

class ListSLARulesResponseBodySLARuleListSLARule(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        id: int = None,
        interval_minutes: int = None,
        node_id: int = None,
        rule_type: int = None,
    ):
        # The ID of the task flow.
        self.dag_id = dag_id
        # The ID of the SLA rule.
        self.id = id
        # The timeout period. Unit: minutes.
        self.interval_minutes = interval_minutes
        # The ID of the task node.
        self.node_id = node_id
        # The type of the rule. Valid values:
        # 
        # *   **0**: an SLA rule for a task flow
        # *   **1**: an SLA rule for a task node
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.id is not None:
            result['Id'] = self.id

        if self.interval_minutes is not None:
            result['IntervalMinutes'] = self.interval_minutes

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IntervalMinutes') is not None:
            self.interval_minutes = m.get('IntervalMinutes')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

