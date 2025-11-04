# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequestDmlAuthSetting(TeaModel):
    def __init__(
        self,
        allow_databases: List[str] = None,
        allow_dictionaries: List[str] = None,
        ddl_authority: bool = None,
        dml_authority: int = None,
    ):
        # The databases on which you want to grant permissions. Separate multiple databases with commas (,).
        self.allow_databases = allow_databases
        # The dictionaries on which you want to grant permissions. Separate multiple dictionaries with commas (,).
        self.allow_dictionaries = allow_dictionaries
        # Specifies whether to grant the DDL permissions to the database account. Valid values:
        # 
        # *   **true**: The account has the permissions to execute DDL statements.
        # *   **false**: The account does not have the permissions to execute DDL statements.
        self.ddl_authority = ddl_authority
        # Specifies whether to grant the DML permissions to the database account. Valid values:
        # 
        # *   **0**: The account has the permissions to read data from the database, write data to the database, and modify the settings of the database.
        # *   **1**: The account only has the permissions to read data from the database.
        # *   **2**: The account only has the permissions to read data from the database and modify the settings of the database.
        self.dml_authority = dml_authority

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases
        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries
        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority
        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')
        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')
        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')
        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_type: str = None,
        dbinstance_id: str = None,
        description: str = None,
        dml_auth_setting: CreateAccountRequestDmlAuthSetting = None,
        password: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The name of the account.
        # 
        # This parameter is required.
        self.account = account
        # The type of the database account. Valid values:
        # 
        # *   **NormalAccount**: standard account
        # *   **SuperAccount**: privileged account
        # 
        # This parameter is required.
        self.account_type = account_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The description of the account.
        self.description = description
        # The information about permissions.
        self.dml_auth_setting = dml_auth_setting
        # The password of the database account. The password must meet the following requirements:
        # 
        # - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - The following special characters are supported: ! @ # $ % ^ & * ( ) _ + - =\
        # - The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.password = password
        # The code of the cloud service.
        self.product = product
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.dml_auth_setting:
            self.dml_auth_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dml_auth_setting is not None:
            result['DmlAuthSetting'] = self.dml_auth_setting.to_map()
        if self.password is not None:
            result['Password'] = self.password
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DmlAuthSetting') is not None:
            temp_model = CreateAccountRequestDmlAuthSetting()
            self.dml_auth_setting = temp_model.from_map(m['DmlAuthSetting'])
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAccountShrinkRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_type: str = None,
        dbinstance_id: str = None,
        description: str = None,
        dml_auth_setting_shrink: str = None,
        password: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The name of the account.
        # 
        # This parameter is required.
        self.account = account
        # The type of the database account. Valid values:
        # 
        # *   **NormalAccount**: standard account
        # *   **SuperAccount**: privileged account
        # 
        # This parameter is required.
        self.account_type = account_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The description of the account.
        self.description = description
        # The information about permissions.
        self.dml_auth_setting_shrink = dml_auth_setting_shrink
        # The password of the database account. The password must meet the following requirements:
        # 
        # - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - The following special characters are supported: ! @ # $ % ^ & * ( ) _ + - =\
        # - The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.password = password
        # The code of the cloud service.
        self.product = product
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dml_auth_setting_shrink is not None:
            result['DmlAuthSetting'] = self.dml_auth_setting_shrink
        if self.password is not None:
            result['Password'] = self.password
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DmlAuthSetting') is not None:
            self.dml_auth_setting_shrink = m.get('DmlAuthSetting')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
    ):
        # The name of the database account.
        self.account = account
        # The cluster ID.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateAccountResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        backup_retention_period: str = None,
        dbinstance_id: str = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        region_id: str = None,
    ):
        # The number of days for which you can retain the backup data.
        self.backup_retention_period = backup_retention_period
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The backup cycle, which indicates the day of the week when the system regularly backs up data. Separate multiple dates with commas (`,`).
        # 
        # This parameter is required.
        self.preferred_backup_period = preferred_backup_period
        # The backup time window within which the backup task is performed. The time is displayed in `UTC`. For example, `12:00Z-13:00Z` indicates that the backup time window ranges from `12:00` (UTC) to `13:00` `(UTC)`.
        # 
        # This parameter is required.
        self.preferred_backup_time = preferred_backup_time
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBackupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        region_id: str = None,
    ):
        # Database remark information.
        self.comment = comment
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database name. The name must meet the following requirements:
        # 
        # *   The name can contain lowercase letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a lowercase letter and end with a lowercase letter or digit.
        # *   The name can be up to 64 characters in length.
        # 
        # >  An underscore (_) is counted as two characters.
        # 
        # This parameter is required.
        self.dbname = dbname
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDBResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.dbname = dbname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class CreateDBResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateDBResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateDBResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequestMultiZone(TeaModel):
    def __init__(
        self,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        client_token: str = None,
        dbinstance_description: str = None,
        dbtime_zone: str = None,
        deploy_schema: str = None,
        engine: str = None,
        engine_version: str = None,
        multi_zone: List[CreateDBInstanceRequestMultiZone] = None,
        node_count: int = None,
        node_scale_max: int = None,
        node_scale_min: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        scale_max: str = None,
        scale_min: str = None,
        source_dbinstance_id: str = None,
        storage_quota: int = None,
        storage_type: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # The backup set ID.
        self.backup_set_id = backup_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token. Make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The cluster description.
        self.dbinstance_description = dbinstance_description
        self.dbtime_zone = dbtime_zone
        # The deployment status of the cluster.
        self.deploy_schema = deploy_schema
        # The engine type.
        self.engine = engine
        # The engine version.
        self.engine_version = engine_version
        # The configurations of multi-zone deployment.
        self.multi_zone = multi_zone
        self.node_count = node_count
        self.node_scale_max = node_scale_max
        self.node_scale_min = node_scale_min
        # The region ID
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The maximum capacity for auto scaling.
        self.scale_max = scale_max
        # The minimum capacity for auto scaling.
        self.scale_min = scale_min
        # The cluster ID.
        self.source_dbinstance_id = source_dbinstance_id
        self.storage_quota = storage_quota
        self.storage_type = storage_type
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.multi_zone:
            for k in self.multi_zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbtime_zone is not None:
            result['DBTimeZone'] = self.dbtime_zone
        if self.deploy_schema is not None:
            result['DeploySchema'] = self.deploy_schema
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        result['MultiZone'] = []
        if self.multi_zone is not None:
            for k in self.multi_zone:
                result['MultiZone'].append(k.to_map() if k else None)
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_scale_max is not None:
            result['NodeScaleMax'] = self.node_scale_max
        if self.node_scale_min is not None:
            result['NodeScaleMin'] = self.node_scale_min
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max
        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min
        if self.source_dbinstance_id is not None:
            result['SourceDBInstanceId'] = self.source_dbinstance_id
        if self.storage_quota is not None:
            result['StorageQuota'] = self.storage_quota
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBTimeZone') is not None:
            self.dbtime_zone = m.get('DBTimeZone')
        if m.get('DeploySchema') is not None:
            self.deploy_schema = m.get('DeploySchema')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        self.multi_zone = []
        if m.get('MultiZone') is not None:
            for k in m.get('MultiZone'):
                temp_model = CreateDBInstanceRequestMultiZone()
                self.multi_zone.append(temp_model.from_map(k))
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeScaleMax') is not None:
            self.node_scale_max = m.get('NodeScaleMax')
        if m.get('NodeScaleMin') is not None:
            self.node_scale_min = m.get('NodeScaleMin')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')
        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')
        if m.get('SourceDBInstanceId') is not None:
            self.source_dbinstance_id = m.get('SourceDBInstanceId')
        if m.get('StorageQuota') is not None:
            self.storage_quota = m.get('StorageQuota')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        client_token: str = None,
        dbinstance_description: str = None,
        dbtime_zone: str = None,
        deploy_schema: str = None,
        engine: str = None,
        engine_version: str = None,
        multi_zone_shrink: str = None,
        node_count: int = None,
        node_scale_max: int = None,
        node_scale_min: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        scale_max: str = None,
        scale_min: str = None,
        source_dbinstance_id: str = None,
        storage_quota: int = None,
        storage_type: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # The backup set ID.
        self.backup_set_id = backup_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token. Make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The cluster description.
        self.dbinstance_description = dbinstance_description
        self.dbtime_zone = dbtime_zone
        # The deployment status of the cluster.
        self.deploy_schema = deploy_schema
        # The engine type.
        self.engine = engine
        # The engine version.
        self.engine_version = engine_version
        # The configurations of multi-zone deployment.
        self.multi_zone_shrink = multi_zone_shrink
        self.node_count = node_count
        self.node_scale_max = node_scale_max
        self.node_scale_min = node_scale_min
        # The region ID
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The maximum capacity for auto scaling.
        self.scale_max = scale_max
        # The minimum capacity for auto scaling.
        self.scale_min = scale_min
        # The cluster ID.
        self.source_dbinstance_id = source_dbinstance_id
        self.storage_quota = storage_quota
        self.storage_type = storage_type
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbtime_zone is not None:
            result['DBTimeZone'] = self.dbtime_zone
        if self.deploy_schema is not None:
            result['DeploySchema'] = self.deploy_schema
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.multi_zone_shrink is not None:
            result['MultiZone'] = self.multi_zone_shrink
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_scale_max is not None:
            result['NodeScaleMax'] = self.node_scale_max
        if self.node_scale_min is not None:
            result['NodeScaleMin'] = self.node_scale_min
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max
        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min
        if self.source_dbinstance_id is not None:
            result['SourceDBInstanceId'] = self.source_dbinstance_id
        if self.storage_quota is not None:
            result['StorageQuota'] = self.storage_quota
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBTimeZone') is not None:
            self.dbtime_zone = m.get('DBTimeZone')
        if m.get('DeploySchema') is not None:
            self.deploy_schema = m.get('DeploySchema')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('MultiZone') is not None:
            self.multi_zone_shrink = m.get('MultiZone')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeScaleMax') is not None:
            self.node_scale_max = m.get('NodeScaleMax')
        if m.get('NodeScaleMin') is not None:
            self.node_scale_min = m.get('NodeScaleMin')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')
        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')
        if m.get('SourceDBInstanceId') is not None:
            self.source_dbinstance_id = m.get('SourceDBInstanceId')
        if m.get('StorageQuota') is not None:
            self.storage_quota = m.get('StorageQuota')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
        order_id: int = None,
    ):
        # The endpoint.
        self.connection_string = connection_string
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateDBInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateDBInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointRequest(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        connection_prefix: str = None,
        dbinstance_id: str = None,
        dbinstance_net_type: str = None,
        region_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The prefix of the new endpoint. The prefix of the ConnectionString parameter.
        self.connection_prefix = connection_prefix
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type.
        # 
        # Valid values:
        # 
        # *   Public
        self.dbinstance_net_type = dbinstance_net_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.connection_prefix is not None:
            result['ConnectionPrefix'] = self.connection_prefix
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('ConnectionPrefix') is not None:
            self.connection_prefix = m.get('ConnectionPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The destination database account.
        # 
        # This parameter is required.
        self.account = account
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The code of the cloud service.
        self.product = product
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
    ):
        # The name of the account.
        self.account = account
        # The cluster ID.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteAccountResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBackupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the destination database.
        # 
        # This parameter is required.
        self.dbname = dbname
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDBResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.dbname = dbname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DeleteDBResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDBResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDBResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the destination cluster.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDBInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDBInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDBInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointRequest(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        connection_string: str = None,
        dbinstance_id: str = None,
        dbinstance_net_type: str = None,
        region_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The prefix of the endpoint, which indicates the prefix of the value of the ConnectionString parameter.
        self.connection_string = connection_string
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.dbinstance_net_type = dbinstance_net_type
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountAuthorityRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account = account
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAccountAuthorityResponseBodyData(TeaModel):
    def __init__(
        self,
        account: str = None,
        allow_databases: List[str] = None,
        allow_dictionaries: List[str] = None,
        dbinstance_id: str = None,
        ddl_authority: bool = None,
        dml_authority: int = None,
        total_databases: List[str] = None,
        total_dictionaries: List[str] = None,
    ):
        # The name of the database account.
        self.account = account
        # The databases on which permissions are granted.
        self.allow_databases = allow_databases
        # The dictionaries on which permissions are granted.
        self.allow_dictionaries = allow_dictionaries
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # Indicates whether the DDL permissions are granted to the database account. Valid values:
        # 
        # *   **true**: The account has the permissions to execute DDL statements.
        # *   **false**: The account does not have the permissions to execute DDL statements.
        self.ddl_authority = ddl_authority
        # Indicates whether the DML permissions are granted to the database account. Valid values:
        # 
        # *   0: The account has the permissions to read data from the database, write data to the database, and modify the settings of the database.
        # *   1: The account only has the permissions to read data from the database.
        # *   2: The account only has the permissions to read data from the database and modify the settings of the database.
        self.dml_authority = dml_authority
        # All databases.
        self.total_databases = total_databases
        # The database.
        self.total_dictionaries = total_dictionaries

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases
        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority
        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority
        if self.total_databases is not None:
            result['TotalDatabases'] = self.total_databases
        if self.total_dictionaries is not None:
            result['TotalDictionaries'] = self.total_dictionaries
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')
        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')
        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')
        if m.get('TotalDatabases') is not None:
            self.total_databases = m.get('TotalDatabases')
        if m.get('TotalDictionaries') is not None:
            self.total_dictionaries = m.get('TotalDictionaries')
        return self


class DescribeAccountAuthorityResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeAccountAuthorityResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeAccountAuthorityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountAuthorityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountAuthorityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccountAuthorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The code of the cloud service.
        self.product = product
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAccountsResponseBodyDataAccounts(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_type: str = None,
        description: str = None,
        status: str = None,
    ):
        # The username of the database account.
        self.account = account
        # The type of the database account. Valid values:
        # 
        # *   **1**: standard account
        # *   **6**: privileged account
        self.account_type = account_type
        # The description.
        self.description = description
        # The state of the database account. Valid values:
        # 
        # *   **0**: The database account is being created.
        # *   **1**: The database account is in use.
        # *   **3**: The database account is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.description is not None:
            result['Description'] = self.description
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAccountsResponseBodyData(TeaModel):
    def __init__(
        self,
        accounts: List[DescribeAccountsResponseBodyDataAccounts] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The database accounts.
        self.accounts = accounts
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeAccountsResponseBodyDataAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeAccountsResponseBodyData = None,
        request_id: str = None,
    ):
        # The result returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeAccountsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        backup_size: str = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        request_id: str = None,
        switch: str = None,
    ):
        self.backup_retention_period = backup_retention_period
        self.backup_size = backup_size
        self.preferred_backup_period = preferred_backup_period
        self.preferred_backup_time = preferred_backup_time
        self.request_id = request_id
        self.switch = switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.switch is not None:
            result['Switch'] = self.switch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        dbinstance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.backup_id = backup_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupsResponseBodyItems(TeaModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_method: str = None,
        backup_set_info: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        dbinstance_id: str = None,
        expire_date: str = None,
    ):
        self.backup_end_time = backup_end_time
        self.backup_id = backup_id
        self.backup_method = backup_method
        self.backup_set_info = backup_set_info
        self.backup_size = backup_size
        self.backup_start_time = backup_start_time
        self.backup_status = backup_status
        self.backup_type = backup_type
        self.dbinstance_id = dbinstance_id
        self.expire_date = expire_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_set_info is not None:
            result['BackupSetInfo'] = self.backup_set_info
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupSetInfo') is not None:
            self.backup_set_info = m.get('BackupSetInfo')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeBackupsResponseBodyItems] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        # 
        # Valid values:
        # 
        # *   cn-beijing
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceAttributeResponseBodyDataMultiZones(TeaModel):
    def __init__(
        self,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBodyDataNodes(TeaModel):
    def __init__(
        self,
        node_status: str = None,
        zone_id: str = None,
    ):
        # The node status.
        self.node_status = node_status
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstanceAttributeResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        bid: str = None,
        category: str = None,
        charge_type: str = None,
        click_observe_service_status: str = None,
        create_time: str = None,
        dbinstance_id: str = None,
        deletion_protection: bool = None,
        deploy_schema: str = None,
        description: str = None,
        disabled_ports: str = None,
        engine: str = None,
        engine_minor_version: str = None,
        engine_version: str = None,
        expire_time: str = None,
        latest_engine_minor_version: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        multi_zones: List[DescribeDBInstanceAttributeResponseBodyDataMultiZones] = None,
        node_count: str = None,
        node_scale_max: str = None,
        node_scale_min: str = None,
        nodes: List[DescribeDBInstanceAttributeResponseBodyDataNodes] = None,
        object_store_size: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        scale_max: int = None,
        scale_min: int = None,
        status: str = None,
        storage_quota: str = None,
        storage_size: int = None,
        storage_type: str = None,
        tags: List[DescribeDBInstanceAttributeResponseBodyDataTags] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The channel ID.
        self.bid = bid
        self.category = category
        # The billing method. Enterprise Edition clusters use the pay-as-you-go billing method.
        self.charge_type = charge_type
        self.click_observe_service_status = click_observe_service_status
        # The time when the cluster was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.create_time = create_time
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # Indicates whether the release protection feature is enabled for the cluster.
        self.deletion_protection = deletion_protection
        # The deployment mode of the cluster. Valid values: single_az and multi_az.
        # 
        # *   single_az: indicates that the server nodes are deployed in the primary zone. The ID of the primary zone is specified by the ZoneID parameter.
        # *   multi_az: indicates that the server nodes are deployed in multiple zones. The information about the zones is specified by the MultiZones parameter.
        # 
        # The keeper nodes are deployed in multiple zones.
        self.deploy_schema = deploy_schema
        # The cluster description.
        self.description = description
        # The disabled database ports. Multiple database ports are separated by commas (,).
        self.disabled_ports = disabled_ports
        # The engine type.
        self.engine = engine
        # The minor engine version of the cluster.
        self.engine_minor_version = engine_minor_version
        # The engine version.
        self.engine_version = engine_version
        # The time when the cluster expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # >  Pay-as-you-go clusters never expire. If the cluster is a pay-as-you-go cluster, an empty string is returned for this parameter.
        self.expire_time = expire_time
        # The latest minor engine version.
        self.latest_engine_minor_version = latest_engine_minor_version
        # The lock mode of the cluster.
        self.lock_mode = lock_mode
        # The reason why the cluster was locked.
        self.lock_reason = lock_reason
        # The end time of the maintenance window.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window.
        self.maintain_start_time = maintain_start_time
        # The information about the zones.
        self.multi_zones = multi_zones
        self.node_count = node_count
        self.node_scale_max = node_scale_max
        self.node_scale_min = node_scale_min
        # The nodes.
        self.nodes = nodes
        # The size of the object storage space.
        self.object_store_size = object_store_size
        # The region ID.
        self.region_id = region_id
        # The resource ID.
        self.resource_group_id = resource_group_id
        # The maximum capacity for elastic scaling.
        self.scale_max = scale_max
        # The minimum capacity for elastic scaling.
        self.scale_min = scale_min
        # The cluster status.
        self.status = status
        self.storage_quota = storage_quota
        # The size of the storage space. Unit: GB.
        self.storage_size = storage_size
        # The storage type.
        self.storage_type = storage_type
        # The details of the tags.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.multi_zones:
            for k in self.multi_zones:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.category is not None:
            result['Category'] = self.category
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.click_observe_service_status is not None:
            result['ClickObserveServiceStatus'] = self.click_observe_service_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.deploy_schema is not None:
            result['DeploySchema'] = self.deploy_schema
        if self.description is not None:
            result['Description'] = self.description
        if self.disabled_ports is not None:
            result['DisabledPorts'] = self.disabled_ports
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_minor_version is not None:
            result['EngineMinorVersion'] = self.engine_minor_version
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.latest_engine_minor_version is not None:
            result['LatestEngineMinorVersion'] = self.latest_engine_minor_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        result['MultiZones'] = []
        if self.multi_zones is not None:
            for k in self.multi_zones:
                result['MultiZones'].append(k.to_map() if k else None)
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_scale_max is not None:
            result['NodeScaleMax'] = self.node_scale_max
        if self.node_scale_min is not None:
            result['NodeScaleMin'] = self.node_scale_min
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.object_store_size is not None:
            result['ObjectStoreSize'] = self.object_store_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max
        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_quota is not None:
            result['StorageQuota'] = self.storage_quota
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClickObserveServiceStatus') is not None:
            self.click_observe_service_status = m.get('ClickObserveServiceStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('DeploySchema') is not None:
            self.deploy_schema = m.get('DeploySchema')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisabledPorts') is not None:
            self.disabled_ports = m.get('DisabledPorts')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineMinorVersion') is not None:
            self.engine_minor_version = m.get('EngineMinorVersion')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LatestEngineMinorVersion') is not None:
            self.latest_engine_minor_version = m.get('LatestEngineMinorVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        self.multi_zones = []
        if m.get('MultiZones') is not None:
            for k in m.get('MultiZones'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDataMultiZones()
                self.multi_zones.append(temp_model.from_map(k))
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeScaleMax') is not None:
            self.node_scale_max = m.get('NodeScaleMax')
        if m.get('NodeScaleMin') is not None:
            self.node_scale_min = m.get('NodeScaleMin')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('ObjectStoreSize') is not None:
            self.object_store_size = m.get('ObjectStoreSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')
        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageQuota') is not None:
            self.storage_quota = m.get('StorageQuota')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceAttributeResponseBodyData = None,
        request_id: str = None,
    ):
        # The result returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceConfigResponseBodyDataParams(TeaModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        is_dynamic: int = None,
        is_user_modifiable: int = None,
        name: str = None,
        optional: str = None,
        param_rely_rule: str = None,
        value: str = None,
    ):
        self.comment = comment
        self.default_value = default_value
        self.is_dynamic = is_dynamic
        self.is_user_modifiable = is_user_modifiable
        self.name = name
        self.optional = optional
        self.param_rely_rule = param_rely_rule
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.is_dynamic is not None:
            result['IsDynamic'] = self.is_dynamic
        if self.is_user_modifiable is not None:
            result['IsUserModifiable'] = self.is_user_modifiable
        if self.name is not None:
            result['Name'] = self.name
        if self.optional is not None:
            result['Optional'] = self.optional
        if self.param_rely_rule is not None:
            result['ParamRelyRule'] = self.param_rely_rule
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('IsDynamic') is not None:
            self.is_dynamic = m.get('IsDynamic')
        if m.get('IsUserModifiable') is not None:
            self.is_user_modifiable = m.get('IsUserModifiable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Optional') is not None:
            self.optional = m.get('Optional')
        if m.get('ParamRelyRule') is not None:
            self.param_rely_rule = m.get('ParamRelyRule')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstanceConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        params: List[DescribeDBInstanceConfigResponseBodyDataParams] = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.params = params

    def validate(self):
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = DescribeDBInstanceConfigResponseBodyDataParams()
                self.params.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceConfigChangeLogRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstanceConfigChangeLogResponseBodyDataParamChangeLogs(TeaModel):
    def __init__(
        self,
        applied: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        new_value: str = None,
        old_value: str = None,
    ):
        self.applied = applied
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.new_value = new_value
        self.old_value = old_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['ID'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        return self


class DescribeDBInstanceConfigChangeLogResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        param_change_logs: List[DescribeDBInstanceConfigChangeLogResponseBodyDataParamChangeLogs] = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.param_change_logs = param_change_logs

    def validate(self):
        if self.param_change_logs:
            for k in self.param_change_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        result['ParamChangeLogs'] = []
        if self.param_change_logs is not None:
            for k in self.param_change_logs:
                result['ParamChangeLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        self.param_change_logs = []
        if m.get('ParamChangeLogs') is not None:
            for k in m.get('ParamChangeLogs'):
                temp_model = DescribeDBInstanceConfigChangeLogResponseBodyDataParamChangeLogs()
                self.param_change_logs.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceConfigChangeLogResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceConfigChangeLogResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceConfigChangeLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceConfigChangeLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceConfigChangeLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceConfigChangeLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceDataSourcesRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
        region_id: str = None,
        table_name: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database name.
        self.dbname = dbname
        # The region ID.
        self.region_id = region_id
        # The table name.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeDBInstanceDataSourcesResponseBodyDataColumns(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        comment: str = None,
        dbname: str = None,
        primary_key: str = None,
        table_name: str = None,
        type: str = None,
    ):
        # The column name.
        self.column_name = column_name
        # The description of the database account.
        self.comment = comment
        # The database name.
        self.dbname = dbname
        # Indicates whether the column is the primary key of the table. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.primary_key = primary_key
        # The table name.
        self.table_name = table_name
        # The type of the stored data.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDBInstanceDataSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        columns: List[DescribeDBInstanceDataSourcesResponseBodyDataColumns] = None,
        dbinstance_id: str = None,
        schemas: str = None,
        tables: List[str] = None,
    ):
        # The columns.
        self.columns = columns
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The account.
        self.schemas = schemas
        # The tables.
        self.tables = tables

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.schemas is not None:
            result['Schemas'] = self.schemas
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = DescribeDBInstanceDataSourcesResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Schemas') is not None:
            self.schemas = m.get('Schemas')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class DescribeDBInstanceDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceDataSourcesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceDataSourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceDataSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequest(TeaModel):
    def __init__(
        self,
        dbinstance_ids: str = None,
        dbinstance_status: str = None,
        description: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The cluster IDs. Separate multiple cluster IDs with commas (,).
        self.dbinstance_ids = dbinstance_ids
        # The cluster status.
        self.dbinstance_status = dbinstance_status
        # The cluster description.
        self.description = description
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.description is not None:
            result['Description'] = self.description
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBInstancesResponseBodyDataDBInstancesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstancesResponseBodyDataDBInstances(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        bid: str = None,
        charge_type: str = None,
        create_time: str = None,
        dbinstance_id: str = None,
        deletion_protection: str = None,
        description: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        scale_max: int = None,
        scale_min: int = None,
        status: str = None,
        storage_type: str = None,
        tags: List[DescribeDBInstancesResponseBodyDataDBInstancesTags] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
        # The channel ID.
        self.bid = bid
        # The billing method. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        self.charge_type = charge_type
        # The time when the cluster was created.
        self.create_time = create_time
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # Indicates whether the release protection feature is enabled for the cluster.
        self.deletion_protection = deletion_protection
        # The cluster description.
        self.description = description
        # The engine type.
        self.engine = engine
        # The engine version.
        self.engine_version = engine_version
        # The time when the cluster expires.
        self.expire_time = expire_time
        # The lock mode.
        self.lock_mode = lock_mode
        # The reason why the cluster was locked.
        self.lock_reason = lock_reason
        # The end time of the maintenance window.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window.
        self.maintain_start_time = maintain_start_time
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The maximum capacity for elastic scaling.
        self.scale_max = scale_max
        # The minimum capacity for elastic scaling.
        self.scale_min = scale_min
        # The cluster status.
        self.status = status
        self.storage_type = storage_type
        # The tags.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max
        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')
        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDBInstancesResponseBodyDataDBInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstances: List[DescribeDBInstancesResponseBodyDataDBInstances] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: str = None,
    ):
        # The clusters.
        self.dbinstances = dbinstances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dbinstances:
            for k in self.dbinstances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k in self.dbinstances:
                result['DBInstances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k in m.get('DBInstances'):
                temp_model = DescribeDBInstancesResponseBodyDataDBInstances()
                self.dbinstances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstancesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEndpointsResponseBodyDataEndpointsPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port used to connect to the cluster. Valid values:
        # 
        # *   8123: This value is returned when the value of Protocol is HttpPort.
        # *   8443: This value is returned when the value of Protocol is HttpsPort.
        # *   9000: This value is returned when the value of Protocol is TcpPort.
        self.port = port
        # The protocol type. Valid values:
        # 
        # *   HttpPort
        # *   HttpsPort
        # *   TcpPort
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeEndpointsResponseBodyDataEndpoints(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        connection_string: str = None,
        ipaddress: str = None,
        net_type: str = None,
        ports: List[DescribeEndpointsResponseBodyDataEndpointsPorts] = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The endpoint of the cluster.
        self.connection_string = connection_string
        # The IP address.
        self.ipaddress = ipaddress
        # The network type of the endpoint. Valid values:
        # 
        # *   VPC
        # *   PUBLIC
        self.net_type = net_type
        # The details of the ports.
        self.ports = ports
        # The state of the cluster.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The VPC ID.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.net_type is not None:
            result['NetType'] = self.net_type
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeEndpointsResponseBodyDataEndpointsPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class DescribeEndpointsResponseBodyData(TeaModel):
    def __init__(
        self,
        endpoints: List[DescribeEndpointsResponseBodyDataEndpoints] = None,
        instance_network_type: str = None,
    ):
        # The details of the endpoints.
        self.endpoints = endpoints
        # The network type of the cluster. Valid values:
        # 
        # *   **VPC**\
        # *   **PUBLIC**\
        self.instance_network_type = instance_network_type

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = DescribeEndpointsResponseBodyDataEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        return self


class DescribeEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeEndpointsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeEndpointsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProcessListRequest(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        query_duration_ms: str = None,
        query_order: int = None,
        region_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The query ID.
        self.initial_query_id = initial_query_id
        # The user who executes the query statement.
        self.initial_user = initial_user
        # The keyword of the query statement.
        self.keyword = keyword
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The execution duration of slow SQL queries. Minimum value: 1000. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # Specifies the columns by which the query results are sorted in descending order.
        # 
        # *   0: The query results are sorted by the query_duration_ms column.
        # *   1: The query results are sorted by the query_duration_ms and query_start_time columns.
        # *   2: The query results are sorted by the query_duration_ms, query_start_time, and user columns.
        self.query_order = query_order
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.query_order is not None:
            result['QueryOrder'] = self.query_order
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('QueryOrder') is not None:
            self.query_order = m.get('QueryOrder')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeProcessListResponseBodyDataResultSet(TeaModel):
    def __init__(
        self,
        initial_address: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        query: str = None,
        query_duration_ms: int = None,
        query_start_time: str = None,
    ):
        # The address to which the query statement is sent.
        self.initial_address = initial_address
        # The query ID.
        self.initial_query_id = initial_query_id
        # The user who executes the query statement.
        self.initial_user = initial_user
        # The query statement that is running.
        self.query = query
        # The minimum query duration. Minimum value: **1000**. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # The beginning of the time range to query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.query_start_time = query_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_address is not None:
            result['InitialAddress'] = self.initial_address
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user
        if self.query is not None:
            result['Query'] = self.query
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        return self


class DescribeProcessListResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        result_set: List[DescribeProcessListResponseBodyDataResultSet] = None,
        total_count: int = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The result sets.
        self.result_set = result_set
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeProcessListResponseBodyDataResultSet()
                self.result_set.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProcessListResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeProcessListResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeProcessListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProcessListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProcessListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProcessListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIPListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSecurityIPListResponseBodyDataGroupItems(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        group_tag: str = None,
        security_iplist: str = None,
        security_iptype: str = None,
        whitelist_net_type: str = None,
    ):
        # The name of the whitelist.
        self.group_name = group_name
        # The tag of the whitelist.
        self.group_tag = group_tag
        # The IP addresses and CIDR blocks in the whitelist.
        self.security_iplist = security_iplist
        # The IP address type.
        self.security_iptype = security_iptype
        # The network type of the whitelist.
        self.whitelist_net_type = whitelist_net_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype
        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')
        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')
        return self


class DescribeSecurityIPListResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        group_items: List[DescribeSecurityIPListResponseBodyDataGroupItems] = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The details about the whitelists.
        self.group_items = group_items

    def validate(self):
        if self.group_items:
            for k in self.group_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['GroupItems'] = []
        if self.group_items is not None:
            for k in self.group_items:
                result['GroupItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.group_items = []
        if m.get('GroupItems') is not None:
            for k in m.get('GroupItems'):
                temp_model = DescribeSecurityIPListResponseBodyDataGroupItems()
                self.group_items.append(temp_model.from_map(k))
        return self


class DescribeSecurityIPListResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeSecurityIPListResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeSecurityIPListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSecurityIPListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecurityIPListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSecurityIPListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        query_duration_ms: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. Specify the time in the yyyy-MM-dd hh:mm:ss format. The time must be in UTC.
        self.end_time = end_time
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   30 (default)
        # *   50
        # *   100
        self.page_size = page_size
        # The execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # The region ID.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd hh:mm:ss format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogRecordsResponseBodyDataResultSet(TeaModel):
    def __init__(
        self,
        initial_address: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        memory_usage: int = None,
        query: str = None,
        query_duration_ms: int = None,
        query_start_time: str = None,
        read_bytes: int = None,
        read_rows: int = None,
        result_bytes: int = None,
        type: str = None,
    ):
        # The address to which the query statement is sent.
        self.initial_address = initial_address
        # The query ID.
        self.initial_query_id = initial_query_id
        # The user who executes the query statement.
        self.initial_user = initial_user
        # The peak memory usage for the query. Unit: bytes.
        self.memory_usage = memory_usage
        # The query statement that is running.
        self.query = query
        # The execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # The beginning of the time range to query. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.query_start_time = query_start_time
        # The size of the data that is scanned. Unit: bytes.
        self.read_bytes = read_bytes
        # The number of read rows.
        self.read_rows = read_rows
        # The size of the result data. Unit: bytes.
        self.result_bytes = result_bytes
        # The type of the slow query logs.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_address is not None:
            result['InitialAddress'] = self.initial_address
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user
        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage
        if self.query is not None:
            result['Query'] = self.query
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes
        if self.read_rows is not None:
            result['ReadRows'] = self.read_rows
        if self.result_bytes is not None:
            result['ResultBytes'] = self.result_bytes
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')
        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')
        if m.get('ReadRows') is not None:
            self.read_rows = m.get('ReadRows')
        if m.get('ResultBytes') is not None:
            self.result_bytes = m.get('ResultBytes')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSlowLogRecordsResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        result_set: List[DescribeSlowLogRecordsResponseBodyDataResultSet] = None,
        total_count: int = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The result sets.
        self.result_set = result_set
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeSlowLogRecordsResponseBodyDataResultSet()
                self.result_set.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSlowLogRecordsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeSlowLogRecordsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSlowLogRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlowLogRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlowLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogTrendRequest(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        end_time: str = None,
        product: str = None,
        query_duration_ms: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. Specify the time in the yyyy-MM-dd hh:mm:ss format. The time must be in UTC.
        self.end_time = end_time
        # The code of the cloud service.
        self.product = product
        # The execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # The region ID.
        self.region_id = region_id
        # The start of the time range to query. Specify the time in the yyyy-MM-dd hh:mm:ss format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.product is not None:
            result['Product'] = self.product
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogTrendResponseBodyDataResultSet(TeaModel):
    def __init__(
        self,
        avg_query_duration_ms: int = None,
        cnt: int = None,
        max_query_duration_ms: int = None,
        min_query_duration_ms: int = None,
        query_start_time: str = None,
    ):
        # The average execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.avg_query_duration_ms = avg_query_duration_ms
        # The total number of SQL queries within the specified time range.
        self.cnt = cnt
        # The maximum execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.max_query_duration_ms = max_query_duration_ms
        # The minimum execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.min_query_duration_ms = min_query_duration_ms
        # The beginning of the time range to query. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.query_start_time = query_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_query_duration_ms is not None:
            result['AvgQueryDurationMs'] = self.avg_query_duration_ms
        if self.cnt is not None:
            result['Cnt'] = self.cnt
        if self.max_query_duration_ms is not None:
            result['MaxQueryDurationMs'] = self.max_query_duration_ms
        if self.min_query_duration_ms is not None:
            result['MinQueryDurationMs'] = self.min_query_duration_ms
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgQueryDurationMs') is not None:
            self.avg_query_duration_ms = m.get('AvgQueryDurationMs')
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')
        if m.get('MaxQueryDurationMs') is not None:
            self.max_query_duration_ms = m.get('MaxQueryDurationMs')
        if m.get('MinQueryDurationMs') is not None:
            self.min_query_duration_ms = m.get('MinQueryDurationMs')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        return self


class DescribeSlowLogTrendResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        result_set: List[DescribeSlowLogTrendResponseBodyDataResultSet] = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The result sets.
        self.result_set = result_set

    def validate(self):
        if self.result_set:
            for k in self.result_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['ResultSet'] = []
        if self.result_set is not None:
            for k in self.result_set:
                result['ResultSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k in m.get('ResultSet'):
                temp_model = DescribeSlowLogTrendResponseBodyDataResultSet()
                self.result_set.append(temp_model.from_map(k))
        return self


class DescribeSlowLogTrendResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeSlowLogTrendResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeSlowLogTrendResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSlowLogTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlowLogTrendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlowLogTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillProcessRequest(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        initial_query_id: str = None,
        region_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The query ID.
        self.initial_query_id = initial_query_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class KillProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
    ):
        # The number of queries that are terminated.
        self.count = count
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class KillProcessResponseBody(TeaModel):
    def __init__(
        self,
        data: KillProcessResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = KillProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillProcessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = KillProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountAuthorityRequestDmlAuthSetting(TeaModel):
    def __init__(
        self,
        allow_databases: List[str] = None,
        allow_dictionaries: List[str] = None,
        ddl_authority: bool = None,
        dml_authority: int = None,
    ):
        # The databases on which you want to grant permissions. Separate multiple databases with commas (,).
        self.allow_databases = allow_databases
        # The dictionaries on which you want to grant permissions. Separate multiple dictionaries with commas (,).
        self.allow_dictionaries = allow_dictionaries
        # Specifies whether to grant the DDL permissions to the database account. Valid values:
        # 
        # *   **true**: The account has the permissions to execute DDL statements.
        # *   **false**: The account does not have the permissions to execute DDL statements.
        # 
        # This parameter is required.
        self.ddl_authority = ddl_authority
        # Specifies whether to grant the DML permissions to the database account. Valid values:
        # 
        # *   **0**: The account has the permissions to read data from the database, write data to the database, and modify the settings of the database.
        # *   **1**: The account only has the permissions to read data from the database.
        # *   **2**: The account only has the permissions to read data from the database and modify the settings of the database.
        # 
        # This parameter is required.
        self.dml_authority = dml_authority

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases
        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries
        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority
        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')
        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')
        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')
        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')
        return self


class ModifyAccountAuthorityRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
        dml_auth_setting: ModifyAccountAuthorityRequestDmlAuthSetting = None,
        region_id: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account = account
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The information about permissions.
        # 
        # This parameter is required.
        self.dml_auth_setting = dml_auth_setting
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.dml_auth_setting:
            self.dml_auth_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dml_auth_setting is not None:
            result['DmlAuthSetting'] = self.dml_auth_setting.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DmlAuthSetting') is not None:
            temp_model = ModifyAccountAuthorityRequestDmlAuthSetting()
            self.dml_auth_setting = temp_model.from_map(m['DmlAuthSetting'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyAccountAuthorityShrinkRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
        dml_auth_setting_shrink: str = None,
        region_id: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account = account
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The information about permissions.
        # 
        # This parameter is required.
        self.dml_auth_setting_shrink = dml_auth_setting_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dml_auth_setting_shrink is not None:
            result['DmlAuthSetting'] = self.dml_auth_setting_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DmlAuthSetting') is not None:
            self.dml_auth_setting_shrink = m.get('DmlAuthSetting')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyAccountAuthorityResponseBodyData(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
    ):
        # The name of the database account.
        self.account = account
        # The cluster ID.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ModifyAccountAuthorityResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyAccountAuthorityResponseBodyData = None,
        request_id: str = None,
    ):
        # The result returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyAccountAuthorityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccountAuthorityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccountAuthorityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccountAuthorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
        description: str = None,
        region_id: str = None,
    ):
        # The name of the account.
        # 
        # This parameter is required.
        self.account = account
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The description of the account.
        # 
        # This parameter is required.
        self.description = description
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyAccountDescriptionResponseBodyData(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
    ):
        # The name of the database account.
        self.account = account
        # The cluster ID.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyAccountDescriptionResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyAccountDescriptionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccountDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        backup_retention_period: str = None,
        dbinstance_id: str = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        region_id: str = None,
    ):
        self.backup_retention_period = backup_retention_period
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.preferred_backup_period = preferred_backup_period
        # This parameter is required.
        self.preferred_backup_time = preferred_backup_time
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBackupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        attribute_type: str = None,
        attribute_value: str = None,
        dbinstance_id: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The configuration that you want to modify.
        # 
        # *   MaintainTime: the O\\&M time
        # *   DBInstanceDescription: the cluster name
        # 
        # This parameter is required.
        self.attribute_type = attribute_type
        # The new value of the configuration.
        # 
        # This parameter is required.
        self.attribute_value = attribute_value
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The code of the cloud service.
        self.product = product
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDBInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceClassRequest(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        node_count: int = None,
        node_scale_max: int = None,
        node_scale_min: int = None,
        region_id: str = None,
        scale_max: int = None,
        scale_min: int = None,
        storage_quota: int = None,
        storage_type: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.node_count = node_count
        self.node_scale_max = node_scale_max
        self.node_scale_min = node_scale_min
        # The region ID.
        self.region_id = region_id
        # The maximum capacity for elastic scaling.
        self.scale_max = scale_max
        # The minimum capacity for elastic scaling.
        self.scale_min = scale_min
        self.storage_quota = storage_quota
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_scale_max is not None:
            result['NodeScaleMax'] = self.node_scale_max
        if self.node_scale_min is not None:
            result['NodeScaleMin'] = self.node_scale_min
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max
        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min
        if self.storage_quota is not None:
            result['StorageQuota'] = self.storage_quota
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeScaleMax') is not None:
            self.node_scale_max = m.get('NodeScaleMax')
        if m.get('NodeScaleMin') is not None:
            self.node_scale_min = m.get('NodeScaleMin')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')
        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')
        if m.get('StorageQuota') is not None:
            self.storage_quota = m.get('StorageQuota')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class ModifyDBInstanceClassResponseBodyData(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        scale_max: int = None,
        scale_min: int = None,
        task_id: int = None,
    ):
        self.computing_group_id = computing_group_id
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The maximum capacity for elastic scaling.
        self.scale_max = scale_max
        # The minimum capacity for elastic scaling.
        self.scale_min = scale_min
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max
        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')
        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyDBInstanceClassResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyDBInstanceClassResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyDBInstanceClassResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceClassResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        parameters: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.parameters = parameters
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDBInstanceConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ModifyDBInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyDBInstanceConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyDBInstanceConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(
        self,
        computing_group_id: str = None,
        connection_string: str = None,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        dbinstance_net_type: str = None,
        disable_ports: str = None,
        region_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The endpoint of the cluster.
        self.connection_string = connection_string
        # The prefix of the endpoint that is used to connect to the database.
        self.connection_string_prefix = connection_string_prefix
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.dbinstance_net_type = dbinstance_net_type
        # *   The database ports that you want to disable. Separate multiple ports with commas (,).
        # 
        # *   This parameter is supported only for clusters whose minor engine version is 24.10.1.11098_1 or later.
        # 
        #     **\
        # 
        #     **Note** If you create a cluster whose minor engine version is earlier than 24.10.1.11098_1 and you update the minor engine version to 24.10.1.11098_1 or later, the cluster still does not support this parameter.
        self.disable_ports = disable_ports
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.disable_ports is not None:
            result['DisablePorts'] = self.disable_ports
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('DisablePorts') is not None:
            self.disable_ports = m.get('DisablePorts')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDBInstanceConnectionStringResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        disabled_ports: str = None,
    ):
        # The endpoint of the cluster.
        self.connection_string = connection_string
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The disabled database ports.
        self.disabled_ports = disabled_ports

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.disabled_ports is not None:
            result['DisabledPorts'] = self.disabled_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DisabledPorts') is not None:
            self.disabled_ports = m.get('DisabledPorts')
        return self


class ModifyDBInstanceConnectionStringResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyDBInstanceConnectionStringResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyDBInstanceConnectionStringResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceConnectionStringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceConnectionStringResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIPListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        group_name: str = None,
        modify_mode: str = None,
        region_id: str = None,
        security_iplist: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the whitelist whose settings you want to modify.
        self.group_name = group_name
        # The modification mode.
        # 
        # *   0: overwrites the original IP addresses and CIDR blocks in the whitelist.
        # *   1: adds the IP addresses and CIDR blocks to the whitelist.
        # *   2: removes the IP addresses and CIDR blocks from the whitelist.
        # 
        # >  We recommend that you set the value to 0.
        self.modify_mode = modify_mode
        # The region ID.
        self.region_id = region_id
        # The IP addresses and CIDR blocks in the whitelist.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class ModifySecurityIPListResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        group_name: str = None,
        group_tag: str = None,
        security_iplist: str = None,
        security_iptype: str = None,
        task_id: int = None,
        whitelist_net_type: str = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The name of the whitelist.
        self.group_name = group_name
        # The tag of the whitelist.
        self.group_tag = group_tag
        # The IP addresses and CIDR blocks in the whitelist.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag
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
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')
        return self


class ModifySecurityIPListResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifySecurityIPListResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifySecurityIPListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySecurityIPListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySecurityIPListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySecurityIPListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
        password: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account = account
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The password of the database account. The password must meet the following requirements:
        # 
        # - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - The following special characters are supported: ! @ # $ % ^ & * ( ) _ + - =\
        # - The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.password = password
        # The service name.
        self.product = product
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetAccountPasswordResponseBodyData(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
    ):
        # The name of the account.
        self.account = account
        # The cluster ID.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(
        self,
        data: ResetAccountPasswordResponseBodyData = None,
        request_id: str = None,
    ):
        # The result returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ResetAccountPasswordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAccountPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RestartDBInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        task_id: int = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RestartDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: RestartDBInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RestartDBInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDBInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartDBInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        task_id: int = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: StartDBInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StartDBInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDBInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopDBInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        task_id: int = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: StopDBInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StopDBInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMinorVersionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_minor_version: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id
        # The update time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  If you set SwitchTimeMode to SpecifyTime, you must configure this parameter to specify the update time.
        self.switch_time = switch_time
        # Specifies whether to update the minor engine version of the cluster immediately. Valid values:
        # 
        # *   **Immediate**: The system immediately performs the update.
        # *   **MaintainTime**: The system performs the update during the specified maintenance window.
        # *   **SpecifyTime**: The system performs the update at a specified time.
        self.switch_time_mode = switch_time_mode
        # The minor engine version to which you want to update.
        # 
        # >  By default, TargetMinorVersion is not set and the minor engine version of the cluster is updated to the latest version.
        self.target_minor_version = target_minor_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')
        return self


class UpgradeMinorVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
    ):
        # The instance ID.
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class UpgradeMinorVersionResponseBody(TeaModel):
    def __init__(
        self,
        data: UpgradeMinorVersionResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpgradeMinorVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeMinorVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeMinorVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeMinorVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


