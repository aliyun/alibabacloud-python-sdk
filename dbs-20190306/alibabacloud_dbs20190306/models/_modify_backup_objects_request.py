# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupObjectsRequest(DaraModel):
    def __init__(
        self,
        backup_objects: str = None,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The backup objects, specified as a JSON string. The structure is as follows:
        # 
        # ```
        # [
        #     {
        #         "DBName":"The name of the database to back up",
        #         "SchemaName":"The name of the schema to back up",
        #         "TableIncludes":[{
        #         	"TableName":"The name of the table to back up"
        #         }],
        #         "TableExcludes":[{
        #             "TableName":"The name of a table in the database that you do not want to back up"
        #         }]
        #     }
        # ]
        # ```
        # 
        # - If you specify only `DBName` without configuring rules for sub-objects, all objects in the database are backed up.
        # 
        # - If you specify `DBName` and configure rules for some objects, any objects without configured rules are not backed up by default. The following regular expressions are supported for defining object names:
        # 
        #   - A period (`.`) matches any single character except `
        # `.
        # 
        #   - An asterisk (`*`) matches the preceding subexpression zero or more times. For example, `h*llo` matches `hllo` and `heeeello`.
        # 
        #   - A question mark (`?`) matches the preceding subexpression zero or one time. For example, `h.?llo` matches `hllo` and `hello`, but not `haello`.
        # 
        #   - A character set `[characters]` matches any single character within the brackets. For example, `h[aello]` matches `hallo` and `hello`.
        # 
        #   - A negated character set `[^characters]` matches any single character not within the brackets. For example, `h[^ae]llo` matches `hcllo` and `hdllo`, but not `hallo` or `hello`.
        # 
        #   - A character range `[character1-character2]` matches any character within the specified range, such as `[0-9]` or `[a-z]`.
        # 
        # > `SchemaName` and `NewSchemaName` are used only for SQL Server. For other database engines, use `DBName` and `NewDBName` to specify database names.
        # 
        # This parameter is required.
        self.backup_objects = backup_objects
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # A client token to ensure the request is idempotent. This prevents the same request from being submitted multiple times.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

