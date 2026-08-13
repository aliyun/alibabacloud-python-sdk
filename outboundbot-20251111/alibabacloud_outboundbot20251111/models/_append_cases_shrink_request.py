# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppendCasesShrinkRequest(DaraModel):
    def __init__(
        self,
        campaign_id: str = None,
        cases_shrink: str = None,
        instance_id: str = None,
    ):
        # The outbound call task ID.
        # 
        # This parameter is required.
        self.campaign_id = campaign_id
        # The list of contacts.
        # 
        # This parameter is required.
        self.cases_shrink = cases_shrink
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.cases_shrink is not None:
            result['Cases'] = self.cases_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('Cases') is not None:
            self.cases_shrink = m.get('Cases')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

