# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAtiChangeLogsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        client_token: str = None,
        end_timestamp: int = None,
        operation_type: str = None,
        operator_account: str = None,
        page_number: int = None,
        page_size: int = None,
        start_timestamp: int = None,
        time_range: str = None,
    ):
        # The agent ID assigned by CNNIC after real-name authentication. The AgentID serves as the unique identifier that binds the agent to the real-name authenticated registrant.
        self.agent_id = agent_id
        # Ensures the idempotency of the request. Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters.
        # 
        # - If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The end time of the query (timestamp).
        self.end_timestamp = end_timestamp
        # The operation type of the Operation logs log record, such as modifying an agent.
        self.operation_type = operation_type
        # The UID of the operator.
        self.operator_account = operator_account
        # The current page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page in a paged query. Maximum value: 100. Default value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The start time of the query (timestamp).
        self.start_timestamp = start_timestamp
        # Ignore.
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.operator_account is not None:
            result['OperatorAccount'] = self.operator_account

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OperatorAccount') is not None:
            self.operator_account = m.get('OperatorAccount')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        return self

