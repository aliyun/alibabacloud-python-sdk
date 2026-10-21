# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgenticGlobalSqlExecutionHistoriesRequest(DaraModel):
    def __init__(
        self,
        actor_id: str = None,
        actor_name: str = None,
        actor_type: str = None,
        catalog_uuid: str = None,
        database_uuid: str = None,
        end_time: str = None,
        page: int = None,
        scenario: str = None,
        size: int = None,
        sql_keyword: str = None,
        sql_type: str = None,
        start_time: str = None,
    ):
        # The ID of the actor. A user ID starts with usr_, and an agent ID starts with agt_. If you do not specify this parameter, all records within the current tenant are queried. If you specify a user ID, the records of the user and the agents under the user are included. If you specify an agent ID, only the records of the agent are matched. The actor must belong to the current tenant.
        self.actor_id = actor_id
        # The name of the actor for exact match.
        self.actor_name = actor_name
        # The type of the actor for exact match. Valid values: HUMAN and AGENT.
        self.actor_type = actor_type
        # The catalog UUID for exact match. You can obtain this value by calling ListAgenticCatalog or SearchAgenticCatalog.
        self.catalog_uuid = catalog_uuid
        # The database UUID for exact match. You can obtain this value by calling ListAgenticDatabase or SearchAgenticDatabase.
        self.database_uuid = database_uuid
        # The end time of the query. Specify the time in the yyyy-MM-dd HH:mm:ss format. If you do not specify this parameter, the default end time is the current time. If the format cannot be parsed or the end time is earlier than the start time, the request fails.
        self.end_time = end_time
        # The page number. Pages start from 1. Default value: 1.
        self.page = page
        # The execution scenario for exact match. Valid values:
        # - AGENT_QUERY: The agent directly executes the SQL statement.
        # - WORKFLOW_QUERY: The SQL statement is asynchronously executed through a workflow.
        # If you do not specify this parameter, both scenarios are queried.
        self.scenario = scenario
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.size = size
        # The keyword for fuzzy match based on the original SQL statement.
        self.sql_keyword = sql_keyword
        # The SQL type for exact match.
        self.sql_type = sql_type
        # The start time of the query. Specify the time in the yyyy-MM-dd HH:mm:ss format. If you do not specify this parameter, the default time range is the last 7 days. If the specified time is earlier than 730 days ago or the format cannot be parsed, the query starts from 730 days ago.
        self.start_time = start_time

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

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page is not None:
            result['Page'] = self.page

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.size is not None:
            result['Size'] = self.size

        if self.sql_keyword is not None:
            result['SqlKeyword'] = self.sql_keyword

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActorId') is not None:
            self.actor_id = m.get('ActorId')

        if m.get('ActorName') is not None:
            self.actor_name = m.get('ActorName')

        if m.get('ActorType') is not None:
            self.actor_type = m.get('ActorType')

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SqlKeyword') is not None:
            self.sql_keyword = m.get('SqlKeyword')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

