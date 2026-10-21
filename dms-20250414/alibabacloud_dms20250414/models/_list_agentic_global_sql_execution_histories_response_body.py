# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListAgenticGlobalSqlExecutionHistoriesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAgenticGlobalSqlExecutionHistoriesResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of SQL execution history.
        self.data = data
        # The error code. This parameter is empty when the request is successful.
        self.error_code = error_code
        # The error message returned when the call fails.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success
        # The total number of entries that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAgenticGlobalSqlExecutionHistoriesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAgenticGlobalSqlExecutionHistoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        actor_id: str = None,
        actor_name: str = None,
        actor_type: str = None,
        affected_rows: int = None,
        agent_owner_id: str = None,
        catalog_uuid: str = None,
        client_ip: str = None,
        cost: int = None,
        database_search_name: str = None,
        database_uuid: str = None,
        error: str = None,
        executed_sql: str = None,
        execution_status: str = None,
        original_sql: str = None,
        query_id: str = None,
        returned_rows: int = None,
        scenario: str = None,
        sql_type: str = None,
        start_time: str = None,
        workflow_id: str = None,
    ):
        # The ID of the actor. A user ID starts with usr_, and an agent ID starts with agt_.
        self.actor_id = actor_id
        # The name of the actor.
        self.actor_name = actor_name
        # The type of the actor. A value of HUMAN indicates a user, and a value of AGENT indicates an agent.
        self.actor_type = actor_type
        # The number of affected rows.
        self.affected_rows = affected_rows
        # The ID of the user to which the agent belongs. The ID starts with usr_.
        self.agent_owner_id = agent_owner_id
        # The catalog UUID to which the execution belongs.
        self.catalog_uuid = catalog_uuid
        # The IP address of the client that initiates the execution, excluding the port. This parameter is empty in workflow scenarios or when the IP address is not recorded.
        self.client_ip = client_ip
        # The execution duration of the SQL statement.
        self.cost = cost
        # The search name of the database.
        self.database_search_name = database_search_name
        # The database UUID to which the execution belongs.
        self.database_uuid = database_uuid
        # The error message returned when the execution fails.
        self.error = error
        # The actual SQL statement that is executed.
        self.executed_sql = executed_sql
        # The execution status. Valid values:
        # - SUCCESS: The execution is successful.
        # - FAILED: The execution fails.
        # - BLOCKED: The execution is blocked or not actually executed.
        self.execution_status = execution_status
        # The original SQL statement.
        self.original_sql = original_sql
        # The query ID of the execution.
        self.query_id = query_id
        # The number of returned rows.
        self.returned_rows = returned_rows
        # The execution scenario. Valid values:
        # - AGENT_QUERY: The agent directly executes the SQL statement.
        # - WORKFLOW_QUERY: The SQL statement is asynchronously executed through a workflow.
        self.scenario = scenario
        # The SQL type.
        self.sql_type = sql_type
        # The start time of the execution. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.start_time = start_time
        # The workflow ID. This parameter may be empty in non-workflow scenarios.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actor_id is not None:
            result['ActorId'] = self.actor_id

        if self.actor_name is not None:
            result['ActorName'] = self.actor_name

        if self.actor_type is not None:
            result['ActorType'] = self.actor_type

        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows

        if self.agent_owner_id is not None:
            result['AgentOwnerId'] = self.agent_owner_id

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.cost is not None:
            result['Cost'] = self.cost

        if self.database_search_name is not None:
            result['DatabaseSearchName'] = self.database_search_name

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.error is not None:
            result['Error'] = self.error

        if self.executed_sql is not None:
            result['ExecutedSql'] = self.executed_sql

        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status

        if self.original_sql is not None:
            result['OriginalSql'] = self.original_sql

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.returned_rows is not None:
            result['ReturnedRows'] = self.returned_rows

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActorId') is not None:
            self.actor_id = m.get('ActorId')

        if m.get('ActorName') is not None:
            self.actor_name = m.get('ActorName')

        if m.get('ActorType') is not None:
            self.actor_type = m.get('ActorType')

        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')

        if m.get('AgentOwnerId') is not None:
            self.agent_owner_id = m.get('AgentOwnerId')

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('DatabaseSearchName') is not None:
            self.database_search_name = m.get('DatabaseSearchName')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('ExecutedSql') is not None:
            self.executed_sql = m.get('ExecutedSql')

        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')

        if m.get('OriginalSql') is not None:
            self.original_sql = m.get('OriginalSql')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('ReturnedRows') is not None:
            self.returned_rows = m.get('ReturnedRows')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

