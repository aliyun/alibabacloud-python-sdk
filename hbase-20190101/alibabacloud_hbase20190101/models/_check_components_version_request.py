# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckComponentsVersionRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        components: str = None,
    ):
        # The cluster ID. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to obtain the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The component to check. Valid values:
        # 
        # - **HBASE**
        # - **HADOOP**
        # - **PHOENIX**
        # - **SOLR**
        # - **THRIFT**.
        # 
        # This parameter is required.
        self.components = components

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.components is not None:
            result['Components'] = self.components

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Components') is not None:
            self.components = m.get('Components')

        return self

