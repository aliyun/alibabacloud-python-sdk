# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PutContactGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_name: str = None,
        contact_names: List[str] = None,
        describe: str = None,
        dry_run: bool = None,
        enable_subscribed: bool = None,
    ):
        # The name of the alert contact group.
        # 
        # This parameter is required.
        self.contact_group_name = contact_group_name
        # The names of the alert contacts.
        self.contact_names = contact_names
        # The description of the alert contact group.
        self.describe = describe
        # Specifies whether to perform a dry run on the request.
        self.dry_run = dry_run
        # Specifies whether to enable the subscription feature. Valid values:
        # 
        # - true: Yes.
        # 
        # - false: No.
        self.enable_subscribed = enable_subscribed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.contact_names is not None:
            result['ContactNames'] = self.contact_names

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_subscribed is not None:
            result['EnableSubscribed'] = self.enable_subscribed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('ContactNames') is not None:
            self.contact_names = m.get('ContactNames')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableSubscribed') is not None:
            self.enable_subscribed = m.get('EnableSubscribed')

        return self

