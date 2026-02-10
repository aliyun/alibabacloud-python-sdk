# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListOperationTaskRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        current_page: int = None,
        lang: str = None,
        operation_task_instances: List[main_models.ListOperationTaskRequestOperationTaskInstances] = None,
        page_size: int = None,
        statuses: List[str] = None,
        task_id: str = None,
        type: str = None,
    ):
        # The ID of the check item.
        # 
        # > You can call the [ListCheckResult](~~ListCheckResult~~) API to obtain the check item ID.
        self.check_id = check_id
        # The page number to display in a paginated query.
        self.current_page = current_page
        # Set the language type for the request and response messages. The default value is **zh**. Values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The instance information of the operation tasks to be queried.
        self.operation_task_instances = operation_task_instances
        # The maximum number of items to display per page in a paginated query.
        self.page_size = page_size
        # A list of task statuses. Multiple statuses should be separated by commas (,). Values:
        # 
        # - **INIT**: Initialization
        # - **FAIL**: Processing failed
        # - **THROTTLING**: Repairing concurrently
        # - **IN_BACKUP**: Backing up
        # - **BACKED_UP**: Backed up
        # - **BACKUP_FAIL**: Backup failed
        # - **REPAIRING**: Repairing
        # - **REPAIR_SUCCESS**: Repair succeeded
        # - **REPAIR_FAIL**: Repair failed
        # - **REPAIR_SUCCESS_VERIFYING**: Verifying repair success
        # - **REPAIR_SUCCESS_UNVERIFIED**: Repair success verification failed
        # - **REPAIR_SUCCESS_VERIFIED**: Repair success verified
        # - **REPAIR_RE_EXECUTE**: Re-executing repair
        # - **ROLL_BACKING**: Rolling back
        # - **ROLL_BACKED**: Rolled back
        # - **ROLL_BACK_FAIL**: Rollback failed
        # - **ROLL_BACK_INIT**: Rollback initiated
        # - **ROLL_BACK_VERIFYING**: Verifying rollback success
        # - **ROLL_BACK_UNVERIFIED**: Rollback success verification failed
        # - **ROLL_BACK_VERIFIED**: Rollback success verified
        self.statuses = statuses
        # The ID of the task to be queried.
        self.task_id = task_id
        # The type of operation task to be queried:
        # - REPAIR: Repair
        # - ROLLBACK: Rollback
        self.type = type

    def validate(self):
        if self.operation_task_instances:
            for v1 in self.operation_task_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        result['OperationTaskInstances'] = []
        if self.operation_task_instances is not None:
            for k1 in self.operation_task_instances:
                result['OperationTaskInstances'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.operation_task_instances = []
        if m.get('OperationTaskInstances') is not None:
            for k1 in m.get('OperationTaskInstances'):
                temp_model = main_models.ListOperationTaskRequestOperationTaskInstances()
                self.operation_task_instances.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListOperationTaskRequestOperationTaskInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        vendor: str = None,
    ):
        # The instance ID of the server.
        self.instance_id = instance_id
        # The ID of the region where the instance is located.
        self.region_id = region_id
        # Cloud asset vendor.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

