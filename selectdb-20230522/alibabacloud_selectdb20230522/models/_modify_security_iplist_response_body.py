# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityIPListResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_name: str = None,
        group_tag: str = None,
        request_id: str = None,
        security_iplist: str = None,
        security_iptype: str = None,
        task_id: int = None,
        whitelist_net_type: str = None,
    ):
        # The name of the instance.
        self.dbinstance_name = dbinstance_name
        # The name of the whitelist.
        self.group_name = group_name
        # The tag of the whitelist.
        self.group_tag = group_tag
        # The request ID.
        self.request_id = request_id
        # The IP addresses in the whitelist of the instance. Multiple IP addresses are separated by commas (,).
        self.security_iplist = security_iplist
        # The IP address type.
        self.security_iptype = security_iptype
        # The task ID.
        self.task_id = task_id
        # The network type of the whitelist.
        self.whitelist_net_type = whitelist_net_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')

        return self

