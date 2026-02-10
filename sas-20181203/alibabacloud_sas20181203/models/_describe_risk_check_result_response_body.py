# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        list: List[main_models.DescribeRiskCheckResultResponseBodyList] = None,
        page_count: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The check items.
        self.list = list
        # The total number of pages returned.
        self.page_count = page_count
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeRiskCheckResultResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRiskCheckResultResponseBodyList(DaraModel):
    def __init__(
        self,
        affected_count: int = None,
        check_time: int = None,
        item_id: int = None,
        remaining_time: int = None,
        repair_status: str = None,
        risk_assert_type: str = None,
        risk_item_resources: List[main_models.DescribeRiskCheckResultResponseBodyListRiskItemResources] = None,
        risk_level: str = None,
        sort: int = None,
        start_status: str = None,
        status: str = None,
        task_id: int = None,
        title: str = None,
        type: str = None,
    ):
        # The number of affected assets.
        self.affected_count = affected_count
        # The timestamp when the last check was performed. Unit: milliseconds.
        self.check_time = check_time
        # The ID of the check item. For more information about the check item, see the check item table in the "Response parameters" section of this topic.
        self.item_id = item_id
        # The time when the next check will be performed.
        self.remaining_time = remaining_time
        # Indicates whether the risks that are detected based on the check item can be fixed. Valid values:
        # 
        # *   **enabled**: yes
        # *   **disabled**: no
        self.repair_status = repair_status
        # The type of the affected assets.
        self.risk_assert_type = risk_assert_type
        # An array that consists of the details about the check item.
        self.risk_item_resources = risk_item_resources
        # The risk level of the check item. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level
        # The sequence number in the check results. The check items are sorted based on the sequence number.
        self.sort = sort
        # Indicates whether the check item is supported by the edition of Security Center that you purchase. Valid values:
        # 
        # *   **enabled**: yes
        # *   **disable**: no
        self.start_status = start_status
        # The status of the check results. Valid values:
        # 
        # *   **pass**
        # *   **failed**
        # *   **running**
        # *   **waiting**
        # *   **ignored**
        # *   **falsePositive**
        self.status = status
        # The ID of the check task.
        self.task_id = task_id
        # The name of the check item.
        self.title = title
        # The type of the check item. Valid values:
        # 
        # *   Identity authentication and permissions
        # *   Network access control
        # *   Log audit
        # *   Data security
        # *   Monitoring and alerting
        # *   Basic security protection
        self.type = type

    def validate(self):
        if self.risk_item_resources:
            for v1 in self.risk_item_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_count is not None:
            result['AffectedCount'] = self.affected_count

        if self.check_time is not None:
            result['CheckTime'] = self.check_time

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time

        if self.repair_status is not None:
            result['RepairStatus'] = self.repair_status

        if self.risk_assert_type is not None:
            result['RiskAssertType'] = self.risk_assert_type

        result['RiskItemResources'] = []
        if self.risk_item_resources is not None:
            for k1 in self.risk_item_resources:
                result['RiskItemResources'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.start_status is not None:
            result['StartStatus'] = self.start_status

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedCount') is not None:
            self.affected_count = m.get('AffectedCount')

        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('RemainingTime') is not None:
            self.remaining_time = m.get('RemainingTime')

        if m.get('RepairStatus') is not None:
            self.repair_status = m.get('RepairStatus')

        if m.get('RiskAssertType') is not None:
            self.risk_assert_type = m.get('RiskAssertType')

        self.risk_item_resources = []
        if m.get('RiskItemResources') is not None:
            for k1 in m.get('RiskItemResources'):
                temp_model = main_models.DescribeRiskCheckResultResponseBodyListRiskItemResources()
                self.risk_item_resources.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartStatus') is not None:
            self.start_status = m.get('StartStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeRiskCheckResultResponseBodyListRiskItemResources(DaraModel):
    def __init__(
        self,
        content_resource: Dict[str, Any] = None,
        resource_name: str = None,
    ):
        # The details about the check results.
        self.content_resource = content_resource
        # The title in the details. Valid values:
        # 
        # *   **bestPractice**: description
        # *   **influence**: risk
        # *   **suggestion**: solution
        # *   **helpResource**: reference
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_resource is not None:
            result['ContentResource'] = self.content_resource

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentResource') is not None:
            self.content_resource = m.get('ContentResource')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

