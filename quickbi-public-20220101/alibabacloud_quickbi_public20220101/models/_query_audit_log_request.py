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
        # The access source. Valid values:
        # 
        # - COMMON: standard access
        # 
        # - IMBEDDED: embedded report
        # 
        # - PUBLIC: public report
        # 
        # - IMBEDDED_COMPONENT: embedded card
        self.access_source_flag = access_source_flag
        # The end date for the query. Use the yyyyMMdd format.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The log type. Valid values:
        # 
        # - dataView: access logs
        # 
        # - function: operation logs
        # 
        # - permission: permission logs
        # 
        # This parameter is required.
        self.log_type = log_type
        # The user ID of the operator.
        self.operator_id = operator_id
        # The permission, access, or operation type. If left empty, all types are queried by default.
        # 
        # For valid values, see audit log codes. To specify multiple types, separate them with commas.
        self.operator_types = operator_types
        # The resource type. For more information, see work types.
        self.resource_type = resource_type
        # The start date for the query. Use the yyyyMMdd format. The date cannot be more than 90 days before the current date.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The device used for access. Valid values:
        # 
        # - MOBILE: mobile device
        # 
        # - PC: PC
        self.user_access_device = user_access_device
        # The ID of the workspace that contains the logs to query.
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

