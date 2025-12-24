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
        # The name of the application to which the live stream belongs.
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
        self.region_id = region_id
        # The name of the live stream. The following rules apply:
        # 
        # *   A stream name can be exactly matched. Example: liveStreamA.
        # *   Fuzzy match is also supported. The use of an asterisk (`*`) allows all approximate matches to be found.
        # *   You can place the asterisk before or after an approximate string.
        # 
        # 
        # 
        # >*   Fuzzy match: Only one asterisk (`*`) before or after an approximate string is allowed. The approximate string must be enclosed in `()`. Separate multiple strings with vertical bars (`|`).
        # >*   For example, `*(t1|t2)` matches all streams whose name has the `t1` or `t2` suffix, and `(abc|123)*` matches all streams whose name has the `abc` or `123` prefix.
        # 
        # This parameter is required.
        self.stream = stream
        # The ID of the watermark template.
        # 
        # >  You can obtain the template ID by checking the value of the TemplateId parameter that is returned by the [AddLiveStreamWatermark](https://help.aliyun.com/document_detail/410759.html) operation.
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

