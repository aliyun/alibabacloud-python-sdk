# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class HandleObjectScanEventRequest(DaraModel):
    def __init__(
        self,
        batch_type: str = None,
        event_id: str = None,
        event_id_list: List[int] = None,
        lang: str = None,
        remark: str = None,
        rule_condition_list: List[main_models.HandleObjectScanEventRequestRuleConditionList] = None,
        status: int = None,
    ):
        self.batch_type = batch_type
        self.event_id = event_id
        self.event_id_list = event_id_list
        self.lang = lang
        self.remark = remark
        self.rule_condition_list = rule_condition_list
        self.status = status

    def validate(self):
        if self.rule_condition_list:
            for v1 in self.rule_condition_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_id_list is not None:
            result['EventIdList'] = self.event_id_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.remark is not None:
            result['Remark'] = self.remark

        result['RuleConditionList'] = []
        if self.rule_condition_list is not None:
            for k1 in self.rule_condition_list:
                result['RuleConditionList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventIdList') is not None:
            self.event_id_list = m.get('EventIdList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        self.rule_condition_list = []
        if m.get('RuleConditionList') is not None:
            for k1 in m.get('RuleConditionList'):
                temp_model = main_models.HandleObjectScanEventRequestRuleConditionList()
                self.rule_condition_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class HandleObjectScanEventRequestRuleConditionList(DaraModel):
    def __init__(
        self,
        key: str = None,
        operate: str = None,
        value: str = None,
    ):
        self.key = key
        self.operate = operate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operate is not None:
            result['Operate'] = self.operate

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

