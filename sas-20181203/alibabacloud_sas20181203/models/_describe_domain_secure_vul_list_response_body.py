# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainSecureVulListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vul_list: List[main_models.DescribeDomainSecureVulListResponseBodyVulList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of vulnerabilities returned.
        self.total_count = total_count
        # The domain name-related vulnerabilities.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VulList'] = []
        if self.vul_list is not None:
            for k1 in self.vul_list:
                result['VulList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vul_list = []
        if m.get('VulList') is not None:
            for k1 in m.get('VulList'):
                temp_model = main_models.DescribeDomainSecureVulListResponseBodyVulList()
                self.vul_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainSecureVulListResponseBodyVulList(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        asap_count: int = None,
        gmt_last: int = None,
        handled_count: int = None,
        later_count: int = None,
        name: str = None,
        nntf_count: int = None,
        tags: str = None,
        type: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The number of the vulnerabilities that have the **high** priority.
        self.asap_count = asap_count
        # The timestamp when the vulnerability was last detected. Unit: milliseconds.
        self.gmt_last = gmt_last
        # The number of handled vulnerabilities.
        self.handled_count = handled_count
        # The number of the vulnerabilities that have the **medium** priority.
        self.later_count = later_count
        # The name of the vulnerability.
        self.name = name
        # The number of the vulnerabilities that have the **low** priority.
        self.nntf_count = nntf_count
        # The tag that is added to the vulnerability. Valid values:
        # 
        # *   Restart required
        # *   Remote utilization
        # *   EXP exists
        # *   Available
        # *   Elevation of Privilege
        # *   Code Execution
        self.tags = tags
        # The type of the vulnerability. Default value: cve. Valid values:
        # 
        # *   **cve**: Linux software vulnerability.
        # *   **sys**: Windows system vulnerability.
        # *   **cms**: Web-CMS vulnerability.
        # *   **app**: application vulnerability that is detected by network scanning.
        # *   **sca**: application vulnerability that is detected by using software component analysis.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count

        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last

        if self.handled_count is not None:
            result['HandledCount'] = self.handled_count

        if self.later_count is not None:
            result['LaterCount'] = self.later_count

        if self.name is not None:
            result['Name'] = self.name

        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')

        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')

        if m.get('HandledCount') is not None:
            self.handled_count = m.get('HandledCount')

        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

