# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryOutboundTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryOutboundTaskResponseBodyData = None,
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
            temp_model = main_models.QueryOutboundTaskResponseBodyData()
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

class QueryOutboundTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        list: List[main_models.QueryOutboundTaskResponseBodyDataList] = None,
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
                temp_model = main_models.QueryOutboundTaskResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')

        return self

class QueryOutboundTaskResponseBodyDataList(DaraModel):
    def __init__(
        self,
        bu_id: int = None,
        caller_num: str = None,
        creator: str = None,
        department_id: int = None,
        description: str = None,
        end_date: str = None,
        end_time: str = None,
        ext_attrs: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_name: str = None,
        id: int = None,
        model: int = None,
        modifier: str = None,
        name: str = None,
        retry_interval: int = None,
        retry_time: int = None,
        skill_group: int = None,
        start_date: str = None,
        start_time: str = None,
        status: int = None,
        type: int = None,
    ):
        self.bu_id = bu_id
        self.caller_num = caller_num
        self.creator = creator
        self.department_id = department_id
        self.description = description
        self.end_date = end_date
        self.end_time = end_time
        self.ext_attrs = ext_attrs
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_name = group_name
        self.id = id
        self.model = model
        self.modifier = modifier
        self.name = name
        self.retry_interval = retry_interval
        self.retry_time = retry_time
        self.skill_group = skill_group
        self.start_date = start_date
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bu_id is not None:
            result['BuId'] = self.bu_id

        if self.caller_num is not None:
            result['CallerNum'] = self.caller_num

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.description is not None:
            result['Description'] = self.description

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.model is not None:
            result['Model'] = self.model

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.name is not None:
            result['Name'] = self.name

        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval

        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time

        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')

        if m.get('CallerNum') is not None:
            self.caller_num = m.get('CallerNum')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')

        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')

        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

