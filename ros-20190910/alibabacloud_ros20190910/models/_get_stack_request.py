# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        log_option: str = None,
        output_option: str = None,
        region_id: str = None,
        show_resource_progress: str = None,
        stack_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\\
        # The token can be up to 64 characters in length.\\
        # For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The option for returning logs. Valid values:
        # 
        # *   None: does not return logs.
        # *   Stack (default): returns the logs of the stack.
        # *   Resource: returns the logs of resources in the stack.
        # *   All: returns all logs.
        self.log_option = log_option
        # Specifies whether to return Outputs. Valid values:
        # 
        # *   Enabled (default)
        # *   Disabled
        # 
        # >  The Outputs parameter requires a long period of time to calculate. If you do not require Outputs of the stack, we recommend that you set OutputOption to Disabled to improve the response speed of the GetStack operation.
        self.output_option = output_option
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to return information about ResourceProgress. Valid values:
        # 
        # *   Disabled (default): does not return information about ResourceProgress.
        # *   PercentageOnly: returns StackOperationProgress and StackActionProgress of ResourceProgress.
        # 
        # >  ROS and Terraform stacks are supported. Creation, resumed creation, update, deletion, import, and rollback operations on stacks are supported.
        # 
        # *   EnabledIfCreateStack (not recommend): returns \\*Count and InProgressResourceDetails of ResourceProgress only during a stack creation operation.
        # 
        # >  During a creation operation, a stack is in one of the following states: CREATE_IN_PROGRESS, CREATE_COMPLETE, CREATE_FAILED, CREATE_ROLLBACK_IN_PROGRESS, CREATE_ROLLBACK_COMPLETE, and CREATE_ROLLBACK_FAILED.
        self.show_resource_progress = show_resource_progress
        # The stack ID.
        # 
        # This parameter is required.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.log_option is not None:
            result['LogOption'] = self.log_option

        if self.output_option is not None:
            result['OutputOption'] = self.output_option

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_resource_progress is not None:
            result['ShowResourceProgress'] = self.show_resource_progress

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('LogOption') is not None:
            self.log_option = m.get('LogOption')

        if m.get('OutputOption') is not None:
            self.output_option = m.get('OutputOption')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowResourceProgress') is not None:
            self.show_resource_progress = m.get('ShowResourceProgress')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

