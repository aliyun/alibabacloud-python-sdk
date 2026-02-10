# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateOpaStrategyNewShrinkRequest(DaraModel):
    def __init__(
        self,
        alarm_detail_shrink: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        description: str = None,
        image_name: List[str] = None,
        label: List[str] = None,
        malicious_image: bool = None,
        rule_action: int = None,
        scopes: List[main_models.CreateOpaStrategyNewShrinkRequestScopes] = None,
        strategy_id: int = None,
        strategy_name: str = None,
        strategy_template_id: int = None,
        un_scaned_image: bool = None,
        white_list: List[str] = None,
    ):
        # The risks that you want to detect by using the rule.
        self.alarm_detail_shrink = alarm_detail_shrink
        # The cluster ID.
        # 
        # > This parameter is deprecated.
        self.cluster_id = cluster_id
        # The cluster name.
        # 
        # > This parameter is deprecated.
        self.cluster_name = cluster_name
        # The rule description.
        self.description = description
        # The image names.
        self.image_name = image_name
        # The container tags.
        self.label = label
        # Specifies whether the rule supports malicious Internet images. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.malicious_image = malicious_image
        # The action that is performed when the rule is hit. Valid values:
        # 
        # *   **1**: trigger alerts
        # *   **2**: block
        # *   **3**: allow
        self.rule_action = rule_action
        # The application scope of the rule.
        self.scopes = scopes
        # The rule ID.
        # 
        # >  You can call the [ListOpaClusterStrategyNew](https://help.aliyun.com/document_detail/2623574.html) operation to query the rule ID.
        # 
        # > This parameter is invalid when you create a rule.
        self.strategy_id = strategy_id
        # The rule name.
        self.strategy_name = strategy_name
        # The ID of the rule template.
        # 
        # >  You can call the [GetOpaStrategyTemplateSummary](https://help.aliyun.com/document_detail/2539952.html) operation to query the ID of the rule template.
        self.strategy_template_id = strategy_template_id
        # Specifies whether the rule supports unscanned images. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.un_scaned_image = un_scaned_image
        # The whitelist.
        self.white_list = white_list

    def validate(self):
        if self.scopes:
            for v1 in self.scopes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_detail_shrink is not None:
            result['AlarmDetail'] = self.alarm_detail_shrink

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.description is not None:
            result['Description'] = self.description

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.label is not None:
            result['Label'] = self.label

        if self.malicious_image is not None:
            result['MaliciousImage'] = self.malicious_image

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        result['Scopes'] = []
        if self.scopes is not None:
            for k1 in self.scopes:
                result['Scopes'].append(k1.to_map() if k1 else None)

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.strategy_template_id is not None:
            result['StrategyTemplateId'] = self.strategy_template_id

        if self.un_scaned_image is not None:
            result['UnScanedImage'] = self.un_scaned_image

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmDetail') is not None:
            self.alarm_detail_shrink = m.get('AlarmDetail')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MaliciousImage') is not None:
            self.malicious_image = m.get('MaliciousImage')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        self.scopes = []
        if m.get('Scopes') is not None:
            for k1 in m.get('Scopes'):
                temp_model = main_models.CreateOpaStrategyNewShrinkRequestScopes()
                self.scopes.append(temp_model.from_map(k1))

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StrategyTemplateId') is not None:
            self.strategy_template_id = m.get('StrategyTemplateId')

        if m.get('UnScanedImage') is not None:
            self.un_scaned_image = m.get('UnScanedImage')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

class CreateOpaStrategyNewShrinkRequestScopes(DaraModel):
    def __init__(
        self,
        ack_policy_instance_id: str = None,
        all_namespace: int = None,
        cluster_id: str = None,
        namespace_list: List[str] = None,
    ):
        # The ID of the cluster node to which the rule is applied.
        # 
        # > This parameter is not required when you create the instance.
        self.ack_policy_instance_id = ack_policy_instance_id
        # Specifies whether to include all namespaces. Valid values:
        # 
        # *   **1**: includes all namespaces.
        # *   **0**: does not include all namespaces.
        self.all_namespace = all_namespace
        # The ID of the cluster that is specified in the rule.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](https://help.aliyun.com/document_detail/421736.html) operation to query the cluster ID.
        self.cluster_id = cluster_id
        # The namespaces.
        # 
        # > This parameter is valid only when the AllNamespace parameter is set to 0.
        self.namespace_list = namespace_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_policy_instance_id is not None:
            result['AckPolicyInstanceId'] = self.ack_policy_instance_id

        if self.all_namespace is not None:
            result['AllNamespace'] = self.all_namespace

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckPolicyInstanceId') is not None:
            self.ack_policy_instance_id = m.get('AckPolicyInstanceId')

        if m.get('AllNamespace') is not None:
            self.all_namespace = m.get('AllNamespace')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')

        return self

