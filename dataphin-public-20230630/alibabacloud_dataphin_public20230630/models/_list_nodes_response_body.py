# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListNodesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListNodesResponseBodyPageResult = None,
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
            temp_model = main_models.ListNodesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListNodesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        node_list: List[main_models.ListNodesResponseBodyPageResultNodeList] = None,
        total_count: int = None,
    ):
        self.node_list = node_list
        self.total_count = total_count

    def validate(self):
        if self.node_list:
            for v1 in self.node_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeList'] = []
        if self.node_list is not None:
            for k1 in self.node_list:
                result['NodeList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_list = []
        if m.get('NodeList') is not None:
            for k1 in m.get('NodeList'):
                temp_model = main_models.ListNodesResponseBodyPageResultNodeList()
                self.node_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNodesResponseBodyPageResultNodeList(DaraModel):
    def __init__(
        self,
        biz_unit_name: str = None,
        create_time: str = None,
        creator: main_models.ListNodesResponseBodyPageResultNodeListCreator = None,
        description: str = None,
        dry_run: bool = None,
        extend_info: str = None,
        from_: str = None,
        has_dev: bool = None,
        has_prod: bool = None,
        id: str = None,
        last_modified_time: str = None,
        modifier: main_models.ListNodesResponseBodyPageResultNodeListModifier = None,
        name: str = None,
        owner_list: List[main_models.ListNodesResponseBodyPageResultNodeListOwnerList] = None,
        priority_list: List[str] = None,
        project_info: main_models.ListNodesResponseBodyPageResultNodeListProjectInfo = None,
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
        self.extend_info = extend_info
        self.from_ = from_
        self.has_dev = has_dev
        self.has_prod = has_prod
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.owner_list = owner_list
        self.priority_list = priority_list
        self.project_info = project_info
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
        if self.project_info:
            self.project_info.validate()

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

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

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

        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()

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
            temp_model = main_models.ListNodesResponseBodyPageResultNodeListCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

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
            temp_model = main_models.ListNodesResponseBodyPageResultNodeListModifier()
            self.modifier = temp_model.from_map(m.get('Modifier'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k1 in m.get('OwnerList'):
                temp_model = main_models.ListNodesResponseBodyPageResultNodeListOwnerList()
                self.owner_list.append(temp_model.from_map(k1))

        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')

        if m.get('ProjectInfo') is not None:
            temp_model = main_models.ListNodesResponseBodyPageResultNodeListProjectInfo()
            self.project_info = temp_model.from_map(m.get('ProjectInfo'))

        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')

        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')

        if m.get('SubDetailType') is not None:
            self.sub_detail_type = m.get('SubDetailType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListNodesResponseBodyPageResultNodeListProjectInfo(DaraModel):
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

class ListNodesResponseBodyPageResultNodeListOwnerList(DaraModel):
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

class ListNodesResponseBodyPageResultNodeListModifier(DaraModel):
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

class ListNodesResponseBodyPageResultNodeListCreator(DaraModel):
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

