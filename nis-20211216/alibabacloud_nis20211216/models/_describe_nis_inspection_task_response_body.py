# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class DescribeNisInspectionTaskResponseBody(DaraModel):
    def __init__(
        self,
        check_resource_list: List[main_models.DescribeNisInspectionTaskResponseBodyCheckResourceList] = None,
        create_time: str = None,
        inspection_interval: str = None,
        inspection_name: str = None,
        inspection_project: str = None,
        inspection_task_id: str = None,
        inspection_trigger_time: str = None,
        last_update_report_id: str = None,
        last_update_time: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.check_resource_list = check_resource_list
        self.create_time = create_time
        self.inspection_interval = inspection_interval
        self.inspection_name = inspection_name
        self.inspection_project = inspection_project
        self.inspection_task_id = inspection_task_id
        self.inspection_trigger_time = inspection_trigger_time
        self.last_update_report_id = last_update_report_id
        self.last_update_time = last_update_time
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.check_resource_list:
            for v1 in self.check_resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckResourceList'] = []
        if self.check_resource_list is not None:
            for k1 in self.check_resource_list:
                result['CheckResourceList'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.inspection_interval is not None:
            result['InspectionInterval'] = self.inspection_interval

        if self.inspection_name is not None:
            result['InspectionName'] = self.inspection_name

        if self.inspection_project is not None:
            result['InspectionProject'] = self.inspection_project

        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id

        if self.inspection_trigger_time is not None:
            result['InspectionTriggerTime'] = self.inspection_trigger_time

        if self.last_update_report_id is not None:
            result['LastUpdateReportId'] = self.last_update_report_id

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_resource_list = []
        if m.get('CheckResourceList') is not None:
            for k1 in m.get('CheckResourceList'):
                temp_model = main_models.DescribeNisInspectionTaskResponseBodyCheckResourceList()
                self.check_resource_list.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InspectionInterval') is not None:
            self.inspection_interval = m.get('InspectionInterval')

        if m.get('InspectionName') is not None:
            self.inspection_name = m.get('InspectionName')

        if m.get('InspectionProject') is not None:
            self.inspection_project = m.get('InspectionProject')

        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')

        if m.get('InspectionTriggerTime') is not None:
            self.inspection_trigger_time = m.get('InspectionTriggerTime')

        if m.get('LastUpdateReportId') is not None:
            self.last_update_report_id = m.get('LastUpdateReportId')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeNisInspectionTaskResponseBodyCheckResourceList(DaraModel):
    def __init__(
        self,
        check_scope: str = None,
        resource_type: str = None,
    ):
        self.check_scope = check_scope
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_scope is not None:
            result['CheckScope'] = self.check_scope

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckScope') is not None:
            self.check_scope = m.get('CheckScope')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

