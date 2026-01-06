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
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The language of file titles and error messages. Valid values:
        # 
        # *   **zh**: simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The query ID.
        # 
        # >  You can call the [DescribeDiagnosisRecords](https://help.aliyun.com/document_detail/308207.html) operation to query the diagnostic information about SQL statements for an AnalyticDB for MySQL cluster, including the query ID.
        self.process_id = process_id
        # The IP address and port number of the AnalyticDB for MySQL frontend node on which the SQL statement is executed.
        # 
        # >  You can call the [DescribeDiagnosisRecords](https://help.aliyun.com/document_detail/308207.html) operation to query the diagnostic information about SQL statements for an AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster, including the IP address and port number of the frontend node.
        self.process_rc_host = process_rc_host
        # The execution start time of the SQL statement. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  You can call the [DescribeDiagnosisRecords](https://help.aliyun.com/document_detail/308207.html) operation to query the diagnostic information about SQL statements for an AnalyticDB for MySQL cluster, including the execution start time of the SQL statement.
        self.process_start_time = process_start_time
        # The status of the SQL statement. Valid values:
        # 
        # *   **running**
        # *   **finished**
        # *   **failed**
        # 
        # >  You can call the [DescribeDiagnosisRecords](https://help.aliyun.com/document_detail/308207.html) operation to query the diagnostic information about SQL statements for an AnalyticDB for MySQL cluster, including the status of the SQL statement.
        self.process_state = process_state
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
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

