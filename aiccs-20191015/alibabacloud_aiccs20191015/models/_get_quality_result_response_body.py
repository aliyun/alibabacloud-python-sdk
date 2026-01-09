# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetQualityResultResponseBody(DaraModel):
    def __init__(
        self,
        channel_type_name: str = None,
        code: str = None,
        data: main_models.GetQualityResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.channel_type_name = channel_type_name
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
        if self.channel_type_name is not None:
            result['ChannelTypeName'] = self.channel_type_name

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
        if m.get('ChannelTypeName') is not None:
            self.channel_type_name = m.get('ChannelTypeName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetQualityResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityResultResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        quality_result_response_list: List[main_models.GetQualityResultResponseBodyDataQualityResultResponseList] = None,
        total_num: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.quality_result_response_list = quality_result_response_list
        self.total_num = total_num

    def validate(self):
        if self.quality_result_response_list:
            for v1 in self.quality_result_response_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['QualityResultResponseList'] = []
        if self.quality_result_response_list is not None:
            for k1 in self.quality_result_response_list:
                result['QualityResultResponseList'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.quality_result_response_list = []
        if m.get('QualityResultResponseList') is not None:
            for k1 in m.get('QualityResultResponseList'):
                temp_model = main_models.GetQualityResultResponseBodyDataQualityResultResponseList()
                self.quality_result_response_list.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class GetQualityResultResponseBodyDataQualityResultResponseList(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        channel_type_name: str = None,
        group_id: str = None,
        group_name: str = None,
        hit_detail: str = None,
        hit_status: bool = None,
        instance_name: str = None,
        member_name: str = None,
        project_id: str = None,
        project_name: str = None,
        rule_id: str = None,
        rule_name: str = None,
        servicer_id: str = None,
        servicer_name: str = None,
        touch_id: str = None,
        touch_start_time: str = None,
    ):
        self.channel_type = channel_type
        self.channel_type_name = channel_type_name
        self.group_id = group_id
        self.group_name = group_name
        self.hit_detail = hit_detail
        self.hit_status = hit_status
        self.instance_name = instance_name
        self.member_name = member_name
        self.project_id = project_id
        self.project_name = project_name
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.servicer_id = servicer_id
        self.servicer_name = servicer_name
        self.touch_id = touch_id
        self.touch_start_time = touch_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.channel_type_name is not None:
            result['ChannelTypeName'] = self.channel_type_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.hit_detail is not None:
            result['HitDetail'] = self.hit_detail

        if self.hit_status is not None:
            result['HitStatus'] = self.hit_status

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        if self.touch_id is not None:
            result['TouchId'] = self.touch_id

        if self.touch_start_time is not None:
            result['TouchStartTime'] = self.touch_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ChannelTypeName') is not None:
            self.channel_type_name = m.get('ChannelTypeName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HitDetail') is not None:
            self.hit_detail = m.get('HitDetail')

        if m.get('HitStatus') is not None:
            self.hit_status = m.get('HitStatus')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')

        if m.get('TouchStartTime') is not None:
            self.touch_start_time = m.get('TouchStartTime')

        return self

