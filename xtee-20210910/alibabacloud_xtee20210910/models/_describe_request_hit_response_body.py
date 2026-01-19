# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeRequestHitResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeRequestHitResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeRequestHitResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeRequestHitResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_name: str = None,
        inputs: str = None,
        outputs: str = None,
        request_time: int = None,
        rule_hit_records: List[main_models.DescribeRequestHitResponseBodyResultObjectRuleHitRecords] = None,
        s_request_id: str = None,
        total_cost: int = None,
    ):
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Input parameters.
        self.inputs = inputs
        # Output parameters
        self.outputs = outputs
        # Timestamp of the request.
        self.request_time = request_time
        # Details of the executed rules.
        self.rule_hit_records = rule_hit_records
        # Request ID
        self.s_request_id = s_request_id
        # Total amount of the request
        self.total_cost = total_cost

    def validate(self):
        if self.rule_hit_records:
            for v1 in self.rule_hit_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.request_time is not None:
            result['requestTime'] = self.request_time

        result['ruleHitRecords'] = []
        if self.rule_hit_records is not None:
            for k1 in self.rule_hit_records:
                result['ruleHitRecords'].append(k1.to_map() if k1 else None)

        if self.s_request_id is not None:
            result['sRequestId'] = self.s_request_id

        if self.total_cost is not None:
            result['totalCost'] = self.total_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')

        self.rule_hit_records = []
        if m.get('ruleHitRecords') is not None:
            for k1 in m.get('ruleHitRecords'):
                temp_model = main_models.DescribeRequestHitResponseBodyResultObjectRuleHitRecords()
                self.rule_hit_records.append(temp_model.from_map(k1))

        if m.get('sRequestId') is not None:
            self.s_request_id = m.get('sRequestId')

        if m.get('totalCost') is not None:
            self.total_cost = m.get('totalCost')

        return self

class DescribeRequestHitResponseBodyResultObjectRuleHitRecords(DaraModel):
    def __init__(
        self,
        cost: int = None,
        hit_successful: bool = None,
        is_show_detail: bool = None,
        order: int = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_snapshot_id: str = None,
        rule_status: str = None,
    ):
        # Duration
        self.cost = cost
        # Whether the rule was hit.
        self.hit_successful = hit_successful
        # Whether to show details
        self.is_show_detail = is_show_detail
        # Order.
        self.order = order
        # Policy ID
        self.rule_id = rule_id
        # Policy name
        self.rule_name = rule_name
        # Rule snapshot ID
        self.rule_snapshot_id = rule_snapshot_id
        # Policy status
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.hit_successful is not None:
            result['hitSuccessful'] = self.hit_successful

        if self.is_show_detail is not None:
            result['isShowDetail'] = self.is_show_detail

        if self.order is not None:
            result['order'] = self.order

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.rule_snapshot_id is not None:
            result['ruleSnapshotId'] = self.rule_snapshot_id

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('hitSuccessful') is not None:
            self.hit_successful = m.get('hitSuccessful')

        if m.get('isShowDetail') is not None:
            self.is_show_detail = m.get('isShowDetail')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('ruleSnapshotId') is not None:
            self.rule_snapshot_id = m.get('ruleSnapshotId')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        return self

