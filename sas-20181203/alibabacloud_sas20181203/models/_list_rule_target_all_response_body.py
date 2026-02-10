# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListRuleTargetAllResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_target_list: List[main_models.ListRuleTargetAllResponseBodyRuleTargetList] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the network objects.
        self.rule_target_list = rule_target_list

    def validate(self):
        if self.rule_target_list:
            for v1 in self.rule_target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleTargetList'] = []
        if self.rule_target_list is not None:
            for k1 in self.rule_target_list:
                result['RuleTargetList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_target_list = []
        if m.get('RuleTargetList') is not None:
            for k1 in m.get('RuleTargetList'):
                temp_model = main_models.ListRuleTargetAllResponseBodyRuleTargetList()
                self.rule_target_list.append(temp_model.from_map(k1))

        return self

class ListRuleTargetAllResponseBodyRuleTargetList(DaraModel):
    def __init__(
        self,
        target_id: int = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # The ID of the network object.
        self.target_id = target_id
        # The name of the network object.
        self.target_name = target_name
        # The type of the object. Valid values:
        # 
        # *   IMAGE
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

