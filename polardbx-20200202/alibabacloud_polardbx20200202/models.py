# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dbinstance_name: str = None,
        connection_string_prefix: str = None,
        port: str = None,
        owner_account: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dbinstance_name = dbinstance_name
        self.connection_string_prefix = connection_string_prefix
        self.port = port
        self.owner_account = owner_account
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.port is not None:
            result['Port'] = self.port
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
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


class AllocateInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AllocateInstancePublicConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AllocateInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPolarxOrderRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        scale_out_token: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.scale_out_token = scale_out_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.scale_out_token is not None:
            result['ScaleOutToken'] = self.scale_out_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('ScaleOutToken') is not None:
            self.scale_out_token = m.get('ScaleOutToken')
        return self


class CancelPolarxOrderResponseBody(TeaModel):
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


class CancelPolarxOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelPolarxOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelPolarxOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        account_name: str = None,
        account_password: str = None,
        dbname: str = None,
        account_privilege: str = None,
        account_description: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.account_name = account_name
        self.account_password = account_password
        self.dbname = dbname
        self.account_privilege = account_privilege
        self.account_description = account_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        backup_type: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.backup_type = backup_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        return self


class CreateBackupResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_set_id: int = None,
    ):
        self.backup_set_id = backup_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        return self


class CreateBackupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[CreateBackupResponseBodyData] = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = CreateBackupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBackupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        account_name: str = None,
        charset: str = None,
        db_name: str = None,
        account_privilege: str = None,
        db_description: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.account_name = account_name
        self.charset = charset
        self.db_name = db_name
        self.account_privilege = account_privilege
        self.db_description = db_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        return self


class CreateDBResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDBResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        pay_type: str = None,
        dbnode_count: int = None,
        dbnode_class: str = None,
        zone_id: str = None,
        client_token: str = None,
        network_type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        used_time: int = None,
        period: str = None,
        resource_group_id: str = None,
        auto_renew: bool = None,
        engine_version: str = None,
        is_read_dbinstance: bool = None,
        primary_dbinstance_name: str = None,
    ):
        self.region_id = region_id
        self.pay_type = pay_type
        self.dbnode_count = dbnode_count
        self.dbnode_class = dbnode_class
        self.zone_id = zone_id
        self.client_token = client_token
        self.network_type = network_type
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.used_time = used_time
        self.period = period
        self.resource_group_id = resource_group_id
        self.auto_renew = auto_renew
        self.engine_version = engine_version
        self.is_read_dbinstance = is_read_dbinstance
        self.primary_dbinstance_name = primary_dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.period is not None:
            result['Period'] = self.period
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.is_read_dbinstance is not None:
            result['IsReadDBInstance'] = self.is_read_dbinstance
        if self.primary_dbinstance_name is not None:
            result['PrimaryDBInstanceName'] = self.primary_dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('IsReadDBInstance') is not None:
            self.is_read_dbinstance = m.get('IsReadDBInstance')
        if m.get('PrimaryDBInstanceName') is not None:
            self.primary_dbinstance_name = m.get('PrimaryDBInstanceName')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
        dbinstance_name: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolarxInstanceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        region_id: str = None,
        zone_id: str = None,
        type: str = None,
        quantity: int = None,
        instance_series: str = None,
        specification: str = None,
        client_token: str = None,
        pay_type: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        is_ha: bool = None,
        pricing_cycle: str = None,
        duration: int = None,
        is_auto_renew: bool = None,
        master_inst_id: str = None,
        my_sqlversion: int = None,
    ):
        self.description = description
        self.region_id = region_id
        self.zone_id = zone_id
        self.type = type
        self.quantity = quantity
        self.instance_series = instance_series
        self.specification = specification
        self.client_token = client_token
        self.pay_type = pay_type
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.is_ha = is_ha
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.is_auto_renew = is_auto_renew
        self.master_inst_id = master_inst_id
        self.my_sqlversion = my_sqlversion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.type is not None:
            result['Type'] = self.type
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.instance_series is not None:
            result['InstanceSeries'] = self.instance_series
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.is_ha is not None:
            result['isHa'] = self.is_ha
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        if self.master_inst_id is not None:
            result['MasterInstId'] = self.master_inst_id
        if self.my_sqlversion is not None:
            result['MySQLVersion'] = self.my_sqlversion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('InstanceSeries') is not None:
            self.instance_series = m.get('InstanceSeries')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('isHa') is not None:
            self.is_ha = m.get('isHa')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('IsAutoRenew') is not None:
            self.is_auto_renew = m.get('IsAutoRenew')
        if m.get('MasterInstId') is not None:
            self.master_inst_id = m.get('MasterInstId')
        if m.get('MySQLVersion') is not None:
            self.my_sqlversion = m.get('MySQLVersion')
        return self


class CreatePolarxInstanceResponseBodyDataDrdsInstanceIdList(TeaModel):
    def __init__(
        self,
        drds_instance_id_list: List[str] = None,
    ):
        self.drds_instance_id_list = drds_instance_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id_list is not None:
            result['drdsInstanceIdList'] = self.drds_instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drdsInstanceIdList') is not None:
            self.drds_instance_id_list = m.get('drdsInstanceIdList')
        return self


class CreatePolarxInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        drds_instance_id_list: CreatePolarxInstanceResponseBodyDataDrdsInstanceIdList = None,
        order_id: int = None,
    ):
        self.drds_instance_id_list = drds_instance_id_list
        self.order_id = order_id

    def validate(self):
        if self.drds_instance_id_list:
            self.drds_instance_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id_list is not None:
            result['DrdsInstanceIdList'] = self.drds_instance_id_list.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrdsInstanceIdList') is not None:
            temp_model = CreatePolarxInstanceResponseBodyDataDrdsInstanceIdList()
            self.drds_instance_id_list = temp_model.from_map(m['DrdsInstanceIdList'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreatePolarxInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: CreatePolarxInstanceResponseBodyData = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreatePolarxInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePolarxInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePolarxInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePolarxInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolarxOrderRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        node_count: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.node_count = node_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        return self


class CreatePolarxOrderResponseBodyOrderResultList(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        order_id: int = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreatePolarxOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_result_list: List[CreatePolarxOrderResponseBodyOrderResultList] = None,
    ):
        self.request_id = request_id
        self.order_result_list = order_result_list

    def validate(self):
        if self.order_result_list:
            for k in self.order_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OrderResultList'] = []
        if self.order_result_list is not None:
            for k in self.order_result_list:
                result['OrderResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.order_result_list = []
        if m.get('OrderResultList') is not None:
            for k in m.get('OrderResultList'):
                temp_model = CreatePolarxOrderResponseBodyOrderResultList()
                self.order_result_list.append(temp_model.from_map(k))
        return self


class CreatePolarxOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePolarxOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePolarxOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSuperAccountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        account_name: str = None,
        account_password: str = None,
        account_description: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.account_name = account_name
        self.account_password = account_password
        self.account_description = account_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        return self


class CreateSuperAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSuperAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSuperAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSuperAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        account_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.account_name = account_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        db_name: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.db_name = db_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        return self


class DeleteDBResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDBResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
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


class DeleteDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        account_name: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeAccountListResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        account_description: str = None,
        dbname: str = None,
        account_privilege: str = None,
        account_type: str = None,
        account_name: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.account_description = account_description
        self.dbname = dbname
        self.account_privilege = account_privilege
        self.account_type = account_type
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeAccountListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[DescribeAccountListResponseBodyData] = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAccountListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAccountListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccountListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAccountListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class DescribeBackupPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        log_local_retention_space: int = None,
        dbinstance_name: str = None,
        backup_way: str = None,
        backup_period: str = None,
        force_clean_on_high_space_usage: int = None,
        backup_type: str = None,
        local_log_retention: int = None,
        remove_log_retention: int = None,
        backup_plan_begin: str = None,
        backup_set_retention: int = None,
        is_enabled: int = None,
    ):
        self.log_local_retention_space = log_local_retention_space
        self.dbinstance_name = dbinstance_name
        self.backup_way = backup_way
        self.backup_period = backup_period
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage
        self.backup_type = backup_type
        self.local_log_retention = local_log_retention
        self.remove_log_retention = remove_log_retention
        self.backup_plan_begin = backup_plan_begin
        self.backup_set_retention = backup_set_retention
        self.is_enabled = is_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[DescribeBackupPolicyResponseBodyData] = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeBackupPolicyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupSetListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        start_time: int = None,
        end_time: int = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeBackupSetListResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        status: int = None,
        backup_set_size: int = None,
        backup_set_id: int = None,
        backup_type: int = None,
        begin_time: int = None,
        backup_model: int = None,
    ):
        self.end_time = end_time
        self.status = status
        self.backup_set_size = backup_set_size
        self.backup_set_id = backup_set_id
        self.backup_type = backup_type
        self.begin_time = begin_time
        self.backup_model = backup_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.backup_model is not None:
            result['BackupModel'] = self.backup_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('BackupModel') is not None:
            self.backup_model = m.get('BackupModel')
        return self


class DescribeBackupSetListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[DescribeBackupSetListResponseBodyData] = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeBackupSetListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBackupSetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupSetListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupSetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs(TeaModel):
    def __init__(
        self,
        type: str = None,
        v_switch_id: str = None,
        connection_string: str = None,
        port: str = None,
        vpcid: str = None,
    ):
        self.type = type
        self.v_switch_id = v_switch_id
        self.connection_string = connection_string
        self.port = port
        self.vpcid = vpcid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes(TeaModel):
    def __init__(
        self,
        node_class: str = None,
        zone_id: str = None,
        id: str = None,
        region_id: str = None,
    ):
        self.node_class = node_class
        self.zone_id = zone_id
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstance(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        dbnode_count: int = None,
        expired: str = None,
        create_time: str = None,
        pay_type: str = None,
        read_dbinstances: List[str] = None,
        port: str = None,
        lock_mode: str = None,
        conn_addrs: List[DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs] = None,
        description: str = None,
        connection_string: str = None,
        storage_used: int = None,
        expire_date: str = None,
        commodity_code: str = None,
        maintain_start_time: str = None,
        dbinstance_type: str = None,
        dbnode_class: str = None,
        maintain_end_time: str = None,
        latest_minor_version: str = None,
        dbtype: str = None,
        vpcid: str = None,
        minor_version: str = None,
        region_id: str = None,
        dbnodes: List[DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes] = None,
        network: str = None,
        dbversion: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        engine: str = None,
        id: str = None,
    ):
        self.type = type
        self.status = status
        self.dbnode_count = dbnode_count
        self.expired = expired
        self.create_time = create_time
        self.pay_type = pay_type
        self.read_dbinstances = read_dbinstances
        self.port = port
        self.lock_mode = lock_mode
        self.conn_addrs = conn_addrs
        self.description = description
        self.connection_string = connection_string
        self.storage_used = storage_used
        self.expire_date = expire_date
        self.commodity_code = commodity_code
        self.maintain_start_time = maintain_start_time
        self.dbinstance_type = dbinstance_type
        self.dbnode_class = dbnode_class
        self.maintain_end_time = maintain_end_time
        self.latest_minor_version = latest_minor_version
        self.dbtype = dbtype
        self.vpcid = vpcid
        self.minor_version = minor_version
        self.region_id = region_id
        self.dbnodes = dbnodes
        self.network = network
        self.dbversion = dbversion
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id
        self.engine = engine
        self.id = id

    def validate(self):
        if self.conn_addrs:
            for k in self.conn_addrs:
                if k:
                    k.validate()
        if self.dbnodes:
            for k in self.dbnodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.port is not None:
            result['Port'] = self.port
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k in self.conn_addrs:
                result['ConnAddrs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k in self.dbnodes:
                result['DBNodes'].append(k.to_map() if k else None)
        if self.network is not None:
            result['Network'] = self.network
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k in m.get('ConnAddrs'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k in m.get('DBNodes'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes()
                self.dbnodes.append(temp_model.from_map(k))
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dbinstance: DescribeDBInstanceAttributeResponseBodyDBInstance = None,
    ):
        self.request_id = request_id
        self.dbinstance = dbinstance

    def validate(self):
        if self.dbinstance:
            self.dbinstance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstance') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstance()
            self.dbinstance = temp_model.from_map(m['DBInstance'])
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDBInstancesResponseBodyDBInstancesNodes(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        id: str = None,
        class_code: str = None,
        region_id: str = None,
    ):
        self.zone_id = zone_id
        self.id = id
        self.class_code = class_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.id is not None:
            result['Id'] = self.id
        if self.class_code is not None:
            result['ClassCode'] = self.class_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstancesResponseBodyDBInstances(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        expired: bool = None,
        create_time: str = None,
        pay_type: str = None,
        read_dbinstances: List[str] = None,
        lock_mode: str = None,
        description: str = None,
        node_class: str = None,
        storage_used: int = None,
        nodes: List[DescribeDBInstancesResponseBodyDBInstancesNodes] = None,
        commodity_code: str = None,
        expire_time: str = None,
        lock_reason: str = None,
        dbtype: str = None,
        vpcid: str = None,
        minor_version: str = None,
        region_id: str = None,
        network: str = None,
        dbversion: str = None,
        node_count: int = None,
        zone_id: str = None,
        engine: str = None,
        id: str = None,
    ):
        self.status = status
        self.type = type
        self.expired = expired
        self.create_time = create_time
        self.pay_type = pay_type
        self.read_dbinstances = read_dbinstances
        self.lock_mode = lock_mode
        self.description = description
        self.node_class = node_class
        self.storage_used = storage_used
        self.nodes = nodes
        self.commodity_code = commodity_code
        self.expire_time = expire_time
        self.lock_reason = lock_reason
        self.dbtype = dbtype
        self.vpcid = vpcid
        self.minor_version = minor_version
        self.region_id = region_id
        self.network = network
        self.dbversion = dbversion
        self.node_count = node_count
        self.zone_id = zone_id
        self.engine = engine
        self.id = id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network is not None:
            result['Network'] = self.network
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeDBInstancesResponseBodyDBInstancesNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        total_number: int = None,
        dbinstances: List[DescribeDBInstancesResponseBodyDBInstances] = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.total_number = total_number
        self.dbinstances = dbinstances

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k in self.dbinstances:
                result['DBInstances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k in m.get('DBInstances'):
                temp_model = DescribeDBInstancesResponseBodyDBInstances()
                self.dbinstances.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        dbname: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.dbname = dbname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DescribeDbListResponseBodyDataAccounts(TeaModel):
    def __init__(
        self,
        account_privilege: str = None,
        account_name: str = None,
    ):
        self.account_privilege = account_privilege
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeDbListResponseBodyData(TeaModel):
    def __init__(
        self,
        dbdescription: str = None,
        dbinstance_name: str = None,
        dbname: str = None,
        character_set_name: str = None,
        accounts: List[DescribeDbListResponseBodyDataAccounts] = None,
    ):
        self.dbdescription = dbdescription
        self.dbinstance_name = dbinstance_name
        self.dbname = dbname
        self.character_set_name = character_set_name
        self.accounts = accounts

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
        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeDbListResponseBodyDataAccounts()
                self.accounts.append(temp_model.from_map(k))
        return self


class DescribeDbListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[DescribeDbListResponseBodyData] = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDbListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDbListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDbListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDbListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDistributeTableListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        db_name: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.db_name = db_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        return self


class DescribeDistributeTableListResponseBodyDataTables(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        db_key: str = None,
        table_type: str = None,
        tb_key: str = None,
    ):
        self.table_name = table_name
        self.db_key = db_key
        self.table_type = table_type
        self.tb_key = tb_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.db_key is not None:
            result['DbKey'] = self.db_key
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.tb_key is not None:
            result['TbKey'] = self.tb_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('DbKey') is not None:
            self.db_key = m.get('DbKey')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('TbKey') is not None:
            self.tb_key = m.get('TbKey')
        return self


class DescribeDistributeTableListResponseBodyData(TeaModel):
    def __init__(
        self,
        tables: List[DescribeDistributeTableListResponseBodyDataTables] = None,
    ):
        self.tables = tables

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = DescribeDistributeTableListResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        return self


class DescribeDistributeTableListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DescribeDistributeTableListResponseBodyData = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDistributeTableListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDistributeTableListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDistributeTableListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDistributeTableListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceDbPerformanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        db_instance_name: str = None,
        keys: str = None,
        start_time: str = None,
        end_time: str = None,
        db_name: str = None,
    ):
        self.region_id = region_id
        self.db_instance_name = db_instance_name
        self.keys = keys
        self.start_time = start_time
        self.end_time = end_time
        self.db_name = db_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        return self


class DescribeInstanceDbPerformanceResponseBodyDataPerformanceItemsPoints(TeaModel):
    def __init__(
        self,
        value: str = None,
        timestamp: int = None,
    ):
        self.value = value
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeInstanceDbPerformanceResponseBodyDataPerformanceItems(TeaModel):
    def __init__(
        self,
        metric_name: str = None,
        measurement: str = None,
        points: List[DescribeInstanceDbPerformanceResponseBodyDataPerformanceItemsPoints] = None,
    ):
        self.metric_name = metric_name
        self.measurement = measurement
        self.points = points

    def validate(self):
        if self.points:
            for k in self.points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.measurement is not None:
            result['Measurement'] = self.measurement
        result['Points'] = []
        if self.points is not None:
            for k in self.points:
                result['Points'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')
        self.points = []
        if m.get('Points') is not None:
            for k in m.get('Points'):
                temp_model = DescribeInstanceDbPerformanceResponseBodyDataPerformanceItemsPoints()
                self.points.append(temp_model.from_map(k))
        return self


class DescribeInstanceDbPerformanceResponseBodyData(TeaModel):
    def __init__(
        self,
        performance_items: List[DescribeInstanceDbPerformanceResponseBodyDataPerformanceItems] = None,
    ):
        self.performance_items = performance_items

    def validate(self):
        if self.performance_items:
            for k in self.performance_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceItems'] = []
        if self.performance_items is not None:
            for k in self.performance_items:
                result['PerformanceItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_items = []
        if m.get('PerformanceItems') is not None:
            for k in m.get('PerformanceItems'):
                temp_model = DescribeInstanceDbPerformanceResponseBodyDataPerformanceItems()
                self.performance_items.append(temp_model.from_map(k))
        return self


class DescribeInstanceDbPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DescribeInstanceDbPerformanceResponseBodyData = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeInstanceDbPerformanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeInstanceDbPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceDbPerformanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceDbPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancePerformanceRequest(TeaModel):
    def __init__(
        self,
        db_instance_name: str = None,
        node_id: str = None,
        keys: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.db_instance_name = db_instance_name
        self.node_id = node_id
        self.keys = keys
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeInstancePerformanceResponseBodyDataPerformanceItemsPoints(TeaModel):
    def __init__(
        self,
        value: str = None,
        timestamp: int = None,
    ):
        self.value = value
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeInstancePerformanceResponseBodyDataPerformanceItems(TeaModel):
    def __init__(
        self,
        metric_name: str = None,
        measurement: str = None,
        points: List[DescribeInstancePerformanceResponseBodyDataPerformanceItemsPoints] = None,
    ):
        self.metric_name = metric_name
        self.measurement = measurement
        self.points = points

    def validate(self):
        if self.points:
            for k in self.points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.measurement is not None:
            result['Measurement'] = self.measurement
        result['Points'] = []
        if self.points is not None:
            for k in self.points:
                result['Points'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')
        self.points = []
        if m.get('Points') is not None:
            for k in m.get('Points'):
                temp_model = DescribeInstancePerformanceResponseBodyDataPerformanceItemsPoints()
                self.points.append(temp_model.from_map(k))
        return self


class DescribeInstancePerformanceResponseBodyData(TeaModel):
    def __init__(
        self,
        performance_items: List[DescribeInstancePerformanceResponseBodyDataPerformanceItems] = None,
    ):
        self.performance_items = performance_items

    def validate(self):
        if self.performance_items:
            for k in self.performance_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceItems'] = []
        if self.performance_items is not None:
            for k in self.performance_items:
                result['PerformanceItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_items = []
        if m.get('PerformanceItems') is not None:
            for k in m.get('PerformanceItems'):
                temp_model = DescribeInstancePerformanceResponseBodyDataPerformanceItems()
                self.performance_items.append(temp_model.from_map(k))
        return self


class DescribeInstancePerformanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DescribeInstancePerformanceResponseBodyData = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeInstancePerformanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeInstancePerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancePerformanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstancePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStoragePerformanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        db_instance_name: str = None,
        storage_instance_id: str = None,
        keys: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.region_id = region_id
        self.db_instance_name = db_instance_name
        self.storage_instance_id = storage_instance_id
        self.keys = keys
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.storage_instance_id is not None:
            result['StorageInstanceId'] = self.storage_instance_id
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('StorageInstanceId') is not None:
            self.storage_instance_id = m.get('StorageInstanceId')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeInstanceStoragePerformanceResponseBodyDataPerformanceItemsPoints(TeaModel):
    def __init__(
        self,
        value: str = None,
        timestamp: int = None,
    ):
        self.value = value
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeInstanceStoragePerformanceResponseBodyDataPerformanceItems(TeaModel):
    def __init__(
        self,
        metric_name: str = None,
        measurement: str = None,
        points: List[DescribeInstanceStoragePerformanceResponseBodyDataPerformanceItemsPoints] = None,
    ):
        self.metric_name = metric_name
        self.measurement = measurement
        self.points = points

    def validate(self):
        if self.points:
            for k in self.points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.measurement is not None:
            result['Measurement'] = self.measurement
        result['Points'] = []
        if self.points is not None:
            for k in self.points:
                result['Points'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')
        self.points = []
        if m.get('Points') is not None:
            for k in m.get('Points'):
                temp_model = DescribeInstanceStoragePerformanceResponseBodyDataPerformanceItemsPoints()
                self.points.append(temp_model.from_map(k))
        return self


class DescribeInstanceStoragePerformanceResponseBodyData(TeaModel):
    def __init__(
        self,
        performance_items: List[DescribeInstanceStoragePerformanceResponseBodyDataPerformanceItems] = None,
    ):
        self.performance_items = performance_items

    def validate(self):
        if self.performance_items:
            for k in self.performance_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceItems'] = []
        if self.performance_items is not None:
            for k in self.performance_items:
                result['PerformanceItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_items = []
        if m.get('PerformanceItems') is not None:
            for k in m.get('PerformanceItems'):
                temp_model = DescribeInstanceStoragePerformanceResponseBodyDataPerformanceItems()
                self.performance_items.append(temp_model.from_map(k))
        return self


class DescribeInstanceStoragePerformanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DescribeInstanceStoragePerformanceResponseBodyData = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeInstanceStoragePerformanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeInstanceStoragePerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceStoragePerformanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceStoragePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_id: str = None,
        param_level: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_id = dbinstance_id
        self.param_level = param_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.param_level is not None:
            result['ParamLevel'] = self.param_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')
        return self


class DescribeParametersResponseBodyDataConfigParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
        parameter_description: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.parameter_description = parameter_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        return self


class DescribeParametersResponseBodyDataRunningParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
        parameter_description: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.parameter_description = parameter_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        return self


class DescribeParametersResponseBodyData(TeaModel):
    def __init__(
        self,
        config_parameters: List[DescribeParametersResponseBodyDataConfigParameters] = None,
        engine: str = None,
        running_parameters: List[DescribeParametersResponseBodyDataRunningParameters] = None,
        engine_version: str = None,
    ):
        self.config_parameters = config_parameters
        self.engine = engine
        self.running_parameters = running_parameters
        self.engine_version = engine_version

    def validate(self):
        if self.config_parameters:
            for k in self.config_parameters:
                if k:
                    k.validate()
        if self.running_parameters:
            for k in self.running_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigParameters'] = []
        if self.config_parameters is not None:
            for k in self.config_parameters:
                result['ConfigParameters'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        result['RunningParameters'] = []
        if self.running_parameters is not None:
            for k in self.running_parameters:
                result['RunningParameters'].append(k.to_map() if k else None)
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_parameters = []
        if m.get('ConfigParameters') is not None:
            for k in m.get('ConfigParameters'):
                temp_model = DescribeParametersResponseBodyDataConfigParameters()
                self.config_parameters.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        self.running_parameters = []
        if m.get('RunningParameters') is not None:
            for k in m.get('RunningParameters'):
                temp_model = DescribeParametersResponseBodyDataRunningParameters()
                self.running_parameters.append(temp_model.from_map(k))
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeParametersResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeParametersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeParametersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolarxDbInstancesRequest(TeaModel):
    def __init__(
        self,
        drds_instance_id: str = None,
        db_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.drds_instance_id = drds_instance_id
        self.db_name = db_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePolarxDbInstancesResponseBodyDbInstancesDbInstance(TeaModel):
    def __init__(
        self,
        status: str = None,
        expire_time: str = None,
        create_time: str = None,
        pay_type: str = None,
        dbtype: str = None,
        vpcid: str = None,
        lock_mode: str = None,
        region_id: str = None,
        network: str = None,
        dbversion: str = None,
        description: str = None,
        node_class: str = None,
        storage_used: int = None,
        node_count: int = None,
        zone_id: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        lock_reason: str = None,
        status_desc: str = None,
    ):
        self.status = status
        self.expire_time = expire_time
        self.create_time = create_time
        self.pay_type = pay_type
        self.dbtype = dbtype
        self.vpcid = vpcid
        self.lock_mode = lock_mode
        self.region_id = region_id
        self.network = network
        self.dbversion = dbversion
        self.description = description
        self.node_class = node_class
        self.storage_used = storage_used
        self.node_count = node_count
        self.zone_id = zone_id
        self.dbinstance_id = dbinstance_id
        self.engine = engine
        self.lock_reason = lock_reason
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network is not None:
            result['Network'] = self.network
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.lock_reason is not None:
            result['lockReason'] = self.lock_reason
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('lockReason') is not None:
            self.lock_reason = m.get('lockReason')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        return self


class DescribePolarxDbInstancesResponseBodyDbInstances(TeaModel):
    def __init__(
        self,
        db_instance: List[DescribePolarxDbInstancesResponseBodyDbInstancesDbInstance] = None,
    ):
        self.db_instance = db_instance

    def validate(self):
        if self.db_instance:
            for k in self.db_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DbInstance'] = []
        if self.db_instance is not None:
            for k in self.db_instance:
                result['DbInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_instance = []
        if m.get('DbInstance') is not None:
            for k in m.get('DbInstance'):
                temp_model = DescribePolarxDbInstancesResponseBodyDbInstancesDbInstance()
                self.db_instance.append(temp_model.from_map(k))
        return self


class DescribePolarxDbInstancesResponseBody(TeaModel):
    def __init__(
        self,
        page_size: str = None,
        request_id: str = None,
        page_number: str = None,
        total: str = None,
        db_instances: DescribePolarxDbInstancesResponseBodyDbInstances = None,
        success: bool = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total = total
        self.db_instances = db_instances
        self.success = success

    def validate(self):
        if self.db_instances:
            self.db_instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        if self.db_instances is not None:
            result['DbInstances'] = self.db_instances.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('DbInstances') is not None:
            temp_model = DescribePolarxDbInstancesResponseBodyDbInstances()
            self.db_instances = temp_model.from_map(m['DbInstances'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePolarxDbInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePolarxDbInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePolarxDbInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        vpc_enabled: bool = None,
    ):
        self.zone_id = zone_id
        self.vpc_enabled = vpc_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeRegionsResponseBodyRegionsRegionZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        support_polarx_10: bool = None,
        zones: DescribeRegionsResponseBodyRegionsRegionZones = None,
        support_polarx_20: bool = None,
        region_id: str = None,
    ):
        self.support_polarx_10 = support_polarx_10
        self.zones = zones
        self.support_polarx_20 = support_polarx_20
        self.region_id = region_id

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support_polarx_10 is not None:
            result['SupportPolarx10'] = self.support_polarx_10
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        if self.support_polarx_20 is not None:
            result['SupportPolarx20'] = self.support_polarx_20
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportPolarx10') is not None:
            self.support_polarx_10 = m.get('SupportPolarx10')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        if m.get('SupportPolarx20') is not None:
            self.support_polarx_20 = m.get('SupportPolarx20')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        error_code: int = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.regions = regions
        self.error_code = error_code
        self.code = code
        self.success = success

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScaleOutMigrateTaskListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dbinstance_name: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dbinstance_name = dbinstance_name
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DescribeScaleOutMigrateTaskListResponseBody(TeaModel):
    def __init__(
        self,
        progress: int = None,
        request_id: str = None,
    ):
        self.progress = progress
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScaleOutMigrateTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScaleOutMigrateTaskListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScaleOutMigrateTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIpsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class DescribeSecurityIpsResponseBodyDataGroupItems(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        security_iplist: str = None,
    ):
        self.group_name = group_name
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeSecurityIpsResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_items: List[DescribeSecurityIpsResponseBodyDataGroupItems] = None,
    ):
        self.dbinstance_name = dbinstance_name
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
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['GroupItems'] = []
        if self.group_items is not None:
            for k in self.group_items:
                result['GroupItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.group_items = []
        if m.get('GroupItems') is not None:
            for k in m.get('GroupItems'):
                temp_model = DescribeSecurityIpsResponseBodyDataGroupItems()
                self.group_items.append(temp_model.from_map(k))
        return self


class DescribeSecurityIpsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DescribeSecurityIpsResponseBodyData = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeSecurityIpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSqlAuditInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_id: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeSqlAuditInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        slslog_store: str = None,
        slsproject: str = None,
        is_enabled: bool = None,
        authenticated: str = None,
    ):
        self.slslog_store = slslog_store
        self.slsproject = slsproject
        self.is_enabled = is_enabled
        self.authenticated = authenticated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store
        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.authenticated is not None:
            result['Authenticated'] = self.authenticated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')
        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('Authenticated') is not None:
            self.authenticated = m.get('Authenticated')
        return self


class DescribeSqlAuditInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeSqlAuditInfoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeSqlAuditInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeSqlAuditInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSqlAuditInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSqlAuditInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dbinstance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        status: str = None,
        task_action: str = None,
        owner_account: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dbinstance_id = dbinstance_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.status = status
        self.task_action = task_action
        self.owner_account = owner_account
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTasksResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbname: str = None,
        begin_time: str = None,
        progress_info: str = None,
        finish_time: str = None,
        task_action: str = None,
        task_id: str = None,
        progress: str = None,
        status: str = None,
        task_error_code: str = None,
        task_error_message: str = None,
        scale_out_token: str = None,
    ):
        self.dbname = dbname
        self.begin_time = begin_time
        self.progress_info = progress_info
        self.finish_time = finish_time
        self.task_action = task_action
        self.task_id = task_id
        self.progress = progress
        self.status = status
        self.task_error_code = task_error_code
        self.task_error_message = task_error_message
        self.scale_out_token = scale_out_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.progress_info is not None:
            result['ProgressInfo'] = self.progress_info
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.task_error_code is not None:
            result['TaskErrorCode'] = self.task_error_code
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.scale_out_token is not None:
            result['ScaleOutToken'] = self.scale_out_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ProgressInfo') is not None:
            self.progress_info = m.get('ProgressInfo')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskErrorCode') is not None:
            self.task_error_code = m.get('TaskErrorCode')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('ScaleOutToken') is not None:
            self.scale_out_token = m.get('ScaleOutToken')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_record_count: int = None,
        page_number: int = None,
        page_record_count: int = None,
        items: List[DescribeTasksResponseBodyItems] = None,
    ):
        self.request_id = request_id
        self.total_record_count = total_record_count
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.items = items

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolarxCommodityRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        order_type: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class GetPolarxCommodityResponseBodyDBInstanceConnAddrs(TeaModel):
    def __init__(
        self,
        type: str = None,
        v_switch_id: str = None,
        connection_string: str = None,
        port: str = None,
        vpcid: str = None,
    ):
        self.type = type
        self.v_switch_id = v_switch_id
        self.connection_string = connection_string
        self.port = port
        self.vpcid = vpcid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        return self


class GetPolarxCommodityResponseBodyDBInstanceDBNodes(TeaModel):
    def __init__(
        self,
        node_class: str = None,
        zone_id: str = None,
        id: str = None,
        region_id: str = None,
    ):
        self.node_class = node_class
        self.zone_id = zone_id
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPolarxCommodityResponseBodyDBInstance(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        dbnode_count: int = None,
        expired: str = None,
        create_time: str = None,
        pay_type: str = None,
        read_dbinstances: List[str] = None,
        port: str = None,
        lock_mode: str = None,
        conn_addrs: List[GetPolarxCommodityResponseBodyDBInstanceConnAddrs] = None,
        description: str = None,
        connection_string: str = None,
        storage_used: int = None,
        expire_date: str = None,
        commodity_code: str = None,
        maintain_start_time: str = None,
        dbinstance_type: str = None,
        dbnode_class: str = None,
        maintain_end_time: str = None,
        latest_minor_version: str = None,
        dbtype: str = None,
        vpcid: str = None,
        minor_version: str = None,
        region_id: str = None,
        dbnodes: List[GetPolarxCommodityResponseBodyDBInstanceDBNodes] = None,
        network: str = None,
        dbversion: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        engine: str = None,
        id: str = None,
    ):
        self.type = type
        self.status = status
        self.dbnode_count = dbnode_count
        self.expired = expired
        self.create_time = create_time
        self.pay_type = pay_type
        self.read_dbinstances = read_dbinstances
        self.port = port
        self.lock_mode = lock_mode
        self.conn_addrs = conn_addrs
        self.description = description
        self.connection_string = connection_string
        self.storage_used = storage_used
        self.expire_date = expire_date
        self.commodity_code = commodity_code
        self.maintain_start_time = maintain_start_time
        self.dbinstance_type = dbinstance_type
        self.dbnode_class = dbnode_class
        self.maintain_end_time = maintain_end_time
        self.latest_minor_version = latest_minor_version
        self.dbtype = dbtype
        self.vpcid = vpcid
        self.minor_version = minor_version
        self.region_id = region_id
        self.dbnodes = dbnodes
        self.network = network
        self.dbversion = dbversion
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id
        self.engine = engine
        self.id = id

    def validate(self):
        if self.conn_addrs:
            for k in self.conn_addrs:
                if k:
                    k.validate()
        if self.dbnodes:
            for k in self.dbnodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.port is not None:
            result['Port'] = self.port
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k in self.conn_addrs:
                result['ConnAddrs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k in self.dbnodes:
                result['DBNodes'].append(k.to_map() if k else None)
        if self.network is not None:
            result['Network'] = self.network
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k in m.get('ConnAddrs'):
                temp_model = GetPolarxCommodityResponseBodyDBInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k in m.get('DBNodes'):
                temp_model = GetPolarxCommodityResponseBodyDBInstanceDBNodes()
                self.dbnodes.append(temp_model.from_map(k))
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetPolarxCommodityResponseBodyComponentList(TeaModel):
    def __init__(
        self,
        type: str = None,
        values: List[str] = None,
        name: str = None,
    ):
        self.type = type
        self.values = values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPolarxCommodityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dbinstance: GetPolarxCommodityResponseBodyDBInstance = None,
        component_list: List[GetPolarxCommodityResponseBodyComponentList] = None,
    ):
        self.request_id = request_id
        self.dbinstance = dbinstance
        self.component_list = component_list

    def validate(self):
        if self.dbinstance:
            self.dbinstance.validate()
        if self.component_list:
            for k in self.component_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance.to_map()
        result['ComponentList'] = []
        if self.component_list is not None:
            for k in self.component_list:
                result['ComponentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstance') is not None:
            temp_model = GetPolarxCommodityResponseBodyDBInstance()
            self.dbinstance = temp_model.from_map(m['DBInstance'])
        self.component_list = []
        if m.get('ComponentList') is not None:
            for k in m.get('ComponentList'):
                temp_model = GetPolarxCommodityResponseBodyComponentList()
                self.component_list.append(temp_model.from_map(k))
        return self


class GetPolarxCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPolarxCommodityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPolarxCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolarXPriceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        node_count: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.node_count = node_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        return self


class GetPolarXPriceResponseBodyOrderPriceListRules(TeaModel):
    def __init__(
        self,
        rule_desc_id: int = None,
        title: str = None,
        name: str = None,
    ):
        self.rule_desc_id = rule_desc_id
        self.title = title
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id
        if self.title is not None:
            result['Title'] = self.title
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPolarXPriceResponseBodyOrderPriceList(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        original_amount: str = None,
        discount_amount: str = None,
        trade_amount: str = None,
        pay_type: str = None,
        total_cost_amount: str = None,
        rules: List[GetPolarXPriceResponseBodyOrderPriceListRules] = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.original_amount = original_amount
        self.discount_amount = discount_amount
        self.trade_amount = trade_amount
        self.pay_type = pay_type
        self.total_cost_amount = total_cost_amount
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.total_cost_amount is not None:
            result['TotalCostAmount'] = self.total_cost_amount
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('TotalCostAmount') is not None:
            self.total_cost_amount = m.get('TotalCostAmount')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetPolarXPriceResponseBodyOrderPriceListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetPolarXPriceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_price_list: List[GetPolarXPriceResponseBodyOrderPriceList] = None,
    ):
        self.request_id = request_id
        self.order_price_list = order_price_list

    def validate(self):
        if self.order_price_list:
            for k in self.order_price_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OrderPriceList'] = []
        if self.order_price_list is not None:
            for k in self.order_price_list:
                result['OrderPriceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.order_price_list = []
        if m.get('OrderPriceList') is not None:
            for k in m.get('OrderPriceList'):
                temp_model = GetPolarXPriceResponseBodyOrderPriceList()
                self.order_price_list.append(temp_model.from_map(k))
        return self


class GetPolarXPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPolarXPriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPolarXPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        account_name: str = None,
        account_description: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.account_name = account_name
        self.account_description = account_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccountDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseDescriptionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        db_name: str = None,
        db_description: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.db_name = db_name
        self.db_description = db_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        return self


class ModifyDatabaseDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDatabaseDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDatabaseDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDatabaseDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceClassRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        target_dbinstance_class: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.target_dbinstance_class = target_dbinstance_class
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.target_dbinstance_class is not None:
            result['TargetDBInstanceClass'] = self.target_dbinstance_class
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('TargetDBInstanceClass') is not None:
            self.target_dbinstance_class = m.get('TargetDBInstanceClass')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyDBInstanceClassResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyDBInstanceClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceClassResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        config_name: str = None,
        config_value: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.config_name = config_name
        self.config_value = config_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        return self


class ModifyDBInstanceConfigResponseBody(TeaModel):
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


class ModifyDBInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        dbinstance_description: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.dbinstance_description = dbinstance_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        return self


class ModifyDBInstanceDescriptionResponseBody(TeaModel):
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


class ModifyDBInstanceDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_id: str = None,
        param_level: str = None,
        parameters: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_id = dbinstance_id
        self.param_level = param_level
        self.parameters = parameters
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.param_level is not None:
            result['ParamLevel'] = self.param_level
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyParameterResponseBody(TeaModel):
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


class ModifyParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyParameterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        group_name: str = None,
        security_iplist: str = None,
        modify_mode: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.group_name = group_name
        self.security_iplist = security_iplist
        self.modify_mode = modify_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dbinstance_name: str = None,
        current_connection_string: str = None,
        owner_account: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dbinstance_name = dbinstance_name
        self.current_connection_string = current_connection_string
        self.owner_account = owner_account
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ReleaseInstancePublicConnectionResponseBody(TeaModel):
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


class ReleaseInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseInstancePublicConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class RestartDBInstanceResponseBody(TeaModel):
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


class RestartDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryPolarxOrderRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        scale_out_token: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.scale_out_token = scale_out_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.scale_out_token is not None:
            result['ScaleOutToken'] = self.scale_out_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('ScaleOutToken') is not None:
            self.scale_out_token = m.get('ScaleOutToken')
        return self


class RetryPolarxOrderResponseBody(TeaModel):
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


class RetryPolarxOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryPolarxOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryPolarxOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        backup_period: str = None,
        backup_plan_begin: str = None,
        backup_set_retention: int = None,
        backup_type: str = None,
        backup_way: str = None,
        force_clean_on_high_space_usage: int = None,
        is_enabled: int = None,
        local_log_retention: int = None,
        remove_log_retention: int = None,
        log_local_retention_space: int = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.backup_period = backup_period
        self.backup_plan_begin = backup_plan_begin
        self.backup_set_retention = backup_set_retention
        self.backup_type = backup_type
        self.backup_way = backup_way
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage
        self.is_enabled = is_enabled
        self.local_log_retention = local_log_retention
        self.remove_log_retention = remove_log_retention
        self.log_local_retention_space = log_local_retention_space

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        return self


class UpdateBackupPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        log_local_retention_space: int = None,
        dbinstance_name: str = None,
        backup_way: str = None,
        backup_period: str = None,
        force_clean_on_high_space_usage: int = None,
        backup_type: str = None,
        local_log_retention: int = None,
        remove_log_retention: int = None,
        backup_plan_begin: str = None,
        backup_set_retention: int = None,
        is_enabled: int = None,
    ):
        self.log_local_retention_space = log_local_retention_space
        self.dbinstance_name = dbinstance_name
        self.backup_way = backup_way
        self.backup_period = backup_period
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage
        self.backup_type = backup_type
        self.local_log_retention = local_log_retention
        self.remove_log_retention = remove_log_retention
        self.backup_plan_begin = backup_plan_begin
        self.backup_set_retention = backup_set_retention
        self.is_enabled = is_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        return self


class UpdateBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[UpdateBackupPolicyResponseBodyData] = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = UpdateBackupPolicyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateBackupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolarDBXInstanceNodeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        db_instance_node_count: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.db_instance_node_count = db_instance_node_count
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_instance_node_count is not None:
            result['DbInstanceNodeCount'] = self.db_instance_node_count
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbInstanceNodeCount') is not None:
            self.db_instance_node_count = m.get('DbInstanceNodeCount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdatePolarDBXInstanceNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class UpdatePolarDBXInstanceNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePolarDBXInstanceNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePolarDBXInstanceNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceKernelVersionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dbinstance_name: str = None,
        upgrade_time: str = None,
        switch_time: str = None,
    ):
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.upgrade_time = upgrade_time
        self.switch_time = switch_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('UpgradeTime') is not None:
            self.upgrade_time = m.get('UpgradeTime')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class UpgradeDBInstanceKernelVersionResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        target_minor_version: str = None,
        dbinstance_name: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.target_minor_version = target_minor_version
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class UpgradeDBInstanceKernelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeDBInstanceKernelVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeDBInstanceKernelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


