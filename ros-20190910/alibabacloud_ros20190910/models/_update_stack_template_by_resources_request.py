# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateStackTemplateByResourcesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        logical_resource_id: List[str] = None,
        region_id: str = None,
        stack_id: str = None,
        template_format: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests.
        # 
        # The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # Specifies whether to only preview the corrected template in this request. Default value: false. Valid values:
        # 
        # *   true: returns the content of the corrected template and does not correct the template. After Resource Orchestration Service (ROS) compares the corrected template with the original template, ROS determines whether to execute the correction.
        # *   false: corrects the template to eliminate drift.
        # 
        # >  We recommend that you set the DryRun parameter to true to preview the corrected template. If the template content meets expectations, set the DryRun parameter to false to execute the correction.
        self.dry_run = dry_run
        # The logical ID of resource.
        self.logical_resource_id = logical_resource_id
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the stack.
        # 
        # This parameter is required.
        self.stack_id = stack_id
        # The format of the returned template. Default value: JSON. Valid values:
        # 
        # *   JSON
        # *   YAML
        self.template_format = template_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')

        return self

