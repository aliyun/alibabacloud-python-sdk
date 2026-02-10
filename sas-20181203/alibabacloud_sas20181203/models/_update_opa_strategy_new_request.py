# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class UpdateOpaStrategyNewRequest(DaraModel):
    def __init__(
        self,
        alarm_detail: main_models.UpdateOpaStrategyNewRequestAlarmDetail = None,
        cluster_id: str = None,
        cluster_name: str = None,
        description: str = None,
        image_name: List[str] = None,
        label: List[str] = None,
        malicious_image: bool = None,
        rule_action: int = None,
        scopes: List[main_models.UpdateOpaStrategyNewRequestScopes] = None,
        strategy_id: int = None,
        strategy_name: str = None,
        strategy_template_id: int = None,
        un_scaned_image: bool = None,
        white_list: List[str] = None,
    ):
        # The risks that you want to detect by using the rule.
        self.alarm_detail = alarm_detail
        # The cluster ID.
        # 
        # > This parameter is deprecated. You can use the Scopes parameter to specify a scope in which cluster parameters take effect.
        self.cluster_id = cluster_id
        # The cluster name.
        # 
        # > This parameter is deprecated.
        self.cluster_name = cluster_name
        # The rule description.
        self.description = description
        # The image names.
        self.image_name = image_name
        # The image tags.
        self.label = label
        # Specifies whether the rule supports malicious Internet images. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.malicious_image = malicious_image
        # The action that is performed when the rule is hit. Valid values:
        # 
        # *   **1**: alert
        # *   **2**: block
        # *   **3**: allow
        self.rule_action = rule_action
        # The application scope.
        self.scopes = scopes
        # The ID of the rule.
        # 
        # >  You can call the [ListOpaClusterStrategyNew](https://help.aliyun.com/document_detail/2623574.html) operation to query the ID.
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
        # The whitelists.
        self.white_list = white_list

    def validate(self):
        if self.alarm_detail:
            self.alarm_detail.validate()
        if self.scopes:
            for v1 in self.scopes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_detail is not None:
            result['AlarmDetail'] = self.alarm_detail.to_map()

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
            temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetail()
            self.alarm_detail = temp_model.from_map(m.get('AlarmDetail'))

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
                temp_model = main_models.UpdateOpaStrategyNewRequestScopes()
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

class UpdateOpaStrategyNewRequestScopes(DaraModel):
    def __init__(
        self,
        ack_policy_instance_id: str = None,
        all_namespace: int = None,
        cluster_id: str = None,
        namespace_list: List[str] = None,
    ):
        # The ID of the cluster node to which the rule is applied.
        # 
        # >  You can call the [GetOpaStrategyDetailNew](~~GetOpaStrategyDetailNew~~) operation to query the ID of the cluster node to which the rule is applied.
        self.ack_policy_instance_id = ack_policy_instance_id
        # Specifies whether all namespaces are included. Valid values:
        # 
        # *   **0**: Not all namespaces are included.
        # *   **1**: All namespaces are included.
        self.all_namespace = all_namespace
        # The cluster ID.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the cluster ID.
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

class UpdateOpaStrategyNewRequestAlarmDetail(DaraModel):
    def __init__(
        self,
        baseline: main_models.UpdateOpaStrategyNewRequestAlarmDetailBaseline = None,
        build_risk: main_models.UpdateOpaStrategyNewRequestAlarmDetailBuildRisk = None,
        malicious_file: main_models.UpdateOpaStrategyNewRequestAlarmDetailMaliciousFile = None,
        sensitive_file: main_models.UpdateOpaStrategyNewRequestAlarmDetailSensitiveFile = None,
        vul: main_models.UpdateOpaStrategyNewRequestAlarmDetailVul = None,
    ):
        # The baseline risks.
        self.baseline = baseline
        # The configuration of image build risk.
        self.build_risk = build_risk
        # The malicious sample risks.
        self.malicious_file = malicious_file
        # The configuration of sensitive file.
        self.sensitive_file = sensitive_file
        # The vulnerability risks.
        self.vul = vul

    def validate(self):
        if self.baseline:
            self.baseline.validate()
        if self.build_risk:
            self.build_risk.validate()
        if self.malicious_file:
            self.malicious_file.validate()
        if self.sensitive_file:
            self.sensitive_file.validate()
        if self.vul:
            self.vul.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline is not None:
            result['Baseline'] = self.baseline.to_map()

        if self.build_risk is not None:
            result['BuildRisk'] = self.build_risk.to_map()

        if self.malicious_file is not None:
            result['MaliciousFile'] = self.malicious_file.to_map()

        if self.sensitive_file is not None:
            result['SensitiveFile'] = self.sensitive_file.to_map()

        if self.vul is not None:
            result['Vul'] = self.vul.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Baseline') is not None:
            temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailBaseline()
            self.baseline = temp_model.from_map(m.get('Baseline'))

        if m.get('BuildRisk') is not None:
            temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailBuildRisk()
            self.build_risk = temp_model.from_map(m.get('BuildRisk'))

        if m.get('MaliciousFile') is not None:
            temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailMaliciousFile()
            self.malicious_file = temp_model.from_map(m.get('MaliciousFile'))

        if m.get('SensitiveFile') is not None:
            temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailSensitiveFile()
            self.sensitive_file = temp_model.from_map(m.get('SensitiveFile'))

        if m.get('Vul') is not None:
            temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailVul()
            self.vul = temp_model.from_map(m.get('Vul'))

        return self

