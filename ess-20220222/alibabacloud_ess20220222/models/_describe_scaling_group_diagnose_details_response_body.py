# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingGroupDiagnoseDetailsResponseBody(DaraModel):
    def __init__(
        self,
        details: List[main_models.DescribeScalingGroupDiagnoseDetailsResponseBodyDetails] = None,
        request_id: str = None,
    ):
        # The diagnostic reports.
        self.details = details
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DescribeScalingGroupDiagnoseDetailsResponseBodyDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeScalingGroupDiagnoseDetailsResponseBodyDetails(DaraModel):
    def __init__(
        self,
        diagnose_type: str = None,
        error_code: str = None,
        resource_id: str = None,
        status: str = None,
    ):
        # The type of the diagnostic item. Valid values:
        # 
        # *   AccountArrearage: Checks whether your Alibaba Cloud account has overdue payments.
        # *   AccountNotEnoughBalance: Checks whether the balance of your Alibaba Cloud account is sufficient.
        # *   ElasticStrength: Checks whether the instance types that are specified in the scaling configuration are sufficient.
        # *   VSwitch: Checks whether the vSwitch is available. If the specified vSwitch is deleted, specify an existing vSwitch for the scaling group.
        # *   SecurityGroup: Checks whether the security group is available. If the specified security group is deleted, specify an existing security group for the scaling group.
        # *   KeyPair: Checks whether the key pair is available. If the specified key pair is deleted, specify another key pair for the scaling group.
        # *   SlbBackendServerQuota: Checks whether the number of ECS instances that are added to the default server group and the vServer groups of the SLB instances associated with the scaling group has reached the upper limit.
        # *   AlbBackendServerQuota: Checks whether the number of ECS instances that are attached to the ALB instances of the scaling group has reached the upper limit.
        # *   NlbBackendServerQuota: Checks whether the number of ECS instances that are attached to the NLB instances of the scaling group has reached the upper limit.
        self.diagnose_type = diagnose_type
        # The error code of the diagnostic item. Valid values:
        # 
        # *   VSwitchIdNotFound: The vSwitch does not exist.
        # *   SecurityGroupNotFound: The security group does not exist.
        # *   KeyPairNotFound: The key pair does not exist.
        # *   SlbBackendServerQuotaExceeded: The number of ECS instances that are added to the default server group and the vServer groups of the SLB instances associated with the scaling group has reached the upper limit.
        # *   AlbBackendServerQuotaExceeded: The number of ECS instances that are attached to the ALB instances of the scaling group has reached the upper limit.
        # *   NlbBackendServerQuotaExceeded: The number of ECS instances that are attached to the NLB instances of the scaling group has reached the upper limit.
        # *   AccountArrearage: Your account has an overdue payment.
        # *   AccountNotEnoughBalance: The balance of your Alibaba Cloud account is insufficient.
        # *   ElasticStrengthAlert: The inventory levels are lower than required.
        self.error_code = error_code
        # The resource ID corresponding to the diagnostic result.
        self.resource_id = resource_id
        # Status of the diagnostic item. Possible values:
        # 
        # - Normal: The diagnostic result is normal.
        # 
        # - Warn: The diagnostic result is a warning.
        # 
        # - Critical: The diagnostic result is critical.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnose_type is not None:
            result['DiagnoseType'] = self.diagnose_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnoseType') is not None:
            self.diagnose_type = m.get('DiagnoseType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

