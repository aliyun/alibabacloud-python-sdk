# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeDataPushResultResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        push_results: main_models.DescribeDataPushResultResponseBodyPushResults = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The push results of data files.
        self.push_results = push_results
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.push_results:
            self.push_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.push_results is not None:
            result['PushResults'] = self.push_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PushResults') is not None:
            temp_model = main_models.DescribeDataPushResultResponseBodyPushResults()
            self.push_results = temp_model.from_map(m.get('PushResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataPushResultResponseBodyPushResults(DaraModel):
    def __init__(
        self,
        push_result: List[main_models.DescribeDataPushResultResponseBodyPushResultsPushResult] = None,
    ):
        self.push_result = push_result

    def validate(self):
        if self.push_result:
            for v1 in self.push_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PushResult'] = []
        if self.push_result is not None:
            for k1 in self.push_result:
                result['PushResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_result = []
        if m.get('PushResult') is not None:
            for k1 in m.get('PushResult'):
                temp_model = main_models.DescribeDataPushResultResponseBodyPushResultsPushResult()
                self.push_result.append(temp_model.from_map(k1))

        return self

class DescribeDataPushResultResponseBodyPushResultsPushResult(DaraModel):
    def __init__(
        self,
        name: str = None,
        status_stat_s: main_models.DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS = None,
        version: str = None,
    ):
        # The name of the data file.
        self.name = name
        # The push status of data files.
        self.status_stat_s = status_stat_s
        # The version number of the data file.
        self.version = version

    def validate(self):
        if self.status_stat_s:
            self.status_stat_s.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.status_stat_s is not None:
            result['StatusStatS'] = self.status_stat_s.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StatusStatS') is not None:
            temp_model = main_models.DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS()
            self.status_stat_s = temp_model.from_map(m.get('StatusStatS'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS(DaraModel):
    def __init__(
        self,
        status_stat: List[main_models.DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat] = None,
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
                temp_model = main_models.DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat()
                self.status_stat.append(temp_model.from_map(k1))

        return self

class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat(DaraModel):
    def __init__(
        self,
        region_id_count: int = None,
        region_ids: main_models.DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds = None,
        status: str = None,
    ):
        # The total number of ENS nodes.
        self.region_id_count = region_id_count
        # The push status of data files on the ENS node.
        self.region_ids = region_ids
        # The push status. The value is of the enumeration type. Valid values: SUCCESS FAILED PUSHING
        self.status = status

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id_count is not None:
            result['RegionIdCount'] = self.region_id_count

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIdCount') is not None:
            self.region_id_count = m.get('RegionIdCount')

        if m.get('RegionIds') is not None:
            temp_model = main_models.DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds()
            self.region_ids = temp_model.from_map(m.get('RegionIds'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds(DaraModel):
    def __init__(
        self,
        region_id: List[main_models.DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId] = None,
    ):
        self.region_id = region_id

    def validate(self):
        if self.region_id:
            for v1 in self.region_id:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionId'] = []
        if self.region_id is not None:
            for k1 in self.region_id:
                result['RegionId'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_id = []
        if m.get('RegionId') is not None:
            for k1 in m.get('RegionId'):
                temp_model = main_models.DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId()
                self.region_id.append(temp_model.from_map(k1))

        return self

class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        start_time: str = None,
        status_descrip: str = None,
        update_time: str = None,
    ):
        # The ID of the ENS node.
        self.region_id = region_id
        # The start time of the push operation. The time is displayed in UTC.
        self.start_time = start_time
        # The description of the status.
        self.status_descrip = status_descrip
        # The time when the status was last updated. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_descrip is not None:
            result['StatusDescrip'] = self.status_descrip

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusDescrip') is not None:
            self.status_descrip = m.get('StatusDescrip')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

