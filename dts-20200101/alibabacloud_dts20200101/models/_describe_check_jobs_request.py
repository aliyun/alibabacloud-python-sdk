# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckJobsRequest(DaraModel):
    def __init__(
        self,
        check_job_id: str = None,
        check_type: int = None,
        instance_id: str = None,
        job_name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The ID of the data validation task.
        self.check_job_id = check_job_id
        # The data validation method. Valid values:
        # 
        # - **1**: full data validation.
        # - **2**: incremental data validation.
        # - **3**: all.
        self.check_type = check_type
        # The ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query the ID.
        self.instance_id = instance_id
        # The name of the data migration or data synchronization task.
        self.job_name = job_name
        # The page number.
        self.page_number = page_number
        # The number of records per page. Valid values: **30**, **50**, and **100**. Default value: **30**.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_job_id is not None:
            result['CheckJobId'] = self.check_job_id

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckJobId') is not None:
            self.check_job_id = m.get('CheckJobId')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

