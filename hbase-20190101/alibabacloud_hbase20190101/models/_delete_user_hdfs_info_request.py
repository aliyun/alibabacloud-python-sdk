# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserHdfsInfoRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        name_service: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The value of dfs.nameservices in addUserHdfsInfo. This value is returned when you call the [QueryXpackRelateDB](https://help.aliyun.com/document_detail/144509.html) operation with relateDB set to hdfs.
        # 
        # This parameter is required.
        self.name_service = name_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.name_service is not None:
            result['NameService'] = self.name_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NameService') is not None:
            self.name_service = m.get('NameService')

        return self

