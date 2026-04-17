# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetRiskListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetRiskListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetRiskListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRiskListResponseBodyData(DaraModel):
    def __init__(
        self,
        risk_list: List[main_models.GetRiskListResponseBodyDataRiskList] = None,
        total: int = None,
    ):
        self.risk_list = risk_list
        self.total = total

    def validate(self):
        if self.risk_list:
            for v1 in self.risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RiskList'] = []
        if self.risk_list is not None:
            for k1 in self.risk_list:
                result['RiskList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.risk_list = []
        if m.get('RiskList') is not None:
            for k1 in m.get('RiskList'):
                temp_model = main_models.GetRiskListResponseBodyDataRiskList()
                self.risk_list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetRiskListResponseBodyDataRiskList(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        grade_type: str = None,
        health: bool = None,
        instance_id: str = None,
        last_alarm_time: int = None,
        level_type: int = None,
        modified_time: int = None,
        name: str = None,
        owner: str = None,
        relation_list: List[str] = None,
        report_tips: str = None,
        report_type: str = None,
        report_value: str = None,
        status: int = None,
        type: str = None,
        value: str = None,
    ):
        self.create_time = create_time
        self.grade_type = grade_type
        self.health = health
        self.instance_id = instance_id
        self.last_alarm_time = last_alarm_time
        self.level_type = level_type
        self.modified_time = modified_time
        self.name = name
        self.owner = owner
        self.relation_list = relation_list
        self.report_tips = report_tips
        self.report_type = report_type
        self.report_value = report_value
        self.status = status
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.grade_type is not None:
            result['GradeType'] = self.grade_type

        if self.health is not None:
            result['Health'] = self.health

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_alarm_time is not None:
            result['LastAlarmTime'] = self.last_alarm_time

        if self.level_type is not None:
            result['LevelType'] = self.level_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.relation_list is not None:
            result['RelationList'] = self.relation_list

        if self.report_tips is not None:
            result['ReportTips'] = self.report_tips

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.report_value is not None:
            result['ReportValue'] = self.report_value

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GradeType') is not None:
            self.grade_type = m.get('GradeType')

        if m.get('Health') is not None:
            self.health = m.get('Health')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastAlarmTime') is not None:
            self.last_alarm_time = m.get('LastAlarmTime')

        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RelationList') is not None:
            self.relation_list = m.get('RelationList')

        if m.get('ReportTips') is not None:
            self.report_tips = m.get('ReportTips')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('ReportValue') is not None:
            self.report_value = m.get('ReportValue')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

