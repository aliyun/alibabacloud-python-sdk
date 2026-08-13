# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AbortCasesRequest(DaraModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
        phone_numbers: List[str] = None,
    ):
        # The ID of the predictive outbound call campaign.
        # 
        # This parameter is required.
        self.campaign_id = campaign_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of contact phone numbers to cancel.
        self.phone_numbers = phone_numbers

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

        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')

        return self

