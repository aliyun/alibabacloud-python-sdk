# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SearchTracesByPageRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        exclusion_filters: List[main_models.SearchTracesByPageRequestExclusionFilters] = None,
        is_error: bool = None,
        min_duration: int = None,
        operation_name: str = None,
        page_number: int = None,
        page_size: int = None,
        pid: str = None,
        region_id: str = None,
        reverse: bool = None,
        service_ip: str = None,
        service_name: str = None,
        start_time: int = None,
        tags: List[main_models.SearchTracesByPageRequestTags] = None,
    ):
        # The end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The filter conditions.
        self.exclusion_filters = exclusion_filters
        # Specifies whether to include the traces of abnormal calls.
        # 
        # *   `true`: No
        # *   `false` (default): Yes
        self.is_error = is_error
        # The minimum amount of time consumed by traces. Unit: milliseconds.
        self.min_duration = min_duration
        # The name of the traced span.
        self.operation_name = operation_name
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100.
        self.page_size = page_size
        # The application ID.
        self.pid = pid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to sort the query results in chronological order or reverse chronological order. Default value: `false`.
        # 
        # *   `true`: sorts the query results in reverse chronological order.
        # *   `false`: sorts the query results in chronological order.
        self.reverse = reverse
        # The IP address of the host where the application resides.
        self.service_ip = service_ip
        # The name of the application.
        self.service_name = service_name
        # The beginning of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.exclusion_filters:
            for v1 in self.exclusion_filters:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k1 in self.exclusion_filters:
                result['ExclusionFilters'].append(k1.to_map() if k1 else None)

        if self.is_error is not None:
            result['IsError'] = self.is_error

        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k1 in m.get('ExclusionFilters'):
                temp_model = main_models.SearchTracesByPageRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k1))

        if m.get('IsError') is not None:
            self.is_error = m.get('IsError')

        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.SearchTracesByPageRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class SearchTracesByPageRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The following system preset fields are provided:
        # 
        # *   traceId: the ID of the trace.
        # *   serverApp: the name of the server application.
        # *   clientApp: the name of the client application.
        # *   service: the name of the interface.
        # *   rpc: the type of the call.
        # *   msOfSpan: the duration exceeds a specific value.
        # *   clientIp: the IP address of the client.
        # *   serverIp: the IP address of the server.
        # *   isError: specifies whether the call is abnormal.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SearchTracesByPageRequestExclusionFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key that is used to filter the query results.
        self.key = key
        # The value of the key that is used to filter the query results.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

