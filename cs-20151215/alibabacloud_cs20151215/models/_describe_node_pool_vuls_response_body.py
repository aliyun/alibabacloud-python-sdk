# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeNodePoolVulsResponseBody(DaraModel):
    def __init__(
        self,
        vul_records: List[main_models.DescribeNodePoolVulsResponseBodyVulRecords] = None,
        vuls_fix_service_purchased: bool = None,
    ):
        # The vulnerability list of all node pools.
        self.vul_records = vul_records
        # Indicates whether the CVE vulnerability patching service provided by Security Center is purchased.
        # 
        # *   true: yes
        # *   false: no
        self.vuls_fix_service_purchased = vuls_fix_service_purchased

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

        if self.vuls_fix_service_purchased is not None:
            result['vuls_fix_service_purchased'] = self.vuls_fix_service_purchased

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vul_records = []
        if m.get('vul_records') is not None:
            for k1 in m.get('vul_records'):
                temp_model = main_models.DescribeNodePoolVulsResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k1))

        if m.get('vuls_fix_service_purchased') is not None:
            self.vuls_fix_service_purchased = m.get('vuls_fix_service_purchased')

        return self

class DescribeNodePoolVulsResponseBodyVulRecords(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_name: str = None,
        vul_list: List[main_models.DescribeNodePoolVulsResponseBodyVulRecordsVulList] = None,
    ):
        # The ID of the node.
        self.instance_id = instance_id
        # The node name. This name is the identifier of the node in the cluster.
        self.node_name = node_name
        # The list of vulnerabilities.
        self.vul_list = vul_list

    def validate(self):
        if self.vul_list:
            for v1 in self.vul_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.node_name is not None:
            result['node_name'] = self.node_name

        result['vul_list'] = []
        if self.vul_list is not None:
            for k1 in self.vul_list:
                result['vul_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('node_name') is not None:
            self.node_name = m.get('node_name')

        self.vul_list = []
        if m.get('vul_list') is not None:
            for k1 in m.get('vul_list'):
                temp_model = main_models.DescribeNodePoolVulsResponseBodyVulRecordsVulList()
                self.vul_list.append(temp_model.from_map(k1))

        return self

class DescribeNodePoolVulsResponseBodyVulRecordsVulList(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        cve_list: List[str] = None,
        name: str = None,
        necessity: str = None,
        need_reboot: bool = None,
        package_list: List[main_models.DescribeNodePoolVulsResponseBodyVulRecordsVulListPackageList] = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # A list of CVE names corresponding to the vulnerabilities.
        self.cve_list = cve_list
        # The name of the vulnerability.
        self.name = name
        # The severity level of the vulnerability.
        # 
        # Valid values:
        # 
        # *   nntf: You can ignore the vulnerability.
        # *   later: You can fix the vulnerability later.
        # *   asap: You need to fix the vulnerability at the earliest opportunity.
        self.necessity = necessity
        # Indicates whether a restart is required.
        self.need_reboot = need_reboot
        self.package_list = package_list

    def validate(self):
        if self.package_list:
            for v1 in self.package_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['alias_name'] = self.alias_name

        if self.cve_list is not None:
            result['cve_list'] = self.cve_list

        if self.name is not None:
            result['name'] = self.name

        if self.necessity is not None:
            result['necessity'] = self.necessity

        if self.need_reboot is not None:
            result['need_reboot'] = self.need_reboot

        result['package_list'] = []
        if self.package_list is not None:
            for k1 in self.package_list:
                result['package_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias_name') is not None:
            self.alias_name = m.get('alias_name')

        if m.get('cve_list') is not None:
            self.cve_list = m.get('cve_list')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('necessity') is not None:
            self.necessity = m.get('necessity')

        if m.get('need_reboot') is not None:
            self.need_reboot = m.get('need_reboot')

        self.package_list = []
        if m.get('package_list') is not None:
            for k1 in m.get('package_list'):
                temp_model = main_models.DescribeNodePoolVulsResponseBodyVulRecordsVulListPackageList()
                self.package_list.append(temp_model.from_map(k1))

        return self

class DescribeNodePoolVulsResponseBodyVulRecordsVulListPackageList(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

