# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallDataAgentMcpRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        endpoint: str = None,
        from_json: str = None,
        headers: str = None,
        name: str = None,
        need_uid_in_header: bool = None,
        net_type: str = None,
        transport_type: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
        workspace_id: str = None,
    ):
        # The brief description of the artifact. This parameter can be empty.
        self.description = description
        # The endpoint of the MCP instance.
        self.endpoint = endpoint
        # The JSON used to create the MCP.
        self.from_json = from_json
        # The request header settings.
        self.headers = headers
        # The MCP name.
        self.name = name
        # Specifies whether to include the Alibaba Cloud UID in the request header.
        self.need_uid_in_header = need_uid_in_header
        # The network type. Valid values:
        # 
        # - `vpc`: virtual private cloud.
        # - `public`: public network.
        self.net_type = net_type
        # The transport channel type. Valid values: streamablehttp and sse.
        self.transport_type = transport_type
        # VPC ID
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vsw_id = vsw_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.from_json is not None:
            result['FromJson'] = self.from_json

        if self.headers is not None:
            result['Headers'] = self.headers

        if self.name is not None:
            result['Name'] = self.name

        if self.need_uid_in_header is not None:
            result['NeedUidInHeader'] = self.need_uid_in_header

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.transport_type is not None:
            result['TransportType'] = self.transport_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('FromJson') is not None:
            self.from_json = m.get('FromJson')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedUidInHeader') is not None:
            self.need_uid_in_header = m.get('NeedUidInHeader')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('TransportType') is not None:
            self.transport_type = m.get('TransportType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

