# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetContainerDefenseRuleDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetContainerDefenseRuleDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The details of the rule.
        self.data = data
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetContainerDefenseRuleDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetContainerDefenseRuleDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        event_name: str = None,
        event_type: str = None,
        id: int = None,
        rule_action: int = None,
        rule_name: str = None,
        rule_switch: int = None,
        rule_type: str = None,
        scope: List[main_models.GetContainerDefenseRuleDetailResponseBodyDataScope] = None,
        whitelist: main_models.GetContainerDefenseRuleDetailResponseBodyDataWhitelist = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
        # The description of the rule.
        self.description = description
        # The alert name. Valid values:
        # 
        # *   **Non-image Program Startup**
        self.event_name = event_name
        # The alert type. Valid values:
        # 
        # *   **Proactive Defense for Containers**
        self.event_type = event_type
        # The ID of the rule.
        self.id = id
        # The action specified in the rule. Valid values:
        # 
        # *   **1**: alert
        # *   **2**: block
        self.rule_action = rule_action
        # The name of the rule.
        self.rule_name = rule_name
        # The status of the rule. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.rule_switch = rule_switch
        # The type of the rule. Valid values:
        # 
        # *   **1**: system rule
        # *   **2**: custom rule
        self.rule_type = rule_type
        # The effective scope of the rule.
        self.scope = scope
        # The whitelist.
        self.whitelist = whitelist

    def validate(self):
        if self.scope:
            for v1 in self.scope:
                 if v1:
                    v1.validate()
        if self.whitelist:
            self.whitelist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.id is not None:
            result['Id'] = self.id

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        result['Scope'] = []
        if self.scope is not None:
            for k1 in self.scope:
                result['Scope'].append(k1.to_map() if k1 else None)

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        self.scope = []
        if m.get('Scope') is not None:
            for k1 in m.get('Scope'):
                temp_model = main_models.GetContainerDefenseRuleDetailResponseBodyDataScope()
                self.scope.append(temp_model.from_map(k1))

        if m.get('Whitelist') is not None:
            temp_model = main_models.GetContainerDefenseRuleDetailResponseBodyDataWhitelist()
            self.whitelist = temp_model.from_map(m.get('Whitelist'))

        return self

class GetContainerDefenseRuleDetailResponseBodyDataWhitelist(DaraModel):
    def __init__(
        self,
        hash: List[str] = None,
        image: List[str] = None,
        path: List[str] = None,
    ):
        # The hash values of the files that are added to the whitelist.
        # 
        # >  This parameter is not supported.
        self.hash = hash
        # An array consisting of images that are added to the whitelist.
        self.image = image
        # The paths to the files that are added to the whitelist.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hash is not None:
            result['Hash'] = self.hash

        if self.image is not None:
            result['Image'] = self.image

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class GetContainerDefenseRuleDetailResponseBodyDataScope(DaraModel):
    def __init__(
        self,
        all_namespace: int = None,
        cluster_id: str = None,
        namespaces: List[str] = None,
    ):
        # Indicates whether all namespaces are included. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.all_namespace = all_namespace
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # An array that consists of queried namespaces.
        self.namespaces = namespaces

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_namespace is not None:
            result['AllNamespace'] = self.all_namespace

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllNamespace') is not None:
            self.all_namespace = m.get('AllNamespace')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        return self

