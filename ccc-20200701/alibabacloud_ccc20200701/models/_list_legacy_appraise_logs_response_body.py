# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListLegacyAppraiseLogsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLegacyAppraiseLogsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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
            temp_model = main_models.ListLegacyAppraiseLogsResponseBodyData()
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

class ListLegacyAppraiseLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListLegacyAppraiseLogsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

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
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListLegacyAppraiseLogsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLegacyAppraiseLogsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        acid: str = None,
        contact_type: str = None,
        id: int = None,
        instance_id: str = None,
        key_mark_relation: str = None,
        note: str = None,
        parent_note: str = None,
        press_key: str = None,
        ram_id: str = None,
        skill_group_id: str = None,
        statistic_date: str = None,
        type: str = None,
    ):
        self.acid = acid
        self.contact_type = contact_type
        self.id = id
        self.instance_id = instance_id
        self.key_mark_relation = key_mark_relation
        self.note = note
        self.parent_note = parent_note
        self.press_key = press_key
        self.ram_id = ram_id
        self.skill_group_id = skill_group_id
        self.statistic_date = statistic_date
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acid is not None:
            result['Acid'] = self.acid

        if self.contact_type is not None:
            result['ContactType'] = self.contact_type

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_mark_relation is not None:
            result['KeyMarkRelation'] = self.key_mark_relation

        if self.note is not None:
            result['Note'] = self.note

        if self.parent_note is not None:
            result['ParentNote'] = self.parent_note

        if self.press_key is not None:
            result['PressKey'] = self.press_key

        if self.ram_id is not None:
            result['RamId'] = self.ram_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.statistic_date is not None:
            result['StatisticDate'] = self.statistic_date

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')

        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyMarkRelation') is not None:
            self.key_mark_relation = m.get('KeyMarkRelation')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('ParentNote') is not None:
            self.parent_note = m.get('ParentNote')

        if m.get('PressKey') is not None:
            self.press_key = m.get('PressKey')

        if m.get('RamId') is not None:
            self.ram_id = m.get('RamId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('StatisticDate') is not None:
            self.statistic_date = m.get('StatisticDate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

