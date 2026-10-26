# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceADAuthServerRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        domain: str = None,
        email_mapping: str = None,
        filter: str = None,
        instance_id: str = None,
        is_default: str = None,
        is_ssl: str = None,
        is_sync_email_attr: str = None,
        is_sync_mobile_attr: str = None,
        is_sync_name_attr: str = None,
        is_sync_ou_as_user_group: str = None,
        mobile_mapping: str = None,
        name_mapping: str = None,
        password: str = None,
        port: str = None,
        region_id: str = None,
        server: str = None,
        server_name: str = None,
        standby_server: str = None,
        sync_interval: str = None,
        user_source_id: str = None,
    ):
        # The server account.
        # 
        # This parameter is required.
        self.account = account
        # The base distinguished name (Base DN).
        # 
        # This parameter is required.
        self.base_dn = base_dn
        # The domain on the AD server.
        # 
        # This parameter is required.
        self.domain = domain
        # The server attribute name that maps to the user email address.
        self.email_mapping = email_mapping
        # The filter condition for users.
        self.filter = filter
        # The instance ID of the Bastionhost instance.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the AD authentication server is the default server. A value of true indicates that the server is the default AD authentication server. A value of false indicates that the server is not the default AD authentication server.
        self.is_default = is_default
        # Specifies whether SSL is supported. Valid values:
        # 
        # - **true**: Supported.
        # - **false**: Not supported.
        self.is_ssl = is_ssl
        # Specifies whether to synchronize the email address. A value of true indicates that the email address is synchronized. A value of false indicates that the email address is not synchronized.
        self.is_sync_email_attr = is_sync_email_attr
        # Specifies whether to synchronize the mobile phone number. A value of true indicates that the mobile phone number is synchronized. A value of false indicates that the mobile phone number is not synchronized.
        self.is_sync_mobile_attr = is_sync_mobile_attr
        # Specifies whether to synchronize the display name. A value of true indicates that the display name is synchronized. A value of false indicates that the display name is not synchronized.
        self.is_sync_name_attr = is_sync_name_attr
        # Specifies whether to synchronize the organization to which the user belongs as a user group. A value of true indicates that the organization is synchronized as a user group. A value of false indicates that the organization is not synchronized as a user group.
        self.is_sync_ou_as_user_group = is_sync_ou_as_user_group
        # The server attribute name that maps to the user mobile phone number.
        self.mobile_mapping = mobile_mapping
        # The server attribute name that maps to the username.
        self.name_mapping = name_mapping
        # The password of the server account.
        self.password = password
        # The port used to access the server.
        # 
        # This parameter is required.
        self.port = port
        # The region ID of the Bastionhost instance.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The address of the server.
        # 
        # This parameter is required.
        self.server = server
        # The name of the AD authentication server.
        self.server_name = server_name
        # The address of the standby server.
        self.standby_server = standby_server
        # The interval at which user snapshots are automatically synchronized, in hours. Valid values: 0, and 4 to 168. A value of 0 indicates that automatic synchronization is disabled.
        self.sync_interval = sync_interval
        self.user_source_id = user_source_id

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

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl

        if self.is_sync_email_attr is not None:
            result['IsSyncEmailAttr'] = self.is_sync_email_attr

        if self.is_sync_mobile_attr is not None:
            result['IsSyncMobileAttr'] = self.is_sync_mobile_attr

        if self.is_sync_name_attr is not None:
            result['IsSyncNameAttr'] = self.is_sync_name_attr

        if self.is_sync_ou_as_user_group is not None:
            result['IsSyncOuAsUserGroup'] = self.is_sync_ou_as_user_group

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

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server

        if self.sync_interval is not None:
            result['SyncInterval'] = self.sync_interval

        if self.user_source_id is not None:
            result['UserSourceId'] = self.user_source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')

        if m.get('IsSyncEmailAttr') is not None:
            self.is_sync_email_attr = m.get('IsSyncEmailAttr')

        if m.get('IsSyncMobileAttr') is not None:
            self.is_sync_mobile_attr = m.get('IsSyncMobileAttr')

        if m.get('IsSyncNameAttr') is not None:
            self.is_sync_name_attr = m.get('IsSyncNameAttr')

        if m.get('IsSyncOuAsUserGroup') is not None:
            self.is_sync_ou_as_user_group = m.get('IsSyncOuAsUserGroup')

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

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')

        if m.get('SyncInterval') is not None:
            self.sync_interval = m.get('SyncInterval')

        if m.get('UserSourceId') is not None:
            self.user_source_id = m.get('UserSourceId')

        return self

