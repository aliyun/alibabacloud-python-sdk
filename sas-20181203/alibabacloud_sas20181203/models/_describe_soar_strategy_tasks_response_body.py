# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSoarStrategyTasksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        soar_strategy_tasks: List[main_models.DescribeSoarStrategyTasksResponseBodySoarStrategyTasks] = None,
        total_count: int = None,
    ):
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The policy tasks.
        self.soar_strategy_tasks = soar_strategy_tasks
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.soar_strategy_tasks:
            for v1 in self.soar_strategy_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SoarStrategyTasks'] = []
        if self.soar_strategy_tasks is not None:
            for k1 in self.soar_strategy_tasks:
                result['SoarStrategyTasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.soar_strategy_tasks = []
        if m.get('SoarStrategyTasks') is not None:
            for k1 in m.get('SoarStrategyTasks'):
                temp_model = main_models.DescribeSoarStrategyTasksResponseBodySoarStrategyTasks()
                self.soar_strategy_tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSoarStrategyTasksResponseBodySoarStrategyTasks(DaraModel):
    def __init__(
        self,
        failed_num: int = None,
        gmt_create: int = None,
        gmt_finish: int = None,
        gmt_modified: int = None,
        id: int = None,
        name: str = None,
        run_mode: str = None,
        status: str = None,
        strategy_id: int = None,
        success_num: int = None,
        total_num: int = None,
    ):
        # The number of execution failures.
        self.failed_num = failed_num
        # The timestamp when the policy task was created. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The timestamp when the policy task was complete. Unit: milliseconds.
        self.gmt_finish = gmt_finish
        # The timestamp when the policy task was modified. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The ID of the policy task.
        self.id = id
        # The name of the policy task.
        self.name = name
        # The execution mode. Valid values:
        # 
        # *   runmode_TRIGGER_BY_USER: manually executed
        self.run_mode = run_mode
        # The status of the policy task. Valid values:
        # 
        # *   \\-1: waiting
        # *   0: starting
        # *   1: running
        # *   2: finished
        # *   3: schedule
        # *   4: pause
        self.status = status
        # The ID of the policy.
        self.strategy_id = strategy_id
        # The number of successful executions.
        self.success_num = success_num
        # The total number of executions.
        self.total_num = total_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_finish is not None:
            result['GmtFinish'] = self.gmt_finish

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.success_num is not None:
            result['SuccessNum'] = self.success_num

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtFinish') is not None:
            self.gmt_finish = m.get('GmtFinish')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('SuccessNum') is not None:
            self.success_num = m.get('SuccessNum')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

