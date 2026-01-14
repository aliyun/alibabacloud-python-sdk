# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAuditLogRequest(DaraModel):
    def __init__(
        self,
        access_source_flag: str = None,
        end_date: str = None,
        log_type: str = None,
        operator_id: str = None,
        operator_types: str = None,
        resource_type: str = None,
        start_date: str = None,
        user_access_device: str = None,
        workspace_id: str = None,
    ):
        self.access_source_flag = access_source_flag
        # End date of the query, format ("yyyyMMdd").
        # 
        # This parameter is required.
        self.end_date = end_date
        # Log type:
        # - dataView - Access
        # - function - Operation
        # - permission - Permission
        # 
        # This parameter is required.
        self.log_type = log_type
        # Operator\\"s user ID.
        self.operator_id = operator_id
        # Permission/Access/Operation type, empty - default all;
        # 
        # Refer to the audit log code values, send multiple values separated by English commas.
        self.operator_types = operator_types
        # Resource type, refer to the work type.
        self.resource_type = resource_type
        # Start date of the query, format ("yyyyMMdd"), cannot be earlier than 90 days from the current time.
        # 
        # This parameter is required.
        self.start_date = start_date
        self.user_access_device = user_access_device
        # Workspace ID, the ID of the workspace to which the logs to be queried belong.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_source_flag is not None:
            result['AccessSourceFlag'] = self.access_source_flag

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.operator_types is not None:
            result['OperatorTypes'] = self.operator_types

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.user_access_device is not None:
            result['UserAccessDevice'] = self.user_access_device

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessSourceFlag') is not None:
            self.access_source_flag = m.get('AccessSourceFlag')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('OperatorTypes') is not None:
            self.operator_types = m.get('OperatorTypes')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('UserAccessDevice') is not None:
            self.user_access_device = m.get('UserAccessDevice')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

