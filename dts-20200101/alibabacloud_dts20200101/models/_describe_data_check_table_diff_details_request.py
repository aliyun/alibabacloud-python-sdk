# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataCheckTableDiffDetailsRequest(DaraModel):
    def __init__(
        self,
        check_type: int = None,
        db_name: str = None,
        dts_job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tb_name: str = None,
    ):
        # The data verification method. Valid values:
        # 
        # *   **1**: full data verification.
        # *   **2**: incremental data verification.
        # 
        # This parameter is required.
        self.check_type = check_type
        # The name of the database to which the table that contains inconsistent data belongs.
        # 
        # This parameter is required.
        self.db_name = db_name
        # The ID of the data migration or data synchronization task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the ID of the task.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The page number of the page to return. The value must be an integer greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The name of the table that contains inconsistent data exists.
        # 
        # This parameter is required.
        self.tb_name = tb_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tb_name is not None:
            result['TbName'] = self.tb_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TbName') is not None:
            self.tb_name = m.get('TbName')

        return self

