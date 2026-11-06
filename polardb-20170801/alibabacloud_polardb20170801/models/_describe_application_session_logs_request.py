# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationSessionLogsRequest(DaraModel):
    def __init__(
        self,
        agent: str = None,
        application_id: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        role: str = None,
        session_id: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The agent name. This parameter must be specified together with the SessionId parameter, or neither of them is specified.
        self.agent = agent
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The end time of the query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. The time must be in UTC. The end time cannot be earlier than the start time, and the query time span cannot exceed 30 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Maximum value: 2147483647. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 30 to 100. Default value: 30.
        self.page_size = page_size
        # The region ID of the application.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The role filter for logs. Valid values: user, assistant, and toolResult.
        self.role = role
        # The session ID. This parameter must be specified together with the Agent parameter, or neither of them is specified.
        self.session_id = session_id
        # The start time of the query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. The time must be in UTC. The start time cannot be later than the current time, and the interval between the start time and the current time cannot exceed 31 days.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The log type. This API operation only queries session logs. Set the value to session.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.role is not None:
            result['Role'] = self.role

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            self.agent = m.get('Agent')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

