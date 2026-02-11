# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudSiemEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeCloudSiemEventDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeCloudSiemEventDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCloudSiemEventDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_num: int = None,
        aliuid: int = None,
        asset_num: int = None,
        att_ck_labels: List[str] = None,
        attck_stages: List[main_models.DescribeCloudSiemEventDetailResponseBodyDataAttckStages] = None,
        data_sources: List[str] = None,
        description: str = None,
        description_en: str = None,
        ext_content: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        incident_name: str = None,
        incident_name_en: str = None,
        incident_type: str = None,
        incident_uuid: str = None,
        refer_account: str = None,
        remark: str = None,
        rule_id: str = None,
        status: int = None,
        threat_level: str = None,
        threat_score: float = None,
    ):
        # The number of alerts that are associated with the event.
        self.alert_num = alert_num
        # The ID of the Alibaba Cloud account to which the event belongs.
        self.aliuid = aliuid
        # The number of assets that are associated with the event.
        self.asset_num = asset_num
        # The tags of the ATT\\&CK attacks.
        self.att_ck_labels = att_ck_labels
        self.attck_stages = attck_stages
        # The source of the alert.
        self.data_sources = data_sources
        # The description of the event.
        self.description = description
        # The description of the event in English.
        self.description_en = description_en
        # The extended information of the event in the JSON format.
        self.ext_content = ext_content
        # The time when the event occurred.
        self.gmt_create = gmt_create
        # The time when the event was last updated.
        self.gmt_modified = gmt_modified
        # The name of the event.
        self.incident_name = incident_name
        # The name of the event in English.
        self.incident_name_en = incident_name_en
        self.incident_type = incident_type
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        # Users associated with the event.
        self.refer_account = refer_account
        # The remarks of the event.
        self.remark = remark
        self.rule_id = rule_id
        # The status of the event. Valid values:
        # 
        # *   0: not handled
        # *   1: handing
        # *   5: handling failed
        # *   10: handled
        self.status = status
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level
        # The risk score of the event. The score ranges from 0 to 100. A higher score indicates a higher risk level.
        self.threat_score = threat_score

    def validate(self):
        if self.attck_stages:
            for v1 in self.attck_stages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num

        if self.att_ck_labels is not None:
            result['AttCkLabels'] = self.att_ck_labels

        result['AttckStages'] = []
        if self.attck_stages is not None:
            for k1 in self.attck_stages:
                result['AttckStages'].append(k1.to_map() if k1 else None)

        if self.data_sources is not None:
            result['DataSources'] = self.data_sources

        if self.description is not None:
            result['Description'] = self.description

        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en

        if self.ext_content is not None:
            result['ExtContent'] = self.ext_content

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name

        if self.incident_name_en is not None:
            result['IncidentNameEn'] = self.incident_name_en

        if self.incident_type is not None:
            result['IncidentType'] = self.incident_type

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.refer_account is not None:
            result['ReferAccount'] = self.refer_account

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.status is not None:
            result['Status'] = self.status

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')

        if m.get('AttCkLabels') is not None:
            self.att_ck_labels = m.get('AttCkLabels')

        self.attck_stages = []
        if m.get('AttckStages') is not None:
            for k1 in m.get('AttckStages'):
                temp_model = main_models.DescribeCloudSiemEventDetailResponseBodyDataAttckStages()
                self.attck_stages.append(temp_model.from_map(k1))

        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')

        if m.get('ExtContent') is not None:
            self.ext_content = m.get('ExtContent')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')

        if m.get('IncidentNameEn') is not None:
            self.incident_name_en = m.get('IncidentNameEn')

        if m.get('IncidentType') is not None:
            self.incident_type = m.get('IncidentType')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('ReferAccount') is not None:
            self.refer_account = m.get('ReferAccount')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')

        return self

class DescribeCloudSiemEventDetailResponseBodyDataAttckStages(DaraModel):
    def __init__(
        self,
        alert_num: int = None,
        tactic_id: str = None,
        tactic_name: str = None,
    ):
        self.alert_num = alert_num
        self.tactic_id = tactic_id
        self.tactic_name = tactic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num

        if self.tactic_id is not None:
            result['TacticId'] = self.tactic_id

        if self.tactic_name is not None:
            result['TacticName'] = self.tactic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')

        if m.get('TacticId') is not None:
            self.tactic_id = m.get('TacticId')

        if m.get('TacticName') is not None:
            self.tactic_name = m.get('TacticName')

        return self

