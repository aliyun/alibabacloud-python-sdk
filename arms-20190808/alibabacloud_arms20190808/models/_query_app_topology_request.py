# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class QueryAppTopologyRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        db: str = None,
        db_name: str = None,
        end_time: int = None,
        filters: Dict[str, str] = None,
        pid: str = None,
        region_id: str = None,
        rpc: str = None,
        start_time: int = None,
        type: str = None,
    ):
        # The application type
        self.app_type = app_type
        # The database domain name.
        self.db = db
        # The name of the database.
        self.db_name = db_name
        # The end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The filter conditions.
        self.filters = filters
        # The ID of the application.
        # 
        # Log on to the **ARMS console**. In the left-side navigation pane, choose **Browser Monitoring** > **Browser Monitoring**. On the Browser Monitoring page, click the name of an application. The URL in the address bar contains the process ID (PID) of the application. The PID is indicated in the pid=xxx format. The PID is usually percent encoded as xxx%40xxx. You must modify this value to remove the percent encoding. For example, if the PID in the URL is eb4zdose6v%409781be0f44d\\*\\*\\*\\*, you must replace %40 with an at sign (@) to obtain eb4zdose6v@9781be0f44d\\*\\*\\*\\*.
        self.pid = pid
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # RPC interface name.
        self.rpc = rpc
        # The start of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type kind of topology.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.db is not None:
            result['Db'] = self.db

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.filters is not None:
            result['Filters'] = self.filters

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rpc is not None:
            result['Rpc'] = self.rpc

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Rpc') is not None:
            self.rpc = m.get('Rpc')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

