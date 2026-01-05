# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApplicationWhitelistRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        component_id: str = None,
        modify_mode: str = None,
        security_groups: str = None,
        security_iparray_name: str = None,
        security_iplist: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.component_id = component_id
        self.modify_mode = modify_mode
        self.security_groups = security_groups
        self.security_iparray_name = security_iparray_name
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups

        if self.security_iparray_name is not None:
            result['SecurityIPArrayName'] = self.security_iparray_name

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')

        if m.get('SecurityIPArrayName') is not None:
            self.security_iparray_name = m.get('SecurityIPArrayName')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

