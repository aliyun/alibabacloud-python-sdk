# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceVpcEndpointResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        domains: List[str] = None,
        enable: bool = None,
        is_success: bool = None,
        linked_vpcs: List[main_models.GetInstanceVpcEndpointResponseBodyLinkedVpcs] = None,
        module_name: str = None,
        request_id: str = None,
    ):
        # The return value.
        self.code = code
        # Domain names.
        self.domains = domains
        # Indicates whether the VPC endpoint is enabled. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.enable = enable
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # List of linked VPCs
        self.linked_vpcs = linked_vpcs
        # The name of the modules that can be accessed. Valid values:
        # 
        # *   `Registry`: image repositories.
        # *   `Chart`: Helm charts.
        self.module_name = module_name
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.linked_vpcs:
            for v1 in self.linked_vpcs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.domains is not None:
            result['Domains'] = self.domains

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        result['LinkedVpcs'] = []
        if self.linked_vpcs is not None:
            for k1 in self.linked_vpcs:
                result['LinkedVpcs'].append(k1.to_map() if k1 else None)

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        self.linked_vpcs = []
        if m.get('LinkedVpcs') is not None:
            for k1 in m.get('LinkedVpcs'):
                temp_model = main_models.GetInstanceVpcEndpointResponseBodyLinkedVpcs()
                self.linked_vpcs.append(temp_model.from_map(k1))

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceVpcEndpointResponseBodyLinkedVpcs(DaraModel):
    def __init__(
        self,
        default_access: bool = None,
        ip: str = None,
        issue: str = None,
        status: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # Indicates whether the VPC is the default VPC over which the Container Registry instance is accessed.
        self.default_access = default_access
        # IP address.
        self.ip = ip
        # The error message detected in the linked VPC access control.
        self.issue = issue
        # The status of the VPC. Valid values:
        # 
        # *   `CREATING`
        # *   `RUNNING`
        self.status = status
        # VPC ID
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_access is not None:
            result['DefaultAccess'] = self.default_access

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.issue is not None:
            result['Issue'] = self.issue

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultAccess') is not None:
            self.default_access = m.get('DefaultAccess')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Issue') is not None:
            self.issue = m.get('Issue')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

