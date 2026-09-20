# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class QueryXpackRelateDBResponseBody(DaraModel):
    def __init__(
        self,
        cluster_list: main_models.QueryXpackRelateDBResponseBodyClusterList = None,
        request_id: str = None,
    ):
        self.cluster_list = cluster_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_list:
            self.cluster_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_list is not None:
            result['ClusterList'] = self.cluster_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterList') is not None:
            temp_model = main_models.QueryXpackRelateDBResponseBodyClusterList()
            self.cluster_list = temp_model.from_map(m.get('ClusterList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryXpackRelateDBResponseBodyClusterList(DaraModel):
    def __init__(
        self,
        cluster: List[main_models.QueryXpackRelateDBResponseBodyClusterListCluster] = None,
    ):
        self.cluster = cluster

    def validate(self):
        if self.cluster:
            for v1 in self.cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cluster'] = []
        if self.cluster is not None:
            for k1 in self.cluster:
                result['Cluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k1 in m.get('Cluster'):
                temp_model = main_models.QueryXpackRelateDBResponseBodyClusterListCluster()
                self.cluster.append(temp_model.from_map(k1))

        return self

class QueryXpackRelateDBResponseBodyClusterListCluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        dbtype: str = None,
        dbversion: str = None,
        is_related: bool = None,
        lock_mode: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.is_related = is_related
        self.lock_mode = lock_mode
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.is_related is not None:
            result['IsRelated'] = self.is_related

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('IsRelated') is not None:
            self.is_related = m.get('IsRelated')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

