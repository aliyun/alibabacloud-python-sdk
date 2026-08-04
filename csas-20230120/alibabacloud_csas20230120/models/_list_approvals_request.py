# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApprovalsRequest(DaraModel):
    def __init__(
        self,
        approval_ids: List[str] = None,
        create_end_time: int = None,
        create_start_time: int = None,
        creator_department: str = None,
        creator_dev_tag: str = None,
        creator_user_id: str = None,
        creator_username: str = None,
        current_page: int = None,
        operator_user_id: str = None,
        operator_username: str = None,
        page_size: int = None,
        policy_type: str = None,
        process_id: str = None,
        process_name: str = None,
        schema_id: str = None,
        schema_name: str = None,
        statuses: List[str] = None,
    ):
        # Collection of approval instance IDs.
        self.approval_ids = approval_ids
        # End time when the approval instance was created, in seconds since the Unix epoch.
        self.create_end_time = create_end_time
        # Start time when the approval instance was created, in seconds since the Unix epoch.
        self.create_start_time = create_start_time
        # Department of the user who created the approval instance.
        self.creator_department = creator_department
        # ID of the device used to create the approval instance.
        self.creator_dev_tag = creator_dev_tag
        # ID of the user who created the approval instance.
        self.creator_user_id = creator_user_id
        # Username of the user who created the approval instance.
        self.creator_username = creator_username
        # Page number for the current page in a paged query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # ID of the user who performed an operation on the approval instance.
        self.operator_user_id = operator_user_id
        # Username of the user who performed an operation on the approval instance.
        self.operator_username = operator_username
        # Number of entries per page in a paged query. Valid values: 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Policy type. Valid values:
        # 
        # - **DomainBlacklist**: Domain blacklist.
        # 
        # - **DomainWhitelist**: Domain whitelist.
        # 
        # - **SoftwareBlock**: Software blocking.
        # 
        # - **AppUninstall**: App uninstallation.
        # 
        # - **DlpSend**: File outbound transfer.
        # 
        # - **PeripheralBlock**: Peripheral control.
        self.policy_type = policy_type
        # ID of the associated approval process.
        self.process_id = process_id
        # Name of the associated approval process.
        self.process_name = process_name
        # ID of the associated approval template.
        self.schema_id = schema_id
        # Name of the associated approval template.
        self.schema_name = schema_name
        # Collection of approval instance statuses.
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_ids is not None:
            result['ApprovalIds'] = self.approval_ids

        if self.create_end_time is not None:
            result['CreateEndTime'] = self.create_end_time

        if self.create_start_time is not None:
            result['CreateStartTime'] = self.create_start_time

        if self.creator_department is not None:
            result['CreatorDepartment'] = self.creator_department

        if self.creator_dev_tag is not None:
            result['CreatorDevTag'] = self.creator_dev_tag

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.creator_username is not None:
            result['CreatorUsername'] = self.creator_username

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.operator_user_id is not None:
            result['OperatorUserId'] = self.operator_user_id

        if self.operator_username is not None:
            result['OperatorUsername'] = self.operator_username

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalIds') is not None:
            self.approval_ids = m.get('ApprovalIds')

        if m.get('CreateEndTime') is not None:
            self.create_end_time = m.get('CreateEndTime')

        if m.get('CreateStartTime') is not None:
            self.create_start_time = m.get('CreateStartTime')

        if m.get('CreatorDepartment') is not None:
            self.creator_department = m.get('CreatorDepartment')

        if m.get('CreatorDevTag') is not None:
            self.creator_dev_tag = m.get('CreatorDevTag')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('CreatorUsername') is not None:
            self.creator_username = m.get('CreatorUsername')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('OperatorUserId') is not None:
            self.operator_user_id = m.get('OperatorUserId')

        if m.get('OperatorUsername') is not None:
            self.operator_username = m.get('OperatorUsername')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

