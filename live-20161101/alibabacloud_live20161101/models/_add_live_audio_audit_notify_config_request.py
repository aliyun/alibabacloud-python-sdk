# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveAudioAuditNotifyConfigRequest(DaraModel):
    def __init__(
        self,
        callback: str = None,
        callback_template: str = None,
        domain_name: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The URL used to receive callbacks for audio that contains problematic content.
        self.callback = callback
        # The callback template for automated reviews. The value is a JSON string that can contain the following variables:
        # 
        # - **{DomainName}**: The streaming domain.
        # 
        # - **{AppName}**: The AppName of the live stream.
        # 
        # - **{StreamName}**: The stream name.
        # 
        # - **{Timestamp}**: The UNIX timestamp of the callback. Unit: seconds.
        # 
        # - **{Result}**: The review result.
        self.callback_template = callback_template
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback is not None:
            result['Callback'] = self.callback

        if self.callback_template is not None:
            result['CallbackTemplate'] = self.callback_template

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('CallbackTemplate') is not None:
            self.callback_template = m.get('CallbackTemplate')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

