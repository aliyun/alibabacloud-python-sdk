# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ScheduledSQLConfiguration(DaraModel):
    def __init__(
        self,
        data_format: str = None,
        dest_endpoint: str = None,
        dest_logstore: str = None,
        dest_project: str = None,
        dest_role_arn: str = None,
        force_complete: bool = None,
        from_time: int = None,
        from_time_expr: str = None,
        max_concurrency: int = None,
        max_retries: int = None,
        max_run_time_in_seconds: int = None,
        parameters: Dict[str, Any] = None,
        resource_pool: str = None,
        role_arn: str = None,
        script: str = None,
        source_logstore: str = None,
        sql_type: str = None,
        to_time: int = None,
        to_time_expr: str = None,
    ):
        # This parameter is required.
        self.data_format = data_format
        # This parameter is required.
        self.dest_endpoint = dest_endpoint
        # This parameter is required.
        self.dest_logstore = dest_logstore
        # This parameter is required.
        self.dest_project = dest_project
        # This parameter is required.
        self.dest_role_arn = dest_role_arn
        self.force_complete = force_complete
        # This parameter is required.
        self.from_time = from_time
        # This parameter is required.
        self.from_time_expr = from_time_expr
        self.max_concurrency = max_concurrency
        # This parameter is required.
        self.max_retries = max_retries
        # This parameter is required.
        self.max_run_time_in_seconds = max_run_time_in_seconds
        # This parameter is required.
        self.parameters = parameters
        # This parameter is required.
        self.resource_pool = resource_pool
        # This parameter is required.
        self.role_arn = role_arn
        # This parameter is required.
        self.script = script
        # This parameter is required.
        self.source_logstore = source_logstore
        # This parameter is required.
        self.sql_type = sql_type
        # This parameter is required.
        self.to_time = to_time
        # This parameter is required.
        self.to_time_expr = to_time_expr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_format is not None:
            result['dataFormat'] = self.data_format

        if self.dest_endpoint is not None:
            result['destEndpoint'] = self.dest_endpoint

        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore

        if self.dest_project is not None:
            result['destProject'] = self.dest_project

        if self.dest_role_arn is not None:
            result['destRoleArn'] = self.dest_role_arn

        if self.force_complete is not None:
            result['forceComplete'] = self.force_complete

        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.from_time_expr is not None:
            result['fromTimeExpr'] = self.from_time_expr

        if self.max_concurrency is not None:
            result['maxConcurrency'] = self.max_concurrency

        if self.max_retries is not None:
            result['maxRetries'] = self.max_retries

        if self.max_run_time_in_seconds is not None:
            result['maxRunTimeInSeconds'] = self.max_run_time_in_seconds

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.resource_pool is not None:
            result['resourcePool'] = self.resource_pool

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.script is not None:
            result['script'] = self.script

        if self.source_logstore is not None:
            result['sourceLogstore'] = self.source_logstore

        if self.sql_type is not None:
            result['sqlType'] = self.sql_type

        if self.to_time is not None:
            result['toTime'] = self.to_time

        if self.to_time_expr is not None:
            result['toTimeExpr'] = self.to_time_expr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataFormat') is not None:
            self.data_format = m.get('dataFormat')

        if m.get('destEndpoint') is not None:
            self.dest_endpoint = m.get('destEndpoint')

        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')

        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')

        if m.get('destRoleArn') is not None:
            self.dest_role_arn = m.get('destRoleArn')

        if m.get('forceComplete') is not None:
            self.force_complete = m.get('forceComplete')

        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('fromTimeExpr') is not None:
            self.from_time_expr = m.get('fromTimeExpr')

        if m.get('maxConcurrency') is not None:
            self.max_concurrency = m.get('maxConcurrency')

        if m.get('maxRetries') is not None:
            self.max_retries = m.get('maxRetries')

        if m.get('maxRunTimeInSeconds') is not None:
            self.max_run_time_in_seconds = m.get('maxRunTimeInSeconds')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('resourcePool') is not None:
            self.resource_pool = m.get('resourcePool')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('script') is not None:
            self.script = m.get('script')

        if m.get('sourceLogstore') is not None:
            self.source_logstore = m.get('sourceLogstore')

        if m.get('sqlType') is not None:
            self.sql_type = m.get('sqlType')

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        if m.get('toTimeExpr') is not None:
            self.to_time_expr = m.get('toTimeExpr')

        return self

