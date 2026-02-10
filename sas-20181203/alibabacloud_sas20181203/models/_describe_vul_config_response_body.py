# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVulConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        target_configs: List[main_models.DescribeVulConfigResponseBodyTargetConfigs] = None,
        total_count: int = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the configurations of vulnerability management.
        self.target_configs = target_configs
        # The total number of configurations.
        self.total_count = total_count

    def validate(self):
        if self.target_configs:
            for v1 in self.target_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TargetConfigs'] = []
        if self.target_configs is not None:
            for k1 in self.target_configs:
                result['TargetConfigs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.target_configs = []
        if m.get('TargetConfigs') is not None:
            for k1 in m.get('TargetConfigs'):
                temp_model = main_models.DescribeVulConfigResponseBodyTargetConfigs()
                self.target_configs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVulConfigResponseBodyTargetConfigs(DaraModel):
    def __init__(
        self,
        config: str = None,
        over_all_config: str = None,
        type: str = None,
    ):
        # The configuration of vulnerability scan.
        # 
        # > Valid values when you set the Type parameter to **cve**, **sys**, **cms**, **app**, **emg**, or **yum**:
        # 
        # *   **on**: enabled
        # 
        # *   **off**: disabled
        # 
        # Valid values when you set the Type parameter to **scanMode**:
        # 
        # *   **real**: displays easily exploitable vulnerability.
        # 
        # *   **all**: displays all vulnerabilities.
        # 
        # When you set the Type parameter to **imageVulClean**, the value of this parameter indicates the vulnerability retention period in days.
        self.config = config
        # Indicates whether the vulnerability management feature is enabled for all servers. Valid values:
        # 
        # *   **off**: disabled
        # *   **on**: enabled
        self.over_all_config = over_all_config
        # The type of configuration. Valid values:
        # 
        # *   **cve**: Linux software vulnerability.
        # *   **sys**: Windows system vulnerability.
        # *   **cms**: Web-CMS vulnerability.
        # *   **app**: application vulnerability that is detected by using web scanner.
        # *   **emg**: urgent vulnerability.
        # *   **scanMode**: displays easily exploitable vulnerability.
        # *   **imageVulClean**: vulnerability retention duration.
        # *   **yum**: preferentially uses YUM or APT sources of Alibaba Cloud to fix vulnerabilities.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.over_all_config is not None:
            result['OverAllConfig'] = self.over_all_config

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('OverAllConfig') is not None:
            self.over_all_config = m.get('OverAllConfig')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

