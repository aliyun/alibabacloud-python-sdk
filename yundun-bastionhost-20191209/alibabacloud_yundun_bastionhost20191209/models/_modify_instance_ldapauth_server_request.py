# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceLDAPAuthServerRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        email_mapping: str = None,
        filter: str = None,
        instance_id: str = None,
        is_ssl: str = None,
        login_name_mapping: str = None,
        mobile_mapping: str = None,
        name_mapping: str = None,
        password: str = None,
        port: str = None,
        region_id: str = None,
        server: str = None,
        standby_server: str = None,
    ):
        # The username of the account that is used for the LDAP server.
        # 
        # This parameter is required.
        self.account = account
        # The Base distinguished name (DN).
        # 
        # This parameter is required.
        self.base_dn = base_dn
        # The field that is used to indicate the email address of a user on the LDAP server.
        self.email_mapping = email_mapping
        # The condition that is used to filter users.
        self.filter = filter
        # The bastion host ID.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to support SSL. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_ssl = is_ssl
        # The field that is used to indicate the logon name of a user on the LDAP server.
        self.login_name_mapping = login_name_mapping
        # The field that is used to indicate the mobile phone number of a user on the LDAP server.
        self.mobile_mapping = mobile_mapping
        # The field that is used to indicate the name of a user on the LDAP server.
        self.name_mapping = name_mapping
        # The password of the account that is used for the LDAP server. You must configure a password when you configure LDAP authentication. If you leave this parameter empty when you modify the settings of LDAP authentication, the current password is used.
        self.password = password
        # The port that is used to access the LDAP server.
        # 
        # This parameter is required.
        self.port = port
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The address of the LDAP server.
        # 
        # This parameter is required.
        self.server = server
        # The address of the secondary LDAP server.
        self.standby_server = standby_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn

        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl

        if self.login_name_mapping is not None:
            result['LoginNameMapping'] = self.login_name_mapping

        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping

        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.server is not None:
            result['Server'] = self.server

        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')

        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')

        if m.get('LoginNameMapping') is not None:
            self.login_name_mapping = m.get('LoginNameMapping')

        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')

        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Server') is not None:
            self.server = m.get('Server')

        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')

        return self

