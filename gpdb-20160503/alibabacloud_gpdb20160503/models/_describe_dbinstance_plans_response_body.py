# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancePlansResponseBody(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        items: main_models.DescribeDBInstancePlansResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        status: str = None,
        total_record_count: int = None,
    ):
        # The error message.
        # 
        # This parameter is returned only if the request fails.
        self.error_message = error_message
        # The queried plans.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # If the request was successful, **success** is returned. If the request failed, this parameter is not returned.
        self.status = status
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstancePlansResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstancePlansResponseBodyItems(DaraModel):
    def __init__(
        self,
        plan_list: List[main_models.DescribeDBInstancePlansResponseBodyItemsPlanList] = None,
    ):
        self.plan_list = plan_list

    def validate(self):
        if self.plan_list:
            for v1 in self.plan_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PlanList'] = []
        if self.plan_list is not None:
            for k1 in self.plan_list:
                result['PlanList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plan_list = []
        if m.get('PlanList') is not None:
            for k1 in m.get('PlanList'):
                temp_model = main_models.DescribeDBInstancePlansResponseBodyItemsPlanList()
                self.plan_list.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancePlansResponseBodyItemsPlanList(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        plan_config: str = None,
        plan_desc: str = None,
        plan_end_date: str = None,
        plan_id: str = None,
        plan_name: str = None,
        plan_schedule_type: str = None,
        plan_start_date: str = None,
        plan_status: str = None,
        plan_type: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The execution information of the plan.
        self.plan_config = plan_config
        # The description of the plan.
        self.plan_desc = plan_desc
        # The end time of the plan. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > 
        # 
        # *   This parameter is returned only for the plans that are periodically executed.
        # 
        # *   If you did not specify the end time when you created the plan, this parameter is not returned.
        self.plan_end_date = plan_end_date
        # The plan ID.
        self.plan_id = plan_id
        # The name of the plan.
        self.plan_name = plan_name
        # The execution mode of the plan. Valid values:
        # 
        # *   **Postpone**: The plan is executed later.
        # *   **Regular**: The plan is executed periodically.
        self.plan_schedule_type = plan_schedule_type
        # The start time of the plan. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > 
        # 
        # *   This parameter is returned only for the plans that are periodically executed.
        # 
        # *   If you did not specify the start time when you created the plan, the current time is returned.
        self.plan_start_date = plan_start_date
        # The status of the plan. Valid values:
        # 
        # *   **active**
        # *   **cancel**
        # *   **deleted**
        # *   **finished**
        self.plan_status = plan_status
        # The type of the plan. Valid values:
        # 
        # *   **PauseResume**: pauses and resumes an instance.
        # *   **Resize**: scales an instance.
        self.plan_type = plan_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.plan_config is not None:
            result['PlanConfig'] = self.plan_config

        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc

        if self.plan_end_date is not None:
            result['PlanEndDate'] = self.plan_end_date

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_schedule_type is not None:
            result['PlanScheduleType'] = self.plan_schedule_type

        if self.plan_start_date is not None:
            result['PlanStartDate'] = self.plan_start_date

        if self.plan_status is not None:
            result['PlanStatus'] = self.plan_status

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PlanConfig') is not None:
            self.plan_config = m.get('PlanConfig')

        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')

        if m.get('PlanEndDate') is not None:
            self.plan_end_date = m.get('PlanEndDate')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanScheduleType') is not None:
            self.plan_schedule_type = m.get('PlanScheduleType')

        if m.get('PlanStartDate') is not None:
            self.plan_start_date = m.get('PlanStartDate')

        if m.get('PlanStatus') is not None:
            self.plan_status = m.get('PlanStatus')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        return self

