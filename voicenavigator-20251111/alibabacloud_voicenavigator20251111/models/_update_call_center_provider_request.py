# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCallCenterProviderRequest(DaraModel):
    def __init__(
        self,
        destination: str = None,
        display_name: str = None,
        extras: str = None,
        instance_id: str = None,
        name: str = None,
        originator: str = None,
        provider_id: str = None,
        provider_type: str = None,
        refer_to: str = None,
        trunk_id: str = None,
    ):
        self.destination = destination
        self.display_name = display_name
        self.extras = extras
        self.instance_id = instance_id
        self.name = name
        self.originator = originator
        self.provider_id = provider_id
        self.provider_type = provider_type
        self.refer_to = refer_to
        self.trunk_id = trunk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination is not None:
            result['Destination'] = self.destination

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.extras is not None:
            result['Extras'] = self.extras

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.originator is not None:
            result['Originator'] = self.originator

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        if self.refer_to is not None:
            result['ReferTo'] = self.refer_to

        if self.trunk_id is not None:
            result['TrunkId'] = self.trunk_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Extras') is not None:
            self.extras = m.get('Extras')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Originator') is not None:
            self.originator = m.get('Originator')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('ReferTo') is not None:
            self.refer_to = m.get('ReferTo')

        if m.get('TrunkId') is not None:
            self.trunk_id = m.get('TrunkId')

        return self

