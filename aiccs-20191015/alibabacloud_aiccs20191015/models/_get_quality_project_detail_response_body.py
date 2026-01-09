# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetQualityProjectDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQualityProjectDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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
            temp_model = main_models.GetQualityProjectDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityProjectDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        check_freq_type: int = None,
        create_time: str = None,
        dep_list: List[int] = None,
        group_list: List[int] = None,
        id: int = None,
        modify_time: str = None,
        project_name: str = None,
        quality_rule_ids: List[int] = None,
        quality_type: int = None,
        servicer_list: List[int] = None,
        status: int = None,
        version: int = None,
    ):
        self.check_freq_type = check_freq_type
        self.create_time = create_time
        self.dep_list = dep_list
        self.group_list = group_list
        self.id = id
        self.modify_time = modify_time
        self.project_name = project_name
        self.quality_rule_ids = quality_rule_ids
        self.quality_type = quality_type
        self.servicer_list = servicer_list
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dep_list is not None:
            result['DepList'] = self.dep_list

        if self.group_list is not None:
            result['GroupList'] = self.group_list

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quality_rule_ids is not None:
            result['QualityRuleIds'] = self.quality_rule_ids

        if self.quality_type is not None:
            result['QualityType'] = self.quality_type

        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')

        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('QualityRuleIds') is not None:
            self.quality_rule_ids = m.get('QualityRuleIds')

        if m.get('QualityType') is not None:
            self.quality_type = m.get('QualityType')

        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

