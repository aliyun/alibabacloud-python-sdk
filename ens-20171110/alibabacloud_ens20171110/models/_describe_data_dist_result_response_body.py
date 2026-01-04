# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeDataDistResultResponseBody(DaraModel):
    def __init__(
        self,
        dist_results: main_models.DescribeDataDistResultResponseBodyDistResults = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The distribution status of data files on edge instances.
        self.dist_results = dist_results
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dist_results:
            self.dist_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dist_results is not None:
            result['DistResults'] = self.dist_results.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistResults') is not None:
            temp_model = main_models.DescribeDataDistResultResponseBodyDistResults()
            self.dist_results = temp_model.from_map(m.get('DistResults'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataDistResultResponseBodyDistResults(DaraModel):
    def __init__(
        self,
        dist_result: List[main_models.DescribeDataDistResultResponseBodyDistResultsDistResult] = None,
    ):
        self.dist_result = dist_result

    def validate(self):
        if self.dist_result:
            for v1 in self.dist_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DistResult'] = []
        if self.dist_result is not None:
            for k1 in self.dist_result:
                result['DistResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dist_result = []
        if m.get('DistResult') is not None:
            for k1 in m.get('DistResult'):
                temp_model = main_models.DescribeDataDistResultResponseBodyDistResultsDistResult()
                self.dist_result.append(temp_model.from_map(k1))

        return self

class DescribeDataDistResultResponseBodyDistResultsDistResult(DaraModel):
    def __init__(
        self,
        name: str = None,
        status_stats: main_models.DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats = None,
        version: str = None,
    ):
        # The name of the data file.
        self.name = name
        # The distribution status statistics.
        self.status_stats = status_stats
        # The version number of the data file.
        self.version = version

    def validate(self):
        if self.status_stats:
            self.status_stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.status_stats is not None:
            result['StatusStats'] = self.status_stats.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StatusStats') is not None:
            temp_model = main_models.DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats()
            self.status_stats = temp_model.from_map(m.get('StatusStats'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats(DaraModel):
    def __init__(
        self,
        status_stat: List[main_models.DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat] = None,
    ):
        self.status_stat = status_stat

    def validate(self):
        if self.status_stat:
            for v1 in self.status_stat:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StatusStat'] = []
        if self.status_stat is not None:
            for k1 in self.status_stat:
                result['StatusStat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.status_stat = []
        if m.get('StatusStat') is not None:
            for k1 in m.get('StatusStat'):
                temp_model = main_models.DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat()
                self.status_stat.append(temp_model.from_map(k1))

        return self

class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat(DaraModel):
    def __init__(
        self,
        instance_count: str = None,
        instances: main_models.DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances = None,
        status: str = None,
    ):
        # The number of associated edge instances.
        self.instance_count = instance_count
        # The distribution status of the edge instance.
        self.instances = instances
        # The distribution status. The value is of the enumeration type. Valid values:
        # 
        # *   SUCCESS: The distribution is successful.
        # *   FAILED: The distribution failed.
        # *   DISTING: The data is being distributed.
        # *   POD_RESTARTING: The idle pod is being restarted.
        # *   DELETED: The data is cleared or removed.
        self.status = status

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('Instances') is not None:
            temp_model = main_models.DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        start_time: str = None,
        status_descrip: str = None,
        update_time: str = None,
    ):
        # The ID of the instance
        self.instance_id = instance_id
        # The start time of the distribution. The time is displayed in UTC.
        self.start_time = start_time
        # The description of the distribution status.
        self.status_descrip = status_descrip
        # The time when the distribution status was last updated. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_descrip is not None:
            result['StatusDescrip'] = self.status_descrip

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusDescrip') is not None:
            self.status_descrip = m.get('StatusDescrip')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

