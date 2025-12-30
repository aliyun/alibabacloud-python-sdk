# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListBizEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListBizEntitiesResponseBodyPageResult = None,
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
            temp_model = main_models.ListBizEntitiesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListBizEntitiesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        biz_entity_list: List[main_models.ListBizEntitiesResponseBodyPageResultBizEntityList] = None,
        total_count: int = None,
    ):
        self.biz_entity_list = biz_entity_list
        self.total_count = total_count

    def validate(self):
        if self.biz_entity_list:
            for v1 in self.biz_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizEntityList'] = []
        if self.biz_entity_list is not None:
            for k1 in self.biz_entity_list:
                result['BizEntityList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_entity_list = []
        if m.get('BizEntityList') is not None:
            for k1 in m.get('BizEntityList'):
                temp_model = main_models.ListBizEntitiesResponseBodyPageResultBizEntityList()
                self.biz_entity_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBizEntitiesResponseBodyPageResultBizEntityList(DaraModel):
    def __init__(
        self,
        belong_to_biz_entity_id_list: List[int] = None,
        biz_unit_id: int = None,
        child_biz_entity_id_list: List[int] = None,
        data_domain_id: int = None,
        description: str = None,
        display_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_child_biz_entity: bool = None,
        id: int = None,
        last_modifier: str = None,
        last_modifier_name: str = None,
        level_sub_biz_object: bool = None,
        name: str = None,
        online_status: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
        ref_biz_entity_id_list: List[int] = None,
        ref_table_count: int = None,
        status: str = None,
        sub_type: str = None,
        suffix_biz_entity_id_list: List[int] = None,
        type: str = None,
    ):
        self.belong_to_biz_entity_id_list = belong_to_biz_entity_id_list
        self.biz_unit_id = biz_unit_id
        self.child_biz_entity_id_list = child_biz_entity_id_list
        self.data_domain_id = data_domain_id
        self.description = description
        self.display_name = display_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.has_child_biz_entity = has_child_biz_entity
        self.id = id
        self.last_modifier = last_modifier
        self.last_modifier_name = last_modifier_name
        self.level_sub_biz_object = level_sub_biz_object
        self.name = name
        self.online_status = online_status
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.ref_biz_entity_id_list = ref_biz_entity_id_list
        self.ref_table_count = ref_table_count
        self.status = status
        self.sub_type = sub_type
        self.suffix_biz_entity_id_list = suffix_biz_entity_id_list
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_to_biz_entity_id_list is not None:
            result['BelongToBizEntityIdList'] = self.belong_to_biz_entity_id_list

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.child_biz_entity_id_list is not None:
            result['ChildBizEntityIdList'] = self.child_biz_entity_id_list

        if self.data_domain_id is not None:
            result['DataDomainId'] = self.data_domain_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.has_child_biz_entity is not None:
            result['HasChildBizEntity'] = self.has_child_biz_entity

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        if self.level_sub_biz_object is not None:
            result['LevelSubBizObject'] = self.level_sub_biz_object

        if self.name is not None:
            result['Name'] = self.name

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.ref_biz_entity_id_list is not None:
            result['RefBizEntityIdList'] = self.ref_biz_entity_id_list

        if self.ref_table_count is not None:
            result['RefTableCount'] = self.ref_table_count

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.suffix_biz_entity_id_list is not None:
            result['SuffixBizEntityIdList'] = self.suffix_biz_entity_id_list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongToBizEntityIdList') is not None:
            self.belong_to_biz_entity_id_list = m.get('BelongToBizEntityIdList')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('ChildBizEntityIdList') is not None:
            self.child_biz_entity_id_list = m.get('ChildBizEntityIdList')

        if m.get('DataDomainId') is not None:
            self.data_domain_id = m.get('DataDomainId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HasChildBizEntity') is not None:
            self.has_child_biz_entity = m.get('HasChildBizEntity')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        if m.get('LevelSubBizObject') is not None:
            self.level_sub_biz_object = m.get('LevelSubBizObject')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('RefBizEntityIdList') is not None:
            self.ref_biz_entity_id_list = m.get('RefBizEntityIdList')

        if m.get('RefTableCount') is not None:
            self.ref_table_count = m.get('RefTableCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('SuffixBizEntityIdList') is not None:
            self.suffix_biz_entity_id_list = m.get('SuffixBizEntityIdList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

