# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterVulsResponseBody(DaraModel):
    def __init__(
        self,
        vul_records: List[main_models.DescribeClusterVulsResponseBodyVulRecords] = None,
    ):
        # The list of vulnerabilities.
        self.vul_records = vul_records

    def validate(self):
        if self.vul_records:
            for v1 in self.vul_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['vul_records'] = []
        if self.vul_records is not None:
            for k1 in self.vul_records:
                result['vul_records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vul_records = []
        if m.get('vul_records') is not None:
            for k1 in m.get('vul_records'):
                temp_model = main_models.DescribeClusterVulsResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k1))

        return self

class DescribeClusterVulsResponseBodyVulRecords(DaraModel):
    def __init__(
        self,
        cve_list: List[str] = None,
        necessity: str = None,
        node_count: int = None,
        nodepool_id: str = None,
        nodepool_name: str = None,
        vul_alias_name: str = None,
        vul_name: str = None,
        vul_type: str = None,
    ):
        # The CVE list.
        self.cve_list = cve_list
        # The severity level of the vulnerability.
        # 
        # Valid values:
        # 
        # *   nntf: low
        # *   later: medium     
        # *   asap: high
        self.necessity = necessity
        # The number of nodes that have the vulnerability.
        self.node_count = node_count
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The name of the node pool.
        self.nodepool_name = nodepool_name
        # The alias of the vulnerability.
        self.vul_alias_name = vul_alias_name
        # The name of the vulnerability.
        self.vul_name = vul_name
        # The type of vulnerability.
        # 
        # Valid values:
        # 
        # *   app: application vulnerabilities
        # *   sca: application vulnerabilities (software component analysis)
        # *   cve: Linux vulnerabilities
        # *   cms: Web-CMS vulnerabilities
        # *   sys: Windows vulnerabilities
        # *   emg:  emergency vulnerabilities
        self.vul_type = vul_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_list is not None:
            result['cve_list'] = self.cve_list

        if self.necessity is not None:
            result['necessity'] = self.necessity

        if self.node_count is not None:
            result['node_count'] = self.node_count

        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id

        if self.nodepool_name is not None:
            result['nodepool_name'] = self.nodepool_name

        if self.vul_alias_name is not None:
            result['vul_alias_name'] = self.vul_alias_name

        if self.vul_name is not None:
            result['vul_name'] = self.vul_name

        if self.vul_type is not None:
            result['vul_type'] = self.vul_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cve_list') is not None:
            self.cve_list = m.get('cve_list')

        if m.get('necessity') is not None:
            self.necessity = m.get('necessity')

        if m.get('node_count') is not None:
            self.node_count = m.get('node_count')

        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('nodepool_name') is not None:
            self.nodepool_name = m.get('nodepool_name')

        if m.get('vul_alias_name') is not None:
            self.vul_alias_name = m.get('vul_alias_name')

        if m.get('vul_name') is not None:
            self.vul_name = m.get('vul_name')

        if m.get('vul_type') is not None:
            self.vul_type = m.get('vul_type')

        return self

