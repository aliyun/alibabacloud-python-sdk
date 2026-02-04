# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePreCheckStatusRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        job_code: str = None,
        name: str = None,
        page_no: str = None,
        page_size: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        struct_phase: str = None,
        struct_type: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the data migration, data synchronization, or change tracking task.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The task code that specifies the type of the DTS subtask. Valid values:
        # 
        # *   **01**: precheck.
        # *   **02**: schema migration or initial schema synchronization.
        # *   **03**: full data migration or initial full data synchronization.
        # *   **04**: incremental data migration or synchronization.
        # 
        # This parameter is required.
        self.job_code = job_code
        # The filter item used to filter tables in fuzzy match.
        self.name = name
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page. Default value: **20**.
        self.page_size = page_size
        # The ID of the region in which the DTS instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The filter item used to filter tables, views, and functions during schema migration.
        self.struct_phase = struct_phase
        # The type of schema definition. Valid values:
        # 
        # *   **before**: schema migration or initial schema synchronization.
        # *   **after**: DDL operations performed during incremental data migration or synchronization.
        self.struct_type = struct_type
        # Whether it is a seamless integration (Zero-ETL) task, the value can be:
        # - **false**: No. - **true**: Yes.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.job_code is not None:
            result['JobCode'] = self.job_code

        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.struct_phase is not None:
            result['StructPhase'] = self.struct_phase

        if self.struct_type is not None:
            result['StructType'] = self.struct_type

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('JobCode') is not None:
            self.job_code = m.get('JobCode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StructPhase') is not None:
            self.struct_phase = m.get('StructPhase')

        if m.get('StructType') is not None:
            self.struct_type = m.get('StructType')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

