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
        effect_statuses: List[str] = None,
        operator_user_id: str = None,
        operator_username: str = None,
        page_size: int = None,
        policy_type: str = None,
        process_id: str = None,
        process_name: str = None,
        report_types: List[str] = None,
        schema_id: str = None,
        schema_name: str = None,
        statuses: List[str] = None,
    ):
        # The collection of approval instance IDs.
        self.approval_ids = approval_ids
        # The end time for approval instance creation, in seconds-level timestamp.
        self.create_end_time = create_end_time
        # The start time for approval instance creation, in seconds-level timestamp.
        self.create_start_time = create_start_time
        # The department of the approval instance creator.
        self.creator_department = creator_department
        # The terminal device ID of the approval instance creator.
        self.creator_dev_tag = creator_dev_tag
        # The ID of the approval instance creator.
        self.creator_user_id = creator_user_id
        # The username of the approval instance creator.
        self.creator_username = creator_username
        # The page number of the current page in a paging query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The list of report effective statuses. Valid values: Enabled, Expired.
        self.effect_statuses = effect_statuses
        # The ID of the approval instance operator.
        self.operator_user_id = operator_user_id
        # The username of the approval instance operator.
        self.operator_username = operator_username
        # The number of entries per page in a paging query. Valid values: 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The adaptation policy type. Valid values:
        self.policy_type = policy_type
        # The associated approval process ID.
        self.process_id = process_id
        # The associated approval process name.
        self.process_name = process_name
        # The list of report types. If not specified, only ApprovalReport is queried.
        self.report_types = report_types
        # The associated approval template ID.
        self.schema_id = schema_id
        # The associated approval template name.
        self.schema_name = schema_name
        # The collection of approval instance statuses.
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

        if self.effect_statuses is not None:
            result['EffectStatuses'] = self.effect_statuses

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

        if self.report_types is not None:
            result['ReportTypes'] = self.report_types

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

        if m.get('EffectStatuses') is not None:
            self.effect_statuses = m.get('EffectStatuses')

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

        if m.get('ReportTypes') is not None:
            self.report_types = m.get('ReportTypes')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

