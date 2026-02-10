# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetStrategyTemplateDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetStrategyTemplateDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The details of the template.
        self.data = data
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
            temp_model = main_models.GetStrategyTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStrategyTemplateDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        alarm_detail: main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetail = None,
        cluster_id: str = None,
        cluster_name: str = None,
        description: str = None,
        image_name: List[str] = None,
        label: List[str] = None,
        malicious_image: bool = None,
        namespace: List[str] = None,
        rule_action: int = None,
        strategy_id: int = None,
        strategy_name: str = None,
        strategy_template_id: int = None,
        un_scaned_image: bool = None,
        white_list: List[str] = None,
    ):
        # The configuration of the rule.
        self.alarm_detail = alarm_detail
        # The cluster ID.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The description of the rule.
        self.description = description
        # The names of images.
        self.image_name = image_name
        # The tags that are added to the containers.
        self.label = label
        # Indicates whether the rule supports malicious Internet images. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.malicious_image = malicious_image
        # The namespaces.
        self.namespace = namespace
        # The action on requests. Valid values:
        # 
        # *   **1**: trigger alerts
        # *   **2**: block
        # *   **3**: allow
        self.rule_action = rule_action
        # The ID of the rule.
        self.strategy_id = strategy_id
        # The name of the rule.
        self.strategy_name = strategy_name
        # The ID of the template.
        self.strategy_template_id = strategy_template_id
        # Indicates whether the rule supports unscanned images. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.un_scaned_image = un_scaned_image
        # The whitelists of tags that are added to images.
        self.white_list = white_list

    def validate(self):
        if self.alarm_detail:
            self.alarm_detail.validate()

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

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

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
            temp_model = main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetail()
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

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

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

class GetStrategyTemplateDetailResponseBodyDataAlarmDetail(DaraModel):
    def __init__(
        self,
        baseline: main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailBaseline = None,
        malicious_file: main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailMaliciousFile = None,
        vul: main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailVul = None,
    ):
        # The configuration of the baseline.
        self.baseline = baseline
        # The configuration of the alert rule for the malicious sample.
        self.malicious_file = malicious_file
        # The configuration of the vulnerability detection rule.
        self.vul = vul

    def validate(self):
        if self.baseline:
            self.baseline.validate()
        if self.malicious_file:
            self.malicious_file.validate()
        if self.vul:
            self.vul.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline is not None:
            result['Baseline'] = self.baseline.to_map()

        if self.malicious_file is not None:
            result['MaliciousFile'] = self.malicious_file.to_map()

        if self.vul is not None:
            result['Vul'] = self.vul.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Baseline') is not None:
            temp_model = main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailBaseline()
            self.baseline = temp_model.from_map(m.get('Baseline'))

        if m.get('MaliciousFile') is not None:
            temp_model = main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailMaliciousFile()
            self.malicious_file = temp_model.from_map(m.get('MaliciousFile'))

        if m.get('Vul') is not None:
            temp_model = main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailVul()
            self.vul = temp_model.from_map(m.get('Vul'))

        return self

class GetStrategyTemplateDetailResponseBodyDataAlarmDetailVul(DaraModel):
    def __init__(
        self,
        item: List[main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailVulItem] = None,
        risk_level: List[str] = None,
    ):
        # The items on which vulnerabilities are detected.
        self.item = item
        # The severities of the vulnerabilities.
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
                temp_model = main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailVulItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class GetStrategyTemplateDetailResponseBodyDataAlarmDetailVulItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the vulnerability.
        self.id = id
        # The alias of the vulnerability.
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

class GetStrategyTemplateDetailResponseBodyDataAlarmDetailMaliciousFile(DaraModel):
    def __init__(
        self,
        item: List[main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailMaliciousFileItem] = None,
        risk_level: List[str] = None,
    ):
        # The items on which malicious samples are detected.
        self.item = item
        # The severities of the malicious samples.
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
                temp_model = main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailMaliciousFileItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class GetStrategyTemplateDetailResponseBodyDataAlarmDetailMaliciousFileItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The unique identifier of the malicious sample.
        self.id = id
        # The name of the malicious sample.
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

class GetStrategyTemplateDetailResponseBodyDataAlarmDetailBaseline(DaraModel):
    def __init__(
        self,
        item: List[main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailBaselineItem] = None,
        risk_level: List[str] = None,
    ):
        # The baseline items.
        self.item = item
        # The severities of the baselines. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
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
                temp_model = main_models.GetStrategyTemplateDetailResponseBodyDataAlarmDetailBaselineItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class GetStrategyTemplateDetailResponseBodyDataAlarmDetailBaselineItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The unique identifier of the baseline check item.
        self.id = id
        # The name of the baseline check item.
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

