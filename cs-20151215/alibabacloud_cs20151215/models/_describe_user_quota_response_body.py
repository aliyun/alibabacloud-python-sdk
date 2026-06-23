# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeUserQuotaResponseBody(DaraModel):
    def __init__(
        self,
        amk_cluster_quota: int = None,
        ask_cluster_quota: int = None,
        cluster_nodepool_quota: int = None,
        cluster_quota: int = None,
        edge_improved_nodepool_quota: main_models.DescribeUserQuotaResponseBodyEdgeImprovedNodepoolQuota = None,
        node_quota: int = None,
        quotas: Dict[str, main_models.QuotasValue] = None,
    ):
        # The quota for managed clusters. Default value: 20. To request a quota increase beyond the default value, [submit a request on the Quota Center page](https://quotas.console.aliyun.com/products/csk/quotas).
        self.amk_cluster_quota = amk_cluster_quota
        # The quota for ASK clusters. Default value: 20. To request a quota increase beyond the default value, [submit a request on the Quota Center page](https://quotas.console.aliyun.com/products/csk/quotas).
        self.ask_cluster_quota = ask_cluster_quota
        # The node pool quota per cluster. Default value: 20. To request a quota increase beyond the default value, [submit a request on the Quota Center page](https://quotas.console.aliyun.com/products/csk/quotas).
        self.cluster_nodepool_quota = cluster_nodepool_quota
        # The total cluster quota per account. Default value: 50. To request a quota increase beyond the default value, [submit a request on the Quota Center page](https://quotas.console.aliyun.com/products/csk/quotas).
        self.cluster_quota = cluster_quota
        self.edge_improved_nodepool_quota = edge_improved_nodepool_quota
        # The node quota per cluster. Default value: 100. To request a quota increase beyond the default value, [submit a request on the Quota Center page](https://quotas.console.aliyun.com/products/csk/quotas).
        self.node_quota = node_quota
        # The new quota items. If this field is returned, the values in this field take precedence.
        self.quotas = quotas

    def validate(self):
        if self.edge_improved_nodepool_quota:
            self.edge_improved_nodepool_quota.validate()
        if self.quotas:
            for v1 in self.quotas.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amk_cluster_quota is not None:
            result['amk_cluster_quota'] = self.amk_cluster_quota

        if self.ask_cluster_quota is not None:
            result['ask_cluster_quota'] = self.ask_cluster_quota

        if self.cluster_nodepool_quota is not None:
            result['cluster_nodepool_quota'] = self.cluster_nodepool_quota

        if self.cluster_quota is not None:
            result['cluster_quota'] = self.cluster_quota

        if self.edge_improved_nodepool_quota is not None:
            result['edge_improved_nodepool_quota'] = self.edge_improved_nodepool_quota.to_map()

        if self.node_quota is not None:
            result['node_quota'] = self.node_quota

        result['quotas'] = {}
        if self.quotas is not None:
            for k1, v1 in self.quotas.items():
                result['quotas'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amk_cluster_quota') is not None:
            self.amk_cluster_quota = m.get('amk_cluster_quota')

        if m.get('ask_cluster_quota') is not None:
            self.ask_cluster_quota = m.get('ask_cluster_quota')

        if m.get('cluster_nodepool_quota') is not None:
            self.cluster_nodepool_quota = m.get('cluster_nodepool_quota')

        if m.get('cluster_quota') is not None:
            self.cluster_quota = m.get('cluster_quota')

        if m.get('edge_improved_nodepool_quota') is not None:
            temp_model = main_models.DescribeUserQuotaResponseBodyEdgeImprovedNodepoolQuota()
            self.edge_improved_nodepool_quota = temp_model.from_map(m.get('edge_improved_nodepool_quota'))

        if m.get('node_quota') is not None:
            self.node_quota = m.get('node_quota')

        self.quotas = {}
        if m.get('quotas') is not None:
            for k1, v1 in m.get('quotas').items():
                temp_model = main_models.QuotasValue()
                self.quotas[k1] = temp_model.from_map(v1)

        return self

class DescribeUserQuotaResponseBodyEdgeImprovedNodepoolQuota(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        count: int = None,
        period: int = None,
    ):
        self.bandwidth = bandwidth
        self.count = count
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth

        if self.count is not None:
            result['count'] = self.count

        if self.period is not None:
            result['period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('period') is not None:
            self.period = m.get('period')

        return self

