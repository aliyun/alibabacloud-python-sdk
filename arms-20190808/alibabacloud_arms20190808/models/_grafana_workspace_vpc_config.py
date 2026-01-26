# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceVpcConfig(DaraModel):
    def __init__(
        self,
        fc_config: str = None,
        id: int = None,
        install_msg: str = None,
        install_status: str = None,
        ip_sections: str = None,
        name: str = None,
        region_id: str = None,
        security_group_id: str = None,
        user_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.fc_config = fc_config
        self.id = id
        self.install_msg = install_msg
        self.install_status = install_status
        self.ip_sections = ip_sections
        self.name = name
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.user_id = user_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fc_config is not None:
            result['fcConfig'] = self.fc_config

        if self.id is not None:
            result['id'] = self.id

        if self.install_msg is not None:
            result['installMsg'] = self.install_msg

        if self.install_status is not None:
            result['installStatus'] = self.install_status

        if self.ip_sections is not None:
            result['ipSections'] = self.ip_sections

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fcConfig') is not None:
            self.fc_config = m.get('fcConfig')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('installMsg') is not None:
            self.install_msg = m.get('installMsg')

        if m.get('installStatus') is not None:
            self.install_status = m.get('installStatus')

        if m.get('ipSections') is not None:
            self.ip_sections = m.get('ipSections')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

