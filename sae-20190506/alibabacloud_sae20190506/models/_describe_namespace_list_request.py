# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNamespaceListRequest(DaraModel):
    def __init__(
        self,
        contain_custom: bool = None,
        hybrid_cloud_exclude: bool = None,
    ):
        # Specifies whether to return custom namespaces. Valid values:
        # 
        # *   **true**: The system returns custom namespaces.
        # *   **false**: The system does not return custom namespaces.
        self.contain_custom = contain_custom
        # Indicates whether hybrid cloud namespaces are excluded. Valid values:
        # 
        # *   **true**: Hybrid cloud namespaces are excluded.
        # *   **false**: Hybrid cloud namespaces are included.
        self.hybrid_cloud_exclude = hybrid_cloud_exclude

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contain_custom is not None:
            result['ContainCustom'] = self.contain_custom

        if self.hybrid_cloud_exclude is not None:
            result['HybridCloudExclude'] = self.hybrid_cloud_exclude

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainCustom') is not None:
            self.contain_custom = m.get('ContainCustom')

        if m.get('HybridCloudExclude') is not None:
            self.hybrid_cloud_exclude = m.get('HybridCloudExclude')

        return self

