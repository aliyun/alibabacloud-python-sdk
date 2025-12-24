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
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The information about the episode list. The value is a JSON string. Use upper camel case for fields of the string. This parameter contains the following fields:
        # 
        # *   **CallbackUrl**: the callback URL.
        # 
        # *   **SideOutputUrl**: the custom standby URL.
        # 
        # *   **RepeatNum**: the number of times the episode list repeats after the first playback is complete. A value of 0 indicates that the episode list is played only once. A value of -1 indicates that the episode list is played in loop mode.
        # 
        # *   **DomainName**: the domain name.
        # 
        # *   **StartTime**: the time when the episode list starts to play. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # *   **Items**: the information about the episode list. It is an array of ItemName and VodUrl.
        # 
        #     *   **ItemName**: the name of the episode.
        #     *   **VodUrl**: the URL of the VOD file. This field takes effect only when the video resource is a video file that is not from the media library. The video file must be in the MP4, FLV, or TS format.
        # 
        # This parameter is required.
        self.content = content
        self.owner_id = owner_id
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

