# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetInterceptionRuleDetailResponseBody(DaraModel):
    def __init__(
        self,
        interception_rule_detail: main_models.GetInterceptionRuleDetailResponseBodyInterceptionRuleDetail = None,
        request_id: str = None,
    ):
        # The details of the rule.
        self.interception_rule_detail = interception_rule_detail
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.interception_rule_detail:
            self.interception_rule_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interception_rule_detail is not None:
            result['InterceptionRuleDetail'] = self.interception_rule_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InterceptionRuleDetail') is not None:
            temp_model = main_models.GetInterceptionRuleDetailResponseBodyInterceptionRuleDetail()
            self.interception_rule_detail = temp_model.from_map(m.get('InterceptionRuleDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInterceptionRuleDetailResponseBodyInterceptionRuleDetail(DaraModel):
    def __init__(
        self,
        dst_target: main_models.GetInterceptionRuleDetailResponseBodyInterceptionRuleDetailDstTarget = None,
        intercept_type: int = None,
        order_index: int = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_switch: int = None,
        rule_type: str = None,
        src_target: main_models.GetInterceptionRuleDetailResponseBodyInterceptionRuleDetailSrcTarget = None,
    ):
        # The destination network object.
        self.dst_target = dst_target
        # The interception mode. Valid values:
        # 
        # *   **0**: monitor
        # *   **1**: block
        # *   **2**: alert
        # *   **3**: allow
        self.intercept_type = intercept_type
        # The priority of the rule. Valid values: 1 to 1000. A smaller value indicates a higher priority.
        self.order_index = order_index
        # The ID of the rule.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # The status of the defense rule. Valid values:
        # 
        # *   **1**: The rule is enabled.
        # *   **0**: The rule is disabled.
        self.rule_switch = rule_switch
        # The type of the rule. Valid values:
        # 
        # *   **suggest**: a suggestion rule
        # *   **customize**: a custom rule
        self.rule_type = rule_type
        # The source network object.
        self.src_target = src_target

    def validate(self):
        if self.dst_target:
            self.dst_target.validate()
        if self.src_target:
            self.src_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_target is not None:
            result['DstTarget'] = self.dst_target.to_map()

        if self.intercept_type is not None:
            result['InterceptType'] = self.intercept_type

        if self.order_index is not None:
            result['OrderIndex'] = self.order_index

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.src_target is not None:
            result['SrcTarget'] = self.src_target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstTarget') is not None:
            temp_model = main_models.GetInterceptionRuleDetailResponseBodyInterceptionRuleDetailDstTarget()
            self.dst_target = temp_model.from_map(m.get('DstTarget'))

        if m.get('InterceptType') is not None:
            self.intercept_type = m.get('InterceptType')

        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SrcTarget') is not None:
            temp_model = main_models.GetInterceptionRuleDetailResponseBodyInterceptionRuleDetailSrcTarget()
            self.src_target = temp_model.from_map(m.get('SrcTarget'))

        return self

class GetInterceptionRuleDetailResponseBodyInterceptionRuleDetailSrcTarget(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        image_list: List[str] = None,
        namespace: str = None,
        rule_type: str = None,
        tag_list: List[str] = None,
        target_id: int = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The images of the network object.
        self.image_list = image_list
        # The namespace to which the network object belongs.
        self.namespace = namespace
        # The type of the rule.
        self.rule_type = rule_type
        # The labels specified for the network object.
        self.tag_list = tag_list
        # The ID of the network object.
        self.target_id = target_id
        # The name of the object.
        self.target_name = target_name
        # The type of the network object.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.image_list is not None:
            result['ImageList'] = self.image_list

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class GetInterceptionRuleDetailResponseBodyInterceptionRuleDetailDstTarget(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        image_list: List[str] = None,
        namespace: str = None,
        ports: List[str] = None,
        rule_type: str = None,
        tag_list: List[str] = None,
        target_id: int = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # An array that consists of the name of the image specified for the network object.
        self.image_list = image_list
        # The namespace to which the network object belongs.
        self.namespace = namespace
        # An array that consists of the port range of the destination network object.
        self.ports = ports
        # The type of the rule.
        self.rule_type = rule_type
        # An array that consists of the labels specified for the network object.
        self.tag_list = tag_list
        # The ID of the network object.
        self.target_id = target_id
        # The name of the object.
        self.target_name = target_name
        # The type of the network object.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.image_list is not None:
            result['ImageList'] = self.image_list

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.ports is not None:
            result['Ports'] = self.ports

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Ports') is not None:
            self.ports = m.get('Ports')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

