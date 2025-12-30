# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UninstallSoftwaresShrinkRequest(DaraModel):
    def __init__(
        self,
        additional_packages_shrink: str = None,
        cluster_id: str = None,
    ):
        # The information about the software systems that you want to uninstall.
        self.additional_packages_shrink = additional_packages_shrink
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_packages_shrink is not None:
            result['AdditionalPackages'] = self.additional_packages_shrink

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalPackages') is not None:
            self.additional_packages_shrink = m.get('AdditionalPackages')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

