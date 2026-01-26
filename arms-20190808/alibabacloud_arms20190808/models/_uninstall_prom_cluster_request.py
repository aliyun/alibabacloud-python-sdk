# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UninstallPromClusterRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        cluster_id: str = None,
        region_id: str = None,
    ):
        # Language environment(If left blank, defaults to zh):
        # - zh
        # - en
        self.aliyun_lang = aliyun_lang
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The region ID. Default value: cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

