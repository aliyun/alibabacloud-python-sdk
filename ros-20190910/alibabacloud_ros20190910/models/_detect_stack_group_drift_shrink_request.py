# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectStackGroupDriftShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        operation_preferences_shrink: str = None,
        region_id: str = None,
        stack_group_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The value can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The operation settings, in JSON format. The following fields are supported:
        # 
        # *   FailureToleranceCount
        # 
        # The maximum number of stack group operation failures that can occur. In a stack group operation, if the total number of failures does not exceed the FailureToleranceCount value, the operation succeeds. Otherwise, the operation fails.
        # 
        # If FailureToleranceCount is not specified, the default value 0 is used. You can specify one of FailureToleranceCount or FailureTolerancePercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 0 to 20.
        # 
        # *   FailureTolerancePercentage
        # 
        # The percentage of stack group operation failures that can occur. In a stack group operation, if the percentage of failures does not exceed the FailureTolerancePercentage value, the operation succeeds. Otherwise, the operation fails.
        # 
        # You can specify one of FailureToleranceCount or FailureTolerancePercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 0 to 100.
        # 
        # *   MaxConcurrentCount
        # 
        # The maximum number of target accounts in which a drift detection operation can be performed at a time.
        # 
        # You can specify one of MaxConcurrentCount or MaxConcurrentPercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 1 to 20.
        # 
        # *   MaxConcurrentPercentage
        # 
        # The maximum percentage of target accounts in which a drift detection operation can be performed at a time.
        # 
        # You can specify one of MaxConcurrentCount or MaxConcurrentPercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 1 to 100.
        self.operation_preferences_shrink = operation_preferences_shrink
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035#doc-api-ROS-DescribeRegions~~ "Queries the DescribeRegions list of a region.") operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the stack group. The name must be unique in a region.
        # 
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or letter.
        # 
        # This parameter is required.
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        return self

