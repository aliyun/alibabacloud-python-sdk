# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveDomainMultiStreamOptimalModeRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain: str = None,
        optimal_mode: str = None,
        owner_id: int = None,
        stream_name: str = None,
    ):
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        # Specifies whether to enable the auto mode of dual-stream disaster recovery. Valid values:
        # 
        # *   **on**: enables the auto mode.
        # *   **off**: disables the auto mode.
        # 
        # This parameter is required.
        self.optimal_mode = optimal_mode
        self.owner_id = owner_id
        # The name of the live stream.
        # 
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.optimal_mode is not None:
            result['OptimalMode'] = self.optimal_mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OptimalMode') is not None:
            self.optimal_mode = m.get('OptimalMode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

