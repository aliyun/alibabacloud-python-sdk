# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class ListAutoScalingRecordsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.ListAutoScalingRecordsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListAutoScalingRecordsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAutoScalingRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        scale_records: List[main_models.ListAutoScalingRecordsResponseBodyDataScaleRecords] = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.scale_records = scale_records
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.scale_records:
            for v1 in self.scale_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ScaleRecords'] = []
        if self.scale_records is not None:
            for k1 in self.scale_records:
                result['ScaleRecords'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.scale_records = []
        if m.get('ScaleRecords') is not None:
            for k1 in m.get('ScaleRecords'):
                temp_model = main_models.ListAutoScalingRecordsResponseBodyDataScaleRecords()
                self.scale_records.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListAutoScalingRecordsResponseBodyDataScaleRecords(DaraModel):
    def __init__(
        self,
        detail: str = None,
        end_time: str = None,
        id: str = None,
        instance_id: str = None,
        old_value: str = None,
        resource_type: str = None,
        spec_group_id: str = None,
        start_time: str = None,
        status: str = None,
        strategy: str = None,
        target_value: str = None,
    ):
        self.detail = detail
        self.end_time = end_time
        self.id = id
        self.instance_id = instance_id
        self.old_value = old_value
        self.resource_type = resource_type
        self.spec_group_id = spec_group_id
        self.start_time = start_time
        self.status = status
        self.strategy = strategy
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.old_value is not None:
            result['OldValue'] = self.old_value

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.spec_group_id is not None:
            result['SpecGroupId'] = self.spec_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SpecGroupId') is not None:
            self.spec_group_id = m.get('SpecGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

