# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteSparkWarehouseBatchSQLRequest(DaraModel):
    def __init__(
        self,
        agency: str = None,
        dbcluster_id: str = None,
        execute_result_limit: int = None,
        execute_time_limit_in_seconds: int = None,
        query: str = None,
        resource_group_name: str = None,
        runtime_config: str = None,
        schema: str = None,
    ):
        # The name of the client.
        self.agency = agency
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The maximum amount of execution result data that can be written to Object Storage Service (OSS). Unit: MB. Default value: 4096. The size of compressed objects is difficult to estimate. The data that is actually written to OSS is smaller than the specified value.
        self.execute_result_limit = execute_result_limit
        # The maximum execution duration. Unit: seconds. If a set of SQL statements fail to be executed for the specified period of time after submission, they are marked as a timeout error. The default value is 360000 seconds, which is equivalent to 100 hours.
        self.execute_time_limit_in_seconds = execute_time_limit_in_seconds
        # The SQL statements that you want to execute in batches. Separate multiple SQL statements with semicolons (;). The execution engine executes the SQL statements in sequence in the same session.
        # 
        # This parameter is required.
        self.query = query
        # The name of the resource group.
        # 
        # This parameter is required.
        self.resource_group_name = resource_group_name
        # The additional runtime parameter. Specify the parameter in the JSON format.
        self.runtime_config = runtime_config
        # The name of the database.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agency is not None:
            result['Agency'] = self.agency

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.execute_result_limit is not None:
            result['ExecuteResultLimit'] = self.execute_result_limit

        if self.execute_time_limit_in_seconds is not None:
            result['ExecuteTimeLimitInSeconds'] = self.execute_time_limit_in_seconds

        if self.query is not None:
            result['Query'] = self.query

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.runtime_config is not None:
            result['RuntimeConfig'] = self.runtime_config

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agency') is not None:
            self.agency = m.get('Agency')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExecuteResultLimit') is not None:
            self.execute_result_limit = m.get('ExecuteResultLimit')

        if m.get('ExecuteTimeLimitInSeconds') is not None:
            self.execute_time_limit_in_seconds = m.get('ExecuteTimeLimitInSeconds')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('RuntimeConfig') is not None:
            self.runtime_config = m.get('RuntimeConfig')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

