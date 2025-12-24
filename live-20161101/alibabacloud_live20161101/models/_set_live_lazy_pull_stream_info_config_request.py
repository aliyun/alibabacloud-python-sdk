# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveLazyPullStreamInfoConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        owner_id: int = None,
        pull_app_name: str = None,
        pull_domain_name: str = None,
        pull_protocol: str = None,
        region_id: str = None,
        transcode_lazy: str = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # >  If you want to configure triggered stream pulling for all applications, set the value to **ali_all_app**.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The name of the application for back-to-origin stream pulling.
        # 
        # >  If you want to use the application specified in the streaming URL, leave this parameter empty.
        self.pull_app_name = pull_app_name
        # The origin server address of the live stream. Separate multiple addresses with semicolons (;).
        # 
        # This parameter is required.
        self.pull_domain_name = pull_domain_name
        # The protocol for back-to-origin stream pulling. Valid values:
        # 
        # *   **rtmp**
        # *   **httpflv**
        # *   **hls**
        # 
        # This parameter is required.
        self.pull_protocol = pull_protocol
        self.region_id = region_id
        # Specifies whether to trigger stream pulling when the transcoded stream is played. The default value is **no**. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.transcode_lazy = transcode_lazy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pull_app_name is not None:
            result['PullAppName'] = self.pull_app_name

        if self.pull_domain_name is not None:
            result['PullDomainName'] = self.pull_domain_name

        if self.pull_protocol is not None:
            result['PullProtocol'] = self.pull_protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.transcode_lazy is not None:
            result['TranscodeLazy'] = self.transcode_lazy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PullAppName') is not None:
            self.pull_app_name = m.get('PullAppName')

        if m.get('PullDomainName') is not None:
            self.pull_domain_name = m.get('PullDomainName')

        if m.get('PullProtocol') is not None:
            self.pull_protocol = m.get('PullProtocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TranscodeLazy') is not None:
            self.transcode_lazy = m.get('TranscodeLazy')

        return self

