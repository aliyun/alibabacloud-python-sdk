# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomScenePoliciesResponseBody(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeCustomScenePoliciesResponseBodyDataModule] = None,
        page_number: int = None,
        page_size: int = None,
        quota: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The scenario-specific policies.
        self.data_module = data_module
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The policy quota.
        self.quota = quota
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data_module:
            for v1 in self.data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeCustomScenePoliciesResponseBodyDataModule()
                self.data_module.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCustomScenePoliciesResponseBodyDataModule(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        objects: List[str] = None,
        policy_id: int = None,
        site_ids: str = None,
        start_time: str = None,
        status: str = None,
        template: str = None,
    ):
        # The time when the policy expires.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The name of the scenario-specific policy.
        self.name = name
        # The IDs of websites that are associated with the policy.
        self.objects = objects
        # The policy ID.
        self.policy_id = policy_id
        self.site_ids = site_ids
        # The time when the policy takes effect.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The status of the policy. Valid values:
        # 
        # *   **Disabled**
        # *   **Pending**
        # *   **Running**
        # *   **Expired**
        self.status = status
        # The name of the policy template. Valid value:
        # 
        # *   **promotion**: major events.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.objects is not None:
            result['Objects'] = self.objects

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.site_ids is not None:
            result['SiteIds'] = self.site_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Objects') is not None:
            self.objects = m.get('Objects')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

