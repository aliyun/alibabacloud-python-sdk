# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class QueryLiveDomainMultiStreamListResponseBody(DaraModel):
    def __init__(
        self,
        online_streams: List[main_models.QueryLiveDomainMultiStreamListResponseBodyOnlineStreams] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The online streams returned.
        self.online_streams = online_streams
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.online_streams:
            for v1 in self.online_streams:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OnlineStreams'] = []
        if self.online_streams is not None:
            for k1 in self.online_streams:
                result['OnlineStreams'].append(k1.to_map() if k1 else None)

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
        self.online_streams = []
        if m.get('OnlineStreams') is not None:
            for k1 in m.get('OnlineStreams'):
                temp_model = main_models.QueryLiveDomainMultiStreamListResponseBodyOnlineStreams()
                self.online_streams.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryLiveDomainMultiStreamListResponseBodyOnlineStreams(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        change_logs: List[main_models.QueryLiveDomainMultiStreamListResponseBodyOnlineStreamsChangeLogs] = None,
        domain: str = None,
        optimal_mode: str = None,
        stream_name: str = None,
        upstream_list: List[main_models.QueryLiveDomainMultiStreamListResponseBodyOnlineStreamsUpstreamList] = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The switchover records.
        self.change_logs = change_logs
        # The main streaming domain.
        self.domain = domain
        # Indicates whether the dual-stream disaster recovery feature is enabled. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.optimal_mode = optimal_mode
        # The name of the live stream.
        self.stream_name = stream_name
        # The standby streams.
        self.upstream_list = upstream_list

    def validate(self):
        if self.change_logs:
            for v1 in self.change_logs:
                 if v1:
                    v1.validate()
        if self.upstream_list:
            for v1 in self.upstream_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        result['ChangeLogs'] = []
        if self.change_logs is not None:
            for k1 in self.change_logs:
                result['ChangeLogs'].append(k1.to_map() if k1 else None)

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.optimal_mode is not None:
            result['OptimalMode'] = self.optimal_mode

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        result['UpstreamList'] = []
        if self.upstream_list is not None:
            for k1 in self.upstream_list:
                result['UpstreamList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        self.change_logs = []
        if m.get('ChangeLogs') is not None:
            for k1 in m.get('ChangeLogs'):
                temp_model = main_models.QueryLiveDomainMultiStreamListResponseBodyOnlineStreamsChangeLogs()
                self.change_logs.append(temp_model.from_map(k1))

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OptimalMode') is not None:
            self.optimal_mode = m.get('OptimalMode')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        self.upstream_list = []
        if m.get('UpstreamList') is not None:
            for k1 in m.get('UpstreamList'):
                temp_model = main_models.QueryLiveDomainMultiStreamListResponseBodyOnlineStreamsUpstreamList()
                self.upstream_list.append(temp_model.from_map(k1))

        return self

class QueryLiveDomainMultiStreamListResponseBodyOnlineStreamsUpstreamList(DaraModel):
    def __init__(
        self,
        master_flag: bool = None,
        upstream_ip: str = None,
        upstream_sequence: str = None,
        upstream_time: str = None,
    ):
        # The active/standby tag.
        # 
        # >  This parameter indicates whether the active or standby stream is being distributed.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.master_flag = master_flag
        # The IP address of the stream ingest client.
        self.upstream_ip = upstream_ip
        # The unique identifier of the stream ingest.
        self.upstream_sequence = upstream_sequence
        # The stream ingest time.
        self.upstream_time = upstream_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_flag is not None:
            result['MasterFlag'] = self.master_flag

        if self.upstream_ip is not None:
            result['UpstreamIp'] = self.upstream_ip

        if self.upstream_sequence is not None:
            result['UpstreamSequence'] = self.upstream_sequence

        if self.upstream_time is not None:
            result['UpstreamTime'] = self.upstream_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterFlag') is not None:
            self.master_flag = m.get('MasterFlag')

        if m.get('UpstreamIp') is not None:
            self.upstream_ip = m.get('UpstreamIp')

        if m.get('UpstreamSequence') is not None:
            self.upstream_sequence = m.get('UpstreamSequence')

        if m.get('UpstreamTime') is not None:
            self.upstream_time = m.get('UpstreamTime')

        return self

class QueryLiveDomainMultiStreamListResponseBodyOnlineStreamsChangeLogs(DaraModel):
    def __init__(
        self,
        change_reason: str = None,
        change_time: str = None,
        master_upstream: str = None,
        upstream_ip: str = None,
        upstream_sequence: str = None,
    ):
        # The reason for the switchover.
        # 
        # *   merge cut manually: You proactively switched the stream.
        # *   master stream no data: No data is available in the active stream.
        # *   master stream low quality: The quality of the active stream deteriorated.
        self.change_reason = change_reason
        # The switchover time.
        self.change_time = change_time
        # The stream used after the switchover.
        self.master_upstream = master_upstream
        # The IP address used after the switchover.
        self.upstream_ip = upstream_ip
        # The identifier of the stream after the switchover.
        self.upstream_sequence = upstream_sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_reason is not None:
            result['ChangeReason'] = self.change_reason

        if self.change_time is not None:
            result['ChangeTime'] = self.change_time

        if self.master_upstream is not None:
            result['MasterUpstream'] = self.master_upstream

        if self.upstream_ip is not None:
            result['UpstreamIp'] = self.upstream_ip

        if self.upstream_sequence is not None:
            result['UpstreamSequence'] = self.upstream_sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeReason') is not None:
            self.change_reason = m.get('ChangeReason')

        if m.get('ChangeTime') is not None:
            self.change_time = m.get('ChangeTime')

        if m.get('MasterUpstream') is not None:
            self.master_upstream = m.get('MasterUpstream')

        if m.get('UpstreamIp') is not None:
            self.upstream_ip = m.get('UpstreamIp')

        if m.get('UpstreamSequence') is not None:
            self.upstream_sequence = m.get('UpstreamSequence')

        return self

