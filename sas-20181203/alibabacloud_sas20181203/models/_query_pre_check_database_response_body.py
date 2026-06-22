# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPreCheckDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        completed_time: int = None,
        created_time: int = None,
        description: str = None,
        progress: int = None,
        request_id: str = None,
        result: str = None,
        updated_time: int = None,
    ):
        # The time when the pre-check was completed.
        self.completed_time = completed_time
        # The time when the pre-check started.
        self.created_time = created_time
        # The status description of the pre-check task. Valid values:
        # 
        # - **completed**: Completed.
        # - **created**: Started.
        # - **error**: Pre-check failed.
        self.description = description
        # The pre-check progress. Valid values: 0 to 100.
        self.progress = progress
        # The request ID. Alibaba Cloud generates a unique identifier for each API request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The task result of the dry run node. The value is a JSON string. The KEY valid values are:
        # 
        # - **instanceId**: the instance ID of the server where the database resides.
        # - **checkTime**: the dry run time.
        # - **sourceType**: the database type.
        # - **results**: the dry run items and task results.
        #     - **item**: the dry run item.
        #     - **result**: the dry run task result.
        # 
        # > Dry run item description
        # > - MSSQL
        # >     - **OSS_INTERNAL_ENDPOINT_CONNECTIVITY**: OSS connectivity check.	
        # >     - **SERVICE_CONNECTIVITY**: control network connectivity check.
        # >     - **SQL_SERVER_DB_IN_SIMPLE_RECOVERY_MODE**: recovery mode check.
        # >     - **SQL_SERVER_DB_NOT_ONLINE**: SQL Server database status check.
        # > - ORACLE
        # >     - **OSS_INTERNAL_ENDPOINT_CONNECTIVITY**: OSS connectivity check.	
        # >     - **SERVICE_CONNECTIVITY**: control network connectivity check.
        # >     - **ORACLE_INSTANCE_STATUS**: Oracle instance status check.
        # >     - **ORACLE_DB_STATUS**: Oracle database status check.
        # >     - **ARCHIVELOG**: archive mode check.
        # > - MYSQL
        # >     - **OSS_INTERNAL_ENDPOINT_CONNECTIVITY**: OSS connectivity check.	
        # >     - **SERVICE_CONNECTIVITY**: control network connectivity check.
        # >     - **MYSQL_VERSION**: version check for full backup support.
        # >     - **MYSQL_BINLOG**: BINLOG check.
        self.result = result
        # The time when the pre-check was last updated.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

