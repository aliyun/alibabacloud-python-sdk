# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListInstancesResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListInstancesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstancesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListInstancesResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        self.data = data
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListInstancesResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyPageResultData(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        due_time: str = None,
        duration: str = None,
        end_execute_time: int = None,
        extend_info: str = None,
        id: str = None,
        index: int = None,
        node_info: main_models.ListInstancesResponseBodyPageResultDataNodeInfo = None,
        start_execute_time: int = None,
        status_list: List[str] = None,
    ):
        self.biz_date = biz_date
        self.due_time = due_time
        self.duration = duration
        self.end_execute_time = end_execute_time
        self.extend_info = extend_info
        self.id = id
        self.index = index
        self.node_info = node_info
        self.start_execute_time = start_execute_time
        self.status_list = status_list

    def validate(self):
        if self.node_info:
            self.node_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.due_time is not None:
            result['DueTime'] = self.due_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_execute_time is not None:
            result['EndExecuteTime'] = self.end_execute_time

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.id is not None:
            result['Id'] = self.id

        if self.index is not None:
            result['Index'] = self.index

        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()

        if self.start_execute_time is not None:
            result['StartExecuteTime'] = self.start_execute_time

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndExecuteTime') is not None:
            self.end_execute_time = m.get('EndExecuteTime')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('NodeInfo') is not None:
            temp_model = main_models.ListInstancesResponseBodyPageResultDataNodeInfo()
            self.node_info = temp_model.from_map(m.get('NodeInfo'))

        if m.get('StartExecuteTime') is not None:
            self.start_execute_time = m.get('StartExecuteTime')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

class ListInstancesResponseBodyPageResultDataNodeInfo(DaraModel):
    def __init__(
        self,
        biz_unit_name: str = None,
        create_time: str = None,
        creator: main_models.ListInstancesResponseBodyPageResultDataNodeInfoCreator = None,
        description: str = None,
        dry_run: bool = None,
        from_: str = None,
        has_dev: bool = None,
        has_prod: bool = None,
        id: str = None,
        last_modified_time: str = None,
        modifier: main_models.ListInstancesResponseBodyPageResultDataNodeInfoModifier = None,
        name: str = None,
        owner_list: List[main_models.ListInstancesResponseBodyPageResultDataNodeInfoOwnerList] = None,
        priority_list: List[str] = None,
        resource_group_list: List[str] = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        sub_detail_type: str = None,
        type: str = None,
    ):
        self.biz_unit_name = biz_unit_name
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.dry_run = dry_run
        self.from_ = from_
        self.has_dev = has_dev
        self.has_prod = has_prod
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.owner_list = owner_list
        self.priority_list = priority_list
        self.resource_group_list = resource_group_list
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        self.sub_detail_type = sub_detail_type
        self.type = type

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.owner_list:
            for v1 in self.owner_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.from_ is not None:
            result['From'] = self.from_

        if self.has_dev is not None:
            result['HasDev'] = self.has_dev

        if self.has_prod is not None:
            result['HasProd'] = self.has_prod

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()

        if self.name is not None:
            result['Name'] = self.name

        result['OwnerList'] = []
        if self.owner_list is not None:
            for k1 in self.owner_list:
                result['OwnerList'].append(k1.to_map() if k1 else None)

        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list

        if self.resource_group_list is not None:
            result['ResourceGroupList'] = self.resource_group_list

        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused

        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list

        if self.sub_detail_type is not None:
            result['SubDetailType'] = self.sub_detail_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            temp_model = main_models.ListInstancesResponseBodyPageResultDataNodeInfoCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('HasDev') is not None:
            self.has_dev = m.get('HasDev')

        if m.get('HasProd') is not None:
            self.has_prod = m.get('HasProd')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('Modifier') is not None:
            temp_model = main_models.ListInstancesResponseBodyPageResultDataNodeInfoModifier()
            self.modifier = temp_model.from_map(m.get('Modifier'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k1 in m.get('OwnerList'):
                temp_model = main_models.ListInstancesResponseBodyPageResultDataNodeInfoOwnerList()
                self.owner_list.append(temp_model.from_map(k1))

        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')

        if m.get('ResourceGroupList') is not None:
            self.resource_group_list = m.get('ResourceGroupList')

        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')

        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')

        if m.get('SubDetailType') is not None:
            self.sub_detail_type = m.get('SubDetailType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListInstancesResponseBodyPageResultDataNodeInfoOwnerList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
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

class ListInstancesResponseBodyPageResultDataNodeInfoModifier(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
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

class ListInstancesResponseBodyPageResultDataNodeInfoCreator(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
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

