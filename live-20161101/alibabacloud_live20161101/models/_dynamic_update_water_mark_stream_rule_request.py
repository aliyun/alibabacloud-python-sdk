# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DynamicUpdateWaterMarkStreamRuleRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        domain: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream: str = None,
        template_id: str = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.app = app
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the stream that contains the watermark.
        # 
        # This parameter is required.
        self.stream = stream
        # The watermark template ID. You can call the [DescribeLiveStreamWatermarks](https://help.aliyun.com/document_detail/2848102.html) operation to obtain available watermark template IDs.
        # 
        # >  The TemplateId parameter is used to replace the watermark template ID during live streaming.
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

        if self.domain is not None:
            result['Domain'] = self.domain

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

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

