# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStackOperationRisksResponseBody(DaraModel):
    def __init__(
        self,
        missing_policy_actions: List[str] = None,
        request_id: str = None,
        risk_resources: List[main_models.ListStackOperationRisksResponseBodyRiskResources] = None,
    ):
        # The operations on which the permissions are not granted to the Alibaba Cloud account of the caller.
        self.missing_policy_actions = missing_policy_actions
        # The ID of the request.
        self.request_id = request_id
        # The resources that are at risk.
        self.risk_resources = risk_resources

    def validate(self):
        if self.risk_resources:
            for v1 in self.risk_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.missing_policy_actions is not None:
            result['MissingPolicyActions'] = self.missing_policy_actions

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskResources'] = []
        if self.risk_resources is not None:
            for k1 in self.risk_resources:
                result['RiskResources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MissingPolicyActions') is not None:
            self.missing_policy_actions = m.get('MissingPolicyActions')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_resources = []
        if m.get('RiskResources') is not None:
            for k1 in m.get('RiskResources'):
                temp_model = main_models.ListStackOperationRisksResponseBodyRiskResources()
                self.risk_resources.append(temp_model.from_map(k1))

        return self

class ListStackOperationRisksResponseBodyRiskResources(DaraModel):
    def __init__(
        self,
        code: str = None,
        logical_resource_id: str = None,
        message: str = None,
        physical_resource_id: str = None,
        reason: str = None,
        request_id: str = None,
        resource_type: str = None,
        risk_type: str = None,
    ):
        # The error code that is returned when the risk detection fails.
        # 
        # >  This parameter is not returned if the risk detection is successful.
        self.code = code
        # The logical ID of the resource. The logical ID is the resource name that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The error message that is returned when the risk detection fails.
        # 
        # >  This parameter is not returned if the risk detection is successful.
        self.message = message
        # The physical ID of the resource. The physical ID is the actual ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The cause of the risk.
        self.reason = reason
        # The ID of the request when the risk detection fails.
        # 
        # >  This parameter is not returned if the risk detection is successful.
        self.request_id = request_id
        # The type of the resource.
        self.resource_type = resource_type
        # The type of the risk. Valid values:
        # 
        # *   Referenced: The resource is referenced by other resources.
        # *   MaybeReferenced: The resource may be referenced by other resources.
        # *   AdditionalRiskCheckRequired: An additional risk detection is required for a nested stack.
        # *   OperationIgnored: The operation does not take effect for the resource.
        self.risk_type = risk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.message is not None:
            result['Message'] = self.message

        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        return self

