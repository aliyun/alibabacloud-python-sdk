# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        check_result_list: List[main_models.DescribeCheckResultResponseBodyCheckResultList] = None,
        request_id: str = None,
    ):
        # The check results.
        self.check_result_list = check_result_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.check_result_list:
            for v1 in self.check_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckResultList'] = []
        if self.check_result_list is not None:
            for k1 in self.check_result_list:
                result['CheckResultList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_result_list = []
        if m.get('CheckResultList') is not None:
            for k1 in m.get('CheckResultList'):
                temp_model = main_models.DescribeCheckResultResponseBodyCheckResultList()
                self.check_result_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCheckResultResponseBodyCheckResultList(DaraModel):
    def __init__(
        self,
        compliance_status: int = None,
        name: str = None,
    ):
        # The compliance status. Valid values:
        # 
        # *   **1**: compliant
        # *   **0**: non-compliant
        self.compliance_status = compliance_status
        # The name of the corresponding section. Valid values:
        # 
        # *   **information_classification**: information classification
        # *   **information_mark**: information labeling
        # *   **network_security_policy**: access to networks and network services
        # *   **login_control**: secure logon procedures
        # *   **week_password**: password management system
        # *   **key_manage**: key management
        # *   **malicious_software**: protection against malware
        # *   **information_backup**: information backup
        # *   **audit_policy**: information system audit control mechanisms
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_status is not None:
            result['ComplianceStatus'] = self.compliance_status

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceStatus') is not None:
            self.compliance_status = m.get('ComplianceStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

