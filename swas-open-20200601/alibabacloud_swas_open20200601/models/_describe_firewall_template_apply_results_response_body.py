# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeFirewallTemplateApplyResultsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
        data: List[main_models.DescribeFirewallTemplateApplyResultsResponseBodyData] = None,
    ):
        # The number of entries per page for a paged query.
        self.page_number = page_number
        # The number of entries per page for a paged query. Default value: 20.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of firewall rules.
        self.total_count = total_count
        # The returned results.
        self.data = data

    def validate(self):
        if self.data:
            for v1 in self.data:
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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeFirewallTemplateApplyResultsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        return self

class DescribeFirewallTemplateApplyResultsResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        failed_count: str = None,
        firewall_template_id: str = None,
        instance_apply_results: List[main_models.DescribeFirewallTemplateApplyResultsResponseBodyDataInstanceApplyResults] = None,
        status: str = None,
        task_id: str = None,
        total_count: str = None,
    ):
        # The time when the firewall template application task was executed, in the format of EEE MMM dd HH:mm:ss zzz yyyy.
        self.create_time = create_time
        # The total number of instances to which the firewall template failed to be applied.
        self.failed_count = failed_count
        # The firewall template ID.
        self.firewall_template_id = firewall_template_id
        # The results of applying the firewall template to instances.
        self.instance_apply_results = instance_apply_results
        # The status of applying the firewall template to all instances. Valid values:
        # 
        # - Running: The firewall template is being applied.
        # - Failed: The firewall template failed to be applied to all instances.
        # - Success: The firewall template was applied.
        # - PartFailed: The firewall template was partially applied. Some instances failed.
        self.status = status
        # The ID of the template application task.
        self.task_id = task_id
        # The total number of instances to which the firewall template is applied.
        self.total_count = total_count

    def validate(self):
        if self.instance_apply_results:
            for v1 in self.instance_apply_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.firewall_template_id is not None:
            result['FirewallTemplateId'] = self.firewall_template_id

        result['InstanceApplyResults'] = []
        if self.instance_apply_results is not None:
            for k1 in self.instance_apply_results:
                result['InstanceApplyResults'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('FirewallTemplateId') is not None:
            self.firewall_template_id = m.get('FirewallTemplateId')

        self.instance_apply_results = []
        if m.get('InstanceApplyResults') is not None:
            for k1 in m.get('InstanceApplyResults'):
                temp_model = main_models.DescribeFirewallTemplateApplyResultsResponseBodyDataInstanceApplyResults()
                self.instance_apply_results.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFirewallTemplateApplyResultsResponseBodyDataInstanceApplyResults(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        status: str = None,
    ):
        # The simple application server instance ID.
        self.instance_id = instance_id
        # The status of applying the firewall template to a specific instance. Valid values:
        # 
        # - Running: The firewall template is being applied.
        # - Failed: The firewall template failed to be applied.
        # - Success: The firewall template was applied.
        # - PartFailed: The firewall template was partially applied. Some rules failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

