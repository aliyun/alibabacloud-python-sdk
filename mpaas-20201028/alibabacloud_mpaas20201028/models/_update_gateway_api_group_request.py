# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateGatewayApiGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        centers: Dict[str, Any] = None,
        description: str = None,
        domain_name: str = None,
        enable_mtls: bool = None,
        group_id: int = None,
        group_name: str = None,
        host: str = None,
        https_model: bool = None,
        instance_id: str = None,
        instance_port: int = None,
        region_mode: bool = None,
        tenant_id: str = None,
        timeout: int = None,
        upstream_type: str = None,
        vpc_id: str = None,
        vpc_model: bool = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.centers = centers
        self.description = description
        self.domain_name = domain_name
        self.enable_mtls = enable_mtls
        # This parameter is required.
        self.group_id = group_id
        # This parameter is required.
        self.group_name = group_name
        self.host = host
        self.https_model = https_model
        self.instance_id = instance_id
        self.instance_port = instance_port
        self.region_mode = region_mode
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.timeout = timeout
        # This parameter is required.
        self.upstream_type = upstream_type
        self.vpc_id = vpc_id
        self.vpc_model = vpc_model
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.centers is not None:
            result['Centers'] = self.centers

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.enable_mtls is not None:
            result['EnableMTLS'] = self.enable_mtls

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.host is not None:
            result['Host'] = self.host

        if self.https_model is not None:
            result['HttpsModel'] = self.https_model

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port

        if self.region_mode is not None:
            result['RegionMode'] = self.region_mode

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_model is not None:
            result['VpcModel'] = self.vpc_model

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Centers') is not None:
            self.centers = m.get('Centers')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EnableMTLS') is not None:
            self.enable_mtls = m.get('EnableMTLS')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HttpsModel') is not None:
            self.https_model = m.get('HttpsModel')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')

        if m.get('RegionMode') is not None:
            self.region_mode = m.get('RegionMode')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcModel') is not None:
            self.vpc_model = m.get('VpcModel')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

