# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgenticSqlExecutionHistoriesRequest(DaraModel):
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
        # The ID of the actor. User IDs start with usr_, and agent IDs start with agt_. If you do not specify this parameter, a user queries their own execution history and the execution history of their agents, while an agent queries only its own execution history. If you specify this parameter, exact matching is performed, and the value must be the ID of the current user or an agent owned by the current user.
        self.actor_id = actor_id
        # The name of the actor for exact matching.
        self.actor_name = actor_name
        # The type of the actor for exact matching. Valid values: HUMAN and AGENT.
        self.actor_type = actor_type
        # The catalog UUID for exact matching. You can obtain this value by calling ListAgenticCatalog or SearchAgenticCatalog.
        self.catalog_uuid = catalog_uuid
        # The database UUID for exact matching. You can obtain this value by calling ListAgenticDatabase or SearchAgenticDatabase.
        self.database_uuid = database_uuid
        # The end time of the query. Specify the time in the yyyy-MM-dd HH:mm:ss format. If you do not specify this parameter, the default value is the current time. If the format cannot be parsed or the end time is earlier than the start time, the request fails.
        self.end_time = end_time
        # The page number. Pages start from 1. Default value: 1.
        self.page = page
        # The execution scenario for exact matching. Valid values:
        # - AGENT_QUERY: The agent directly executes the SQL statement.
        # - WORKFLOW_QUERY: The SQL statement is asynchronously executed through a workflow.
        # If you do not specify this parameter, both scenarios are queried.
        self.scenario = scenario
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.size = size
        # The keyword for fuzzy matching against the original SQL statement.
        self.sql_keyword = sql_keyword
        # The SQL type for exact matching.
        self.sql_type = sql_type
        # The start time of the query. Specify the time in the yyyy-MM-dd HH:mm:ss format. If you do not specify this parameter, the default time range is the last 7 days. If the specified time is more than 730 days ago or the format cannot be parsed, the query is performed for the last 730 days.
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

