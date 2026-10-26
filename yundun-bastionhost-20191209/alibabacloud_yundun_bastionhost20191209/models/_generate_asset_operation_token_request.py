# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateAssetOperationTokenRequest(DaraModel):
    def __init__(
        self,
        asset_account_id: str = None,
        asset_account_name: str = None,
        asset_account_password: str = None,
        asset_account_protocol_name: str = None,
        asset_id: str = None,
        asset_type: str = None,
        database_schema: str = None,
        instance_id: str = None,
        login_attribute: str = None,
        operation_mode: str = None,
        operation_note: str = None,
        region_id: str = None,
        sso_client: str = None,
    ):
        # The ID of the asset account for which you want to apply for an O&M token.
        # > You must specify at least one of AssetAccountId and AssetAccountName. If both are specified, AssetAccountId takes precedence.
        self.asset_account_id = asset_account_id
        # The name of the host account. If the account is a custom account, specify the actual account name.
        # 
        # > If both AssetAccountId and AssetAccountName are specified, AssetAccountId takes precedence.
        self.asset_account_name = asset_account_name
        # The Base64-encoded password. This parameter is required when you apply for an O&M token for a custom account.
        self.asset_account_password = asset_account_password
        # The name of the protocol. Valid values:
        # 
        # - **SSH**
        # - **RDP**
        # - **Oracle**
        # - **PostgreSQL**
        # - **MySQL**
        # - **SQLServer**
        # 
        # > This parameter is required when you apply for an O&M token for a custom account.
        self.asset_account_protocol_name = asset_account_protocol_name
        # The ID of the asset for which you want to apply for an O&M token.
        # 
        # This parameter is required.
        self.asset_id = asset_id
        # The Asset Type for which you want to apply for a token. Valid values:
        # - **Host**: host
        # - **Database**: database
        # 
        # This parameter is required.
        self.asset_type = asset_type
        # The name of the database. This parameter is required when OperationMode is set to Sso, AssetAccountProtocolName is set to PostgreSQL or Oracle, and the account is a custom account.
        # > This parameter is supported only in Bastionhost V3.2.44 and later.
        self.database_schema = database_schema
        # The instance ID of the Bastionhost instance for which you want to apply for an O&M token.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The logon attribute. This parameter is required when OperationMode is set to Sso and the account is a custom Oracle account. Valid values:
        # - **SERVICENAME**
        # - **SID**
        # > This parameter is supported only in Bastionhost V3.2.44 and later.
        self.login_attribute = login_attribute
        # The O&M logon method. Valid values:
        # - **WebToken**: obtain an O&M token
        # - **Sso**: log on by using a local client
        # > This parameter is supported only in Bastionhost V3.2.44 and later. If this parameter is left empty, the default value WebToken is used.
        self.operation_mode = operation_mode
        # The logon note. This parameter is required when the administrator enables the logon note feature in the control policy.
        self.operation_note = operation_note
        # The region ID of the Bastionhost instance.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The type of the local client to be opened for O&M operations on Linux assets. This parameter is required when OperationMode is set to Sso and the asset protocol is SSH. Valid values:
        # - **ssh**: open an SSH client to perform O&M operations with SSH permissions
        # - **sftp**: open an SFTP client to perform O&M operations with SFTP permissions
        # > This parameter is supported only in Bastionhost V3.2.44 and later.
        self.sso_client = sso_client

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_account_id is not None:
            result['AssetAccountId'] = self.asset_account_id

        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name

        if self.asset_account_password is not None:
            result['AssetAccountPassword'] = self.asset_account_password

        if self.asset_account_protocol_name is not None:
            result['AssetAccountProtocolName'] = self.asset_account_protocol_name

        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.database_schema is not None:
            result['DatabaseSchema'] = self.database_schema

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_attribute is not None:
            result['LoginAttribute'] = self.login_attribute

        if self.operation_mode is not None:
            result['OperationMode'] = self.operation_mode

        if self.operation_note is not None:
            result['OperationNote'] = self.operation_note

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sso_client is not None:
            result['SsoClient'] = self.sso_client

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetAccountId') is not None:
            self.asset_account_id = m.get('AssetAccountId')

        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')

        if m.get('AssetAccountPassword') is not None:
            self.asset_account_password = m.get('AssetAccountPassword')

        if m.get('AssetAccountProtocolName') is not None:
            self.asset_account_protocol_name = m.get('AssetAccountProtocolName')

        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('DatabaseSchema') is not None:
            self.database_schema = m.get('DatabaseSchema')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginAttribute') is not None:
            self.login_attribute = m.get('LoginAttribute')

        if m.get('OperationMode') is not None:
            self.operation_mode = m.get('OperationMode')

        if m.get('OperationNote') is not None:
            self.operation_note = m.get('OperationNote')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SsoClient') is not None:
            self.sso_client = m.get('SsoClient')

        return self

