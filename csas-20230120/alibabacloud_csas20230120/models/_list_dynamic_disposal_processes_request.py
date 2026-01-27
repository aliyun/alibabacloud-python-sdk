# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDynamicDisposalProcessesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dev_tag: str = None,
        disposal_action: str = None,
        disposal_process_id: str = None,
        end_time: int = None,
        page_size: int = None,
        recovery_type: str = None,
        start_time: int = None,
        status: str = None,
        user_name: str = None,
    ):
        # The page number to display in the paginated query. Range: 1~10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Terminal device ID.
        self.dev_tag = dev_tag
        # Disposal action.
        # - **ztna_connect**: Prohibit connection to the zero-trust intranet.
        # - **nac_connect**: Prohibit connection to the office network access.
        # - **none**: No disposal action.
        self.disposal_action = disposal_action
        # Disposal process ID.
        self.disposal_process_id = disposal_process_id
        # The end time for querying dynamic disposal processes. Format: Unix timestamp (in seconds).
        self.end_time = end_time
        # The number of items per page in the paginated query. Range: 1~1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Recovery type.
        # - **auto**: Automatic recovery.
        # - **console**: Console recovery.
        # - **auth**: Recovery by authentication and reporting.
        self.recovery_type = recovery_type
        # The start time for querying dynamic disposal processes. Format: Unix timestamp (in seconds).
        self.start_time = start_time
        # Disposal status. Values:
        # - **disposal**: In the disposal state.
        # - **finished**: Already automatically recovered.
        # - **recovery**: Recovered by authentication and reporting or console recovery.
        self.status = status
        # Username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.disposal_action is not None:
            result['DisposalAction'] = self.disposal_action

        if self.disposal_process_id is not None:
            result['DisposalProcessId'] = self.disposal_process_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.recovery_type is not None:
            result['RecoveryType'] = self.recovery_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DisposalAction') is not None:
            self.disposal_action = m.get('DisposalAction')

        if m.get('DisposalProcessId') is not None:
            self.disposal_process_id = m.get('DisposalProcessId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecoveryType') is not None:
            self.recovery_type = m.get('RecoveryType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

