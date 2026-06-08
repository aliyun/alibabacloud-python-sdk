# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetStackPolicyRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        stack_id: str = None,
        stack_policy_body: str = None,
        stack_policy_url: str = None,
    ):
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the stack.
        # 
        # This parameter is required.
        self.stack_id = stack_id
        # The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length.
        # 
        # You can specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them.
        self.stack_policy_body = stack_policy_body
        # The URL for the file that contains the stack policy. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. The template can be up to 16,384 bytes in length, and the URL can be up to 1,350 bytes in length.
        # 
        # >  If the region of the OSS bucket is not specified, the RegionId value is used.
        # 
        # You can specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them.
        self.stack_policy_url = stack_policy_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body

        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')

        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')

        return self

