# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiagnosisSQLInfoRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        lang: str = None,
        process_id: str = None,
        process_rc_host: str = None,
        process_start_time: int = None,
        process_state: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the cluster IDs of AnalyticDB for MySQL clusters in a specific region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The language of the file title and error messages in the downloaded file. Valid values:
        # - **zh**: simplified Chinese.
        # - **en**: English.
        # - **ja**: Japanese.
        # - **zh-tw**: traditional Chinese.
        self.lang = lang
        # The query ID.
        # > You can call the [DescribeDiagnosisRecords](https://help.aliyun.com/document_detail/308207.html) operation to query the SQL summary information of a specific AnalyticDB for MySQL cluster, including the query ID.
        self.process_id = process_id
        # The IP address and port number of the AnalyticDB for MySQL frontend node that executes the SQL statement.
        # > You can call the [DescribeDiagnosisRecords](https://help.aliyun.com/document_detail/308207.html) operation to query the SQL summary information of a specific AnalyticDB for MySQL cluster, including the IP address and port number of the frontend node.
        self.process_rc_host = process_rc_host
        # The start time of the SQL statement execution. Specify the value as a UNIX timestamp in milliseconds.
        # > You can call the [DescribeDiagnosisRecords](https://help.aliyun.com/document_detail/308207.html) operation to query the SQL summary information of a specific AnalyticDB for MySQL cluster, including the start time of the SQL statement execution.
        self.process_start_time = process_start_time
        # The status of the SQL statement. Valid values:
        # - **running**: The SQL statement is being executed.
        # - **finished**: The SQL statement has been executed.
        # - **failed**: The SQL statement failed to be executed.
        # > You can call the [DescribeDiagnosisRecords](https://help.aliyun.com/document_detail/308207.html) operation to query the SQL summary information of a specific AnalyticDB for MySQL cluster, including the status of the SQL statement.
        self.process_state = process_state
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the region IDs supported by AnalyticDB for MySQL.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_rc_host is not None:
            result['ProcessRcHost'] = self.process_rc_host

        if self.process_start_time is not None:
            result['ProcessStartTime'] = self.process_start_time

        if self.process_state is not None:
            result['ProcessState'] = self.process_state

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessRcHost') is not None:
            self.process_rc_host = m.get('ProcessRcHost')

        if m.get('ProcessStartTime') is not None:
            self.process_start_time = m.get('ProcessStartTime')

        if m.get('ProcessState') is not None:
            self.process_state = m.get('ProcessState')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

