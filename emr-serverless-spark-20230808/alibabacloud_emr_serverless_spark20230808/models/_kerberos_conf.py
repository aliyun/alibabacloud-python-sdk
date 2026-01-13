# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class KerberosConf(DaraModel):
    def __init__(
        self,
        creator: str = None,
        enabled: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        kerberos_conf_id: str = None,
        keytabs: List[str] = None,
        krb_5conf: str = None,
        name: str = None,
        network_service_id: str = None,
        workspace_id: str = None,
    ):
        self.creator = creator
        self.enabled = enabled
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.kerberos_conf_id = kerberos_conf_id
        self.keytabs = keytabs
        self.krb_5conf = krb_5conf
        self.name = name
        self.network_service_id = network_service_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['creator'] = self.creator

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.kerberos_conf_id is not None:
            result['kerberosConfId'] = self.kerberos_conf_id

        if self.keytabs is not None:
            result['keytabs'] = self.keytabs

        if self.krb_5conf is not None:
            result['krb5Conf'] = self.krb_5conf

        if self.name is not None:
            result['name'] = self.name

        if self.network_service_id is not None:
            result['networkServiceId'] = self.network_service_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('kerberosConfId') is not None:
            self.kerberos_conf_id = m.get('kerberosConfId')

        if m.get('keytabs') is not None:
            self.keytabs = m.get('keytabs')

        if m.get('krb5Conf') is not None:
            self.krb_5conf = m.get('krb5Conf')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkServiceId') is not None:
            self.network_service_id = m.get('networkServiceId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

