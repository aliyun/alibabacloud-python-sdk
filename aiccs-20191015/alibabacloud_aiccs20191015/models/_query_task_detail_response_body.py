# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryTaskDetailResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            temp_model = main_models.QueryTaskDetailResponseBodyData()
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

class QueryTaskDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        list: List[main_models.QueryTaskDetailResponseBodyDataList] = None,
        page_size: str = None,
        total_results: str = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total_results = total_results

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_results is not None:
            result['TotalResults'] = self.total_results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryTaskDetailResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')

        return self

class QueryTaskDetailResponseBodyDataList(DaraModel):
    def __init__(
        self,
        ani: str = None,
        bu_id: int = None,
        department_id: int = None,
        dnis: str = None,
        end_reason: int = None,
        ext_attrs: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        member_id: int = None,
        member_name: str = None,
        outbound_num: int = None,
        outbound_task_id: int = None,
        priority: int = None,
        retry_time: str = None,
        servicer_id: int = None,
        servicer_name: str = None,
        skill_group: int = None,
        status: int = None,
    ):
        self.ani = ani
        self.bu_id = bu_id
        self.department_id = department_id
        self.dnis = dnis
        self.end_reason = end_reason
        self.ext_attrs = ext_attrs
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.member_id = member_id
        self.member_name = member_name
        self.outbound_num = outbound_num
        self.outbound_task_id = outbound_task_id
        self.priority = priority
        self.retry_time = retry_time
        self.servicer_id = servicer_id
        self.servicer_name = servicer_name
        self.skill_group = skill_group
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ani is not None:
            result['Ani'] = self.ani

        if self.bu_id is not None:
            result['BuId'] = self.bu_id

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.dnis is not None:
            result['Dnis'] = self.dnis

        if self.end_reason is not None:
            result['EndReason'] = self.end_reason

        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.outbound_num is not None:
            result['OutboundNum'] = self.outbound_num

        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time

        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')

        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')

        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')

        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('OutboundNum') is not None:
            self.outbound_num = m.get('OutboundNum')

        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')

        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

