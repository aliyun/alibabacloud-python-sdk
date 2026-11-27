# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAutoLiveStreamRuleRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        call_back: str = None,
        channel_id_prefixes: List[str] = None,
        channel_ids: List[str] = None,
        media_encode: int = None,
        owner_id: int = None,
        play_domain: str = None,
        rule_name: str = None,
    ):
        # The application ID, which can be created and queried in the console.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The callback URL used to notify the start and end of the relay. For details about the callback content, see the CallBack callback example below.
        self.call_back = call_back
        # The list of channel ID prefixes that are fuzzy matched.
        self.channel_id_prefixes = channel_id_prefixes
        # The list of channel IDs that are exactly matched.
        self.channel_ids = channel_ids
        # The encoding option. For more information, see the MediaEncode enumeration values below.
        self.media_encode = media_encode
        self.owner_id = owner_id
        # The streaming domain name for automatic relay. The streaming URL of an automatic relay task is in the format rtmp://${domain}/${app}/${stream}.
        # 
        # - domain: your live streaming domain name.
        # - app: live.
        # - stream: urlencode(${AppId}_${ChannelId}_${UserId}_${SourceType}), where SourceType indicates the type of the input source.
        # 
        # This parameter is required.
        self.play_domain = play_domain
        # The name of the relay rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.call_back is not None:
            result['CallBack'] = self.call_back

        if self.channel_id_prefixes is not None:
            result['ChannelIdPrefixes'] = self.channel_id_prefixes

        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')

        if m.get('ChannelIdPrefixes') is not None:
            self.channel_id_prefixes = m.get('ChannelIdPrefixes')

        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

