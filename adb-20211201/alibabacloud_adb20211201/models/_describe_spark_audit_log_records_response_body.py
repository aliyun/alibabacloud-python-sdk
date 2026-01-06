# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeSparkAuditLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        dbcluster_id: str = None,
        items: List[main_models.DescribeSparkAuditLogRecordsResponseBodyItems] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The list of SQL audit logs.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries to return per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSparkAuditLogRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSparkAuditLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_ip: str = None,
        error_msg: str = None,
        error_trace: str = None,
        execute_time: str = None,
        inner_query_id: str = None,
        is_diagnosable: bool = None,
        process_id: str = None,
        resource_group_name: str = None,
        sqltext: str = None,
        statement_id: str = None,
        statement_source: str = None,
        status: str = None,
        total_time: int = None,
        user: str = None,
    ):
        # The Spark application ID.
        self.app_id = app_id
        # The source IP address.
        self.client_ip = client_ip
        # The SQL execution error message.
        self.error_msg = error_msg
        # The SQL execution error stack trace.
        self.error_trace = error_trace
        # The start time of the SQL statement. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is in UTC.
        self.execute_time = execute_time
        # The ID of the query executed within the Spark application.
        self.inner_query_id = inner_query_id
        # Whether it can be diagnosed.
        self.is_diagnosable = is_diagnosable
        # The query ID.
        self.process_id = process_id
        # The resource group name.
        self.resource_group_name = resource_group_name
        # The SQL statement.
        self.sqltext = sqltext
        # The ID of the statement.
        self.statement_id = statement_id
        # The source from which the query was initiated.
        # 
        # Valid values:
        # 
        # *   SQL_EDITOR: SQL_EDITOR.
        # *   JDBC: JDBC.
        self.statement_source = statement_source
        # The execution status of the SQL statement.
        # 
        # Valid values:
        # 
        # *   cancel: The task is canceled .
        # *   finished: The execution succeeds .
        # *   error: The execution fails .
        # *   timeout: The execution of the command timed out.
        self.status = status
        # The duration of the SQL statement. Unit: milliseconds.
        self.total_time = total_time
        # The username that is used to execute SQL statements.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.error_trace is not None:
            result['ErrorTrace'] = self.error_trace

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.inner_query_id is not None:
            result['InnerQueryId'] = self.inner_query_id

        if self.is_diagnosable is not None:
            result['IsDiagnosable'] = self.is_diagnosable

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        if self.statement_source is not None:
            result['StatementSource'] = self.statement_source

        if self.status is not None:
            result['Status'] = self.status

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('ErrorTrace') is not None:
            self.error_trace = m.get('ErrorTrace')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('InnerQueryId') is not None:
            self.inner_query_id = m.get('InnerQueryId')

        if m.get('IsDiagnosable') is not None:
            self.is_diagnosable = m.get('IsDiagnosable')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        if m.get('StatementSource') is not None:
            self.statement_source = m.get('StatementSource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

