# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsAppKeysResponseBody(DaraModel):
    def __init__(
        self,
        app_keys: List[main_models.DescribePdnsAppKeysResponseBodyAppKeys] = None,
        request_id: str = None,
    ):
        self.app_keys = app_keys
        self.request_id = request_id

    def validate(self):
        if self.app_keys:
            for v1 in self.app_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppKeys'] = []
        if self.app_keys is not None:
            for k1 in self.app_keys:
                result['AppKeys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_keys = []
        if m.get('AppKeys') is not None:
            for k1 in m.get('AppKeys'):
                temp_model = main_models.DescribePdnsAppKeysResponseBodyAppKeys()
                self.app_keys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePdnsAppKeysResponseBodyAppKeys(DaraModel):
    def __init__(
        self,
        app_key_id: str = None,
        bind_edge_dns_clusters: List[main_models.DescribePdnsAppKeysResponseBodyAppKeysBindEdgeDnsClusters] = None,
        create_date: str = None,
        create_timestamp: int = None,
        remark: str = None,
        state: str = None,
    ):
        self.app_key_id = app_key_id
        self.bind_edge_dns_clusters = bind_edge_dns_clusters
        self.create_date = create_date
        self.create_timestamp = create_timestamp
        self.remark = remark
        self.state = state

    def validate(self):
        if self.bind_edge_dns_clusters:
            for v1 in self.bind_edge_dns_clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key_id is not None:
            result['AppKeyId'] = self.app_key_id

        result['BindEdgeDnsClusters'] = []
        if self.bind_edge_dns_clusters is not None:
            for k1 in self.bind_edge_dns_clusters:
                result['BindEdgeDnsClusters'].append(k1.to_map() if k1 else None)

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKeyId') is not None:
            self.app_key_id = m.get('AppKeyId')

        self.bind_edge_dns_clusters = []
        if m.get('BindEdgeDnsClusters') is not None:
            for k1 in m.get('BindEdgeDnsClusters'):
                temp_model = main_models.DescribePdnsAppKeysResponseBodyAppKeysBindEdgeDnsClusters()
                self.bind_edge_dns_clusters.append(temp_model.from_map(k1))

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribePdnsAppKeysResponseBodyAppKeysBindEdgeDnsClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_user_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_user_id = cluster_user_id

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

        if self.cluster_user_id is not None:
            result['ClusterUserId'] = self.cluster_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterUserId') is not None:
            self.cluster_user_id = m.get('ClusterUserId')

        return self

