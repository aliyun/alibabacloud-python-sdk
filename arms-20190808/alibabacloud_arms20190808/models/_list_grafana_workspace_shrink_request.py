# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGrafanaWorkspaceShrinkRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
    ):
        # The language. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # The region ID. Default value: cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Prometheus instance belongs.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

