# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLivePackageChannelCredentialsRequest(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        group_name: str = None,
        rotate_credentials: int = None,
    ):
        # The channel name.
        # 
        # This parameter is required.
        self.channel_name = channel_name
        # The channel group name.
        # 
        # This parameter is required.
        self.group_name = group_name
        # Specifies whether to update the credentials. 1: updates the credentials of endpoint 1. 2: updates the credentials of endpoint 2. 3: updates the credentials of endpoints 1 and 2.
        # 
        # This parameter is required.
        self.rotate_credentials = rotate_credentials

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.rotate_credentials is not None:
            result['RotateCredentials'] = self.rotate_credentials

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RotateCredentials') is not None:
            self.rotate_credentials = m.get('RotateCredentials')

        return self

