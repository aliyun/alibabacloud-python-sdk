# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeJobResourceUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeJobResourceUsageResponseBodyData = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The queried resource usage.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeJobResourceUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeJobResourceUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        job_acu_usage: List[main_models.DescribeJobResourceUsageResponseBodyDataJobAcuUsage] = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        total_count: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The AnalyticDB compute unit (ACU) usage of the job resource group.
        self.job_acu_usage = job_acu_usage
        self.page_number = page_number
        self.page_size = page_size
        # The start time of the query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        self.total_count = total_count

    def validate(self):
        if self.job_acu_usage:
            for v1 in self.job_acu_usage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['JobAcuUsage'] = []
        if self.job_acu_usage is not None:
            for k1 in self.job_acu_usage:
                result['JobAcuUsage'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.job_acu_usage = []
        if m.get('JobAcuUsage') is not None:
            for k1 in m.get('JobAcuUsage'):
                temp_model = main_models.DescribeJobResourceUsageResponseBodyDataJobAcuUsage()
                self.job_acu_usage.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeJobResourceUsageResponseBodyDataJobAcuUsage(DaraModel):
    def __init__(
        self,
        acu_usage_detail: main_models.DescribeJobResourceUsageResponseBodyDataJobAcuUsageAcuUsageDetail = None,
        job_end_time: str = None,
        job_id: str = None,
        job_start_time: str = None,
        resource_group_name: str = None,
        use_cache_pool: bool = None,
    ):
        # The ACU usage.
        self.acu_usage_detail = acu_usage_detail
        # The end time of the job. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.job_end_time = job_end_time
        # The job ID.
        self.job_id = job_id
        # The start time of the job. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.job_start_time = job_start_time
        # The name of the job resource group.
        self.resource_group_name = resource_group_name
        self.use_cache_pool = use_cache_pool

    def validate(self):
        if self.acu_usage_detail:
            self.acu_usage_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acu_usage_detail is not None:
            result['AcuUsageDetail'] = self.acu_usage_detail.to_map()

        if self.job_end_time is not None:
            result['JobEndTime'] = self.job_end_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_start_time is not None:
            result['JobStartTime'] = self.job_start_time

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.use_cache_pool is not None:
            result['UseCachePool'] = self.use_cache_pool

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcuUsageDetail') is not None:
            temp_model = main_models.DescribeJobResourceUsageResponseBodyDataJobAcuUsageAcuUsageDetail()
            self.acu_usage_detail = temp_model.from_map(m.get('AcuUsageDetail'))

        if m.get('JobEndTime') is not None:
            self.job_end_time = m.get('JobEndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobStartTime') is not None:
            self.job_start_time = m.get('JobStartTime')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('UseCachePool') is not None:
            self.use_cache_pool = m.get('UseCachePool')

        return self

class DescribeJobResourceUsageResponseBodyDataJobAcuUsageAcuUsageDetail(DaraModel):
    def __init__(
        self,
        elastic_acu_number: float = None,
        reserved_acu_number: float = None,
        spot_acu_number: float = None,
        spot_acu_percentage: float = None,
        total_acu_number: float = None,
    ):
        # The number of ACUs for the elastic resources.
        self.elastic_acu_number = elastic_acu_number
        # The number of ACUs for the reserved resources.
        self.reserved_acu_number = reserved_acu_number
        # The number of spot ACUs.
        self.spot_acu_number = spot_acu_number
        # The percent of spot ACUs.
        self.spot_acu_percentage = spot_acu_percentage
        # The total number of ACUs.
        self.total_acu_number = total_acu_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_acu_number is not None:
            result['ElasticAcuNumber'] = self.elastic_acu_number

        if self.reserved_acu_number is not None:
            result['ReservedAcuNumber'] = self.reserved_acu_number

        if self.spot_acu_number is not None:
            result['SpotAcuNumber'] = self.spot_acu_number

        if self.spot_acu_percentage is not None:
            result['SpotAcuPercentage'] = self.spot_acu_percentage

        if self.total_acu_number is not None:
            result['TotalAcuNumber'] = self.total_acu_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticAcuNumber') is not None:
            self.elastic_acu_number = m.get('ElasticAcuNumber')

        if m.get('ReservedAcuNumber') is not None:
            self.reserved_acu_number = m.get('ReservedAcuNumber')

        if m.get('SpotAcuNumber') is not None:
            self.spot_acu_number = m.get('SpotAcuNumber')

        if m.get('SpotAcuPercentage') is not None:
            self.spot_acu_percentage = m.get('SpotAcuPercentage')

        if m.get('TotalAcuNumber') is not None:
            self.total_acu_number = m.get('TotalAcuNumber')

        return self

