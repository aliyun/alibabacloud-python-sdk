# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class ListClusterTypeResponseBody(DaraModel):
    def __init__(
        self,
        cluster_type_detail_list: List[main_models.ListClusterTypeResponseBodyClusterTypeDetailList] = None,
        cluster_type_list: List[str] = None,
        request_id: str = None,
    ):
        self.cluster_type_detail_list = cluster_type_detail_list
        self.cluster_type_list = cluster_type_list
        self.request_id = request_id

    def validate(self):
        if self.cluster_type_detail_list:
            for v1 in self.cluster_type_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterTypeDetailList'] = []
        if self.cluster_type_detail_list is not None:
            for k1 in self.cluster_type_detail_list:
                result['ClusterTypeDetailList'].append(k1.to_map() if k1 else None)

        if self.cluster_type_list is not None:
            result['ClusterTypeList'] = self.cluster_type_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_type_detail_list = []
        if m.get('ClusterTypeDetailList') is not None:
            for k1 in m.get('ClusterTypeDetailList'):
                temp_model = main_models.ListClusterTypeResponseBodyClusterTypeDetailList()
                self.cluster_type_detail_list.append(temp_model.from_map(k1))

        if m.get('ClusterTypeList') is not None:
            self.cluster_type_list = m.get('ClusterTypeList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterTypeResponseBodyClusterTypeDetailList(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        is_multi_az: bool = None,
    ):
        self.cluster_type = cluster_type
        self.is_multi_az = is_multi_az

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.is_multi_az is not None:
            result['IsMultiAZ'] = self.is_multi_az

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('IsMultiAZ') is not None:
            self.is_multi_az = m.get('IsMultiAZ')

        return self

