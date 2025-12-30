# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmRecoveryPlansResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        recovery_plans: main_models.DescribeGtmRecoveryPlansResponseBodyRecoveryPlans = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The details about the queried disaster recovery plans.
        self.recovery_plans = recovery_plans
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.recovery_plans:
            self.recovery_plans.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.recovery_plans is not None:
            result['RecoveryPlans'] = self.recovery_plans.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecoveryPlans') is not None:
            temp_model = main_models.DescribeGtmRecoveryPlansResponseBodyRecoveryPlans()
            self.recovery_plans = temp_model.from_map(m.get('RecoveryPlans'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeGtmRecoveryPlansResponseBodyRecoveryPlans(DaraModel):
    def __init__(
        self,
        recovery_plan: List[main_models.DescribeGtmRecoveryPlansResponseBodyRecoveryPlansRecoveryPlan] = None,
    ):
        self.recovery_plan = recovery_plan

    def validate(self):
        if self.recovery_plan:
            for v1 in self.recovery_plan:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecoveryPlan'] = []
        if self.recovery_plan is not None:
            for k1 in self.recovery_plan:
                result['RecoveryPlan'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recovery_plan = []
        if m.get('RecoveryPlan') is not None:
            for k1 in m.get('RecoveryPlan'):
                temp_model = main_models.DescribeGtmRecoveryPlansResponseBodyRecoveryPlansRecoveryPlan()
                self.recovery_plan.append(temp_model.from_map(k1))

        return self

class DescribeGtmRecoveryPlansResponseBodyRecoveryPlansRecoveryPlan(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        fault_addr_pool_num: int = None,
        last_execute_time: str = None,
        last_execute_timestamp: int = None,
        last_rollback_time: str = None,
        last_rollback_timestamp: int = None,
        name: str = None,
        recovery_plan_id: int = None,
        remark: str = None,
        status: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the disaster recovery plan was created.
        self.create_time = create_time
        # The UNIX timestamp that indicates when the disaster recovery plan was created.
        self.create_timestamp = create_timestamp
        # The number of faulty address pools.
        self.fault_addr_pool_num = fault_addr_pool_num
        # The last time when the disaster recovery plan was executed.
        self.last_execute_time = last_execute_time
        # The UNIX timestamp that indicates the last time when the disaster recovery plan was executed.
        self.last_execute_timestamp = last_execute_timestamp
        # The last time when the disaster recovery plan was rolled back.
        self.last_rollback_time = last_rollback_time
        # The UNIX timestamp that indicates the last time when the disaster recovery plan was rolled back.
        self.last_rollback_timestamp = last_rollback_timestamp
        # The name of the disaster recovery plan.
        self.name = name
        # The ID of the disaster recovery plan.
        self.recovery_plan_id = recovery_plan_id
        # The remarks about the disaster recovery plan.
        self.remark = remark
        # The status of the disaster recovery plan. Valid values:
        # 
        # *   **UNEXECUTED**: The plan is not executed.
        # *   **EXECUTED**: The plan is executed.
        # *   **ROLLED_BACK**: The plan is rolled back.
        self.status = status
        # The last time when the disaster recovery plan was updated.
        self.update_time = update_time
        # The UNIX timestamp that indicates the last time when the disaster recovery plan was updated.
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.fault_addr_pool_num is not None:
            result['FaultAddrPoolNum'] = self.fault_addr_pool_num

        if self.last_execute_time is not None:
            result['LastExecuteTime'] = self.last_execute_time

        if self.last_execute_timestamp is not None:
            result['LastExecuteTimestamp'] = self.last_execute_timestamp

        if self.last_rollback_time is not None:
            result['LastRollbackTime'] = self.last_rollback_time

        if self.last_rollback_timestamp is not None:
            result['LastRollbackTimestamp'] = self.last_rollback_timestamp

        if self.name is not None:
            result['Name'] = self.name

        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('FaultAddrPoolNum') is not None:
            self.fault_addr_pool_num = m.get('FaultAddrPoolNum')

        if m.get('LastExecuteTime') is not None:
            self.last_execute_time = m.get('LastExecuteTime')

        if m.get('LastExecuteTimestamp') is not None:
            self.last_execute_timestamp = m.get('LastExecuteTimestamp')

        if m.get('LastRollbackTime') is not None:
            self.last_rollback_time = m.get('LastRollbackTime')

        if m.get('LastRollbackTimestamp') is not None:
            self.last_rollback_timestamp = m.get('LastRollbackTimestamp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

