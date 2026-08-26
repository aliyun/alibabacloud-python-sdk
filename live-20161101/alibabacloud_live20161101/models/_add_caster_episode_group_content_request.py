# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCasterEpisodeGroupContentRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # A client-generated token that is used to ensure the idempotence of the request.
        # 
        # > The client generates this value. Make sure that the value is unique among different requests. The value can be up to 64 ASCII characters in length.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The properties of the episode in the production studio. This parameter is a JSON string. The parameter names are in upper camel case. The properties are described as follows:
        # 
        # - **CallbackUrl**: The webhook address.
        # 
        # - **SideOutputUrl**: The custom bypass output URL.
        # 
        # - **RepeatNum**: The number of times to loop the episode. A value of 0 means the episode does not loop. A value of -1 means the episode loops indefinitely.
        # 
        # - **StartTime**: The start time in UTC. The format is *yyyy-MM-dd*T*HH:mm:ss*Z.
        # 
        # - **DomainName**: The domain name.
        # 
        # - **Items**
        # 
        #   : The list of items in the episode.
        # 
        #   - **ItemName**: The item name.
        # 
        #   - **VodUrl**: The URL of the video-on-demand (VOD) file. This parameter is required only when the resource is a video file that has not been imported to the Material Library. The MP4, FLV, and TS formats are supported.
        # 
        # This parameter is required.
        self.content = content
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content is not None:
            result['Content'] = self.content

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

