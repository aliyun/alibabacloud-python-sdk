# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityScanRunsResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListDataQualityScanRunsResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The page information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListDataQualityScanRunsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityScanRunsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        data_quality_scan_runs: List[main_models.ListDataQualityScanRunsResponseBodyPageInfoDataQualityScanRuns] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of data quality monitor run records.
        self.data_quality_scan_runs = data_quality_scan_runs
        # The page number of the results. Default value: 1.
        self.page_number = page_number
        # The number of records per page. Default value: 10.
        self.page_size = page_size
        # The total number of records returned.
        self.total_count = total_count

    def validate(self):
        if self.data_quality_scan_runs:
            for v1 in self.data_quality_scan_runs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityScanRuns'] = []
        if self.data_quality_scan_runs is not None:
            for k1 in self.data_quality_scan_runs:
                result['DataQualityScanRuns'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_scan_runs = []
        if m.get('DataQualityScanRuns') is not None:
            for k1 in m.get('DataQualityScanRuns'):
                temp_model = main_models.ListDataQualityScanRunsResponseBodyPageInfoDataQualityScanRuns()
                self.data_quality_scan_runs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityScanRunsResponseBodyPageInfoDataQualityScanRuns(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        finish_time: int = None,
        id: int = None,
        parameters: List[main_models.ListDataQualityScanRunsResponseBodyPageInfoDataQualityScanRunsParameters] = None,
        status: str = None,
    ):
        # The time when the data quality monitor starts running.
        self.create_time = create_time
        # The time when the data quality monitor stops.
        self.finish_time = finish_time
        # The ID of the data quality monitor running record.
        self.id = id
        # The parameters configured for the instance.
        self.parameters = parameters
        # The status of the instance.
        # 
        # *   Pass
        # *   Running
        # *   Error
        # *   Warn
        # *   Fail
        self.status = status

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.ListDataQualityScanRunsResponseBodyPageInfoDataQualityScanRunsParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListDataQualityScanRunsResponseBodyPageInfoDataQualityScanRunsParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value. You can use a scheduling time expression.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

