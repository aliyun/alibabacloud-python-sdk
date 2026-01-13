# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListExecutorsRequest(DaraModel):
    def __init__(
        self,
        filter: main_models.ListExecutorsRequestFilter = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Queries the Executor filter conditions.
        self.filter = filter
        # The current page number.\\
        # Starting value: 1\\
        # Default value: 1
        self.page_number = page_number
        # The number of entries per page. The number of entries returned per page. Default value: 50. Maximum value: 100.
        self.page_size = page_size

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = main_models.ListExecutorsRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListExecutorsRequestFilter(DaraModel):
    def __init__(
        self,
        executor_ids: List[str] = None,
        image: str = None,
        ip_addresses: List[str] = None,
        job_name: str = None,
        status: List[str] = None,
        time_created_after: int = None,
        time_created_before: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The list of executor IDs. A maximum of 100 IDs are supported.
        self.executor_ids = executor_ids
        # Executor image.
        self.image = image
        # The list of internal IP addresses. A maximum of 100 IP addresses are supported.
        self.ip_addresses = ip_addresses
        # The job name. Exact filtering. Fuzzy query is not supported.
        self.job_name = job_name
        # Executor status list.
        self.status = status
        # For jobs submitted after this time, the time in the region is converted into a UNIX timestamp (UI8).
        self.time_created_after = time_created_after
        # For jobs submitted before this time, the time in the region is converted into a Unix timestamp (for domestic sites, the UI8 region).
        self.time_created_before = time_created_before
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids

        if self.image is not None:
            result['Image'] = self.image

        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.status is not None:
            result['Status'] = self.status

        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after

        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids = m.get('ExecutorIds')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')

        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

