# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSoarSubscribedStrategyResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        soar_strategies: List[main_models.DescribeSoarSubscribedStrategyResponseBodySoarStrategies] = None,
        total_count: int = None,
    ):
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The policies.
        self.soar_strategies = soar_strategies
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.soar_strategies:
            for v1 in self.soar_strategies:
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

        result['SoarStrategies'] = []
        if self.soar_strategies is not None:
            for k1 in self.soar_strategies:
                result['SoarStrategies'].append(k1.to_map() if k1 else None)

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

        self.soar_strategies = []
        if m.get('SoarStrategies') is not None:
            for k1 in m.get('SoarStrategies'):
                temp_model = main_models.DescribeSoarSubscribedStrategyResponseBodySoarStrategies()
                self.soar_strategies.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSoarSubscribedStrategyResponseBodySoarStrategies(DaraModel):
    def __init__(
        self,
        creator: str = None,
        description: str = None,
        execute_num: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        name: str = None,
        run_mode: str = None,
        type: str = None,
    ):
        # The Alibaba Cloud account ID of the creator.
        self.creator = creator
        # The description of the policy.
        self.description = description
        # The total number of times that the policy is executed.
        self.execute_num = execute_num
        # The timestamp when the policy was created. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The timestamp when the policy was modified. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The ID of the policy.
        self.id = id
        # The name of the policy.
        self.name = name
        # The execution mode. Valid values:
        # 
        # *   runmode_TRIGGER_BY_USER: manually executed
        self.run_mode = run_mode
        # The type of the policy. Valid values:
        # 
        # *   type_vulfix: vulnerability operations
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.execute_num is not None:
            result['ExecuteNum'] = self.execute_num

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecuteNum') is not None:
            self.execute_num = m.get('ExecuteNum')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

