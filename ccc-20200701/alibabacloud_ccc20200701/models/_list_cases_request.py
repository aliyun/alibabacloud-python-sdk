# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCasesRequest(DaraModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        phone_number: str = None,
        state: str = None,
    ):
        # Predictive outbound dialing activity ID.
        # 
        # This parameter is required.
        self.campaign_id = campaign_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The paging ordinal number, ranging from 1 to 100.
        # 
        # This parameter is required.
        self.page_number = page_number
        # Page size, ranging from 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Filters by phone number. Fuzzy Matching is not supported. This parameter is not Required and defaults to empty.
        self.phone_number = phone_number
        # Pending (to be dialed)<br>
        # Executing (dialing in progress)<br>
        # Connected (contact succeeded)<br>
        # Failed (contact failed)<br>
        # Aborted (call stopped or canceled)<br>
        # Forbidden (call prohibited by rule, such as blacklist)
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

