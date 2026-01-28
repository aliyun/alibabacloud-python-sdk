# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPlaybooksRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_field: str = None,
        page_number: int = None,
        page_size: int = None,
        playbook_execution_end_time: int = None,
        playbook_execution_start_time: int = None,
        playbook_name: str = None,
        playbook_param_types: List[str] = None,
        playbook_status: int = None,
        playbook_type: str = None,
        playbook_uuids: List[str] = None,
        role_for: int = None,
    ):
        # Language type for request and response messages.
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # Maximum number of results returned in a single request. Range: 1~100.
        self.max_results = max_results
        # Token for the next query start.
        self.next_token = next_token
        # Sorting logic, default is **desc**, with values as follows:
        # - **desc**: Descending order.
        # - **asc**: Ascending order.
        self.order = order
        # Sorting field. Values:
        # 
        # - **UpdateTime**: Sort by update time.
        # - **ExecutionTime**: Sort by the latest execution time.
        self.order_field = order_field
        # Page number for pagination, default value is 1.
        self.page_number = page_number
        # Number of items per page for pagination. Range: 1~100.
        self.page_size = page_size
        # End time of the latest execution of the playbook.
        self.playbook_execution_end_time = playbook_execution_end_time
        # Start time of the latest execution of the playbook.
        self.playbook_execution_start_time = playbook_execution_start_time
        # Name of the playbook, supports fuzzy search.
        self.playbook_name = playbook_name
        # Collection of input parameter types for the playbook.
        self.playbook_param_types = playbook_param_types
        # Publication status of the playbook, with values as follows:
        # 
        # - **0**: Unpublished.
        # - **1**: Published.
        self.playbook_status = playbook_status
        # Type of the playbook, with values as follows:
        # 
        # - **preset**: Predefined playbook.
        # - **user**: Custom playbook.
        # - **component**: Security response component.
        self.playbook_type = playbook_type
        # Collection of UUIDs of playbooks.
        self.playbook_uuids = playbook_uuids
        # User ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.playbook_execution_end_time is not None:
            result['PlaybookExecutionEndTime'] = self.playbook_execution_end_time

        if self.playbook_execution_start_time is not None:
            result['PlaybookExecutionStartTime'] = self.playbook_execution_start_time

        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name

        if self.playbook_param_types is not None:
            result['PlaybookParamTypes'] = self.playbook_param_types

        if self.playbook_status is not None:
            result['PlaybookStatus'] = self.playbook_status

        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type

        if self.playbook_uuids is not None:
            result['PlaybookUuids'] = self.playbook_uuids

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlaybookExecutionEndTime') is not None:
            self.playbook_execution_end_time = m.get('PlaybookExecutionEndTime')

        if m.get('PlaybookExecutionStartTime') is not None:
            self.playbook_execution_start_time = m.get('PlaybookExecutionStartTime')

        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')

        if m.get('PlaybookParamTypes') is not None:
            self.playbook_param_types = m.get('PlaybookParamTypes')

        if m.get('PlaybookStatus') is not None:
            self.playbook_status = m.get('PlaybookStatus')

        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')

        if m.get('PlaybookUuids') is not None:
            self.playbook_uuids = m.get('PlaybookUuids')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

