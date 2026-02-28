# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyCampaignNumbersRequest(DaraModel):
    def __init__(
        self,
        campaign_id: str = None,
        inst_group_id: str = None,
        instance_id: str = None,
        number_list: List[str] = None,
    ):
        # This parameter is required.
        self.campaign_id = campaign_id
        self.inst_group_id = inst_group_id
        # This parameter is required.
        self.instance_id = instance_id
        self.number_list = number_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.inst_group_id is not None:
            result['InstGroupId'] = self.inst_group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('InstGroupId') is not None:
            self.inst_group_id = m.get('InstGroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        return self

