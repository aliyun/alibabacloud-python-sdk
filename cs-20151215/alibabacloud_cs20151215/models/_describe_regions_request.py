# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_type: str = None,
        profile: str = None,
    ):
        # Filters the results by language (Chinese or English).
        self.accept_language = accept_language
        # The cluster type.
        self.cluster_type = cluster_type
        # The subtype of managed clusters.
        self.profile = profile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language

        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type

        if self.profile is not None:
            result['profile'] = self.profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')

        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')

        if m.get('profile') is not None:
            self.profile = m.get('profile')

        return self

