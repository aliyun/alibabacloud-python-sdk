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
        phone_number_list: List[str] = None,
    ):
        self.campaign_id = campaign_id
        self.instance_id = instance_id
        self.phone_number_list = phone_number_list

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

        if self.phone_number_list is not None:
            result['PhoneNumberList'] = self.phone_number_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PhoneNumberList') is not None:
            self.phone_number_list = m.get('PhoneNumberList')

        return self