class UpdateOpaStrategyNewRequestAlarmDetailVul(DaraModel):
    def __init__(
        self,
        item: List[main_models.UpdateOpaStrategyNewRequestAlarmDetailVulItem] = None,
        risk_class: List[main_models.UpdateOpaStrategyNewRequestAlarmDetailVulRiskClass] = None,
        risk_level: List[str] = None,
    ):
        # The vulnerabilities.
        self.item = item
        # Risk type of vulnerability.
        self.risk_class = risk_class
        # The risk levels.
        self.risk_level = risk_level

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()
        if self.risk_class:
            for v1 in self.risk_class:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        result['RiskClass'] = []
        if self.risk_class is not None:
            for k1 in self.risk_class:
                result['RiskClass'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailVulItem()
                self.item.append(temp_model.from_map(k1))

        self.risk_class = []
        if m.get('RiskClass') is not None:
            for k1 in m.get('RiskClass'):
                temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailVulRiskClass()
                self.risk_class.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailVulRiskClass(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the vulnerability types. Valid values:
        # 
        # *   **cve**: system vulnerability
        # *   **app**: application vulnerability
        self.id = id
        # The name of the vulnerability. Valid values:
        # 
        # *   **system vulnerability**
        # *   **application vulnerability**
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailVulItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the vulnerability.
        # 
        # >  You can call the [DescribeVulListPage](https://help.aliyun.com/document_detail/471928.html) operation to query the ID.
        self.id = id
        # The name of the vulnerability.
        # 
        # >  You can call the [DescribeVulListPage](https://help.aliyun.com/document_detail/471928.html) operation to query the name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailSensitiveFile(DaraModel):
    def __init__(
        self,
        item: List[main_models.UpdateOpaStrategyNewRequestAlarmDetailSensitiveFileItem] = None,
        risk_level: List[str] = None,
    ):
        # The configuration of sensitive file.
        self.item = item
        # The risk levels.
        self.risk_level = risk_level

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailSensitiveFileItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailSensitiveFileItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the sensitive files.
        # 
        # >  You can call the [GetSensitiveDefineRuleConfig](~~GetSensitiveDefineRuleConfig~~) operation to query the ID of the malicious sample.
        self.id = id
        # The name of the sensitive files.
        # 
        # >  You can call the [GetSensitiveDefineRuleConfig](~~GetSensitiveDefineRuleConfig~~) operation to query the ID of the malicious sample.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailMaliciousFile(DaraModel):
    def __init__(
        self,
        item: List[main_models.UpdateOpaStrategyNewRequestAlarmDetailMaliciousFileItem] = None,
        risk_level: List[str] = None,
    ):
        # The malicious samples.
        self.item = item
        # The risk levels.
        self.risk_level = risk_level

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailMaliciousFileItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailMaliciousFileItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the malicious sample.
        # 
        # >  You can call the [DescribeMatchedMaliciousNames](~~DescribeMatchedMaliciousNames~~) operation to query the ID.
        self.id = id
        # The name of the malicious sample.
        # 
        # >  You can call the [DescribeMatchedMaliciousNames](~~DescribeMatchedMaliciousNames~~) operation to query the name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailBuildRisk(DaraModel):
    def __init__(
        self,
        item: List[main_models.UpdateOpaStrategyNewRequestAlarmDetailBuildRiskItem] = None,
        risk_level: List[str] = None,
    ):
        # The configuration of image build risk.
        self.item = item
        # The risk levels.
        self.risk_level = risk_level

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailBuildRiskItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailBuildRiskItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the image build risk.
        # 
        # >  You can call the [ListImageBuildRiskItem](~~ListImageBuildRiskItem~~) operation to query the ID of the malicious sample.
        self.id = id
        # The name of the image build risk.
        # 
        # >  You can call the [ListImageBuildRiskItem](~~ListImageBuildRiskItem~~) operation to query the ID of the malicious sample.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailBaseline(DaraModel):
    def __init__(
        self,
        item: List[main_models.UpdateOpaStrategyNewRequestAlarmDetailBaselineItem] = None,
        risk_level: List[str] = None,
    ):
        # The baseline check items.
        self.item = item
        # The risk levels.
        self.risk_level = risk_level

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.UpdateOpaStrategyNewRequestAlarmDetailBaselineItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class UpdateOpaStrategyNewRequestAlarmDetailBaselineItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the baseline check item.
        # 
        # >  You can call the [GetOpaClusterBaseLineList](https://help.aliyun.com/document_detail/2539883.html) operation to query the ID.
        self.id = id
        # The name of the baseline check item.
        # 
        # >  You can call the [GetOpaClusterBaseLineList](https://help.aliyun.com/document_detail/2539883.html) operation to query the name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

