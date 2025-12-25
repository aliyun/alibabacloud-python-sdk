# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class UpdateSLARulesRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        sla_rule_list: List[main_models.UpdateSLARulesRequestSlaRuleList] = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The list of SLA rules.
        self.sla_rule_list = sla_rule_list
        # The ID of the tenant.
        # 
        # > :To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        if self.sla_rule_list:
            for v1 in self.sla_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        result['SlaRuleList'] = []
        if self.sla_rule_list is not None:
            for k1 in self.sla_rule_list:
                result['SlaRuleList'].append(k1.to_map() if k1 else None)

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        self.sla_rule_list = []
        if m.get('SlaRuleList') is not None:
            for k1 in m.get('SlaRuleList'):
                temp_model = main_models.UpdateSLARulesRequestSlaRuleList()
                self.sla_rule_list.append(temp_model.from_map(k1))

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class UpdateSLARulesRequestSlaRuleList(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        interval_minutes: int = None,
        node_id: int = None,
        type: int = None,
    ):
        # The ID of the task flow.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The timeout period. Unit: minutes.
        # 
        # This parameter is required.
        self.interval_minutes = interval_minutes
        # The ID of the task node.
        self.node_id = node_id
        # The rule type. Valid values:
        # 
        # *   **0**: SLA rules for task flows
        # *   **1**: SLA rules for nodes
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.interval_minutes is not None:
            result['IntervalMinutes'] = self.interval_minutes

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('IntervalMinutes') is not None:
            self.interval_minutes = m.get('IntervalMinutes')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

