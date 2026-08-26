# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveStreamWatermarkRuleRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        description: str = None,
        domain: str = None,
        name: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream: str = None,
        template_id: str = None,
    ):
        # The AppName of the live stream.
        # 
        # This parameter is required.
        self.app = app
        # The description of the custom rule.
        self.description = description
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        # The name of the custom rule.
        # 
        # This parameter is required.
        self.name = name
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The stream name. The following rules apply:
        # 
        # - To match a specific stream, enter the full stream name. For example, liveStreamA.
        # 
        # - You can use a wildcard match. The asterisk (`*`) matches all streams.
        # 
        # - You can perform prefix and suffix matching.
        # 
        # > * You can use only one asterisk (`*`). The asterisk must be at the beginning or end of the string. The matching items must be enclosed in parentheses (`()`) and separated by a vertical bar (`|`).
        # >
        # > * For example, `*(t1|t2)` matches all streams that end with `t1` or `t2`. `(abc|123)*` matches all streams that start with `abc` or `123`.
        # 
        # This parameter is required.
        self.stream = stream
        # The ID of the watermark template.
        # 
        # > Get the template ID from the response of the [AddLiveStreamWatermark](https://help.aliyun.com/document_detail/2848096.html) operation.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

