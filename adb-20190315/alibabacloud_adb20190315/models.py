# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AllocateClusterPublicConnectionRequest(TeaModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The prefix of the public endpoint.
        # 
        # *   The prefix must contain lowercase letters, digits, and hyphens (-). It must start with a lowercase letter.
        # *   The prefix can be up to 30 characters in length.
        # *   By default, the cluster name is used as the prefix of the public endpoint.
        self.connection_string_prefix = connection_string_prefix
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AllocateClusterPublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class AllocateClusterPublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateClusterPublicConnectionResponseBody = None,
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
            temp_model = AllocateClusterPublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAdviceByIdRequest(TeaModel):
    def __init__(
        self,
        advice_date: int = None,
        advice_id: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The date when the suggestion is generated. Specify the date in the yyyyMMdd format. The date must be in UTC.
        self.advice_date = advice_date
        # The suggestion ID.
        self.advice_id = advice_id
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of Data Warehouse Edition (V3.0) clusters.
        self.dbcluster_id = dbcluster_id
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_date is not None:
            result['AdviceDate'] = self.advice_date
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceDate') is not None:
            self.advice_date = m.get('AdviceDate')
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ApplyAdviceByIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The message returned for the operation. Valid values:
        # 
        # *   **SUCCESS** is returned if the operation is successful.
        # *   An error message is returned if the operation fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyAdviceByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyAdviceByIdResponseBody = None,
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
            temp_model = ApplyAdviceByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachUserENIRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query cluster IDs.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AttachUserENIResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class AttachUserENIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachUserENIResponseBody = None,
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
            temp_model = AttachUserENIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchApplyAdviceByIdListRequest(TeaModel):
    def __init__(
        self,
        advice_date: int = None,
        advice_id_list: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        self.advice_date = advice_date
        self.advice_id_list = advice_id_list
        # The message returned for the operation. Valid values:
        # 
        # *   **SUCCESS** is returned if the operation is successful.
        # *   An error message is returned if the operation fails.
        self.dbcluster_id = dbcluster_id
        # The ID of the request.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_date is not None:
            result['AdviceDate'] = self.advice_date
        if self.advice_id_list is not None:
            result['AdviceIdList'] = self.advice_id_list
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceDate') is not None:
            self.advice_date = m.get('AdviceDate')
        if m.get('AdviceIdList') is not None:
            self.advice_id_list = m.get('AdviceIdList')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchApplyAdviceByIdListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchApplyAdviceByIdListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchApplyAdviceByIdListResponseBody = None,
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
            temp_model = BatchApplyAdviceByIdListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindDBResourceGroupWithUserRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        group_user: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        self.group_name = group_name
        # The database account with which to associate the resource group. It can be a standard account or a privileged account.
        self.group_user = group_user
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_user is not None:
            result['GroupUser'] = self.group_user
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupUser') is not None:
            self.group_user = m.get('GroupUser')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BindDBResourceGroupWithUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class BindDBResourceGroupWithUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindDBResourceGroupWithUserResponseBody = None,
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
            temp_model = BindDBResourceGroupWithUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindDBResourcePoolWithUserRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_name: str = None,
        pool_user: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the resource group.
        self.pool_name = pool_name
        # The database account with which to associate the resource group. It can be a standard account or a privileged account.
        self.pool_user = pool_user
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.pool_user is not None:
            result['PoolUser'] = self.pool_user
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('PoolUser') is not None:
            self.pool_user = m.get('PoolUser')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BindDBResourcePoolWithUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class BindDBResourcePoolWithUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindDBResourcePoolWithUserResponseBody = None,
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
            temp_model = BindDBResourcePoolWithUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        account_type: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the database account.
        # 
        # *   The description cannot start with `http://` or `https://`.
        # *   The description can be up to 256 characters in length.
        self.account_description = account_description
        # The name of the database account.
        # 
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   The name can contain lowercase letters, digits, and underscores (\_).
        # *   The name must be 2 to 16 characters in length.
        # *   Reserved account names such as root, admin, and opsadmin cannot be used.
        self.account_name = account_name
        # The password of the database account.
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # *   The password must be 8 to 32 characters in length.
        self.account_password = account_password
        # The type of the database account. Valid values:
        # 
        # *   **Normal**: standard account. Up to 256 standard accounts can be created for a cluster.
        # *   **Super** (default): privileged account. Only a single privileged account can be created for a cluster.
        # 
        # >  If a cluster does not have accounts, you can specify this parameter to create a privileged account or standard account. If a cluster has a privileged account, you must set this parameter to Normal to create a standard account. Otherwise, the operation fails. After an account is created, the privileged account has permissions on all databases of the cluster. The standard account does not have permissions and must be granted permissions on specific databases by the privileged account. For more information, see GRANT.
        self.account_type = account_type
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to view cluster IDs.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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


class CreateDBClusterRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the cluster. You can use tags to filter clusters. Valid values of N: 1 to 20. The values that you specify for N must be unique and consecutive integers that start from 1. Each value of `Tag.N.Key` is paired with a value of `Tag.N.Value`.
        # 
        # >  The tag key can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.key = key
        # The value of tag N to add to the cluster. You can use tags to filter clusters. Valid values of N: 1 to 20. The values that you specify for N must be unique and consecutive integers that start from 1. Each value of `Tag.N.Key` is paired with a value of `Tag.N.Value`.
        # 
        # >  The tag value can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
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


class CreateDBClusterRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        client_token: str = None,
        compute_resource: str = None,
        dbcluster_category: str = None,
        dbcluster_class: str = None,
        dbcluster_description: str = None,
        dbcluster_network_type: str = None,
        dbcluster_version: str = None,
        dbnode_group_count: str = None,
        dbnode_storage: str = None,
        disk_encryption: str = None,
        elastic_ioresource: str = None,
        executor_count: str = None,
        kms_id: str = None,
        mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
        source_dbinstance_name: str = None,
        storage_resource: str = None,
        storage_type: str = None,
        tag: List[CreateDBClusterRequestTag] = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # A reserved parameter.
        self.backup_set_id = backup_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The value is case-sensitive and can contain a maximum of 64 ASCII characters in length.
        self.client_token = client_token
        # The computing resources of the cluster. This parameter is required if the Mode parameter is set to **Flexible**.
        # 
        # >  You can call the [DescribeAvailableResource](~~190632~~) operation to query the computing resources that are available within a specific region.
        self.compute_resource = compute_resource
        # The edition of the cluster. Valid values:
        # 
        # *   **Cluster**: reserved mode for Cluster Edition
        # 
        # <!---->
        # 
        # *   **MixedStorage**: elastic mode for Cluster Edition
        # 
        # >  If the DBClusterCategory parameter is set to Cluster, you must set the Mode parameter to Reserver. If the DBClusterCategory parameter is set to MixedStorage, you must set the Mode parameter to Flexible. Otherwise, the cluster fails to be created.
        self.dbcluster_category = dbcluster_category
        # The specification of the cluster. Valid values:
        # 
        # *   **C8**\
        # *   **C32**\
        # 
        # >  This parameter is required if the Mode parameter is set to Reserver.
        self.dbcluster_class = dbcluster_class
        # The description of the cluster.
        # 
        # *   The description cannot start with `http://` or `https`.
        # *   The description must be 2 to 256 characters in length.
        self.dbcluster_description = dbcluster_description
        # The network type of the cluster. Set the value to **VPC**.
        self.dbcluster_network_type = dbcluster_network_type
        # The version of the cluster. Set the value to **3.0**.
        self.dbcluster_version = dbcluster_version
        # The number of node groups. Valid values: 1 to 200 (integer).
        # 
        # >  This parameter is required if the Mode parameter is set to Reserver.
        self.dbnode_group_count = dbnode_group_count
        # The storage capacity of the cluster. Unit: GB.
        # 
        # *   Valid values when DBClusterClass is set to C8: 100 to 1000
        # *   Valid values when DBClusterClass is set to C32: 100 to 8000
        # 
        # > * This parameter is required if the Mode parameter is set to Reserver.
        # > * 1000 The storage capacity less than 1,000 GB increases in 100 GB increments. The storage capacity greater than 1,000 GB increases in 1,000 GB increments.
        self.dbnode_storage = dbnode_storage
        # Specifies whether to enable disk encryption.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.disk_encryption = disk_encryption
        # The number of elastic I/O units (EIUs). For more information, see [Use EIUs to scale up storage resources](~~189505~~).
        self.elastic_ioresource = elastic_ioresource
        # A reserved parameter.
        self.executor_count = executor_count
        # The Key Management Service (KMS) ID that is used for disk encryption. This parameter is valid only when DiskEncryption is set to true.
        self.kms_id = kms_id
        # The mode of the cluster. Valid values:
        # 
        # *   **Reserver**: the reserved mode.
        # *   **Flexible**: the elastic mode.
        self.mode = mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        # The subscription type of the subscription cluster. Valid values:
        # 
        # *   **Year**: subscription on a yearly basis
        # *   **Month**: subscription on a monthly basis
        # 
        # >  This parameter is required if the PayType parameter is set to Prepaid.
        self.period = period
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A reserved parameter.
        self.restore_time = restore_time
        # A reserved parameter.
        self.restore_type = restore_type
        # A reserved parameter.
        self.source_dbinstance_name = source_dbinstance_name
        # A reserved parameter.
        self.storage_resource = storage_resource
        # A reserved parameter.
        self.storage_type = storage_type
        # The tags to add to the cluster.
        self.tag = tag
        # The subscription period of the subscription cluster.
        # 
        # *   Valid values when Period is set to Year: 1, 2, 3, and 5 (integer)
        # *   Valid values when Period is set to Month: 1 to 11 (integer)
        # 
        # > * This parameter is required if the PayType parameter is set to Prepaid.
        # > * Longer subscription periods offer more savings. Purchasing a cluster for one year is more cost-effective than purchasing the cluster for 10 or 11 months.
        self.used_time = used_time
        # The virtual private cloud (VPC) ID of the cluster.
        self.vpcid = vpcid
        # The vSwitch ID of the cluster.
        self.v_switch_id = v_switch_id
        # The zone ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetID'] = self.backup_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.dbcluster_category is not None:
            result['DBClusterCategory'] = self.dbcluster_category
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version
        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.disk_encryption is not None:
            result['DiskEncryption'] = self.disk_encryption
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.kms_id is not None:
            result['KmsId'] = self.kms_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.source_dbinstance_name is not None:
            result['SourceDBInstanceName'] = self.source_dbinstance_name
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetID') is not None:
            self.backup_set_id = m.get('BackupSetID')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('DBClusterCategory') is not None:
            self.dbcluster_category = m.get('DBClusterCategory')
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')
        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DiskEncryption') is not None:
            self.disk_encryption = m.get('DiskEncryption')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('KmsId') is not None:
            self.kms_id = m.get('KmsId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SourceDBInstanceName') is not None:
            self.source_dbinstance_name = m.get('SourceDBInstanceName')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDBClusterRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBClusterResponseBody = None,
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
            temp_model = CreateDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        group_type: str = None,
        node_num: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        # 
        # *   The name can be up to 255 characters in length.
        # *   The name must start with a letter or a digit.
        # *   The name can contain letters, digits, hyphens (\_), and underscores (\_).
        self.group_name = group_name
        # The query execution mode. Default value: batch. Valid values:
        # 
        # *   **interactive**\
        # *   **batch**\
        self.group_type = group_type
        # The number of nodes. Default value: 0.
        # 
        # *   Each node is configured with the resources of 16 cores and 64 GB memory.
        # *   Make sure that the amount of resources of the nodes (Number of nodes × 16 cores and 64 GB memory) is less than or equal to the amount of unused resources of the cluster.
        self.node_num = node_num
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDBResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class CreateDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBResourceGroupResponseBody = None,
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
            temp_model = CreateDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBResourcePoolRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        node_num: int = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_name: str = None,
        query_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The number of nodes. Default value: 0.
        # 
        # *   Each node provides 16 cores and 64 GB memory.
        # *   The total amount of resources provided by the nodes (number of nodes × 16 cores, number of nodes × 64 GB memory) cannot exceed the total amount of resources in the cluster. Set this parameter to a proper value.
        self.node_num = node_num
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the resource group.
        # 
        # *   The name can be up to 255 characters in length.
        # *   The name must start with a letter or a digit.
        # *   The name can contain letters, digits, hyphens (\_), and underscores (\_).
        self.pool_name = pool_name
        # The mode in which to execute SQL statements.
        # 
        # *   **batch**\
        # 
        # *   **interactive**\
        # 
        # > For more information, see [Query execution modes](~~189502~~).
        self.query_type = query_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDBResourcePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class CreateDBResourcePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBResourcePoolResponseBody = None,
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
            temp_model = CreateDBResourcePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateElasticPlanRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_plan_enable: bool = None,
        elastic_plan_end_day: str = None,
        elastic_plan_monthly_repeat: str = None,
        elastic_plan_name: str = None,
        elastic_plan_node_num: int = None,
        elastic_plan_start_day: str = None,
        elastic_plan_time_end: str = None,
        elastic_plan_time_start: str = None,
        elastic_plan_type: str = None,
        elastic_plan_weekly_repeat: str = None,
        elastic_plan_worker_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pool_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # Specifies whether the scaling plan takes effect. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.elastic_plan_enable = elastic_plan_enable
        # The end date of the scaling plan. Specify the date in the yyyy-MM-dd format.
        self.elastic_plan_end_day = elastic_plan_end_day
        self.elastic_plan_monthly_repeat = elastic_plan_monthly_repeat
        # The name of the scaling plan.
        # 
        # *   The name must be 2 to 30 characters in length.
        # *   The name can contain letters, digits, and underscores (\_).
        self.elastic_plan_name = elastic_plan_name
        # The number of nodes that are involved in the scaling plan.
        # 
        # *   If ElasticPlanType is set to **worker**, you can set this parameter to 0 or leave this parameter empty.
        # *   If ElasticPlanType is set to **executorcombineworker** or **executor**, you must set this parameter to a value that is greater than 0.
        self.elastic_plan_node_num = elastic_plan_node_num
        # The start date of the scaling plan. Specify the date in the yyyy-MM-dd format.
        self.elastic_plan_start_day = elastic_plan_start_day
        # The restoration time of the scaling plan. Specify the time on the hour in the HH:mm:ss format. The interval between the scale-up time and the restoration time cannot be more than 24 hours.
        self.elastic_plan_time_end = elastic_plan_time_end
        # The scale-up time of the scaling plan. Specify the time on the hour in the HH:mm:ss format.
        self.elastic_plan_time_start = elastic_plan_time_start
        # The type of the scaling plan. Valid values:
        # 
        # *   **worker**: scales only elastic I/O resources.
        # *   **executor**: scales only computing resources.
        # *   **executorcombineworker** (default): scales both elastic I/O resources and computing resources by proportion.
        # > - If you want to set this parameter to **executorcombineworker**, make sure that the cluster runs a minor version of 3.1.3.2 or later.
        # > - If you want to set this parameter to **worker** or **executor**, make sure that the cluster runs a minor version of 3.1.6.1 or later and a ticket is submitted. After your request is approved, you can set this parameter to **worker** or **executor**.
        self.elastic_plan_type = elastic_plan_type
        # The days of the week when you want to execute the scaling plan. Valid values: 0 to 6, which indicates Sunday to Saturday. Separate multiple values with commas (,).
        self.elastic_plan_weekly_repeat = elastic_plan_weekly_repeat
        # The resource specifications that can be scaled up by the scaling plan. Valid values:
        # 
        # *   8 Core 64 GB (default)
        # *   16 Core 64 GB
        # *   32 Core 64 GB
        # *   64 Core 128 GB
        # *   12 Core 96 GB
        # *   24 Core 96 GB
        # *   52 Core 86 GB
        self.elastic_plan_worker_spec = elastic_plan_worker_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the resource group.
        # 
        # > You can call the [DescribeDBResourceGroup](~~466685~~) operation to query the resource group name.
        self.resource_pool_name = resource_pool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_enable is not None:
            result['ElasticPlanEnable'] = self.elastic_plan_enable
        if self.elastic_plan_end_day is not None:
            result['ElasticPlanEndDay'] = self.elastic_plan_end_day
        if self.elastic_plan_monthly_repeat is not None:
            result['ElasticPlanMonthlyRepeat'] = self.elastic_plan_monthly_repeat
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.elastic_plan_node_num is not None:
            result['ElasticPlanNodeNum'] = self.elastic_plan_node_num
        if self.elastic_plan_start_day is not None:
            result['ElasticPlanStartDay'] = self.elastic_plan_start_day
        if self.elastic_plan_time_end is not None:
            result['ElasticPlanTimeEnd'] = self.elastic_plan_time_end
        if self.elastic_plan_time_start is not None:
            result['ElasticPlanTimeStart'] = self.elastic_plan_time_start
        if self.elastic_plan_type is not None:
            result['ElasticPlanType'] = self.elastic_plan_type
        if self.elastic_plan_weekly_repeat is not None:
            result['ElasticPlanWeeklyRepeat'] = self.elastic_plan_weekly_repeat
        if self.elastic_plan_worker_spec is not None:
            result['ElasticPlanWorkerSpec'] = self.elastic_plan_worker_spec
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanEnable') is not None:
            self.elastic_plan_enable = m.get('ElasticPlanEnable')
        if m.get('ElasticPlanEndDay') is not None:
            self.elastic_plan_end_day = m.get('ElasticPlanEndDay')
        if m.get('ElasticPlanMonthlyRepeat') is not None:
            self.elastic_plan_monthly_repeat = m.get('ElasticPlanMonthlyRepeat')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('ElasticPlanNodeNum') is not None:
            self.elastic_plan_node_num = m.get('ElasticPlanNodeNum')
        if m.get('ElasticPlanStartDay') is not None:
            self.elastic_plan_start_day = m.get('ElasticPlanStartDay')
        if m.get('ElasticPlanTimeEnd') is not None:
            self.elastic_plan_time_end = m.get('ElasticPlanTimeEnd')
        if m.get('ElasticPlanTimeStart') is not None:
            self.elastic_plan_time_start = m.get('ElasticPlanTimeStart')
        if m.get('ElasticPlanType') is not None:
            self.elastic_plan_type = m.get('ElasticPlanType')
        if m.get('ElasticPlanWeeklyRepeat') is not None:
            self.elastic_plan_weekly_repeat = m.get('ElasticPlanWeeklyRepeat')
        if m.get('ElasticPlanWorkerSpec') is not None:
            self.elastic_plan_worker_spec = m.get('ElasticPlanWorkerSpec')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        return self


class CreateElasticPlanResponseBody(TeaModel):
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


class CreateElasticPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateElasticPlanResponseBody = None,
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
            temp_model = CreateElasticPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The account of the database.
        self.account_name = account_name
        # *   Normal: standard account
        # *   Super: privileged account
        self.account_type = account_type
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DeleteDBClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBClusterResponseBody = None,
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
            temp_model = DeleteDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        self.group_name = group_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBResourceGroupResponseBody(TeaModel):
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


class DeleteDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBResourceGroupResponseBody = None,
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
            temp_model = DeleteDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBResourcePoolRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the resource group.
        self.pool_name = pool_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBResourcePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DeleteDBResourcePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBResourcePoolResponseBody = None,
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
            temp_model = DeleteDBResourcePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteElasticPlanRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_plan_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~612241~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the scaling plan.
        # 
        # > You can call the [DescribeElasticPlans](~~601334~~) operation to query the names of scaling plans.
        self.elastic_plan_name = elastic_plan_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteElasticPlanResponseBody(TeaModel):
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


class DeleteElasticPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteElasticPlanResponseBody = None,
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
            temp_model = DeleteElasticPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the database account.
        # 
        # >  If you do not specify this parameter, the information about all database accounts is returned.
        self.account_name = account_name
        # The type of the database account. If you do not specify this parameter, the information about all account types is returned. Valid values:
        # 
        # *   **Normal**: standard account.
        # *   **Super**: privileged account.
        self.account_type = account_type
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAccountsResponseBodyAccountListDBAccount(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
    ):
        # The description of the database account.
        self.account_description = account_description
        # The name of the database account.
        self.account_name = account_name
        # The state of the database account. Valid values:
        # 
        # *   **Creating**\
        # *   **Available**\
        # *   **Deleting**\
        self.account_status = account_status
        # The type of the database account. Valid values:
        # 
        # *   **Normal**: standard account.
        # *   **Super**: privileged account.
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class DescribeAccountsResponseBodyAccountList(TeaModel):
    def __init__(
        self,
        dbaccount: List[DescribeAccountsResponseBodyAccountListDBAccount] = None,
    ):
        self.dbaccount = dbaccount

    def validate(self):
        if self.dbaccount:
            for k in self.dbaccount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBAccount'] = []
        if self.dbaccount is not None:
            for k in self.dbaccount:
                result['DBAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbaccount = []
        if m.get('DBAccount') is not None:
            for k in m.get('DBAccount'):
                temp_model = DescribeAccountsResponseBodyAccountListDBAccount()
                self.dbaccount.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(
        self,
        account_list: DescribeAccountsResponseBodyAccountList = None,
        request_id: str = None,
    ):
        # The queried database accounts.
        self.account_list = account_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account_list:
            self.account_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_list is not None:
            result['AccountList'] = self.account_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountList') is not None:
            temp_model = DescribeAccountsResponseBodyAccountList()
            self.account_list = temp_model.from_map(m['AccountList'])
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


class DescribeAdviceServiceEnabledRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of Data Warehouse Edition (V3.0) clusters.
        self.dbcluster_id = dbcluster_id
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAdviceServiceEnabledResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        # The returned message.
        # 
        # *   If the request was successful, **Success** is returned.
        # *   If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the suggestion feature is enabled. Valid values:
        # 
        # *   **True**\
        # *   **False**\
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeAdviceServiceEnabledResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdviceServiceEnabledResponseBody = None,
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
            temp_model = DescribeAdviceServiceEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllAccountsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAllAccountsResponseBodyAccountList(TeaModel):
    def __init__(
        self,
        user: str = None,
    ):
        # The name of the account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeAllAccountsResponseBody(TeaModel):
    def __init__(
        self,
        account_list: List[DescribeAllAccountsResponseBodyAccountList] = None,
        request_id: str = None,
    ):
        # The list of accounts.
        self.account_list = account_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account_list:
            for k in self.account_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountList'] = []
        if self.account_list is not None:
            for k in self.account_list:
                result['AccountList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_list = []
        if m.get('AccountList') is not None:
            for k in m.get('AccountList'):
                temp_model = DescribeAllAccountsResponseBodyAccountList()
                self.account_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAllAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAllAccountsResponseBody = None,
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
            temp_model = DescribeAllAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllDataSourceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAllDataSourceResponseBodyColumnsColumn(TeaModel):
    def __init__(
        self,
        auto_increment_column: bool = None,
        column_name: str = None,
        dbcluster_id: str = None,
        primary_key: bool = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        # Indicates whether the column is an auto-increment column. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_increment_column = auto_increment_column
        # The name of the column.
        self.column_name = column_name
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # Indicates whether the column is the primary key of the table. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.primary_key = primary_key
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name
        # The data type of the column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment_column is not None:
            result['AutoIncrementColumn'] = self.auto_increment_column
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrementColumn') is not None:
            self.auto_increment_column = m.get('AutoIncrementColumn')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAllDataSourceResponseBodyColumns(TeaModel):
    def __init__(
        self,
        column: List[DescribeAllDataSourceResponseBodyColumnsColumn] = None,
    ):
        self.column = column

    def validate(self):
        if self.column:
            for k in self.column:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Column'] = []
        if self.column is not None:
            for k in self.column:
                result['Column'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k in m.get('Column'):
                temp_model = DescribeAllDataSourceResponseBodyColumnsColumn()
                self.column.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBodySchemasSchema(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        schema_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeAllDataSourceResponseBodySchemas(TeaModel):
    def __init__(
        self,
        schema: List[DescribeAllDataSourceResponseBodySchemasSchema] = None,
    ):
        self.schema = schema

    def validate(self):
        if self.schema:
            for k in self.schema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Schema'] = []
        if self.schema is not None:
            for k in self.schema:
                result['Schema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k in m.get('Schema'):
                temp_model = DescribeAllDataSourceResponseBodySchemasSchema()
                self.schema.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBodyTablesTable(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAllDataSourceResponseBodyTables(TeaModel):
    def __init__(
        self,
        table: List[DescribeAllDataSourceResponseBodyTablesTable] = None,
    ):
        self.table = table

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeAllDataSourceResponseBodyTablesTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        columns: DescribeAllDataSourceResponseBodyColumns = None,
        request_id: str = None,
        schemas: DescribeAllDataSourceResponseBodySchemas = None,
        tables: DescribeAllDataSourceResponseBodyTables = None,
    ):
        # The queried columns.
        self.columns = columns
        # The request ID.
        self.request_id = request_id
        # The queried databases.
        self.schemas = schemas
        # The queried tables.
        self.tables = tables

    def validate(self):
        if self.columns:
            self.columns.validate()
        if self.schemas:
            self.schemas.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['Columns'] = self.columns.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schemas is not None:
            result['Schemas'] = self.schemas.to_map()
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            temp_model = DescribeAllDataSourceResponseBodyColumns()
            self.columns = temp_model.from_map(m['Columns'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schemas') is not None:
            temp_model = DescribeAllDataSourceResponseBodySchemas()
            self.schemas = temp_model.from_map(m['Schemas'])
        if m.get('Tables') is not None:
            temp_model = DescribeAllDataSourceResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        return self


class DescribeAllDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAllDataSourceResponseBody = None,
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
            temp_model = DescribeAllDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppliedAdvicesRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: int = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyyMMdd format. The time must be in UTC.
        self.end_time = end_time
        # The display language of the suggestion. Valid values:
        # 
        # *   **zh** (default): simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyyMMdd format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAppliedAdvicesResponseBodyItems(TeaModel):
    def __init__(
        self,
        advice_id: str = None,
        benefit: str = None,
        build_sql: str = None,
        job_status: str = None,
        page_number: int = None,
        page_size: int = None,
        rollback_sql: str = None,
        sql: str = None,
        submit_status: str = None,
        submit_time: str = None,
        total_count: int = None,
    ):
        # The suggestion ID.
        self.advice_id = advice_id
        # The benefit of the suggestion.
        self.benefit = benefit
        # The SQL statement that is used to execute the BUILD job.
        self.build_sql = build_sql
        # The state of the suggestion execution job. Valid values:
        # 
        # *   **SUCCEED**\
        # *   **FAILED**\
        self.job_status = job_status
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The SQL statement that is used to roll back the suggestion.
        self.rollback_sql = rollback_sql
        # The SQL statement that is used to apply the suggestion.
        self.sql = sql
        # The submission state of the suggestion. Valid values:
        # 
        # *   **SUCCEED**\
        # *   **FAILED**\
        self.submit_status = submit_status
        # The time when the suggestion was submitted. The time follows the ISO 8601 standard in the yyMMddHHmm format. The time is displayed in UTC.
        self.submit_time = submit_time
        # The total number of entries returned. Minimum value: 0. Default value: 0.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id
        if self.benefit is not None:
            result['Benefit'] = self.benefit
        if self.build_sql is not None:
            result['BuildSQL'] = self.build_sql
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rollback_sql is not None:
            result['RollbackSQL'] = self.rollback_sql
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('Benefit') is not None:
            self.benefit = m.get('Benefit')
        if m.get('BuildSQL') is not None:
            self.build_sql = m.get('BuildSQL')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RollbackSQL') is not None:
            self.rollback_sql = m.get('RollbackSQL')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppliedAdvicesResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeAppliedAdvicesResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried suggestions.
        self.items = items
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned. The value is an integer that is greater than or equal to 0. Default value: 0.
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
                temp_model = DescribeAppliedAdvicesResponseBodyItems()
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


class DescribeAppliedAdvicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppliedAdvicesResponseBody = None,
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
            temp_model = DescribeAppliedAdvicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogConfigRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region. You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAuditLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        audit_log_status: str = None,
        dbcluster_id: str = None,
        request_id: str = None,
    ):
        # The status of SQL audit. Valid values:
        # 
        # *   **on**: SQL audit is enabled.
        # *   **off**: SQL audit is disabled.
        self.audit_log_status = audit_log_status
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAuditLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditLogConfigResponseBody = None,
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
            temp_model = DescribeAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogRecordsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbname: str = None,
        end_time: str = None,
        host_address: str = None,
        order: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_keyword: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sql_type: str = None,
        start_time: str = None,
        succeed: str = None,
        user: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the database on which you want to execute the SQL statement.
        self.dbname = dbname
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        # 
        # > - The end time must be later than the start time.
        # > - The maximum time range that can be specified is 24 hours.
        self.end_time = end_time
        # The IP address and port number of the client that is used to execute the SQL statement.
        self.host_address = host_address
        # The order in which specified fields are sorted. Specify this parameter as an ordered JSON array that consists of the Field and Type fields.
        # 
        # *   Field specifies the field that is used to sort the retrieved entries. Valid values:
        # 
        #     *   HostAddress: the IP address of the client that is used to connect to the database.
        #     *   Succeed: specifies whether the SQL statement is successfully executed.
        #     *   TotalTime: the total amount of time that is consumed to execute the SQL statement.
        #     *   DBName: the name of the database on which the SQL statement is executed.
        #     *   SQLType: the type of the SQL statement.
        #     *   User: the username that is used to execute the SQL statement.
        #     *   ExecuteTime: the time to start executing the SQL statement.
        # 
        # *   Type specifies the sorting order. Valid values:
        # 
        #     *   Desc: descending order.
        #     *   Asc: ascending order.
        self.order = order
        # The sorting order of the retrieved entries. Valid values:
        # 
        # *   **asc**: sorts the retrieved entries by time in ascending order.
        # *   **desc**: sorts the retrieved entries by time in descending order.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value is an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **10**\
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # > If you do not specify this parameter, the value 10 is used.
        self.page_size = page_size
        # The keywords that are included in the SQL statement to query.
        self.query_keyword = query_keyword
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the SQL statement. Valid values:
        # 
        # *   **DELETE**\
        # *   **SELECT**\
        # *   **UPDATE**\
        # *   **INSERT_INTO_SELECT**\
        # *   **ALTER**\
        # *   **DROP**\
        # *   **CREATE**\
        # 
        # > You can query only a single type of SQL statements at a time. If you leave this parameter empty, the **SELECT** statements are queried.
        self.sql_type = sql_type
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        # 
        # > SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried.
        self.start_time = start_time
        # Specifies whether the execution of the SQL statement succeeds. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.succeed = succeed
        # The name of the user who executed the SQL statement.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.order is not None:
            result['Order'] = self.order
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeAuditLogRecordsResponseBodyItems(TeaModel):
    def __init__(
        self,
        conn_id: str = None,
        dbname: str = None,
        execute_time: str = None,
        host_address: str = None,
        process_id: str = None,
        sqltext: str = None,
        sqltype: str = None,
        succeed: str = None,
        total_time: str = None,
        user: str = None,
    ):
        # This parameter is unavailable.
        self.conn_id = conn_id
        # The name of the database on which the SQL statement was executed.
        self.dbname = dbname
        # The start time of the execution of the SQL statement. The time is displayed in the ISO 8601 standard in the yyyy-MM-dd HH:mm:ss format. The time must be in UTC.
        self.execute_time = execute_time
        # The IP address and port number of the client that is used to execute the SQL statement.
        self.host_address = host_address
        # The task ID.
        self.process_id = process_id
        # Details of the SQL statement.
        self.sqltext = sqltext
        # The type of the SQL statement.
        self.sqltype = sqltype
        # Indicates whether the SQL statement was successfully executed. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.succeed = succeed
        # The amount of time that is consumed to execute the SQL statement. Unit: milliseconds.
        self.total_time = total_time
        # The name of the user who executed the SQL statement.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_id is not None:
            result['ConnId'] = self.conn_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.process_id is not None:
            result['ProcessID'] = self.process_id
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnId') is not None:
            self.conn_id = m.get('ConnId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeAuditLogRecordsResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: List[DescribeAuditLogRecordsResponseBodyItems] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried SQL audit logs.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeAuditLogRecordsResponseBodyItems()
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


class DescribeAuditLogRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditLogRecordsResponseBody = None,
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
            temp_model = DescribeAuditLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_ids: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cluster ID. Separate multiple clusters with commas (,).
        self.dbcluster_ids = dbcluster_ids
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        # 
        # Default value: 30.
        self.page_size = page_size
        # The region ID of the cluster.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute(TeaModel):
    def __init__(
        self,
        auto_renew_enabled: bool = None,
        dbcluster_id: str = None,
        duration: int = None,
        period_unit: str = None,
        region_id: str = None,
        renewal_status: str = None,
    ):
        # Indicates whether auto-renewal is enabled for the cluster. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_renew_enabled = auto_renew_enabled
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The renewal duration.
        self.duration = duration
        # The unit of the renewal duration. Valid values:
        # 
        # *   **Year**\
        # *   **Month**\
        self.period_unit = period_unit
        # The region ID of the cluster.
        self.region_id = region_id
        # The renewal status of the cluster. Valid values:
        # 
        # *   **AutoRenewal**: The cluster is automatically renewed.
        # *   **Normal**: The cluster is manually renewed. Before the cluster expires, the system sends you a reminder by SMS message.
        # *   **NotRenewal**: The cluster is not renewed. Three days before the cluster expires, the system sends you a reminder by SMS message to remind you that the cluster is not renewed. However, the system does not send you a reminder when the cluster expires.
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_enabled is not None:
            result['AutoRenewEnabled'] = self.auto_renew_enabled
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewEnabled') is not None:
            self.auto_renew_enabled = m.get('AutoRenewEnabled')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class DescribeAutoRenewAttributeResponseBodyItems(TeaModel):
    def __init__(
        self,
        auto_renew_attribute: List[DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute] = None,
    ):
        self.auto_renew_attribute = auto_renew_attribute

    def validate(self):
        if self.auto_renew_attribute:
            for k in self.auto_renew_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoRenewAttribute'] = []
        if self.auto_renew_attribute is not None:
            for k in self.auto_renew_attribute:
                result['AutoRenewAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_renew_attribute = []
        if m.get('AutoRenewAttribute') is not None:
            for k in m.get('AutoRenewAttribute'):
                temp_model = DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute()
                self.auto_renew_attribute.append(temp_model.from_map(k))
        return self


class DescribeAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeAutoRenewAttributeResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The renewal information of the cluster.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeAutoRenewAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAutoRenewAttributeResponseBody = None,
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
            temp_model = DescribeAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableAdvicesRequest(TeaModel):
    def __init__(
        self,
        advice_date: int = None,
        dbcluster_id: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The date when the suggestion is generated. Specify the date in the yyyyMMdd format. The date must be in UTC.
        self.advice_date = advice_date
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of Data Warehouse Edition (V3.0) clusters.
        self.dbcluster_id = dbcluster_id
        # The display language of the suggestion. Default value: zh. Valid values:
        # 
        # *   **zh**: simplified Chinese
        # *   **en**: English
        # *   **ja**: Japanese
        # *   **zh-tw**: traditional Chinese
        self.lang = lang
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 30. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_date is not None:
            result['AdviceDate'] = self.advice_date
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceDate') is not None:
            self.advice_date = m.get('AdviceDate')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAvailableAdvicesResponseBodyItems(TeaModel):
    def __init__(
        self,
        advice_date: str = None,
        advice_id: str = None,
        advice_type: str = None,
        benefit: str = None,
        page_number: int = None,
        page_size: int = None,
        reason: str = None,
        sql: str = None,
        total_count: int = None,
    ):
        # The time when the suggestion was generated. The time follows the ISO 8601 standard in the yyyyMMdd format. The time is displayed in UTC.
        self.advice_date = advice_date
        # The suggestion ID.
        self.advice_id = advice_id
        # The type of the suggestion. Valid values:
        # 
        # *   **Index**: index optimization.
        # *   **Tiering**: hot and cold data optimization.
        self.advice_type = advice_type
        # The benefit of the suggestion.
        self.benefit = benefit
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The reason why the suggestion was generated.
        self.reason = reason
        # The SQL statement that is used to apply the suggestion.
        self.sql = sql
        # The total number of entries returned. Minimum value: 0. Default value: 0.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_date is not None:
            result['AdviceDate'] = self.advice_date
        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id
        if self.advice_type is not None:
            result['AdviceType'] = self.advice_type
        if self.benefit is not None:
            result['Benefit'] = self.benefit
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceDate') is not None:
            self.advice_date = m.get('AdviceDate')
        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')
        if m.get('AdviceType') is not None:
            self.advice_type = m.get('AdviceType')
        if m.get('Benefit') is not None:
            self.benefit = m.get('Benefit')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAvailableAdvicesResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeAvailableAdvicesResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried suggestions.
        self.items = items
        # The page number of the returned page. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page. Default value: 30. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned. The value must be an integer that is greater than or equal to 0. Default value: 0.
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
                temp_model = DescribeAvailableAdvicesResponseBodyItems()
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


class DescribeAvailableAdvicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableAdvicesResponseBody = None,
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
            temp_model = DescribeAvailableAdvicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        charge_type: str = None,
        dbcluster_version: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The language of query results. Valid values:
        # 
        # *   **zh-CN** (default): Chinese.
        # *   **en-US**: English.
        self.accept_language = accept_language
        # The resources available in the supported modes.
        self.charge_type = charge_type
        # The version of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_version = dbcluster_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The zone ID.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource(TeaModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # The maximum amount of elastic I/O resources.
        self.max_count = max_count
        # The minimum amount of elastic I/O resources.
        self.min_count = min_count
        # The step size.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource(TeaModel):
    def __init__(
        self,
        storage_type: str = None,
        supported_compute_resource: List[str] = None,
        supported_elastic_ioresource: DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource = None,
        supported_storage_resource: List[str] = None,
    ):
        # The disk storage type. Valid values:
        # 
        # *   **hdd**\
        # *   **ssd**\
        self.storage_type = storage_type
        # The supported computing resources.
        self.supported_compute_resource = supported_compute_resource
        # The supported elastic I/O resources.
        self.supported_elastic_ioresource = supported_elastic_ioresource
        # The supported storage resources.
        self.supported_storage_resource = supported_storage_resource

    def validate(self):
        if self.supported_elastic_ioresource:
            self.supported_elastic_ioresource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.supported_compute_resource is not None:
            result['SupportedComputeResource'] = self.supported_compute_resource
        if self.supported_elastic_ioresource is not None:
            result['SupportedElasticIOResource'] = self.supported_elastic_ioresource.to_map()
        if self.supported_storage_resource is not None:
            result['SupportedStorageResource'] = self.supported_storage_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SupportedComputeResource') is not None:
            self.supported_compute_resource = m.get('SupportedComputeResource')
        if m.get('SupportedElasticIOResource') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource()
            self.supported_elastic_ioresource = temp_model.from_map(m['SupportedElasticIOResource'])
        if m.get('SupportedStorageResource') is not None:
            self.supported_storage_resource = m.get('SupportedStorageResource')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount(TeaModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # A reserved parameter.
        self.max_count = max_count
        # A reserved parameter.
        self.min_count = min_count
        # A reserved parameter.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList(TeaModel):
    def __init__(
        self,
        node_count: DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount = None,
    ):
        # The information about the supported compute nodes.
        self.node_count = node_count

    def validate(self):
        if self.node_count:
            self.node_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount(TeaModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # The maximum number of compute nodes.
        self.max_count = max_count
        # The minimum number of compute nodes.
        self.min_count = min_count
        # The step size.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList(TeaModel):
    def __init__(
        self,
        node_count: DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount = None,
        storage_size: List[str] = None,
    ):
        # The number of the supported compute nodes.
        self.node_count = node_count
        # The support storage capacity. Unit: GB.
        self.storage_size = storage_size

    def validate(self):
        if self.node_count:
            self.node_count.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList(TeaModel):
    def __init__(
        self,
        instance_class: str = None,
        supported_executor_list: List[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList] = None,
        supported_node_count_list: List[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList] = None,
        tips: str = None,
    ):
        # The supported instance type.
        self.instance_class = instance_class
        # A reserved parameter.
        self.supported_executor_list = supported_executor_list
        # The supported compute nodes.
        self.supported_node_count_list = supported_node_count_list
        # The description of the instance type.
        self.tips = tips

    def validate(self):
        if self.supported_executor_list:
            for k in self.supported_executor_list:
                if k:
                    k.validate()
        if self.supported_node_count_list:
            for k in self.supported_node_count_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        result['SupportedExecutorList'] = []
        if self.supported_executor_list is not None:
            for k in self.supported_executor_list:
                result['SupportedExecutorList'].append(k.to_map() if k else None)
        result['SupportedNodeCountList'] = []
        if self.supported_node_count_list is not None:
            for k in self.supported_node_count_list:
                result['SupportedNodeCountList'].append(k.to_map() if k else None)
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        self.supported_executor_list = []
        if m.get('SupportedExecutorList') is not None:
            for k in m.get('SupportedExecutorList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList()
                self.supported_executor_list.append(temp_model.from_map(k))
        self.supported_node_count_list = []
        if m.get('SupportedNodeCountList') is not None:
            for k in m.get('SupportedNodeCountList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList()
                self.supported_node_count_list.append(temp_model.from_map(k))
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList(TeaModel):
    def __init__(
        self,
        serial: str = None,
        supported_flexible_resource: List[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource] = None,
        supported_instance_class_list: List[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList] = None,
    ):
        # The supported edition. Valid values:
        # 
        # *   **basic**: Basic Edition.
        # *   **cluster**: Cluster Edition.
        # *   **mixed_storage**: elastic mode for Cluster Edition.
        self.serial = serial
        # The supported resources in elastic mode.
        self.supported_flexible_resource = supported_flexible_resource
        # The supported resources in reserved mode.
        self.supported_instance_class_list = supported_instance_class_list

    def validate(self):
        if self.supported_flexible_resource:
            for k in self.supported_flexible_resource:
                if k:
                    k.validate()
        if self.supported_instance_class_list:
            for k in self.supported_instance_class_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial is not None:
            result['Serial'] = self.serial
        result['SupportedFlexibleResource'] = []
        if self.supported_flexible_resource is not None:
            for k in self.supported_flexible_resource:
                result['SupportedFlexibleResource'].append(k.to_map() if k else None)
        result['SupportedInstanceClassList'] = []
        if self.supported_instance_class_list is not None:
            for k in self.supported_instance_class_list:
                result['SupportedInstanceClassList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Serial') is not None:
            self.serial = m.get('Serial')
        self.supported_flexible_resource = []
        if m.get('SupportedFlexibleResource') is not None:
            for k in m.get('SupportedFlexibleResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource()
                self.supported_flexible_resource.append(temp_model.from_map(k))
        self.supported_instance_class_list = []
        if m.get('SupportedInstanceClassList') is not None:
            for k in m.get('SupportedInstanceClassList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList()
                self.supported_instance_class_list.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode(TeaModel):
    def __init__(
        self,
        mode: str = None,
        supported_serial_list: List[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList] = None,
    ):
        # The supported mode. Valid values:
        # 
        # *   **flexible**: elastic mode.
        # *   **reserver**: reserved mode.
        self.mode = mode
        # The supported editions.
        self.supported_serial_list = supported_serial_list

    def validate(self):
        if self.supported_serial_list:
            for k in self.supported_serial_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        result['SupportedSerialList'] = []
        if self.supported_serial_list is not None:
            for k in self.supported_serial_list:
                result['SupportedSerialList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        self.supported_serial_list = []
        if m.get('SupportedSerialList') is not None:
            for k in m.get('SupportedSerialList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList()
                self.supported_serial_list.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneList(TeaModel):
    def __init__(
        self,
        supported_compute_resource: List[str] = None,
        supported_mode: List[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode] = None,
        supported_storage_resource: List[str] = None,
        zone_id: str = None,
    ):
        # A reserved parameter.
        self.supported_compute_resource = supported_compute_resource
        # The supported modes.
        self.supported_mode = supported_mode
        # A reserved parameter.
        self.supported_storage_resource = supported_storage_resource
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.supported_mode:
            for k in self.supported_mode:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_compute_resource is not None:
            result['SupportedComputeResource'] = self.supported_compute_resource
        result['SupportedMode'] = []
        if self.supported_mode is not None:
            for k in self.supported_mode:
                result['SupportedMode'].append(k.to_map() if k else None)
        if self.supported_storage_resource is not None:
            result['SupportedStorageResource'] = self.supported_storage_resource
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedComputeResource') is not None:
            self.supported_compute_resource = m.get('SupportedComputeResource')
        self.supported_mode = []
        if m.get('SupportedMode') is not None:
            for k in m.get('SupportedMode'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode()
                self.supported_mode.append(temp_model.from_map(k))
        if m.get('SupportedStorageResource') is not None:
            self.supported_storage_resource = m.get('SupportedStorageResource')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(
        self,
        available_zone_list: List[DescribeAvailableResourceResponseBodyAvailableZoneList] = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The supported zones.
        self.available_zone_list = available_zone_list
        # The resources available in the supported editions.
        self.region_id = region_id
        # The supported edition. Valid values:
        # 
        # *   **basic**: Basic Edition
        # *   **cluster**: Cluster Edition
        # *   **mixed_storage**: elastic mode for Cluster Edition
        self.request_id = request_id

    def validate(self):
        if self.available_zone_list:
            for k in self.available_zone_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZoneList'] = []
        if self.available_zone_list is not None:
            for k in self.available_zone_list:
                result['AvailableZoneList'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone_list = []
        if m.get('AvailableZoneList') is not None:
            for k in m.get('AvailableZoneList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneList()
                self.available_zone_list.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableResourceResponseBody = None,
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
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        enable_backup_log: str = None,
        log_backup_retention_period: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        request_id: str = None,
    ):
        # The number of days for which data backup files are retained.
        self.backup_retention_period = backup_retention_period
        # Specifies whether to enable the origin protocol policy.
        # 
        # *   true: enabled
        # *   false: disabled
        self.enable_backup_log = enable_backup_log
        # The number of days for which log backup files are retained.
        self.log_backup_retention_period = log_backup_retention_period
        # The cycle based on which backups are performed. If more than one day of the week is specified, the days of the week are separated by commas (,). Valid values:
        # 
        # *   Monday
        # *   Tuesday
        # *   Wednesday
        # *   Thursday
        # *   Friday
        # *   Saturday
        # *   Sunday
        self.preferred_backup_period = preferred_backup_period
        # The backup time. Specify the time in the HH:mmZ-HH:mmZ format.
        self.preferred_backup_time = preferred_backup_time
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        dbcluster_id: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The ID of the backup set.
        self.backup_id = backup_id
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupsResponseBodyItemsBackup(TeaModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_method: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_type: str = None,
        dbcluster_id: str = None,
    ):
        # The end time of the backup.
        self.backup_end_time = backup_end_time
        # The backup set ID.
        self.backup_id = backup_id
        # The backup method. Only Snapshot is returned.
        self.backup_method = backup_method
        # The size of the backup set. Unit: bytes.
        self.backup_size = backup_size
        # The start time of the backup.
        self.backup_start_time = backup_start_time
        # The backup type. Valid values:
        # 
        # *   **FullBackup**\
        # *   **IncrementalBackup**\
        self.backup_type = backup_type
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id

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
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeBackupsResponseBodyItems(TeaModel):
    def __init__(
        self,
        backup: List[DescribeBackupsResponseBodyItemsBackup] = None,
    ):
        self.backup = backup

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k in m.get('Backup'):
                temp_model = DescribeBackupsResponseBodyItemsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeBackupsResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The queried backup sets.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('Items') is not None:
            temp_model = DescribeBackupsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
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


class DescribeColumnsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsResponseBodyItemsColumn(TeaModel):
    def __init__(
        self,
        auto_increment_column: bool = None,
        column_name: str = None,
        dbcluster_id: str = None,
        primary_key: bool = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        # Indicates whether the columns are auto-incremented.
        self.auto_increment_column = auto_increment_column
        # The name of the column.
        self.column_name = column_name
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # Indicates whether the column is a primary key.
        self.primary_key = primary_key
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name
        # The data type of the column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment_column is not None:
            result['AutoIncrementColumn'] = self.auto_increment_column
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrementColumn') is not None:
            self.auto_increment_column = m.get('AutoIncrementColumn')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeColumnsResponseBodyItems(TeaModel):
    def __init__(
        self,
        column: List[DescribeColumnsResponseBodyItemsColumn] = None,
    ):
        self.column = column

    def validate(self):
        if self.column:
            for k in self.column:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Column'] = []
        if self.column is not None:
            for k in self.column:
                result['Column'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k in m.get('Column'):
                temp_model = DescribeColumnsResponseBodyItemsColumn()
                self.column.append(temp_model.from_map(k))
        return self


class DescribeColumnsResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeColumnsResponseBodyItems = None,
        request_id: str = None,
    ):
        # The list of columns.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeColumnsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeColumnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeColumnsResponseBody = None,
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
            temp_model = DescribeColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComputeResourceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbcluster_version: str = None,
        migrate: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The version of the AnalyticDB for MySQL Data Warehouse Edition cluster. Set the value to **3**.
        self.dbcluster_version = dbcluster_version
        # The available computing resources for migrating AnalyticDB MySQL Data Warehouse Edition to AnalyticDB MySQL Lakehouse Edition. Possible values are:
        # - **true**\
        # - **false**(default value)
        self.migrate = migrate
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The zone ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~129857~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version
        if self.migrate is not None:
            result['Migrate'] = self.migrate
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')
        if m.get('Migrate') is not None:
            self.migrate = m.get('Migrate')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeComputeResourceResponseBodyComputeResource(TeaModel):
    def __init__(
        self,
        display_value: str = None,
        real_value: str = None,
    ):
        # The specifications of computing resources displayed in the console.
        self.display_value = display_value
        # The actual specifications of computing resources.
        self.real_value = real_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_value is not None:
            result['DisplayValue'] = self.display_value
        if self.real_value is not None:
            result['RealValue'] = self.real_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayValue') is not None:
            self.display_value = m.get('DisplayValue')
        if m.get('RealValue') is not None:
            self.real_value = m.get('RealValue')
        return self


class DescribeComputeResourceResponseBody(TeaModel):
    def __init__(
        self,
        compute_resource: List[DescribeComputeResourceResponseBodyComputeResource] = None,
        request_id: str = None,
    ):
        # The queried specifications of computing resources.
        self.compute_resource = compute_resource
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.compute_resource:
            for k in self.compute_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComputeResource'] = []
        if self.compute_resource is not None:
            for k in self.compute_resource:
                result['ComputeResource'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compute_resource = []
        if m.get('ComputeResource') is not None:
            for k in m.get('ComputeResource'):
                temp_model = DescribeComputeResourceResponseBodyComputeResource()
                self.compute_resource.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComputeResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeComputeResourceResponseBody = None,
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
            temp_model = DescribeComputeResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConnectionCountRecordsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeConnectionCountRecordsResponseBodyAccessIpRecords(TeaModel):
    def __init__(
        self,
        access_ip: str = None,
        count: int = None,
    ):
        # The IP address of the client.
        self.access_ip = access_ip
        # The number of connections.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeConnectionCountRecordsResponseBodyUserRecords(TeaModel):
    def __init__(
        self,
        count: int = None,
        user: str = None,
    ):
        # The number of connections.
        self.count = count
        # The username of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeConnectionCountRecordsResponseBody(TeaModel):
    def __init__(
        self,
        access_ip_records: List[DescribeConnectionCountRecordsResponseBodyAccessIpRecords] = None,
        dbcluster_id: str = None,
        request_id: str = None,
        user_records: List[DescribeConnectionCountRecordsResponseBodyUserRecords] = None,
    ):
        # The queried client IP addresses.
        self.access_ip_records = access_ip_records
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The queried database accounts.
        self.user_records = user_records

    def validate(self):
        if self.access_ip_records:
            for k in self.access_ip_records:
                if k:
                    k.validate()
        if self.user_records:
            for k in self.user_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessIpRecords'] = []
        if self.access_ip_records is not None:
            for k in self.access_ip_records:
                result['AccessIpRecords'].append(k.to_map() if k else None)
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserRecords'] = []
        if self.user_records is not None:
            for k in self.user_records:
                result['UserRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_ip_records = []
        if m.get('AccessIpRecords') is not None:
            for k in m.get('AccessIpRecords'):
                temp_model = DescribeConnectionCountRecordsResponseBodyAccessIpRecords()
                self.access_ip_records.append(temp_model.from_map(k))
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_records = []
        if m.get('UserRecords') is not None:
            for k in m.get('UserRecords'):
                temp_model = DescribeConnectionCountRecordsResponseBodyUserRecords()
                self.user_records.append(temp_model.from_map(k))
        return self


class DescribeConnectionCountRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeConnectionCountRecordsResponseBody = None,
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
            temp_model = DescribeConnectionCountRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAccessWhiteListRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterAccessWhiteListResponseBodyItemsIPArray(TeaModel):
    def __init__(
        self,
        dbcluster_iparray_attribute: str = None,
        dbcluster_iparray_name: str = None,
        security_iplist: str = None,
    ):
        # The attribute of the IP address whitelist. By default, this parameter is empty.
        # 
        # >  The IP address whitelists that have the **hidden** attribute are not displayed in the console. These IP address whitelists are used to access services such as Data Transmission Service (DTS) and PolarDB-X.
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        # The name of the IP address whitelist.
        # 
        # *   The name of an IP address whitelist must be 2 to 32 characters in length. The name can contain lowercase letters, digits, and underscores (\_). The name must start with a lowercase letter and end with a lowercase letter or digit.
        # *   Each cluster supports up to 50 IP address whitelists.
        self.dbcluster_iparray_name = dbcluster_iparray_name
        # The IP addresses in the IP address whitelist. Up to 1,000 IP addresses can be returned. Multiple IP addresses are separated by commas (,).
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeDBClusterAccessWhiteListResponseBodyItems(TeaModel):
    def __init__(
        self,
        iparray: List[DescribeDBClusterAccessWhiteListResponseBodyItemsIPArray] = None,
    ):
        self.iparray = iparray

    def validate(self):
        if self.iparray:
            for k in self.iparray:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IPArray'] = []
        if self.iparray is not None:
            for k in self.iparray:
                result['IPArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.iparray = []
        if m.get('IPArray') is not None:
            for k in m.get('IPArray'):
                temp_model = DescribeDBClusterAccessWhiteListResponseBodyItemsIPArray()
                self.iparray.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAccessWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDBClusterAccessWhiteListResponseBodyItems = None,
        request_id: str = None,
    ):
        # The queried IP address whitelists.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBClusterAccessWhiteListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterAccessWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterAccessWhiteListResponseBody = None,
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
            temp_model = DescribeDBClusterAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAttributeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # >  You can call the [TagResources](~~179253~~) operation to add a tag to the cluster.
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


class DescribeDBClusterAttributeResponseBodyItemsDBClusterTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAttributeResponseBodyItemsDBCluster(TeaModel):
    def __init__(
        self,
        category: str = None,
        commodity_code: str = None,
        compute_resource: str = None,
        connection_string: str = None,
        creation_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbcluster_type: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnode_storage: int = None,
        dbversion: str = None,
        disk_encryption: str = None,
        disk_performance_level: str = None,
        disk_type: str = None,
        dts_job_id: str = None,
        elastic_ioresource: int = None,
        elastic_ioresource_size: str = None,
        enable_airflow: bool = None,
        enable_spark: bool = None,
        engine: str = None,
        engine_version: str = None,
        executor_count: str = None,
        expire_time: str = None,
        expired: str = None,
        inner_ip: str = None,
        inner_port: str = None,
        kms_id: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_time: str = None,
        mode: str = None,
        pay_type: str = None,
        port: int = None,
        rds_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_resource: str = None,
        tags: DescribeDBClusterAttributeResponseBodyItemsDBClusterTags = None,
        user_enistatus: bool = None,
        vpccloud_instance_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The edition of the cluster. Valid values:
        # 
        # *   **BASIC**: reserved mode for Basic Edition.
        # *   **CLUSTER**: reserved mode for Cluster Edition.
        # *   **MIXED_STORAGE**: elastic mode for Cluster Edition.
        # 
        # >  For more information about cluster editions, see [Editions](~~205001~~).
        self.category = category
        # The billing method of the cluster. Valid values:
        # 
        # *   **ads**: pay-as-you-go.
        # *   **ads_pre**: subscription.
        self.commodity_code = commodity_code
        # The specifications of computing resources that are used in the cluster in elastic mode. Computing resources are used to compute data. The increase in the computing resources can accelerate queries. You can scale computing resources based on your business requirements.
        self.compute_resource = compute_resource
        # The Virtual Private Cloud (VPC) endpoint that is used to connect to the cluster.
        self.connection_string = connection_string
        # The time when the cluster was created. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the cluster.
        self.dbcluster_description = dbcluster_description
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The network type of the cluster. **VPC** is returned.
        self.dbcluster_network_type = dbcluster_network_type
        # The state of the cluster. For more information, see [Cluster states](~~143075~~).
        self.dbcluster_status = dbcluster_status
        # The cluster type. Valid values:
        # 
        # *   **Common**: common cluster.
        # *   **RDS_ANALYSIS**: MySQL analytic instance.
        self.dbcluster_type = dbcluster_type
        # The instance type of the cluster.
        self.dbnode_class = dbnode_class
        # The number of node groups.
        self.dbnode_count = dbnode_count
        # The storage capacity of the cluster. Unit: GB.
        self.dbnode_storage = dbnode_storage
        # The engine version of the cluster. **3.0** is returned.
        self.dbversion = dbversion
        # Indicates whether disk encryption is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.disk_encryption = disk_encryption
        # The ESSD performance level.
        self.disk_performance_level = disk_performance_level
        # The disk type of the cluster. Valid values:
        # 
        # *   **local_ssd**: local disk.
        # *   **cloud**: basic disk.
        # *   **cloud_ssd**: standard SSD.
        # *   **cloud_efficiency**: ultra disk.
        # *   **cloud_essd0**: PL0 enhanced SSD (ESSD).
        # *   **cloud_essd**: PL1 ESSD.
        # *   **cloud_essd2**: PL2 ESSD.
        # *   **cloud_essd3**: PL3 ESSD.
        # 
        # >  For more information about ESSDs, see [ESSDs](~~122389~~).
        self.disk_type = disk_type
        # The ID of the Data Transmission Service (DTS) synchronization job. This parameter is returned only for MySQL analytic instances.
        self.dts_job_id = dts_job_id
        # The number of elastic I/O units (EIUs).
        self.elastic_ioresource = elastic_ioresource
        # The single-node specifications of an EIU. Valid values:
        # 
        # *   8Core64GB: If this value is returned, the specifications of an EIU are 24 cores and 192 GB memory.
        # *   12Core96GB: If this value is returned, the specifications of an EIU are 36 cores and 288 GB memory.
        self.elastic_ioresource_size = elastic_ioresource_size
        # Indicates whether an Airflow cluster was created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_airflow = enable_airflow
        # Indicates whether a Spark cluster was created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_spark = enable_spark
        # The engine of the cluster. **AnalyticDB** is returned.
        self.engine = engine
        # The minor version of the cluster.
        self.engine_version = engine_version
        # The number of compute nodes that are used by the cluster in elastic mode.
        self.executor_count = executor_count
        # The expiration time of the cluster. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC. Example: *2999-09-08T16:00:00Z*.
        # 
        # > 
        # 
        # *   If the billing method of the cluster is subscription, the actual expiration time is returned.
        # 
        # *   If the billing method of the cluster is pay-as-you-go, **2999-09-08T16:00:00Z** is returned.
        self.expire_time = expire_time
        # Indicates whether the cluster has expired. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.expired = expired
        # The public IP address of the cluster.
        self.inner_ip = inner_ip
        # The public port number.
        self.inner_port = inner_port
        # The ID of the key that is used to encrypt disk data.
        # 
        # >  This parameter is returned only when disk encryption is enabled.
        self.kms_id = kms_id
        # The lock mode of the cluster. Valid values:
        # 
        # *   **Unlock**: The cluster is not locked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The cluster is automatically locked due to cluster expiration.
        # *   **LockByRestoration**: The cluster is automatically locked due to cluster restoration.
        # *   **LockByDiskQuota**: The cluster is automatically locked when 90% of the cluster storage is used.
        self.lock_mode = lock_mode
        # The reason why the cluster is locked.
        # 
        # >  This parameter is returned only when the cluster was locked. **instance_expire** is returned.
        self.lock_reason = lock_reason
        # The maintenance window of the cluster. The time is displayed in the *HH:mmZ-HH:mmZ* format in UTC. An example is *04:00Z-05:00Z*, which indicates that routine maintenance is performed from 04:00 to 05:00.
        # 
        # >  For more information about maintenance windows, see [Configure a maintenance window](~~122569~~).
        self.maintain_time = maintain_time
        # The mode of the cluster. Valid values:
        # 
        # *   **flexible**: elastic mode.
        # *   **reserver**: reserved mode.
        # 
        # >  For more information about cluster modes, see [Editions](~~205001~~).
        self.mode = mode
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type
        # The port number that is used to connect to the cluster.
        self.port = port
        # The ID of the ApsaraDB RDS instance from which data is synchronized to the cluster. This parameter is returned only for MySQL analytic instances.
        self.rds_instance_id = rds_instance_id
        # The region ID of the cluster.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The specifications of storage resources that are used in the cluster in elastic mode. Storage resources are used to read and write data. The increase in the storage resources can improve the read and write performance of the cluster.
        self.storage_resource = storage_resource
        # The tags that are added to the cluster.
        self.tags = tags
        # Indicates whether Elastic Network Interface (ENI) is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.user_enistatus = user_enistatus
        # The ID of the cluster that resides in the VPC.
        self.vpccloud_instance_id = vpccloud_instance_id
        # The VPC ID of the cluster.
        self.vpcid = vpcid
        # The vSwitch ID of the cluster.
        self.v_switch_id = v_switch_id
        # The zone ID of the cluster.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.disk_encryption is not None:
            result['DiskEncryption'] = self.disk_encryption
        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.elastic_ioresource_size is not None:
            result['ElasticIOResourceSize'] = self.elastic_ioresource_size
        if self.enable_airflow is not None:
            result['EnableAirflow'] = self.enable_airflow
        if self.enable_spark is not None:
            result['EnableSpark'] = self.enable_spark
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip
        if self.inner_port is not None:
            result['InnerPort'] = self.inner_port
        if self.kms_id is not None:
            result['KmsId'] = self.kms_id
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.rds_instance_id is not None:
            result['RdsInstanceId'] = self.rds_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.user_enistatus is not None:
            result['UserENIStatus'] = self.user_enistatus
        if self.vpccloud_instance_id is not None:
            result['VPCCloudInstanceId'] = self.vpccloud_instance_id
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('DiskEncryption') is not None:
            self.disk_encryption = m.get('DiskEncryption')
        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('ElasticIOResourceSize') is not None:
            self.elastic_ioresource_size = m.get('ElasticIOResourceSize')
        if m.get('EnableAirflow') is not None:
            self.enable_airflow = m.get('EnableAirflow')
        if m.get('EnableSpark') is not None:
            self.enable_spark = m.get('EnableSpark')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')
        if m.get('InnerPort') is not None:
            self.inner_port = m.get('InnerPort')
        if m.get('KmsId') is not None:
            self.kms_id = m.get('KmsId')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RdsInstanceId') is not None:
            self.rds_instance_id = m.get('RdsInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('Tags') is not None:
            temp_model = DescribeDBClusterAttributeResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UserENIStatus') is not None:
            self.user_enistatus = m.get('UserENIStatus')
        if m.get('VPCCloudInstanceId') is not None:
            self.vpccloud_instance_id = m.get('VPCCloudInstanceId')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClusterAttributeResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbcluster: List[DescribeDBClusterAttributeResponseBodyItemsDBCluster] = None,
    ):
        self.dbcluster = dbcluster

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClusterAttributeResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAttributeResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDBClusterAttributeResponseBodyItems = None,
        request_id: str = None,
    ):
        # The queried cluster information.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBClusterAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterAttributeResponseBody = None,
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
            temp_model = DescribeDBClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterHealthStatusRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBClusterHealthStatusResponseBodyCS(TeaModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        # The number of healthy access nodes.
        self.active_count = active_count
        # The total number of access nodes.
        self.expected_count = expected_count
        # The number of risky access nodes.
        self.risk_count = risk_count
        # The health state of access nodes. Valid values:
        # 
        # *   **RISK**: risky
        # *   **NORMAL**: healthy
        # *   **UNAVAILABLE**: unavailable
        self.status = status
        # The number of unavailable access nodes.
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.status is not None:
            result['Status'] = self.status
        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')
        return self


class DescribeDBClusterHealthStatusResponseBodyExecutor(TeaModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        # The number of healthy compute node groups.
        self.active_count = active_count
        # The total number of compute node groups.
        self.expected_count = expected_count
        # The number of risky compute node groups.
        self.risk_count = risk_count
        # The health state of compute node groups. Valid values:
        # 
        # *   **RISK**: risky
        # *   **NORMAL**: healthy
        # *   **UNAVAILABLE**: unavailable
        self.status = status
        # The number of unavailable compute node groups.
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.status is not None:
            result['Status'] = self.status
        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')
        return self


class DescribeDBClusterHealthStatusResponseBodyWorker(TeaModel):
    def __init__(
        self,
        active_count: int = None,
        expected_count: int = None,
        risk_count: int = None,
        status: str = None,
        unavailable_count: int = None,
    ):
        # The number of healthy storage node groups.
        self.active_count = active_count
        # The total number of storage node groups.
        self.expected_count = expected_count
        # The number of risky storage node groups.
        self.risk_count = risk_count
        # The health state of storage node groups. Valid values:
        # 
        # *   **RISK**: risky
        # *   **NORMAL**: healthy
        # *   **UNAVAILABLE**: unavailable
        self.status = status
        # The number of unavailable storage node groups.
        self.unavailable_count = unavailable_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        if self.expected_count is not None:
            result['ExpectedCount'] = self.expected_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.status is not None:
            result['Status'] = self.status
        if self.unavailable_count is not None:
            result['UnavailableCount'] = self.unavailable_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        if m.get('ExpectedCount') is not None:
            self.expected_count = m.get('ExpectedCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnavailableCount') is not None:
            self.unavailable_count = m.get('UnavailableCount')
        return self


class DescribeDBClusterHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        cs: DescribeDBClusterHealthStatusResponseBodyCS = None,
        executor: DescribeDBClusterHealthStatusResponseBodyExecutor = None,
        instance_status: str = None,
        request_id: str = None,
        worker: DescribeDBClusterHealthStatusResponseBodyWorker = None,
    ):
        # Health state details of access nodes.
        self.cs = cs
        # Health state details of compute node groups.
        self.executor = executor
        # The health state of the cluster. Valid values:
        # 
        # *   **RISK**: risky
        # 
        # *   **NORMAL**: healthy
        # 
        # *   **UNAVAILABLE**: unavailable
        # 
        # > If the health states of access nodes, compute node groups, and storage node groups are all **healthy** and the cluster is detected to be alive, the health state of the cluster is **healthy**. If the preceding three health states include **risky**, the health state of the cluster is **risky**. If the preceding three health states include **unavailable**, the health state of the cluster is **unavailable**.
        self.instance_status = instance_status
        # The ID of the request.
        self.request_id = request_id
        # Health state details of storage node groups.
        self.worker = worker

    def validate(self):
        if self.cs:
            self.cs.validate()
        if self.executor:
            self.executor.validate()
        if self.worker:
            self.worker.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cs is not None:
            result['CS'] = self.cs.to_map()
        if self.executor is not None:
            result['Executor'] = self.executor.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.worker is not None:
            result['Worker'] = self.worker.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CS') is not None:
            temp_model = DescribeDBClusterHealthStatusResponseBodyCS()
            self.cs = temp_model.from_map(m['CS'])
        if m.get('Executor') is not None:
            temp_model = DescribeDBClusterHealthStatusResponseBodyExecutor()
            self.executor = temp_model.from_map(m['Executor'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Worker') is not None:
            temp_model = DescribeDBClusterHealthStatusResponseBodyWorker()
            self.worker = temp_model.from_map(m['Worker'])
        return self


class DescribeDBClusterHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterHealthStatusResponseBody = None,
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
            temp_model = DescribeDBClusterHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterNetInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterNetInfoResponseBodyItemsAddress(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        connection_string_prefix: str = None,
        ipaddress: str = None,
        net_type: str = None,
        port: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The endpoint of the cluster.
        self.connection_string = connection_string
        # The prefix of the cluster endpoint.
        self.connection_string_prefix = connection_string_prefix
        # The IP address.
        self.ipaddress = ipaddress
        # The network type of the endpoint. Valid values:
        # 
        # *   **Public**: public endpoint
        # *   **VPC**: Virtual Private Cloud (VPC) endpoint
        self.net_type = net_type
        # The port number that is used to connect to the cluster.
        self.port = port
        # The ID of the VPC.
        # 
        # >  This parameter is empty when Public is returned for NetType.
        self.vpcid = vpcid
        # The ID of the vSwitch.
        # 
        # >  This parameter is empty when Public is returned for NetType.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeDBClusterNetInfoResponseBodyItems(TeaModel):
    def __init__(
        self,
        address: List[DescribeDBClusterNetInfoResponseBodyItemsAddress] = None,
    ):
        self.address = address

    def validate(self):
        if self.address:
            for k in self.address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Address'] = []
        if self.address is not None:
            for k in self.address:
                result['Address'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address = []
        if m.get('Address') is not None:
            for k in m.get('Address'):
                temp_model = DescribeDBClusterNetInfoResponseBodyItemsAddress()
                self.address.append(temp_model.from_map(k))
        return self


class DescribeDBClusterNetInfoResponseBody(TeaModel):
    def __init__(
        self,
        cluster_network_type: str = None,
        items: DescribeDBClusterNetInfoResponseBodyItems = None,
        request_id: str = None,
    ):
        # The network type of the cluster.
        self.cluster_network_type = cluster_network_type
        # The network information of the cluster.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')
        if m.get('Items') is not None:
            temp_model = DescribeDBClusterNetInfoResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterNetInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterNetInfoResponseBody = None,
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
            temp_model = DescribeDBClusterNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        key: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pools: str = None,
        start_time: str = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        # 
        # > The end time must be later than the start time. The maximum time range that can be specified is two days.
        self.end_time = end_time
        # The performance metrics to be queried. Separate multiple values with commas (,). Valid values:
        # 
        # *   CPU
        # 
        #     *   **AnalyticDB_CPU**: the average CPU utilization.
        # 
        # *   Connections
        # 
        #     *   **AnalyticDB_Connections**: the number of database connections.
        # 
        # *   Writes
        # 
        #     *   **AnalyticDB_TPS**: the write transactions per second (TPS).
        #     *   **AnalyticDB_InsertRT**: the write response time.
        #     *   **AnalyticDB_InsertBytes**: the write throughput.
        # 
        # *   Updates
        # 
        #     *   **AnalyticDB_UpdateRT**: the update response time.
        # 
        # *   Deletion
        # 
        #     *   **AnalyticDB_DeleteRT**: the delete response time.
        # 
        # *   Queries
        # 
        #     *   **AnalyticDB_QPS**: the queries per second (QPS).
        #     *   **AnalyticDB_QueryRT**: the query response time.
        #     *   **AnalyticDB_QueryWaitTime**: the query wait time.
        # 
        # *   Disks
        # 
        #     *   **AnalyticDB_IO**: the disk I/O throughput.
        #     *   **AnalyticDB_IO_UTIL**: the I/O utilization.
        #     *   **AnalyticDB_IO_WAIT**: the I/O wait time.
        #     *   **AnalyticDB_IOPS**: the disk input/output operations per second (IOPS).
        #     *   **AnalyticDB_DiskUsage**: the disk space that is used.
        #     *   **AnalyticDB_HotDataDiskUsage**: the disk space that is used by hot data.
        #     *   **AnalyticDB_ColdDataDiskUsage**: the disk space that is used by cold data.
        # 
        # >  If you leave this parameter empty, the values of all the preceding performance metrics are returned.
        self.key = key
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the resource group.
        self.resource_pools = resource_pools
        # The start time of the query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_pools is not None:
            result['ResourcePools'] = self.resource_pools
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourcePools') is not None:
            self.resource_pools = m.get('ResourcePools')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformancesSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        tags: str = None,
        values: List[str] = None,
    ):
        # The name of the performance metric value.
        self.name = name
        # The tags that are added to the cluster.
        self.tags = tags
        # The values of the queried performance metrics.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        key: str = None,
        series: List[DescribeDBClusterPerformanceResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        # The name of the performance metric.
        self.key = key
        # The queried performance metric data.
        self.series = series
        # The unit of the performance metrics.
        self.unit = unit

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performances: List[DescribeDBClusterPerformanceResponseBodyPerformances] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.end_time = end_time
        # The queried performance metrics.
        self.performances = performances
        # The request ID.
        self.request_id = request_id
        # The start time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterPerformanceResponseBody = None,
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
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterResourcePoolPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        key: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pools: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to monitor the resource group. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        self.end_time = end_time
        # The metrics of the resource group. You can enter multiple metrics at the same time to query the monitoring information. Separate multiple metrics with commas (,). Valid values:
        # 
        # *   **AnalyticDB_RP_CPU**: the average CPU utilization. Unit: %.
        # *   **AnalyticDB_RP_RT**: the query response time (RT). Unit: milliseconds.
        # *   **AnalyticDB_RP_QPS**: the queries per second (QPS). The value of this parameter must be a numeric value.
        # *   **AnalyticDB_RP_WaitTime**: the query waiting time. Unit: milliseconds.
        # *   **AnalyticDB_RP_OriginalNode**: the number of basic nodes in the resource group.
        # *   **AnalyticDB_RP_ActualNode**: the number of scheduled nodes that are scaled out in the resource group.
        # *   **AnalyticDB_RP_PlanNode**: the number of scheduled nodes to be scaled out in the resource group.
        # *   **AnalyticDB_RP_TotalNode**: the total number of nodes in the resource group. Total number of nodes = Number of basic nodes + Number of scheduled nodes that are scaled out.
        # 
        # > 
        # 
        # *   If you leave this parameter empty, the monitoring information about all metrics is returned.
        # 
        # *   For more information about scaling plans, see [Create a resource scaling plan](~~189507~~).
        self.key = key
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The names of the resource groups that you want to query. You can enter multiple names of resource groups. Separate multiple names with commas (,).
        # 
        # > 
        # 
        # *   The value of this parameter is case-insensitive. For example, `USER_DEFAULT` and `user_default` specify the same resource group.
        # 
        # *   If you leave this parameter empty, the monitoring information about the `USER_DEFAULT` resource group is returned.
        self.resource_pools = resource_pools
        # The beginning of the time range to monitor the resource group. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        # 
        # > You can view only the monitoring information about the resource groups within the last two days.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_pools is not None:
            result['ResourcePools'] = self.resource_pools
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourcePools') is not None:
            self.resource_pools = m.get('ResourcePools')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # The name of the metric.
        self.name = name
        # The value of the metric.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances(TeaModel):
    def __init__(
        self,
        resource_pool_name: str = None,
        resource_pool_series: List[DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries] = None,
    ):
        # The name of the resource group.
        self.resource_pool_name = resource_pool_name
        # The sequential monitoring information about the resource groups.
        self.resource_pool_series = resource_pool_series

    def validate(self):
        if self.resource_pool_series:
            for k in self.resource_pool_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        result['ResourcePoolSeries'] = []
        if self.resource_pool_series is not None:
            for k in self.resource_pool_series:
                result['ResourcePoolSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        self.resource_pool_series = []
        if m.get('ResourcePoolSeries') is not None:
            for k in m.get('ResourcePoolSeries'):
                temp_model = DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries()
                self.resource_pool_series.append(temp_model.from_map(k))
        return self


class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        key: str = None,
        resource_pool_performances: List[DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances] = None,
        unit: str = None,
    ):
        # The metric of the resource group.
        self.key = key
        # The queried monitoring information about the resource groups.
        self.resource_pool_performances = resource_pool_performances
        # The unit of the metric value.
        self.unit = unit

    def validate(self):
        if self.resource_pool_performances:
            for k in self.resource_pool_performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['ResourcePoolPerformances'] = []
        if self.resource_pool_performances is not None:
            for k in self.resource_pool_performances:
                result['ResourcePoolPerformances'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.resource_pool_performances = []
        if m.get('ResourcePoolPerformances') is not None:
            for k in m.get('ResourcePoolPerformances'):
                temp_model = DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances()
                self.resource_pool_performances.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDBClusterResourcePoolPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performances: List[DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end of the time range for monitoring the resource group. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.end_time = end_time
        # The queried monitoring information about the metrics.
        self.performances = performances
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range for monitoring the resource group. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterResourcePoolPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterResourcePoolPerformanceResponseBody = None,
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
            temp_model = DescribeDBClusterResourcePoolPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterStatusRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # >  You can call [DescribeRegions](~~143074~~) to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The states of clusters. Valid values:
        # 
        # *   **Preparing**: The cluster is being prepared.
        # *   **Creating**: The cluster is being created.
        # *   **Restoring**: The cluster is being restored from a backup.
        # *   **Running**: The cluster is running.
        # *   **Deleting**: The cluster is being deleted.
        # *   **ClassChanging**: The cluster configurations are being changed.
        # *   **NetAddressCreating**: A network connection is being created.
        # *   **NetAddressDeleting**: A network connection is being released.
        # *   **NetAddressModifying**: A network connection is being modified.
        # *   **EngineVersionUpgrading**: The engine version is being updated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDBClusterStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterStatusResponseBody = None,
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
            temp_model = DescribeDBClusterStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClustersRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that is added to the cluster. You can use tags to filter clusters. A tag is a key-value pair. You can specify up to 20 tags in one request. The letter N specifies the sequence number of each key-value pair and must be unique. The values of N must be consecutive integers that start from 1. Each value of `Tag.N.Key` is paired with a value of `Tag.N.Value`.
        # 
        # > The tag key can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.key = key
        # The value of tag N that is added to the cluster. You can use tags to filter clusters. A tag is a key-value pair. You can specify up to 20 tags in one request. The letter N specifies the sequence number of each key-value pair and must be unique. The values of N must be consecutive integers that start from 1. Each value of `Tag.N.Key` is paired with a value of `Tag.N.Value`.
        # 
        # > The tag key can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
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


class DescribeDBClustersRequest(TeaModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_ids: str = None,
        dbcluster_status: str = None,
        dbversion: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[DescribeDBClustersRequestTag] = None,
    ):
        # The description of the cluster.
        # 
        # *   The description cannot start with `http://` or `https://`.
        # *   The description must be 2 to 256 characters in length
        self.dbcluster_description = dbcluster_description
        # The cluster IDs.
        # 
        # > You can specify the ID of one cluster or IDs of more clusters within the preceding region.
        self.dbcluster_ids = dbcluster_ids
        # The state of the cluster. Valid values:
        # 
        # *   **Preparing**: The cluster is being prepared.
        # *   **Creating**: The cluster is being created.
        # *   **Restoring**: The cluster is being restored from a backup.
        # *   **Running**: The cluster is running.
        # *   **Deleting**: The cluster is being deleted.
        # *   **ClassChanging**: The cluster specifications are being changed.
        # *   **NetAddressCreating**: A network connection is being created.
        # *   **NetAddressDeleting**: A network connection is being deleted.
        self.dbcluster_status = dbcluster_status
        # The version of the cluster. Set the value to **3.0**.
        self.dbversion = dbversion
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The region ID of the clusters.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags that are added to the cluster.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyItemsDBClusterTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # >  You can call the [TagResources](~~179253~~) operation to add tags to a cluster.
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


class DescribeDBClustersResponseBodyItemsDBClusterTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeDBClustersResponseBodyItemsDBClusterTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBClustersResponseBodyItemsDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyItemsDBCluster(TeaModel):
    def __init__(
        self,
        category: str = None,
        commodity_code: str = None,
        compute_resource: str = None,
        connection_string: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbcluster_type: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnode_storage: int = None,
        dbversion: str = None,
        disk_type: str = None,
        dts_job_id: str = None,
        elastic_ioresource: int = None,
        engine: str = None,
        executor_count: str = None,
        expire_time: str = None,
        expired: str = None,
        inner_ip: str = None,
        inner_port: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        mode: str = None,
        pay_type: str = None,
        port: str = None,
        rds_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_resource: str = None,
        tags: DescribeDBClustersResponseBodyItemsDBClusterTags = None,
        vpccloud_instance_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The edition of the cluster. Valid values:
        # 
        # *   **BASIC**: reserved mode for Basic Edition.
        # *   **CLUSTER**: reserved mode for Cluster Edition.
        # *   **MIXED_STORAGE**: elastic mode for Cluster Edition.
        # 
        # >  For more information about cluster editions, see [Editions](~~205001~~).
        self.category = category
        # The commodity code. **ads** is returned.
        self.commodity_code = commodity_code
        # The specifications of computing resources that are used in the cluster in elastic mode. The increase of computing resources can speed up queries. You can adjust the value of this parameter to scale the cluster.
        self.compute_resource = compute_resource
        # The public endpoint that is used to connect to the cluster.
        self.connection_string = connection_string
        # The time when the cluster was created. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC. Example: *2021-04-01T09:50:18Z*.
        self.create_time = create_time
        # The description of the cluster.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The network type of the cluster. **VPC** is returned.
        self.dbcluster_network_type = dbcluster_network_type
        # The state of the cluster. For more information, see [Cluster states](~~143075~~).
        self.dbcluster_status = dbcluster_status
        # The type of the cluster. Valid values:
        # 
        # *   **Common**: common cluster.
        # *   **RDS_ANALYSIS**: MySQL analytic instance.
        self.dbcluster_type = dbcluster_type
        # The instance type of the cluster.
        self.dbnode_class = dbnode_class
        # The number of node groups.
        self.dbnode_count = dbnode_count
        # The storage capacity of the cluster. Unit: GB.
        self.dbnode_storage = dbnode_storage
        # The version of the database engine. **3.0** is returned.
        self.dbversion = dbversion
        # The disk type of the cluster. Valid values:
        # 
        # *   **local_ssd**: local disk.
        # *   **cloud**: basic disk.
        # *   **cloud_ssd**: standard SSD.
        # *   **cloud_efficiency**: ultra disk.
        # *   **cloud_essd**: PL0 enhanced SSD (ESSD).
        # *   **cloud_essd**: PL1 ESSD.
        # *   **cloud_essd2**: PL2 ESSD.
        # *   **cloud_essd3**: PL3 ESSD.
        # 
        # >  For more information, see [ESSDs](~~122389~~).
        self.disk_type = disk_type
        # The ID of the Data Transmission Service (DTS) synchronization task. This parameter is returned only for MySQL analytic instances.
        self.dts_job_id = dts_job_id
        # The number of elastic I/O units (EIUs). For more information, see [Use EIUs to scale up storage resources](~~189505~~).
        # 
        # >  This parameter is returned only for clusters in elastic mode.
        self.elastic_ioresource = elastic_ioresource
        # The engine of the cluster. **AnalyticDB** is returned.
        self.engine = engine
        # The number of compute nodes that are used by the cluster in elastic mode.
        self.executor_count = executor_count
        # The time when the cluster expires. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC. Example: *2999-09-08T16:00:00Z*.
        # 
        # > 
        # 
        # *   If the billing method of the cluster is subscription, the actual expiration time is returned.
        # 
        # *   If the billing method of the cluster is pay-as-you-go, **2999-09-08T16:00:00Z** is returned.
        self.expire_time = expire_time
        # Indicates whether the cluster has expired. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.expired = expired
        # The public IP address of the cluster.
        self.inner_ip = inner_ip
        # The port number that is used to connect to the cluster.
        self.inner_port = inner_port
        # The lock mode of the cluster. Valid values:
        # 
        # *   **Unlock**: The cluster is not locked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The cluster is automatically locked due to cluster expiration.
        # *   **LockByRestoration**: The cluster is automatically locked due to cluster restoration.
        # *   **LockByDiskQuota**: The cluster is automatically locked when it has used 90% of its storage.
        self.lock_mode = lock_mode
        # The reason why the cluster is locked.
        # 
        # >  This parameter is returned only when the cluster was locked. **instance_expire** is returned.
        self.lock_reason = lock_reason
        # The mode of the cluster. Valid values:
        # 
        # *   **flexible**: elastic mode.
        # *   **reserver**: reserved mode.
        # 
        # > 
        # 
        # *   For more information about cluster modes, see [Editions](~~205001~~).
        self.mode = mode
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type
        # The port number that is used to connect to the cluster. Default value: 3306.
        self.port = port
        # The ID of the ApsaraDB RDS instance from which data is synchronized to the cluster. This parameter is returned only for MySQL analytic instances.
        self.rds_instance_id = rds_instance_id
        # The region ID of the cluster.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The specifications of storage resources that are used in the cluster in elastic mode. These resources are used to read and write data. You can increase the value of this parameter to improve the read and write performance of the cluster.
        self.storage_resource = storage_resource
        # The tags that are added to the cluster.
        self.tags = tags
        # The ID of the cluster that is deployed in the VPC.
        self.vpccloud_instance_id = vpccloud_instance_id
        # The virtual private cloud (VPC) ID of the cluster.
        self.vpcid = vpcid
        # The vSwitch ID of the cluster.
        self.v_switch_id = v_switch_id
        # The zone ID of the cluster.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip
        if self.inner_port is not None:
            result['InnerPort'] = self.inner_port
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.rds_instance_id is not None:
            result['RdsInstanceId'] = self.rds_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpccloud_instance_id is not None:
            result['VPCCloudInstanceId'] = self.vpccloud_instance_id
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')
        if m.get('InnerPort') is not None:
            self.inner_port = m.get('InnerPort')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RdsInstanceId') is not None:
            self.rds_instance_id = m.get('RdsInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('Tags') is not None:
            temp_model = DescribeDBClustersResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VPCCloudInstanceId') is not None:
            self.vpccloud_instance_id = m.get('VPCCloudInstanceId')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClustersResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbcluster: List[DescribeDBClustersResponseBodyItemsDBCluster] = None,
    ):
        self.dbcluster = dbcluster

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClustersResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeDBClustersResponseBodyItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried clusters.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('Items') is not None:
            temp_model = DescribeDBClustersResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClustersResponseBody = None,
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
            temp_model = DescribeDBClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        self.group_name = group_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBResourceGroupResponseBodyGroupsInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        group_name: str = None,
        group_type: str = None,
        group_users: str = None,
        node_num: int = None,
        update_time: str = None,
    ):
        # The time when the resource group was created.
        self.create_time = create_time
        # The name of the resource group.
        self.group_name = group_name
        # The query execution mode. Valid values:
        # 
        # *   **interactive**\
        # *   **batch** (default)
        # 
        # > For more information, see [Query execution modes](~~189502~~).
        self.group_type = group_type
        # The database accounts that are associated with the resource group.
        self.group_users = group_users
        # The number of nodes. Each node provides 16 cores and 64 GB memory.
        self.node_num = node_num
        # The time when the resource group was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_users is not None:
            result['GroupUsers'] = self.group_users
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupUsers') is not None:
            self.group_users = m.get('GroupUsers')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDBResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        groups_info: List[DescribeDBResourceGroupResponseBodyGroupsInfo] = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried resource group.
        self.groups_info = groups_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.groups_info:
            for k in self.groups_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['GroupsInfo'] = []
        if self.groups_info is not None:
            for k in self.groups_info:
                result['GroupsInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.groups_info = []
        if m.get('GroupsInfo') is not None:
            for k in m.get('GroupsInfo'):
                temp_model = DescribeDBResourceGroupResponseBodyGroupsInfo()
                self.groups_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBResourceGroupResponseBody = None,
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
            temp_model = DescribeDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBResourcePoolRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the resource group.
        self.pool_name = pool_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBResourcePoolResponseBodyPoolsInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        node_num: int = None,
        pool_name: str = None,
        pool_users: str = None,
        query_type: str = None,
        update_time: str = None,
    ):
        # The time when the resource group was created.
        self.create_time = create_time
        # The number of nodes.
        # 
        # >  Each node consumes 16 cores and 64 GB memory.
        self.node_num = node_num
        # The name of the resource group.
        self.pool_name = pool_name
        # The database accounts that are associated with the resource group.
        self.pool_users = pool_users
        # The mode in which SQL statements are executed.
        # 
        # *   **batch**\
        # *   **interactive**\
        # 
        # >  For more information, see [Query execution modes](~~189502~~).
        self.query_type = query_type
        # The time when the resource group was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.pool_users is not None:
            result['PoolUsers'] = self.pool_users
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('PoolUsers') is not None:
            self.pool_users = m.get('PoolUsers')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDBResourcePoolResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        pools_info: List[DescribeDBResourcePoolResponseBodyPoolsInfo] = None,
        request_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # Details of the resource group.
        self.pools_info = pools_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.pools_info:
            for k in self.pools_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['PoolsInfo'] = []
        if self.pools_info is not None:
            for k in self.pools_info:
                result['PoolsInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.pools_info = []
        if m.get('PoolsInfo') is not None:
            for k in m.get('PoolsInfo'):
                temp_model = DescribeDBResourcePoolResponseBodyPoolsInfo()
                self.pools_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBResourcePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBResourcePoolResponseBody = None,
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
            temp_model = DescribeDBResourcePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisDimensionsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        lang: str = None,
        query_condition: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > 
        # 
        # *   The end time must be later than the start time.
        # 
        # *   The maximum time range that can be specified is 24 hours.
        self.end_time = end_time
        # The language of file titles and error messages. Valid values:
        # 
        # *   **zh** (default): simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The query condition for SQL statements, which can contain the `Type`, `Value`, and `Min` or `Max` fields. Specify the condition in the JSON format. `Type` specifies the query dimension. Valid values for Type: `maxCost`, `status`, and `cost`. `Value`, `Min`, or `Max` specifies the query range for the dimension. Valid values:
        # 
        # *   `{"Type":"maxCost","Value":"100"}`: queries the top 100 most time-consuming SQL statements. Set `Value` to 100.
        # *   `{"Type":"status","Value":"finished"}`: queries executed SQL statements. You can set `Value` to `running` to query SQL statements that are being executed. You can also set Value to `failed` to query SQL statements that failed to be executed.
        # *   `{"Type":"cost","Min":"10","Max":"200"}`: queries SQL statements whose execution durations are in the range of 10 to 200 milliseconds. You can also customize the maximum and minimum execution durations.
        self.query_condition = query_condition
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > Only data within the last 14 days can be queried. If you call this operation to query data that is earlier than 14 days, an empty string is returned.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDiagnosisDimensionsResponseBody(TeaModel):
    def __init__(
        self,
        client_ips: List[str] = None,
        databases: List[str] = None,
        request_id: str = None,
        resource_groups: List[str] = None,
        user_names: List[str] = None,
    ):
        # The source IP addresses.
        self.client_ips = client_ips
        # The databases.
        self.databases = databases
        # The request ID.
        self.request_id = request_id
        # The resource groups.
        self.resource_groups = resource_groups
        # The usernames.
        self.user_names = user_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ips is not None:
            result['ClientIps'] = self.client_ips
        if self.databases is not None:
            result['Databases'] = self.databases
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups
        if self.user_names is not None:
            result['UserNames'] = self.user_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIps') is not None:
            self.client_ips = m.get('ClientIps')
        if m.get('Databases') is not None:
            self.databases = m.get('Databases')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroups') is not None:
            self.resource_groups = m.get('ResourceGroups')
        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')
        return self


class DescribeDiagnosisDimensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisDimensionsResponseBody = None,
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
            temp_model = DescribeDiagnosisDimensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisMonitorPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        lang: str = None,
        query_condition: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        self.end_time = end_time
        # The language of file titles and error messages. Default value: zh. Valid values:
        # 
        # *   **zh**: simplified Chinese
        # *   **en**: English
        # *   **ja**: Japanese
        # *   **zh-tw**: traditional Chinese
        self.lang = lang
        # The query conditions for SQL statements, which can be a combination of the `Type` and `Value` fields or a combination of the Type, `Min`, and `Max` fields. Specify the conditions in the JSON format. `Type` specifies the query dimension. Valid values for Type: `maxCost`, `status`, and `cost`. `Value`, `Min`, or `Max` specifies the query range for the dimension. Valid values:
        # 
        # *   `{"Type":"maxCost","Value":"100"}`: queries the top 100 most time-consuming SQL statements. Set `Value` to 100.
        # *   `{"Type":"status","Value":"finished"}`: queries executed SQL statements. You can set `Value` to `running` to query SQL statements that are being executed. You can also set Value to `failed` to query SQL statements that failed to be executed.
        # *   `{"Type":"cost","Min":"10","Max":"200"}`: queries SQL statements whose execution durations are in the range of 10 to 200 milliseconds. You can also customize the maximum and minimum execution durations.
        self.query_condition = query_condition
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDiagnosisMonitorPerformanceResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        cost: int = None,
        peak_memory: int = None,
        process_id: str = None,
        rc_host: str = None,
        scan_rows: int = None,
        scan_size: int = None,
        start_time: int = None,
        status: str = None,
        user_name: str = None,
    ):
        # The total amount of time consumed by the query. Unit: milliseconds.
        # 
        # >  This parameter indicates the sum of `QueuedTime`, `TotalPlanningTime`, and `ExecutionTime`.
        self.cost = cost
        # The peak memory of the query. Unit: bytes.
        self.peak_memory = peak_memory
        # The ID of the query.
        # 
        # >  You can call the [DescribeProcessList](~~143382~~) operation to query the IDs of queries that are being executed.
        self.process_id = process_id
        # The IP address of the AnalyticDB for MySQL frontend node on which the SQL statement is executed.
        self.rc_host = rc_host
        # The number of entries scanned.
        self.scan_rows = scan_rows
        # The amount of scanned data. Unit: bytes.
        self.scan_size = scan_size
        # The execution start time of the SQL statement. The time is in the UNIX timestamp format. Unit: milliseconds.
        self.start_time = start_time
        # The state of the SQL statement. Valid values:
        # 
        # *   **running**\
        # *   **finished**\
        # *   **failed**\
        self.status = status
        # The database account that is used to submit the query.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.rc_host is not None:
            result['RcHost'] = self.rc_host
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('RcHost') is not None:
            self.rc_host = m.get('RcHost')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDiagnosisMonitorPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        performances: List[DescribeDiagnosisMonitorPerformanceResponseBodyPerformances] = None,
        performances_threshold: int = None,
        performances_truncated: bool = None,
        request_id: str = None,
    ):
        # The monitoring information of queries displayed in Gantt charts.
        self.performances = performances
        # The threshold for the number of queries displayed in a Gantt chart. The default value is 10000.
        # 
        # >  A maximum of 10,000 queries can be displayed in a Gantt chart even if more queries exist.
        self.performances_threshold = performances_threshold
        # Indicates whether all queries are returned. Valid values:
        # 
        # *   true: All queries are returned.
        # *   false: Only a specified number of queries are returned.
        self.performances_truncated = performances_truncated
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.performances_threshold is not None:
            result['PerformancesThreshold'] = self.performances_threshold
        if self.performances_truncated is not None:
            result['PerformancesTruncated'] = self.performances_truncated
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDiagnosisMonitorPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('PerformancesThreshold') is not None:
            self.performances_threshold = m.get('PerformancesThreshold')
        if m.get('PerformancesTruncated') is not None:
            self.performances_truncated = m.get('PerformancesTruncated')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDiagnosisMonitorPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisMonitorPerformanceResponseBody = None,
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
            temp_model = DescribeDiagnosisMonitorPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisRecordsRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        dbcluster_id: str = None,
        database: str = None,
        end_time: str = None,
        keyword: str = None,
        lang: str = None,
        max_peak_memory: int = None,
        max_scan_size: int = None,
        min_peak_memory: int = None,
        min_scan_size: int = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        pattern_id: str = None,
        query_condition: str = None,
        region_id: str = None,
        resource_group: str = None,
        start_time: str = None,
        user_name: str = None,
    ):
        # The source IP address.
        # 
        # > You can call the [DescribeDiagnosisDimensions](~~308210~~) operation to query the resource group, database name, username, and source IP address of the SQL statements to be queried.
        self.client_ip = client_ip
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The database on which the SQL statements are executed.
        # 
        # > You can call the [DescribeDiagnosisDimensions](~~308210~~) operation to query the resource group, database name, username, and source IP address of the SQL statements to be queried.
        self.database = database
        # The end of the time range to query. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > 
        # 
        # *   The end time must be later than the start time.
        # 
        # *   The maximum time range that can be specified is 24 hours.
        self.end_time = end_time
        # The keyword for the query.
        self.keyword = keyword
        # The language of file titles and error messages. Valid values:
        # 
        # *   **zh** (default): simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The maximum peak memory of the SQL statements. Unit: bytes.
        self.max_peak_memory = max_peak_memory
        # The maximum scan size of the SQL statements. Unit: bytes.
        self.max_scan_size = max_scan_size
        # The minimum peak memory of the SQL statements. Unit: bytes.
        self.min_peak_memory = min_peak_memory
        # The minimum scan size of the SQL statements. Unit: bytes.
        self.min_scan_size = min_scan_size
        # The order in which to sort the retrieved SQL statements by field. Specify this value in the JSON format. The value is an ordered array that uses the order of the input array and contains the `Field` and `Type` fields. Example: `[{"Field":"StartTime", "Type": "desc" }]`. Fields:
        # 
        # *   `Field` specifies the field that is used to sort the retrieved SQL statements. Valid values:
        # 
        #     *   `StartTime`: the start time of the execution.
        #     *   `Status`: the execution state.
        #     *   `UserName`: the username.
        #     *   `Cost`: the execution duration.
        #     *   `PeakMemory`: the peak memory.
        #     *   `ScanSize`: the amount of data to be scanned.
        #     *   `Database`: the name of the database.
        #     *   `ClientIp`: the source IP address.
        #     *   `ResourceGroup`: the name of the resource group.
        #     *   `QueueTime`: the amount of time that is consumed for queuing.
        #     *   `OutputRows`: the number of output rows.
        #     *   `OutputDataSize`: the amount of output data.
        #     *   `ResourceCostRank`: the execution duration rank of operators that are used in the SQL statements. This field takes effect only when `QueryCondition` is set to `{"Type":"status","Value":"running"}`.
        # 
        # *   `Type` specifies the sorting order. Valid values (case-insensitive):
        # 
        #     *   `Desc`: descending order.
        #     *   `Asc`: ascending order.
        self.order = order
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**. Default value: 30.
        self.page_size = page_size
        # The ID of the SQL pattern.[](~~321868~~)
        self.pattern_id = pattern_id
        # The query condition for SQL statements, which can contain the `Type`, `Value`, and `Min` or `Max` fields. Specify the condition in the JSON format. `Type` specifies the query dimension. Valid values for Type: `maxCost`, `status`, and `cost`. `Value`, `Min`, or `Max` specifies the query range for the dimension. Valid values:
        # 
        # *   `{"Type":"maxCost","Value":"100"}`: queries the top 100 most time-consuming SQL statements. Set `Value` to 100.
        # *   `{"Type":"status","Value":"finished"}`: queries executed SQL statements. You can set `Value` to `running` to query SQL statements that are being executed. You can also set Value to `failed` to query SQL statements that failed to be executed.
        # *   `{"Type":"cost","Min":"10","Max":"200"}`: queries SQL statements whose execution durations are in the range of 10 to 200 milliseconds. You can also customize the maximum and minimum execution durations.
        self.query_condition = query_condition
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The resource group to which the SQL statements belong.
        # 
        # > You can call the [DescribeDiagnosisDimensions](~~308210~~) operation to query the resource group, database name, username, and source IP address of the SQL statements to be queried.
        self.resource_group = resource_group
        # The beginning of the time range to query. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > Only data within the last 14 days can be queried.
        self.start_time = start_time
        # The username that is used to execute the SQL statements.
        # 
        # > You can call the [DescribeDiagnosisDimensions](~~308210~~) operation to query the resource group, database name, username, and source IP address of the SQL statements to be queried.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory
        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size
        if self.min_peak_memory is not None:
            result['MinPeakMemory'] = self.min_peak_memory
        if self.min_scan_size is not None:
            result['MinScanSize'] = self.min_scan_size
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')
        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')
        if m.get('MinPeakMemory') is not None:
            self.min_peak_memory = m.get('MinPeakMemory')
        if m.get('MinScanSize') is not None:
            self.min_scan_size = m.get('MinScanSize')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDiagnosisRecordsResponseBodyQuerys(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        cost: int = None,
        database: str = None,
        etl_write_rows: int = None,
        execution_time: int = None,
        output_data_size: int = None,
        output_rows: int = None,
        peak_memory: int = None,
        process_id: str = None,
        queue_time: int = None,
        rc_host: str = None,
        resource_cost_rank: int = None,
        resource_group: str = None,
        sql: str = None,
        sqltruncated: bool = None,
        sqltruncated_threshold: int = None,
        scan_rows: int = None,
        scan_size: int = None,
        start_time: int = None,
        status: str = None,
        total_planning_time: int = None,
        total_stages: int = None,
        user_name: str = None,
    ):
        # The source IP address.
        self.client_ip = client_ip
        # The total execution duration. Unit: milliseconds.
        # 
        # >  This value is the cumulative value of the `QueuedTime`, `TotalPlanningTime`, and `ExecutionTime` parameters.
        self.cost = cost
        # The name of the database on which the SQL statement is executed.
        self.database = database
        # The number of rows written to the table by an extract, transform, and load (ETL) task.
        self.etl_write_rows = etl_write_rows
        # The execution duration. Unit: milliseconds.
        self.execution_time = execution_time
        # The amount of returned data. Unit: bytes.
        self.output_data_size = output_data_size
        # The number of rows returned.
        self.output_rows = output_rows
        # The peak memory. Unit: bytes.
        self.peak_memory = peak_memory
        # The query ID.
        self.process_id = process_id
        # The amount of time that is consumed for queuing. Unit: milliseconds.
        self.queue_time = queue_time
        # The IP address and port number of the AnalyticDB for MySQL frontend node on which the SQL statement is executed.
        self.rc_host = rc_host
        # The execution duration rank of operators that are used in the SQL statement.
        # 
        # > This field is returned only for SQL statements that have the `Status` parameter set to `running`.
        self.resource_cost_rank = resource_cost_rank
        # The resource group to which the SQL statement belongs.
        self.resource_group = resource_group
        # The SQL statement.
        # 
        # > For performance considerations, an SQL statement cannot exceed 5,120 characters in length. Otherwise, the SQL statement is truncated. You can call the [DownloadDiagnosisRecords](~~308212~~) operation to download the diagnostic information about SQL statements that meet a condition in an AnalyticDB for MySQL cluster, including the complete SQL statements.
        self.sql = sql
        # Indicates whether the SQL statement is truncated. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.sqltruncated = sqltruncated
        # The maximum length of the SQL statement. 5120 is returned. Unit: character. SQL statements that exceed this limit are truncated.
        self.sqltruncated_threshold = sqltruncated_threshold
        # The number of entries scanned.
        self.scan_rows = scan_rows
        # The amount of scanned data. Unit: bytes.
        self.scan_size = scan_size
        # The beginning of the time range in which the SQL statement is executed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The state of the SQL statement. Valid values:
        # 
        # *   **running**\
        # *   **finished**\
        # *   **failed**\
        self.status = status
        # The amount of time that is consumed to generate an execution plan. Unit: milliseconds.
        self.total_planning_time = total_planning_time
        # The total number of stages generated.
        self.total_stages = total_stages
        # The username that is used to execute the SQL statement.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.database is not None:
            result['Database'] = self.database
        if self.etl_write_rows is not None:
            result['EtlWriteRows'] = self.etl_write_rows
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rc_host is not None:
            result['RcHost'] = self.rc_host
        if self.resource_cost_rank is not None:
            result['ResourceCostRank'] = self.resource_cost_rank
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.sqltruncated is not None:
            result['SQLTruncated'] = self.sqltruncated
        if self.sqltruncated_threshold is not None:
            result['SQLTruncatedThreshold'] = self.sqltruncated_threshold
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.total_planning_time is not None:
            result['TotalPlanningTime'] = self.total_planning_time
        if self.total_stages is not None:
            result['TotalStages'] = self.total_stages
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EtlWriteRows') is not None:
            self.etl_write_rows = m.get('EtlWriteRows')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RcHost') is not None:
            self.rc_host = m.get('RcHost')
        if m.get('ResourceCostRank') is not None:
            self.resource_cost_rank = m.get('ResourceCostRank')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('SQLTruncated') is not None:
            self.sqltruncated = m.get('SQLTruncated')
        if m.get('SQLTruncatedThreshold') is not None:
            self.sqltruncated_threshold = m.get('SQLTruncatedThreshold')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalPlanningTime') is not None:
            self.total_planning_time = m.get('TotalPlanningTime')
        if m.get('TotalStages') is not None:
            self.total_stages = m.get('TotalStages')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDiagnosisRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        querys: List[DescribeDiagnosisRecordsResponseBodyQuerys] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The queried SQL statements.
        self.querys = querys
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.querys:
            for k in self.querys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Querys'] = []
        if self.querys is not None:
            for k in self.querys:
                result['Querys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.querys = []
        if m.get('Querys') is not None:
            for k in m.get('Querys'):
                temp_model = DescribeDiagnosisRecordsResponseBodyQuerys()
                self.querys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiagnosisRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisRecordsResponseBody = None,
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
            temp_model = DescribeDiagnosisRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisSQLInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        lang: str = None,
        process_id: str = None,
        process_rc_host: str = None,
        process_start_time: int = None,
        process_state: str = None,
        region_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The language of file titles and error messages. Valid values:
        # 
        # *   **zh**: simplified Chinese
        # *   **en**: English
        # *   **ja**: Japanese
        # *   **zh-tw**: traditional Chinese
        self.lang = lang
        # The ID of the query.
        # 
        # >  You can call the [DescribeDiagnosisRecords](~~308207~~) operation to query the SQL summary information of a specified AnalyticDB for MySQL cluster, including the query ID.
        self.process_id = process_id
        # The IP address and port number of the AnalyticDB for MySQL frontend node on which the SQL statement is executed.
        # 
        # >  You can call the [DescribeDiagnosisRecords](~~308207~~) operation to query the SQL summary information of a specified AnalyticDB for MySQL cluster, including the IP address and port number of the frontend node.
        self.process_rc_host = process_rc_host
        # The execution start time of the SQL statement. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        # 
        # >  You can call the [DescribeDiagnosisRecords](~~308207~~) operation to query the SQL summary information of a specified AnalyticDB for MySQL cluster, including the execution start time of the SQL statement.
        self.process_start_time = process_start_time
        # The state of the SQL statement. Valid values:
        # 
        # *   **running**\
        # 
        # *   **finished**\
        # 
        # *   **failed**\
        # 
        # > You can call the [DescribeDiagnosisRecords](~~308207~~) operation to query the SQL summary information of a specified AnalyticDB for MySQL cluster, including the state of the SQL statement.
        self.process_state = process_state
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.process_rc_host is not None:
            result['ProcessRcHost'] = self.process_rc_host
        if self.process_start_time is not None:
            result['ProcessStartTime'] = self.process_start_time
        if self.process_state is not None:
            result['ProcessState'] = self.process_state
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('ProcessRcHost') is not None:
            self.process_rc_host = m.get('ProcessRcHost')
        if m.get('ProcessStartTime') is not None:
            self.process_start_time = m.get('ProcessStartTime')
        if m.get('ProcessState') is not None:
            self.process_state = m.get('ProcessState')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDiagnosisSQLInfoResponseBodyStageInfos(TeaModel):
    def __init__(
        self,
        input_data_size: int = None,
        input_rows: int = None,
        operator_cost: int = None,
        output_data_size: int = None,
        output_rows: int = None,
        peak_memory: int = None,
        progress: float = None,
        stage_id: str = None,
        state: str = None,
    ):
        # The total amount of input data in the stage. Unit: bytes.
        self.input_data_size = input_data_size
        # The total number of input rows in the stage.
        self.input_rows = input_rows
        # The total amount of time consumed by all operators in the stage. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The total amount of output data in the stage. Unit: bytes.
        self.output_data_size = output_data_size
        # The total number of output rows in the stage.
        self.output_rows = output_rows
        # The total peak memory of the stage. Unit: bytes.
        self.peak_memory = peak_memory
        # The execution progress of the stage.
        self.progress = progress
        # The ID of the stage.
        self.stage_id = stage_id
        # The state of the stage.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_data_size is not None:
            result['InputDataSize'] = self.input_data_size
        if self.input_rows is not None:
            result['InputRows'] = self.input_rows
        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost
        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputDataSize') is not None:
            self.input_data_size = m.get('InputDataSize')
        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')
        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')
        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeDiagnosisSQLInfoResponseBody(TeaModel):
    def __init__(
        self,
        diagnosis_sqlinfo: str = None,
        request_id: str = None,
        stage_infos: List[DescribeDiagnosisSQLInfoResponseBodyStageInfos] = None,
    ):
        # Execution details of the SQL statement, including the SQL statement text, statistics, execution plan, and operator information.
        self.diagnosis_sqlinfo = diagnosis_sqlinfo
        # The ID of the request.
        self.request_id = request_id
        # Execution details of the query by stage.
        self.stage_infos = stage_infos

    def validate(self):
        if self.stage_infos:
            for k in self.stage_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnosis_sqlinfo is not None:
            result['DiagnosisSQLInfo'] = self.diagnosis_sqlinfo
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StageInfos'] = []
        if self.stage_infos is not None:
            for k in self.stage_infos:
                result['StageInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosisSQLInfo') is not None:
            self.diagnosis_sqlinfo = m.get('DiagnosisSQLInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stage_infos = []
        if m.get('StageInfos') is not None:
            for k in m.get('StageInfos'):
                temp_model = DescribeDiagnosisSQLInfoResponseBodyStageInfos()
                self.stage_infos.append(temp_model.from_map(k))
        return self


class DescribeDiagnosisSQLInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisSQLInfoResponseBody = None,
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
            temp_model = DescribeDiagnosisSQLInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisTasksRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        host: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        process_id: str = None,
        region_id: str = None,
        stage_id: str = None,
        state: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The IP address from which the query was initiated.
        self.host = host
        # The order in which to sort the tasks by field. Specify the value in the JSON format. Example: `[{"Field":"CreateTime", "Type":"desc"}]`.
        # 
        # > 
        # 
        # *   `Field` indicates the field that is used to sort the tasks. Valid values of Field: `State`, `CreateTime`, `DBName`, `ProcessID`, `UpdateTime`, `JobName`, and `ProcessRows`.
        # 
        # *   `Type` indicates the sort type. Valid values of Type: `Desc` and `Asc`. The values are case-insensitive.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   30 (default)
        # *   50
        # *   100
        self.page_size = page_size
        # The query ID.
        # 
        # > You can call the [DescribeProcessList](~~190092~~) operation to query the IDs of queries that are being executed.
        self.process_id = process_id
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of a stage in the query that is specified by the `ProcessId` parameter.
        self.stage_id = stage_id
        # The state of the asynchronous import or export task to be queried. Valid values:
        # 
        # *   **RUNNING**\
        # *   **FINISHED**\
        # *   **FAILED**\
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.host is not None:
            result['Host'] = self.host
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeDiagnosisTasksResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        compute_time_ratio: str = None,
        drivers: str = None,
        elapsed_time: int = None,
        input_data_size: int = None,
        input_rows: int = None,
        operator_cost: int = None,
        output_data_size: int = None,
        output_rows: int = None,
        peak_memory: int = None,
        queued_time: str = None,
        scan_cost: int = None,
        scan_data_size: int = None,
        scan_rows: int = None,
        state: str = None,
        task_create_time: int = None,
        task_end_time: int = None,
        task_host: str = None,
        task_id: str = None,
    ):
        # The compute time ratio, which can be used to determine whether the task is really time-consuming. This parameter can be calculated by using the following formula: OperatorCost/Drivers/ElapsedTime. A greater value indicates that the task was executed for computing for most of the task time. A less value indicates that the task was waiting for scheduling or blocked due to other reasons for most of the task time.
        self.compute_time_ratio = compute_time_ratio
        # The number of tasks that can be executed concurrently.
        self.drivers = drivers
        # The amount of time that elapsed from when the task was created to when the task was completed. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The amount of input data in the task. Unit: bytes.
        self.input_data_size = input_data_size
        # The number of input rows in the task.
        self.input_rows = input_rows
        # The total amount of time that is consumed by all operators in the task on a node. This parameter can be used to determine whether long tails occur in computing. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The amount of output data in the task. Unit: bytes.
        self.output_data_size = output_data_size
        # The number of output rows in the task.
        self.output_rows = output_rows
        # The peak memory of the task. Unit: bytes.
        self.peak_memory = peak_memory
        # The queuing duration of the task. Unit: milliseconds.
        self.queued_time = queued_time
        # The amount of time that is consumed to scan data from a data source in the task. Unit: milliseconds.
        self.scan_cost = scan_cost
        # The amount of scanned data in the task. Unit: bytes.
        self.scan_data_size = scan_data_size
        # The number of rows that are scanned from a data source in the task.
        self.scan_rows = scan_rows
        # The final execution state of the task. Valid values:
        # 
        # *   FINISHED
        # *   CANCELED
        # *   ABORTED
        # *   FAILED
        self.state = state
        # The timestamp when the task was created.
        self.task_create_time = task_create_time
        # The timestamp when the task ends.
        self.task_end_time = task_end_time
        # The IP address of the host where the task was executed.
        self.task_host = task_host
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_time_ratio is not None:
            result['ComputeTimeRatio'] = self.compute_time_ratio
        if self.drivers is not None:
            result['Drivers'] = self.drivers
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.input_data_size is not None:
            result['InputDataSize'] = self.input_data_size
        if self.input_rows is not None:
            result['InputRows'] = self.input_rows
        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost
        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.queued_time is not None:
            result['QueuedTime'] = self.queued_time
        if self.scan_cost is not None:
            result['ScanCost'] = self.scan_cost
        if self.scan_data_size is not None:
            result['ScanDataSize'] = self.scan_data_size
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.state is not None:
            result['State'] = self.state
        if self.task_create_time is not None:
            result['TaskCreateTime'] = self.task_create_time
        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time
        if self.task_host is not None:
            result['TaskHost'] = self.task_host
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeTimeRatio') is not None:
            self.compute_time_ratio = m.get('ComputeTimeRatio')
        if m.get('Drivers') is not None:
            self.drivers = m.get('Drivers')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('InputDataSize') is not None:
            self.input_data_size = m.get('InputDataSize')
        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')
        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')
        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('QueuedTime') is not None:
            self.queued_time = m.get('QueuedTime')
        if m.get('ScanCost') is not None:
            self.scan_cost = m.get('ScanCost')
        if m.get('ScanDataSize') is not None:
            self.scan_data_size = m.get('ScanDataSize')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TaskCreateTime') is not None:
            self.task_create_time = m.get('TaskCreateTime')
        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')
        if m.get('TaskHost') is not None:
            self.task_host = m.get('TaskHost')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDiagnosisTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[DescribeDiagnosisTasksResponseBodyTaskList] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried tasks.
        self.task_list = task_list
        # The total number of tasks in the stage.
        self.total_count = total_count

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = DescribeDiagnosisTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiagnosisTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosisTasksResponseBody = None,
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
            temp_model = DescribeDiagnosisTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadRecordsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        lang: str = None,
        region_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the detailed information of all AnalyticDB for MySQL clusters within a specific region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The languages available for file titles and some error messages. Default value: zh. Valid values:
        # 
        # *   **zh**: Simplified Chinese
        # *   **en**: English
        # *   **ja**: Japanese
        # *   **zh-tw**: Traditional Chinese
        self.lang = lang
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the regions and zones supported by AnalyticDB for MySQL, including region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDownloadRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        download_id: int = None,
        exception_msg: str = None,
        file_name: str = None,
        status: str = None,
        url: str = None,
    ):
        # The ID of the download task.
        self.download_id = download_id
        # The error message returned when the download task has failed.
        self.exception_msg = exception_msg
        # The name of the downloaded file.
        self.file_name = file_name
        # The status of the download task.
        # 
        # *   **running**: The download task is currently in progress.
        # *   **finished**: The download task is complete.
        # *   **failed**: The download task has failed.
        self.status = status
        # The download URL of the file.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDownloadRecordsResponseBody(TeaModel):
    def __init__(
        self,
        records: List[DescribeDownloadRecordsResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # Details about the download tasks.
        self.records = records
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDownloadRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDownloadRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadRecordsResponseBody = None,
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
            temp_model = DescribeDownloadRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEIURangeRequest(TeaModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_id: str = None,
        dbcluster_version: str = None,
        operation: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The specifications of computing resources.
        # 
        # >  You can call the [DescribeComputeResource](~~469002~~) operation to query the specifications of computing resources.
        self.compute_resource = compute_resource
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # *   This parameter can be left empty when **Operation** is set to **Buy**.
        # *   This parameter must be specified when **Operation** is set to **Upgrade** or **Downgrade**.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The version of the AnalyticDB for MySQL Data Warehouse Edition cluster. Set the value to **3.0**.
        self.dbcluster_version = dbcluster_version
        # The type of the operation. Valid values:
        # 
        # *   **Buy**: purchases a cluster.
        # *   **Upgrade**: upgrades a cluster.
        # *   **Downgrade**: downgrades a cluster.
        self.operation = operation
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The zone ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~612293~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeEIURangeResponseBodyEIUInfo(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        eiurange: List[int] = None,
        storage_resource_range: List[str] = None,
    ):
        # The suggested value for the number of EIUs.
        self.default_value = default_value
        # The queried range for the number of EIUs.
        self.eiurange = eiurange
        # A reserved parameter.
        self.storage_resource_range = storage_resource_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.eiurange is not None:
            result['EIURange'] = self.eiurange
        if self.storage_resource_range is not None:
            result['StorageResourceRange'] = self.storage_resource_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('EIURange') is not None:
            self.eiurange = m.get('EIURange')
        if m.get('StorageResourceRange') is not None:
            self.storage_resource_range = m.get('StorageResourceRange')
        return self


class DescribeEIURangeResponseBody(TeaModel):
    def __init__(
        self,
        eiuinfo: DescribeEIURangeResponseBodyEIUInfo = None,
        request_id: str = None,
    ):
        # The queried information about the number of EIUs.
        self.eiuinfo = eiuinfo
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.eiuinfo:
            self.eiuinfo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eiuinfo is not None:
            result['EIUInfo'] = self.eiuinfo.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EIUInfo') is not None:
            temp_model = DescribeEIURangeResponseBodyEIUInfo()
            self.eiuinfo = temp_model.from_map(m['EIUInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEIURangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEIURangeResponseBody = None,
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
            temp_model = DescribeEIURangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticDailyPlanRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_daily_plan_day: str = None,
        elastic_daily_plan_status_list: str = None,
        elastic_plan_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pool_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The start date of the current-day scaling plan. Specify the date in the yyyy-MM-dd format.
        self.elastic_daily_plan_day = elastic_daily_plan_day
        # The execution state of the current-day scaling plan. Separate multiple values with commas (,). Valid values:
        # 
        # *   **1**: The scaling plan is not executed.
        # *   **2**: The scaling plan is being executed.
        # *   **3**: The scaling plan is executed.
        # *   **4**: The scaling plan fails to be executed.
        self.elastic_daily_plan_status_list = elastic_daily_plan_status_list
        # The name of the scaling plan. Valid values:
        # 
        # *   The name must be 2 to 30 characters in length.
        # *   The name can contain letters, digits, and underscores (\_).
        self.elastic_plan_name = elastic_plan_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the resource group.
        # 
        # >  You can call the [DescribeDBResourceGroup](~~466685~~) operation to query the resource group name.
        self.resource_pool_name = resource_pool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_daily_plan_day is not None:
            result['ElasticDailyPlanDay'] = self.elastic_daily_plan_day
        if self.elastic_daily_plan_status_list is not None:
            result['ElasticDailyPlanStatusList'] = self.elastic_daily_plan_status_list
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticDailyPlanDay') is not None:
            self.elastic_daily_plan_day = m.get('ElasticDailyPlanDay')
        if m.get('ElasticDailyPlanStatusList') is not None:
            self.elastic_daily_plan_status_list = m.get('ElasticDailyPlanStatusList')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        return self


class DescribeElasticDailyPlanResponseBodyElasticDailyPlanList(TeaModel):
    def __init__(
        self,
        day: str = None,
        elastic_node_num: int = None,
        elastic_plan_type: str = None,
        elastic_plan_worker_spec: str = None,
        end_ts: str = None,
        plan_end_ts: str = None,
        plan_name: str = None,
        plan_start_ts: str = None,
        resource_pool_name: str = None,
        start_ts: str = None,
        status: int = None,
    ):
        # The start date of the current-day scaling plan. The date is in the yyyy-MM-dd format.
        self.day = day
        # The number of nodes involved in the scaling plan.
        # 
        # *   If ElasticPlanType is set to **worker**, a value of 0 or null is returned.
        # *   If ElasticPlanType is set to **executorcombineworker** or **executor**, a value greater than 0 is returned.
        self.elastic_node_num = elastic_node_num
        # The type of the scaling plan. Default value: executorcombineworker. Valid values:
        # 
        # *   **worker**: scales only elastic I/O resources.
        # *   **executor**: scales only computing resources.
        # *   **executorcombineworker**: scales both elastic I/O resources and computing resources by proportion.
        self.elastic_plan_type = elastic_plan_type
        # The resource specifications that can be scaled up by the scaling plan. Default value: 8 Core 64 GB. Valid values:
        # 
        # *   8 Core 64 GB
        # *   16 Core 64 GB
        # *   32 Core 64 GB
        # *   64 Core 128 GB
        # *   12 Core 96 GB
        # *   24 Core 96 GB
        # *   52 Core 86 GB
        self.elastic_plan_worker_spec = elastic_plan_worker_spec
        # The actual restoration time. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.end_ts = end_ts
        # The scheduled restoration time. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.plan_end_ts = plan_end_ts
        # The name of the scaling plan.
        self.plan_name = plan_name
        # The scheduled scale-up time. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.plan_start_ts = plan_start_ts
        # The name of the resource group.
        self.resource_pool_name = resource_pool_name
        # The actual scale-up time. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.start_ts = start_ts
        # The execution state of the current-day scaling plan. Multiple values are separated by commas (,). Valid values:
        # 
        # *   **1**: The scaling plan is not executed.
        # *   **2**: The scaling plan is being executed.
        # *   **3**: The scaling plan is executed.
        # *   **4**: The scaling plan fails to be executed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.elastic_node_num is not None:
            result['ElasticNodeNum'] = self.elastic_node_num
        if self.elastic_plan_type is not None:
            result['ElasticPlanType'] = self.elastic_plan_type
        if self.elastic_plan_worker_spec is not None:
            result['ElasticPlanWorkerSpec'] = self.elastic_plan_worker_spec
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.plan_end_ts is not None:
            result['PlanEndTs'] = self.plan_end_ts
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_start_ts is not None:
            result['PlanStartTs'] = self.plan_start_ts
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('ElasticNodeNum') is not None:
            self.elastic_node_num = m.get('ElasticNodeNum')
        if m.get('ElasticPlanType') is not None:
            self.elastic_plan_type = m.get('ElasticPlanType')
        if m.get('ElasticPlanWorkerSpec') is not None:
            self.elastic_plan_worker_spec = m.get('ElasticPlanWorkerSpec')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('PlanEndTs') is not None:
            self.plan_end_ts = m.get('PlanEndTs')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanStartTs') is not None:
            self.plan_start_ts = m.get('PlanStartTs')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeElasticDailyPlanResponseBody(TeaModel):
    def __init__(
        self,
        elastic_daily_plan_list: List[DescribeElasticDailyPlanResponseBodyElasticDailyPlanList] = None,
        request_id: str = None,
    ):
        # Details of the current-day scaling plans.
        self.elastic_daily_plan_list = elastic_daily_plan_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.elastic_daily_plan_list:
            for k in self.elastic_daily_plan_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ElasticDailyPlanList'] = []
        if self.elastic_daily_plan_list is not None:
            for k in self.elastic_daily_plan_list:
                result['ElasticDailyPlanList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elastic_daily_plan_list = []
        if m.get('ElasticDailyPlanList') is not None:
            for k in m.get('ElasticDailyPlanList'):
                temp_model = DescribeElasticDailyPlanResponseBodyElasticDailyPlanList()
                self.elastic_daily_plan_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeElasticDailyPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeElasticDailyPlanResponseBody = None,
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
            temp_model = DescribeElasticDailyPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticPlanRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_plan_enable: bool = None,
        elastic_plan_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pool_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # Specifies whether the scaling plan takes effect. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.elastic_plan_enable = elastic_plan_enable
        # The name of the scaling plan.
        # 
        # *   The name must be 2 to 30 characters in length.
        # *   The name can contain letters, digits, and underscores (\_).
        # 
        # > If you do not specify this parameter, the information about all scaling plans for the specified cluster is returned.
        self.elastic_plan_name = elastic_plan_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the resource group.
        # 
        # > You can call the [DescribeDBResourceGroup](~~466685~~) operation to query the resource group name.
        self.resource_pool_name = resource_pool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_enable is not None:
            result['ElasticPlanEnable'] = self.elastic_plan_enable
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanEnable') is not None:
            self.elastic_plan_enable = m.get('ElasticPlanEnable')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        return self


class DescribeElasticPlanResponseBodyElasticPlanList(TeaModel):
    def __init__(
        self,
        elastic_node_num: int = None,
        elastic_plan_type: str = None,
        elastic_plan_worker_spec: str = None,
        enable: bool = None,
        end_day: str = None,
        end_time: str = None,
        monthly_repeat: str = None,
        plan_name: str = None,
        resource_pool_name: str = None,
        start_day: str = None,
        start_time: str = None,
        weekly_repeat: str = None,
    ):
        # The number of nodes that are involved in the scaling plan.
        # 
        # *   If ElasticPlanType is set to **worker**, a value of 0 or null is returned.
        # *   If ElasticPlanType is set to **executorcombineworker** or **executor**, a value greater than 0 is returned.
        self.elastic_node_num = elastic_node_num
        # The type of the scaling plan. Valid values:
        # 
        # *   **worker**: scales only elastic I/O resources.
        # *   **executor**: scales only computing resources.
        # *   **executorcombineworker** (default): scales both elastic I/O resources and computing resources by proportion.
        self.elastic_plan_type = elastic_plan_type
        # The resource specifications that can be scaled up by the scaling plan. Valid values:
        # 
        # *   8 Core 64 GB (default)
        # *   16 Core 64 GB
        # *   32 Core 64 GB
        # *   64 Core 128 GB
        # *   12 Core 96 GB
        # *   24 Core 96 GB
        # *   52 Core 86 GB
        self.elastic_plan_worker_spec = elastic_plan_worker_spec
        # Indicates whether the scaling plan takes effect. Default value: true. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.enable = enable
        # The end date of the scaling plan. This parameter is returned only if the end date of the scaling plan is set. The date is in the yyyy-MM-dd format.
        self.end_day = end_day
        # The restoration time of the scaling plan. The interval between the scale-up time and the restoration time cannot be more than 24 hours. The time is in the HH:mm:ss format.
        self.end_time = end_time
        self.monthly_repeat = monthly_repeat
        # The name of the scaling plan.
        self.plan_name = plan_name
        # The name of the resource group.
        self.resource_pool_name = resource_pool_name
        # The start date of the scaling plan. This parameter is returned only if the start date of the scaling plan is set. The date is in the yyyy-MM-dd format.
        self.start_day = start_day
        # The scale-up time of the scaling plan. The time is in the HH:mm:ss format.
        self.start_time = start_time
        # The days of the week when the scaling plan was executed. Valid values: 0 to 6, which indicate Sunday to Saturday. Multiple values are separated by commas (,).
        self.weekly_repeat = weekly_repeat

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_node_num is not None:
            result['ElasticNodeNum'] = self.elastic_node_num
        if self.elastic_plan_type is not None:
            result['ElasticPlanType'] = self.elastic_plan_type
        if self.elastic_plan_worker_spec is not None:
            result['ElasticPlanWorkerSpec'] = self.elastic_plan_worker_spec
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_day is not None:
            result['EndDay'] = self.end_day
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.monthly_repeat is not None:
            result['MonthlyRepeat'] = self.monthly_repeat
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        if self.start_day is not None:
            result['StartDay'] = self.start_day
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.weekly_repeat is not None:
            result['WeeklyRepeat'] = self.weekly_repeat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNodeNum') is not None:
            self.elastic_node_num = m.get('ElasticNodeNum')
        if m.get('ElasticPlanType') is not None:
            self.elastic_plan_type = m.get('ElasticPlanType')
        if m.get('ElasticPlanWorkerSpec') is not None:
            self.elastic_plan_worker_spec = m.get('ElasticPlanWorkerSpec')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndDay') is not None:
            self.end_day = m.get('EndDay')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MonthlyRepeat') is not None:
            self.monthly_repeat = m.get('MonthlyRepeat')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        if m.get('StartDay') is not None:
            self.start_day = m.get('StartDay')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('WeeklyRepeat') is not None:
            self.weekly_repeat = m.get('WeeklyRepeat')
        return self


class DescribeElasticPlanResponseBody(TeaModel):
    def __init__(
        self,
        elastic_plan_list: List[DescribeElasticPlanResponseBodyElasticPlanList] = None,
        request_id: str = None,
    ):
        # The queried scaling plans.
        self.elastic_plan_list = elastic_plan_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.elastic_plan_list:
            for k in self.elastic_plan_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ElasticPlanList'] = []
        if self.elastic_plan_list is not None:
            for k in self.elastic_plan_list:
                result['ElasticPlanList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elastic_plan_list = []
        if m.get('ElasticPlanList') is not None:
            for k in m.get('ElasticPlanList'):
                temp_model = DescribeElasticPlanResponseBodyElasticPlanList()
                self.elastic_plan_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeElasticPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeElasticPlanResponseBody = None,
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
            temp_model = DescribeElasticPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInclinedTablesRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        table_type: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The order in which queries are sorted in the JSON format based on the specified fields. Specify the fields used to sort the queries and the order type.
        # 
        # Example:
        # 
        # ```
        # 
        # [
        # 
        #     {
        # 
        #         "Field":"Name",
        # 
        #         "Type":"Asc"
        # 
        #     }
        # 
        # ]
        # ```
        # 
        # In the preceding code, Field indicates the field used to sort queries. Set the value of Field to Name.
        # 
        # Type indicates the order type. Valid values of Type: Desc and Asc. A value of Desc indicates a descending order. A value of Asc indicates an ascending order.
        # 
        # Both fields are not case-sensitive.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        # 
        # Default value: 30.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the table. Valid values:
        # 
        # *   FactTable
        # *   DimensionTable
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order is not None:
            result['Order'] = self.order
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class DescribeInclinedTablesResponseBodyItemsTable(TeaModel):
    def __init__(
        self,
        is_incline: bool = None,
        name: str = None,
        schema: str = None,
        size: int = None,
        type: str = None,
    ):
        # Indicates whether data is skewed in partitions of the table. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_incline = is_incline
        # The name of the table.
        self.name = name
        # The name of the database.
        self.schema = schema
        # The number of rows in the table.
        self.size = size
        # The type of the table. Valid values:
        # 
        # *   **FactTable**\
        # *   **DimensionTable**\
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_incline is not None:
            result['IsIncline'] = self.is_incline
        if self.name is not None:
            result['Name'] = self.name
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsIncline') is not None:
            self.is_incline = m.get('IsIncline')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeInclinedTablesResponseBodyItems(TeaModel):
    def __init__(
        self,
        table: List[DescribeInclinedTablesResponseBodyItemsTable] = None,
    ):
        self.table = table

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeInclinedTablesResponseBodyItemsTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeInclinedTablesResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeInclinedTablesResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The monitoring information about tables.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('Items') is not None:
            temp_model = DescribeInclinedTablesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInclinedTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInclinedTablesResponseBody = None,
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
            temp_model = DescribeInclinedTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadTasksRecordsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbname: str = None,
        end_time: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        state: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters in a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The name of the database that is involved in the import or export task.
        self.dbname = dbname
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        self.end_time = end_time
        # The order in which to sort the tasks by field. Specify the field and the sort order in the JSON format. Example: `[{"Field":"CreateTime", "Type":"desc"}]`.
        # 
        # > 
        # 
        # *   `Field` specifies the field that is used to sort the tasks. Valid values of Field: `State`, `CreateTime`, `DBName`, `ProcessID`, `UpdateTime`, `JobName`, and `ProcessRows`.
        # 
        # *   `Type` specifies the sort order. Valid values of Type: `Desc` and `Asc`. The values are case-insensitive.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # > We recommend that you set the query start time to any point in time within 30 days.
        self.start_time = start_time
        # The state of the asynchronous import or export task to be queried. Valid values:
        # 
        # *   **INIT**: The task is being initialized.
        # *   **RUNNING**: The task is running.
        # *   **FINISH**: The task is successful.
        # *   **FAILED**: The task fails.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order is not None:
            result['Order'] = self.order
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeLoadTasksRecordsResponseBodyLoadTasksRecords(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dbname: str = None,
        job_name: str = None,
        process_id: str = None,
        process_rows: int = None,
        sql: str = None,
        state: str = None,
        update_time: str = None,
    ):
        # The start time of the task. The time is accurate to milliseconds. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ss.SSSZ* format. The time is displayed in UTC.
        self.create_time = create_time
        # The name of the database that is involved in the import or export task.
        self.dbname = dbname
        # The task ID.
        self.job_name = job_name
        # The process ID.
        self.process_id = process_id
        # The number of rows that are processed in the asynchronous import or export task.
        self.process_rows = process_rows
        # The SQL statement that is used in the asynchronous import or export task.
        self.sql = sql
        # The state of the task.
        self.state = state
        # The time when the task state was updated. The time is accurate to milliseconds. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ss.SSSZ* format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.process_id is not None:
            result['ProcessID'] = self.process_id
        if self.process_rows is not None:
            result['ProcessRows'] = self.process_rows
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')
        if m.get('ProcessRows') is not None:
            self.process_rows = m.get('ProcessRows')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeLoadTasksRecordsResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        load_tasks_records: List[DescribeLoadTasksRecordsResponseBodyLoadTasksRecords] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried asynchronous import and export tasks.
        self.load_tasks_records = load_tasks_records
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.load_tasks_records:
            for k in self.load_tasks_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['LoadTasksRecords'] = []
        if self.load_tasks_records is not None:
            for k in self.load_tasks_records:
                result['LoadTasksRecords'].append(k.to_map() if k else None)
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.load_tasks_records = []
        if m.get('LoadTasksRecords') is not None:
            for k in m.get('LoadTasksRecords'):
                temp_model = DescribeLoadTasksRecordsResponseBodyLoadTasksRecords()
                self.load_tasks_records.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLoadTasksRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLoadTasksRecordsResponseBody = None,
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
            temp_model = DescribeLoadTasksRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMaintenanceActionRequest(TeaModel):
    def __init__(
        self,
        is_history: int = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_type: str = None,
    ):
        # Specifies whether to return the information about pending or historical O\&M events. Valid values:
        # 
        # *   **0**: returns the information about pending O\&M event.
        # *   **1**: returns the information about historical O\&M event.
        # 
        # If you do not specify this parameter, the information about pending O\&M event are returned.
        self.is_history = is_history
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**. Default value: 30.
        self.page_size = page_size
        # The region ID. Valid values:
        # 
        # *   The ID of the region where the O\&M event occurs. Example: `cn-hangzhou`. You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        # *   You can also set Region to `all` to query the O\&M events in all regions. If you set `Region` to `all`, you must set `TaskType` to `all`.
        self.region = region
        # The ID of the region where the O\&M event occurs.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the O\&M event. Valid values:
        # 
        # *   **rds_apsaradb_upgrade**: database software upgrades.
        # *   **all**: all the O\&M events in all regions within the current account. If you set `Region` to `all`, you must set `TaskType` to `all`.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_history is not None:
            result['IsHistory'] = self.is_history
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsHistory') is not None:
            self.is_history = m.get('IsHistory')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeMaintenanceActionResponseBodyItems(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        dbcluster_id: str = None,
        dbtype: str = None,
        dbversion: str = None,
        deadline: str = None,
        id: int = None,
        modified_time: str = None,
        prepare_interval: str = None,
        region: str = None,
        result_info: str = None,
        start_time: str = None,
        status: str = None,
        switch_time: str = None,
        task_type: str = None,
    ):
        # The time when the O\&M event was created. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.created_time = created_time
        # The ID of the cluster that is involved in the O\&M event.
        self.dbcluster_id = dbcluster_id
        # The database engine.
        self.dbtype = dbtype
        # The version of the database engine.
        self.dbversion = dbversion
        # The deadline before which the event can be executed. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.deadline = deadline
        # The ID of the O\&M event.
        self.id = id
        # The point in time at which the switchover time of the O\&M event was modified. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The preparation time that is required before the pending O\&M event can be switched. The time is in the `HH:mm:ss` format.
        self.prepare_interval = prepare_interval
        # The ID of the region where the O\&M event occurs.
        self.region = region
        # The execution result of the O\&M event.
        # 
        # > This parameter is returned only when the value of `Status` is **FAILED** or **CANCEL**.
        self.result_info = result_info
        # The time when the task was executed in the backend. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.start_time = start_time
        # The state of the event.
        # 
        # *   If you set `IsHistory` to **0**, the state of the pending O\&M event is returned. Valid values:
        # 
        #     *   **WAITING_MODIFY**: The start time of the O\&M event is waiting to be set.
        #     *   **WAITING**: The O\&M event is waiting to be processed.
        #     *   **PROCESSING**: The O\&M event is being processed. The switchover time of an event in this state cannot be changed.
        # 
        # *   If you set `IsHistory` to **1**, the state of the historical O\&M event is returned. Valid values:
        # 
        #     *   **SUCCESS**: The event ended and the execution succeeded.
        #     *   **FAILED**: The event ended but the execution failed.
        #     *   **CANCEL**: The event was canceled.
        self.status = status
        # The time when the pending O\&M event is switched. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.switch_time = switch_time
        # The type of the O\&M event.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.deadline is not None:
            result['Deadline'] = self.deadline
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.prepare_interval is not None:
            result['PrepareInterval'] = self.prepare_interval
        if self.region is not None:
            result['Region'] = self.region
        if self.result_info is not None:
            result['ResultInfo'] = self.result_info
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PrepareInterval') is not None:
            self.prepare_interval = m.get('PrepareInterval')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResultInfo') is not None:
            self.result_info = m.get('ResultInfo')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeMaintenanceActionResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeMaintenanceActionResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The queried O\&M events.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

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
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeMaintenanceActionResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeMaintenanceActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMaintenanceActionResponseBody = None,
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
            temp_model = DescribeMaintenanceActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOperatorPermissionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeOperatorPermissionResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        dbcluster_id: str = None,
        expired_time: str = None,
        privileges: str = None,
        request_id: str = None,
    ):
        # The time when the authorization takes effect.
        self.created_time = created_time
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The time when the authorization expires.
        self.expired_time = expired_time
        # The type of authorization. Valid values: Control | Data.
        self.privileges = privileges
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.privileges is not None:
            result['Privileges'] = self.privileges
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOperatorPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOperatorPermissionResponseBody = None,
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
            temp_model = DescribeOperatorPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePatternPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        pattern_id: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The SQL pattern ID.
        # 
        # > You can call the [DescribeSQLPatterns](~~321868~~) operation to query the information about all SQL patterns in an AnalyticDB for MySQL cluster within a period of time, including SQL pattern IDs.
        self.pattern_id = pattern_id
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # > 
        # 
        # *   Only data within the last 14 days can be queried. For example, if the current date is November 22 (UTC+8), you can query data on a day as early as November 9 by setting StartTime to 2021-11-08T16:00:00Z. If you set StartTime to a value earlier than 2021-11-08T16:00:00Z, the Performances parameter is empty.
        # 
        # *   The maximum time range that can be specified is 24 hours.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePatternPerformanceResponseBodyPerformancesSeries(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # The name of the performance metric value. Valid values:
        # 
        # *   When the `Key` parameter is set to `AnalyticDB_PatternQueryCount`, `pattern_query_count` is returned, which indicates the number of executions of the SQL statements in association with the SQL pattern.
        # 
        # *   When the `Key` parameter is set to `AnalyticDB_PatternQueryTime`, the following values are returned:
        # 
        #     *   `average_query_time`, which indicates the average total amount of time consumed by the SQL statements in association with the SQL pattern.
        #     *   `max_query_time`, which indicates the maximum total amount of time consumed by the SQL statements in association with the SQL pattern.
        # 
        # *   When the `Key` parameter is set to `AnalyticDB_PatternExecutionTime`, the following values are returned:
        # 
        #     *   `average_execution_time`, which indicates the average execution duration of the SQL statements in association with the SQL pattern.
        #     *   `max_execution_time`, which indicates the maximum execution duration of the SQL statements in association with the SQL pattern.
        # 
        # *   When the `Key` parameter is set to `AnalyticDB_PatternPeakMemory`, the following values are returned:
        # 
        #     *   `average_peak_memory`, which indicates the average peak memory usage of the SQL statements in association with the SQL pattern.
        #     *   `max_peak_memory`, which indicates the maximum peak memory usage of the SQL statements in association with the SQL pattern.
        # 
        # *   When the `Key` parameter is set `AnalyticDB_PatternScanSize`, the following values are returned:
        # 
        #     *   `average_scan_size`, which indicates the average amount of data scanned by the SQL statements in association with the SQL pattern.
        #     *   `max_scan_size`, which indicates the maximum amount of data scanned by the SQL statements in association with the SQL pattern.
        self.name = name
        # The queried performance metrics.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribePatternPerformanceResponseBodyPerformances(TeaModel):
    def __init__(
        self,
        key: str = None,
        series: List[DescribePatternPerformanceResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        # The performance metric that was queried. Valid values:
        # 
        # *   **AnalyticDB_PatternQueryCount**: the total number of queries executed in association with the SQL pattern.
        # *   **AnalyticDB_PatternQueryTime**: the total amount of time consumed by the queries executed in association with the SQL pattern.
        # *   **AnalyticDB_PatternExecutionTime**: the total execution duration of the queries executed in association with the SQL pattern.
        # *   **AnalyticDB_PatternPeakMemory**: the peak memory usage of the queries executed in association with the SQL pattern.
        # *   **AnalyticDB_PatternScanSize**: the amount of data scanned in the queries executed in association with the SQL pattern.
        self.key = key
        # The queried performance metrics.
        self.series = series
        # The unit of the performance metric. Valid values:
        # 
        # *   When the performance metric is related to the query duration (the `Key` value is `AnalyticDB_PatternQueryTime` or `AnalyticDB_PatternExecutionTime`), **ms** is returned.
        # *   When the performance metric is related to the memory usage (the `Key` value is `AnalyticDB_PatternPeakMemory`), **MB** is returned.
        # *   When the performance metric is related to the amount of data scanned (the `Key` value is `AnalyticDB_PatternScanSize`), **MB** is returned.
        # *   When the performance metric is related to the number of queries (the `Key` value is `AnalyticDB_PatternQueryCount`), this parameter is empty.
        self.unit = unit

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribePatternPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribePatternPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        performances: List[DescribePatternPerformanceResponseBodyPerformances] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.end_time = end_time
        # The queried performance metrics.
        self.performances = performances
        # The request ID.
        self.request_id = request_id
        # The start time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribePatternPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePatternPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePatternPerformanceResponseBody = None,
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
            temp_model = DescribePatternPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProcessListRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        keyword: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        running_time: int = None,
        show_full: bool = None,
        user: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The keyword in an SQL statement, which is used to filter queries. Set the value to **SELECT**.
        self.keyword = keyword
        # The order in which queries are sorted based on the specified fields. Specify this parameter as an ordered JSON array in the `[{"Field":"Time","Type":"Desc" },{ "Field":"User", "Type":"Asc" }]` format.
        # 
        # *   **Field** specifies the field used to sort queries. Valid values: Time, User, Host, and DB.
        # *   **Type** specifies the sorting sequence. Valid values: **Desc** and **Asc**.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 30. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The execution duration used to filter queries. Queries that take a longer time than the specified execution duration are displayed. Unit: seconds.
        self.running_time = running_time
        # Specifies whether to show a complete SQL statement. Valid values:
        # 
        # *   **True**: shows a complete SQL statement.
        # *   **False**: shows only the first 100 characters of an SQL statement.
        # 
        # >  The default value is False.
        self.show_full = show_full
        # The name of the user used to filter queries.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order is not None:
            result['Order'] = self.order
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.show_full is not None:
            result['ShowFull'] = self.show_full
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('ShowFull') is not None:
            self.show_full = m.get('ShowFull')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeProcessListResponseBodyItemsProcess(TeaModel):
    def __init__(
        self,
        command: str = None,
        db: str = None,
        host: str = None,
        id: int = None,
        info: str = None,
        process_id: str = None,
        start_time: str = None,
        time: int = None,
        user: str = None,
    ):
        # The type of the statement. Only SELECT can be returned.
        self.command = command
        # The name of the database.
        self.db = db
        # The IP address from which the query was initiated.
        self.host = host
        # The ID of the worker thread.
        self.id = id
        # The SQL statement that is being executed. By default, the first 100 characters of the SQL statement are returned. If the ShowFull parameter is set to True, the complete SQL statement is returned.
        self.info = info
        # The unique ID of the query. You must specify this parameter when you use the KILL PROCESS statement.
        self.process_id = process_id
        # The start time of the query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The amount of time that has elapsed from the start time of the query. Unit: seconds.
        self.time = time
        # The username.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.db is not None:
            result['DB'] = self.db
        if self.host is not None:
            result['Host'] = self.host
        if self.id is not None:
            result['Id'] = self.id
        if self.info is not None:
            result['Info'] = self.info
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time is not None:
            result['Time'] = self.time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('DB') is not None:
            self.db = m.get('DB')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeProcessListResponseBodyItems(TeaModel):
    def __init__(
        self,
        process: List[DescribeProcessListResponseBodyItemsProcess] = None,
    ):
        self.process = process

    def validate(self):
        if self.process:
            for k in self.process:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Process'] = []
        if self.process is not None:
            for k in self.process:
                result['Process'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.process = []
        if m.get('Process') is not None:
            for k in m.get('Process'):
                temp_model = DescribeProcessListResponseBodyItemsProcess()
                self.process.append(temp_model.from_map(k))
        return self


class DescribeProcessListResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeProcessListResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # Details of the queries.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The total number of pages returned.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('Items') is not None:
            temp_model = DescribeProcessListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Th language of the `LocalName` response parameter. Valid values:
        # 
        # *   **zh-CN**: Chinese.
        # *   **en-US**: English.
        # *   **ja**: Japanese.
        # 
        # > If you do not specify this parameter, the Chinese language is used.
        self.accept_language = accept_language
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        vpc_enabled: bool = None,
        zone_id: str = None,
    ):
        # The zone name.
        self.local_name = local_name
        # Indicates whether Virtual Private Cloud (VPC) is supported in the zone. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.vpc_enabled = vpc_enabled
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        zones: DescribeRegionsResponseBodyRegionsRegionZones = None,
    ):
        # The region name.
        self.local_name = local_name
        # The endpoint of the region.
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id
        # The queried zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
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
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The queried regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResubmitConfigRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        # 
        # >  You can call the [DescribeDBResourceGroup](~~459446~~) operation to query the resource group name of a cluster.
        self.group_name = group_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeResubmitConfigResponseBodyRules(TeaModel):
    def __init__(
        self,
        exceed_memory_exception: bool = None,
        group_name: str = None,
        peak_memory: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        # Indicates whether out-of-memory (OOM) check is configured.
        self.exceed_memory_exception = exceed_memory_exception
        # The name of the source resource group.
        self.group_name = group_name
        # The peak memory usage.
        self.peak_memory = peak_memory
        # The duration of the SQL statement. Unit: milliseconds.
        self.query_time = query_time
        # The name of the destination resource group.
        self.target_group_name = target_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exceed_memory_exception is not None:
            result['ExceedMemoryException'] = self.exceed_memory_exception
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.target_group_name is not None:
            result['TargetGroupName'] = self.target_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceedMemoryException') is not None:
            self.exceed_memory_exception = m.get('ExceedMemoryException')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('TargetGroupName') is not None:
            self.target_group_name = m.get('TargetGroupName')
        return self


class DescribeResubmitConfigResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        rules: List[DescribeResubmitConfigResponseBodyRules] = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The job resubmission rules.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeResubmitConfigResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeResubmitConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResubmitConfigResponseBody = None,
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
            temp_model = DescribeResubmitConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQAConfigRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        # 
        # >  You can call the [DescribeDBResourceGroup](~~612410~~) operation to query the resource group name of a cluster.
        self.group_name = group_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeSQAConfigResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        request_id: str = None,
        sqastatus: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        self.group_name = group_name
        # The request ID.
        self.request_id = request_id
        # Indicates whether short query acceleration (SQA) is enabled.
        self.sqastatus = sqastatus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sqastatus is not None:
            result['SQAStatus'] = self.sqastatus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SQAStatus') is not None:
            self.sqastatus = m.get('SQAStatus')
        return self


class DescribeSQAConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQAConfigResponseBody = None,
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
            temp_model = DescribeSQAConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPatternsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        keyword: str = None,
        lang: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters in a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The keyword that is used for the query.
        self.keyword = keyword
        # The language of file titles and error messages. Valid values:
        # 
        # *   **zh** (default): simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The order by which to sort query results. Specify the parameter value in the JSON format. Example: `[{"Field":"AverageQueryTime","Type":"Asc"}]`.
        # 
        # *   `Field` specifies the field by which to sort the query results. Valid values:
        # 
        #     *   `PatternCreationTime`: the earliest commit time of the SQL pattern within the time range to query.
        #     *   `AverageQueryTime`: the average total amount of time consumed by the SQL pattern within the time range to query.
        #     *   `MaxQueryTime`: the maximum total amount of time consumed by the SQL pattern within the time range to query.
        #     *   `AverageExecutionTime`: the average execution duration of the SQL pattern within the time range to query.
        #     *   `MaxExecutionTime`: the maximum execution duration of the SQL pattern within the time range to query.
        #     *   `AveragePeakMemory`: the average peak memory usage of the SQL pattern within the time range to query.
        #     *   `MaxPeakMemory`: the maximum peak memory usage of the SQL pattern within the time range to query.
        #     *   `AverageScanSize`: the average amount of data scanned based on the SQL pattern within the time range to query.
        #     *   `MaxScanSize`: the maximum amount of data scanned based on the SQL pattern within the time range to query.
        #     *   `QueryCount`: the number of queries performed in association with the SQL pattern within the time range to query.
        #     *   `FailedCount`: the number of failed queries performed in association with the SQL pattern within the time range to query.
        # 
        # *   `Type` specifies the sorting order. Valid values (case-insensitive):
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        self.order = order
        # The page number. Pages start from page 1.
        # 
        # > If you do not specify this parameter, the value **1** is used.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # > If you do not specify this parameter, the value **30** is used.
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # > 
        # 
        # *   Only data within the last 14 days can be queried. For example, if the current time is 2021-11-22T12:00:00Z, you can query SQL patterns at a point in time as early as 2021-11-09T12:00:00Z.
        # 
        # *   The maximum time range that can be specified is 24 hours.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order is not None:
            result['Order'] = self.order
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSQLPatternsResponseBodyPatternDetails(TeaModel):
    def __init__(
        self,
        access_ip: str = None,
        average_execution_time: float = None,
        average_peak_memory: float = None,
        average_query_time: float = None,
        average_scan_size: float = None,
        blockable: bool = None,
        failed_count: int = None,
        max_execution_time: int = None,
        max_peak_memory: int = None,
        max_query_time: int = None,
        max_scan_size: int = None,
        pattern_creation_time: str = None,
        pattern_id: str = None,
        query_count: int = None,
        sqlpattern: str = None,
        tables: str = None,
        user: str = None,
    ):
        # The IP address of the SQL client that commits the SQL pattern.
        self.access_ip = access_ip
        # The average execution duration of the SQL pattern within the query time range. Unit: milliseconds.
        self.average_execution_time = average_execution_time
        # The average peak memory usage of the SQL pattern within the query time range. Unit: bytes.
        self.average_peak_memory = average_peak_memory
        # The average total amount of time consumed by the SQL pattern within the query time range. Unit: milliseconds.
        self.average_query_time = average_query_time
        # The average amount of data scanned based on the SQL pattern within the query time range. Unit: bytes.
        self.average_scan_size = average_scan_size
        # Indicates whether the execution of the SQL pattern can be blocked. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # > Only SELECT and INSERT statements can be blocked.
        self.blockable = blockable
        # The number of failed queries executed in association with the SQL pattern within the query time range.
        self.failed_count = failed_count
        # The maximum execution duration of the SQL pattern within the query time range. Unit: milliseconds.
        self.max_execution_time = max_execution_time
        # The maximum peak memory usage of the SQL pattern within the query time range. Unit: bytes.
        self.max_peak_memory = max_peak_memory
        # The maximum total amount of time consumed by the SQL pattern within the query time range. Unit: milliseconds.
        self.max_query_time = max_query_time
        # The maximum amount of data scanned based on the SQL pattern within the query time range. Unit: bytes.
        self.max_scan_size = max_scan_size
        # The earliest commit time of the SQL pattern within the query time range. Unit: milliseconds.
        self.pattern_creation_time = pattern_creation_time
        # The ID of the SQL pattern.
        self.pattern_id = pattern_id
        # The number of queries executed in association with the SQL pattern within the query time range.
        self.query_count = query_count
        # The statement of the SQL pattern.
        self.sqlpattern = sqlpattern
        # The tables scanned based on the SQL pattern.
        self.tables = tables
        # The database username that is used to commit the SQL pattern.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip
        if self.average_execution_time is not None:
            result['AverageExecutionTime'] = self.average_execution_time
        if self.average_peak_memory is not None:
            result['AveragePeakMemory'] = self.average_peak_memory
        if self.average_query_time is not None:
            result['AverageQueryTime'] = self.average_query_time
        if self.average_scan_size is not None:
            result['AverageScanSize'] = self.average_scan_size
        if self.blockable is not None:
            result['Blockable'] = self.blockable
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.max_execution_time is not None:
            result['MaxExecutionTime'] = self.max_execution_time
        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory
        if self.max_query_time is not None:
            result['MaxQueryTime'] = self.max_query_time
        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size
        if self.pattern_creation_time is not None:
            result['PatternCreationTime'] = self.pattern_creation_time
        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.sqlpattern is not None:
            result['SQLPattern'] = self.sqlpattern
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')
        if m.get('AverageExecutionTime') is not None:
            self.average_execution_time = m.get('AverageExecutionTime')
        if m.get('AveragePeakMemory') is not None:
            self.average_peak_memory = m.get('AveragePeakMemory')
        if m.get('AverageQueryTime') is not None:
            self.average_query_time = m.get('AverageQueryTime')
        if m.get('AverageScanSize') is not None:
            self.average_scan_size = m.get('AverageScanSize')
        if m.get('Blockable') is not None:
            self.blockable = m.get('Blockable')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('MaxExecutionTime') is not None:
            self.max_execution_time = m.get('MaxExecutionTime')
        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')
        if m.get('MaxQueryTime') is not None:
            self.max_query_time = m.get('MaxQueryTime')
        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')
        if m.get('PatternCreationTime') is not None:
            self.pattern_creation_time = m.get('PatternCreationTime')
        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('SQLPattern') is not None:
            self.sqlpattern = m.get('SQLPattern')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLPatternsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pattern_details: List[DescribeSQLPatternsResponseBodyPatternDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The queried SQL patterns.
        self.pattern_details = pattern_details
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.pattern_details:
            for k in self.pattern_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PatternDetails'] = []
        if self.pattern_details is not None:
            for k in self.pattern_details:
                result['PatternDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.pattern_details = []
        if m.get('PatternDetails') is not None:
            for k in m.get('PatternDetails'):
                temp_model = DescribeSQLPatternsResponseBodyPatternDetails()
                self.pattern_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSQLPatternsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLPatternsResponseBody = None,
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
            temp_model = DescribeSQLPatternsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPlanRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        process_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The query ID.
        # 
        # > You can call the [DescribeProcessList](~~143382~~) operation to query the IDs of queries that are being executed.
        self.process_id = process_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeSQLPlanResponseBodyDetail(TeaModel):
    def __init__(
        self,
        cputime: int = None,
        client_ip: str = None,
        database: str = None,
        output_rows: int = None,
        output_size: int = None,
        peak_memory: int = None,
        planning_time: int = None,
        queued_time: int = None,
        sql: str = None,
        start_time: str = None,
        state: str = None,
        total_stage: int = None,
        total_task: int = None,
        total_time: int = None,
        user: str = None,
    ):
        # The total CPU time consumed by all operators on multithreaded servers when the SQL statement is executed. Unit: milliseconds.
        self.cputime = cputime
        # The IP address of the client that is used to execute the SQL statement.
        self.client_ip = client_ip
        # The name of the database on which the SQL statement was executed.
        self.database = database
        # The total number of rows generated by the SQL statement.
        self.output_rows = output_rows
        # The total amount of data generated by the SQL statement. Unit: bytes.
        self.output_size = output_size
        # The maximum memory usage when the SQL statement is executed. Unit: bytes.
        self.peak_memory = peak_memory
        # The amount of time consumed to generate the execution plan of the SQL statement. Unit: milliseconds.
        self.planning_time = planning_time
        # The amount of time consumed to queue the SQL statement. Unit: milliseconds.
        self.queued_time = queued_time
        # The SQL statement.
        self.sql = sql
        # The execution start time of the SQL statement. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The final execution state of the SQL statement. Valid values:
        # 
        # *   FINISHED
        # *   FAILED
        self.state = state
        # The total number of stages in the SQL statement.
        self.total_stage = total_stage
        # The total number of tasks in the SQL statement.
        self.total_task = total_task
        # The total amount of time consumed to execute the SQL statement. Unit: milliseconds.
        self.total_time = total_time
        # The name of the user who submitted the SQL statement.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cputime is not None:
            result['CPUTime'] = self.cputime
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.database is not None:
            result['Database'] = self.database
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.output_size is not None:
            result['OutputSize'] = self.output_size
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.planning_time is not None:
            result['PlanningTime'] = self.planning_time
        if self.queued_time is not None:
            result['QueuedTime'] = self.queued_time
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.total_stage is not None:
            result['TotalStage'] = self.total_stage
        if self.total_task is not None:
            result['TotalTask'] = self.total_task
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPUTime') is not None:
            self.cputime = m.get('CPUTime')
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('PlanningTime') is not None:
            self.planning_time = m.get('PlanningTime')
        if m.get('QueuedTime') is not None:
            self.queued_time = m.get('QueuedTime')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TotalStage') is not None:
            self.total_stage = m.get('TotalStage')
        if m.get('TotalTask') is not None:
            self.total_task = m.get('TotalTask')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLPlanResponseBodyStageList(TeaModel):
    def __init__(
        self,
        cputime_avg: int = None,
        cputime_max: int = None,
        cputime_min: int = None,
        input_size_avg: int = None,
        input_size_max: int = None,
        input_size_min: int = None,
        operator_cost: int = None,
        peak_memory: int = None,
        scan_size_avg: int = None,
        scan_size_max: int = None,
        scan_size_min: int = None,
        scan_time_avg: int = None,
        scan_time_max: int = None,
        scan_time_min: int = None,
        stage_id: int = None,
        state: str = None,
    ):
        # The average `CPU Time` value on each compute node in the stage. Unit: milliseconds.
        self.cputime_avg = cputime_avg
        # The maximum `CPU Time` value on each compute node in the stage. Unit: milliseconds.
        self.cputime_max = cputime_max
        # The minimum `CPU Time` value on each compute node in the stage. Unit: milliseconds.
        self.cputime_min = cputime_min
        # The average amount of input data on each compute node in the stage. Unit: bytes.
        self.input_size_avg = input_size_avg
        # The maximum amount of input data on each compute node in the stage. Unit: byte.
        self.input_size_max = input_size_max
        # The minimum amount of input data on each compute node in the stage. Unit: bytes.
        self.input_size_min = input_size_min
        # The total CPU time consumed by all operators in the stage, which is equivalent to the total CPU time of the stage. You can use this parameter to determine which parts of the stage consume a large amount of computing resources. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The maximum memory usage when the SQL statement is executed. Unit: bytes.
        self.peak_memory = peak_memory
        # The average amount of data scanned by a scan operator on each storage node in the stage. Unit: bytes.
        self.scan_size_avg = scan_size_avg
        # The maximum amount of data scanned by a scan operator on each storage node in the stage. Unit: bytes.
        self.scan_size_max = scan_size_max
        # The minimum amount of data scanned by a scan operator on each storage node in the stage. Unit: bytes.
        self.scan_size_min = scan_size_min
        # The average amount of time consumed by a scan operator to read data on each storage node in the stage. Unit: milliseconds.
        self.scan_time_avg = scan_time_avg
        # The maximum amount of time consumed by a scan operator to read data on each storage node in the stage. Unit: milliseconds.
        self.scan_time_max = scan_time_max
        # The minimum amount of time consumed by a scan operator to read data on each storage node in the stage. Unit: milliseconds.
        self.scan_time_min = scan_time_min
        # The stage ID.
        self.stage_id = stage_id
        # The final execution state of the stage. Valid values:
        # 
        # *   FINISHED
        # *   CANCELED
        # *   ABORTED
        # *   FAILED
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cputime_avg is not None:
            result['CPUTimeAvg'] = self.cputime_avg
        if self.cputime_max is not None:
            result['CPUTimeMax'] = self.cputime_max
        if self.cputime_min is not None:
            result['CPUTimeMin'] = self.cputime_min
        if self.input_size_avg is not None:
            result['InputSizeAvg'] = self.input_size_avg
        if self.input_size_max is not None:
            result['InputSizeMax'] = self.input_size_max
        if self.input_size_min is not None:
            result['InputSizeMin'] = self.input_size_min
        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.scan_size_avg is not None:
            result['ScanSizeAvg'] = self.scan_size_avg
        if self.scan_size_max is not None:
            result['ScanSizeMax'] = self.scan_size_max
        if self.scan_size_min is not None:
            result['ScanSizeMin'] = self.scan_size_min
        if self.scan_time_avg is not None:
            result['ScanTimeAvg'] = self.scan_time_avg
        if self.scan_time_max is not None:
            result['ScanTimeMax'] = self.scan_time_max
        if self.scan_time_min is not None:
            result['ScanTimeMin'] = self.scan_time_min
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPUTimeAvg') is not None:
            self.cputime_avg = m.get('CPUTimeAvg')
        if m.get('CPUTimeMax') is not None:
            self.cputime_max = m.get('CPUTimeMax')
        if m.get('CPUTimeMin') is not None:
            self.cputime_min = m.get('CPUTimeMin')
        if m.get('InputSizeAvg') is not None:
            self.input_size_avg = m.get('InputSizeAvg')
        if m.get('InputSizeMax') is not None:
            self.input_size_max = m.get('InputSizeMax')
        if m.get('InputSizeMin') is not None:
            self.input_size_min = m.get('InputSizeMin')
        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('ScanSizeAvg') is not None:
            self.scan_size_avg = m.get('ScanSizeAvg')
        if m.get('ScanSizeMax') is not None:
            self.scan_size_max = m.get('ScanSizeMax')
        if m.get('ScanSizeMin') is not None:
            self.scan_size_min = m.get('ScanSizeMin')
        if m.get('ScanTimeAvg') is not None:
            self.scan_time_avg = m.get('ScanTimeAvg')
        if m.get('ScanTimeMax') is not None:
            self.scan_time_max = m.get('ScanTimeMax')
        if m.get('ScanTimeMin') is not None:
            self.scan_time_min = m.get('ScanTimeMin')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeSQLPlanResponseBody(TeaModel):
    def __init__(
        self,
        detail: DescribeSQLPlanResponseBodyDetail = None,
        origin_info: str = None,
        request_id: str = None,
        stage_list: List[DescribeSQLPlanResponseBodyStageList] = None,
    ):
        # The execution information about the SQL statement.
        self.detail = detail
        # The original information about the SQL statement.
        self.origin_info = origin_info
        # The request ID.
        self.request_id = request_id
        # The queried plan in different stages.
        self.stage_list = stage_list

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.stage_list:
            for k in self.stage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.origin_info is not None:
            result['OriginInfo'] = self.origin_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StageList'] = []
        if self.stage_list is not None:
            for k in self.stage_list:
                result['StageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = DescribeSQLPlanResponseBodyDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('OriginInfo') is not None:
            self.origin_info = m.get('OriginInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stage_list = []
        if m.get('StageList') is not None:
            for k in m.get('StageList'):
                temp_model = DescribeSQLPlanResponseBodyStageList()
                self.stage_list.append(temp_model.from_map(k))
        return self


class DescribeSQLPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLPlanResponseBody = None,
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
            temp_model = DescribeSQLPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPlanTaskRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        process_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        stage_id: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the task.
        self.process_id = process_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The stage of the task.
        self.stage_id = stage_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        return self


class DescribeSQLPlanTaskResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        elapsed_time: int = None,
        input_rows: int = None,
        input_size: int = None,
        operator_cost: int = None,
        output_rows: int = None,
        output_size: int = None,
        peak_memory: int = None,
        scan_cost: int = None,
        scan_rows: int = None,
        scan_size: int = None,
        state: str = None,
        task_id: int = None,
    ):
        # The time elapsed from when the task was created to when the task was complete. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The number of input rows in the task.
        self.input_rows = input_rows
        # The amount of input data in the task. Unit: bytes.
        self.input_size = input_size
        # The total amount of time consumed by operators in the task on a specific node. This parameter can be used to determine whether long tails occur in computing. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The number of output rows in the task.
        self.output_rows = output_rows
        # The amount of output data in the task. Unit: bytes.
        self.output_size = output_size
        # The peak memory of the task on a specific node. Unit: bytes.
        self.peak_memory = peak_memory
        # The time consumed to scan data from a data source in the task. Unit: milliseconds.
        self.scan_cost = scan_cost
        # The number of rows scanned from a data source in the task.
        self.scan_rows = scan_rows
        # The amount of data scanned from a data source in the task. Unit: bytes.
        self.scan_size = scan_size
        # The final execution status of the task. Valid values:
        # 
        # *   FINISHED
        # *   CANCELED
        # *   ABORTED
        # *   FAILED
        self.state = state
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.input_rows is not None:
            result['InputRows'] = self.input_rows
        if self.input_size is not None:
            result['InputSize'] = self.input_size
        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.output_size is not None:
            result['OutputSize'] = self.output_size
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.scan_cost is not None:
            result['ScanCost'] = self.scan_cost
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size
        if self.state is not None:
            result['State'] = self.state
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')
        if m.get('InputSize') is not None:
            self.input_size = m.get('InputSize')
        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('ScanCost') is not None:
            self.scan_cost = m.get('ScanCost')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeSQLPlanTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[DescribeSQLPlanTaskResponseBodyTaskList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of tasks.
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = DescribeSQLPlanTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class DescribeSQLPlanTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLPlanTaskResponseBody = None,
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
            temp_model = DescribeSQLPlanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSchemasRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeSchemasResponseBodyItemsSchema(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        schema_name: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeSchemasResponseBodyItems(TeaModel):
    def __init__(
        self,
        schema: List[DescribeSchemasResponseBodyItemsSchema] = None,
    ):
        self.schema = schema

    def validate(self):
        if self.schema:
            for k in self.schema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Schema'] = []
        if self.schema is not None:
            for k in self.schema:
                result['Schema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k in m.get('Schema'):
                temp_model = DescribeSchemasResponseBodyItemsSchema()
                self.schema.append(temp_model.from_map(k))
        return self


class DescribeSchemasResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeSchemasResponseBodyItems = None,
        request_id: str = None,
    ):
        # The databases.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeSchemasResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSchemasResponseBody = None,
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
            temp_model = DescribeSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbname: str = None,
        end_time: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        process_id: str = None,
        range: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        state: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.dbname = dbname
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time. The specified time range must be less than seven days.
        self.end_time = end_time
        # The order in which to sort the retrieved entries by field. Specify this parameter in the JSON format. The value is an ordered array that uses the order of the input array and contains `Field` and `Type`. Example: `[{"Field":"ExecutionStartTime","Type":"Desc"},{"Field":"ScanRows","Type":"Asc"}]`.
        # 
        # *   `Field`: the field that is used to sort the retrieved entries. Valid values:
        # 
        #     *   **HostAddress**: the IP address of the client that is used to connect to the database.
        #     *   **UserName**: the username.
        #     *   **ExecutionStartTime**: the start time of the query execution.
        #     *   **QueryTime**: the amount of time consumed to execute the SQL statement.
        #     *   **PeakMemoryUsage**: the maximum memory usage when the SQL statement is executed.
        #     *   **ScanRows**: the number of rows to be scanned from a data source in the task.
        #     *   **ScanSize**: the amount of data to be scanned.
        #     *   **ScanTime**: the total amount of time consumed to scan data.
        #     *   **PlanningTime**: the amount of time consumed to generate execution plans.
        #     *   **WallTime**: the accumulated CPU Time values of all operators in the query on each node.
        #     *   **ProcessID**: the ID of the process.
        # 
        # *   `Type`: the sorting type of the retrieved entries. Valid values:
        # 
        #     *   **Desc**: descending order
        #     *   **Asc**: ascending order
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: 30.
        self.page_size = page_size
        # The ID of the process.
        self.process_id = process_id
        # The range conditions used to filter specified fields, including `Max` and `Min`. Specify this parameter in the JSON format. Example: `[{"Field":"ScanSize","Min":"1000000","Max":"10000000"},{"Field":"QueryTime","Min":"1000","Max":"10000"}]`.
        # 
        # `Field`: the field to be filtered. Valid values:
        # 
        # *   **ScanSize**: the amount of data to be scanned. Unit: KB.
        # *   **QueryTime**: the amount of time consumed to execute the statement. Unit: milliseconds.
        # *   **PeakMemoryUsage**: the maximum memory usage when the SQL statement is executed. Unit: KB.
        # 
        # >  `Min` indicates the minimum value of the query range (left operand). `Max` indicates the maximum value of the query range (right operand). Max and Min are both of the String type.
        self.range = range
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        self.start_time = start_time
        # The state of the query. Valid values:
        # 
        # *   **Successed**: successful
        # *   **Failed**: failed
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order is not None:
            result['Order'] = self.order
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.process_id is not None:
            result['ProcessID'] = self.process_id
        if self.range is not None:
            result['Range'] = self.range
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord(TeaModel):
    def __init__(
        self,
        dbname: str = None,
        execution_start_time: str = None,
        host_address: str = None,
        output_size: str = None,
        parse_row_counts: int = None,
        peak_memory_usage: str = None,
        planning_time: int = None,
        process_id: str = None,
        query_time: int = None,
        queue_time: int = None,
        return_row_counts: int = None,
        sqltext: str = None,
        scan_rows: int = None,
        scan_size: str = None,
        scan_time: int = None,
        state: str = None,
        user_name: str = None,
        wall_time: int = None,
    ):
        # The name of the database.
        self.dbname = dbname
        # The time when the execution started. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.execution_start_time = execution_start_time
        # The IP address of the client that is used to connect to the database.
        self.host_address = host_address
        # The amount of output data in the task. Unit: bytes.
        self.output_size = output_size
        # The number of rows parsed by the SQL statement.
        self.parse_row_counts = parse_row_counts
        # The maximum memory usage when the SQL statement is executed. Unit: KB.
        self.peak_memory_usage = peak_memory_usage
        # The amount of time consumed to generate execution plans. Unit: milliseconds.
        self.planning_time = planning_time
        # The ID of the process.
        self.process_id = process_id
        # The time consumed to execute the SQL statement. Unit: milliseconds.
        self.query_time = query_time
        # The queuing duration before the query is executed. Unit: milliseconds.
        self.queue_time = queue_time
        # The number of rows returned by the SQL statement.
        self.return_row_counts = return_row_counts
        # Details of the SQL statement.
        self.sqltext = sqltext
        # The number of rows scanned from a data source in the task.
        self.scan_rows = scan_rows
        # The amount of scanned data. Unit: KB.
        self.scan_size = scan_size
        # The total amount of time consumed to scan data. It is an accumulated value collected from multiple TableScanNode nodes. Unit: milliseconds.
        self.scan_time = scan_time
        # The execution state of the SQL statement.
        self.state = state
        # The username.
        self.user_name = user_name
        # The accumulated CPU Time value of all operators collected from all nodes. Unit: milliseconds.
        self.wall_time = wall_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.output_size is not None:
            result['OutputSize'] = self.output_size
        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts
        if self.peak_memory_usage is not None:
            result['PeakMemoryUsage'] = self.peak_memory_usage
        if self.planning_time is not None:
            result['PlanningTime'] = self.planning_time
        if self.process_id is not None:
            result['ProcessID'] = self.process_id
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size
        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time
        if self.state is not None:
            result['State'] = self.state
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.wall_time is not None:
            result['WallTime'] = self.wall_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')
        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')
        if m.get('PeakMemoryUsage') is not None:
            self.peak_memory_usage = m.get('PeakMemoryUsage')
        if m.get('PlanningTime') is not None:
            self.planning_time = m.get('PlanningTime')
        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')
        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WallTime') is not None:
            self.wall_time = m.get('WallTime')
        return self


class DescribeSlowLogRecordsResponseBodyItems(TeaModel):
    def __init__(
        self,
        slow_log_record: List[DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord] = None,
    ):
        self.slow_log_record = slow_log_record

    def validate(self):
        if self.slow_log_record:
            for k in self.slow_log_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SlowLogRecord'] = []
        if self.slow_log_record is not None:
            for k in self.slow_log_record:
                result['SlowLogRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slow_log_record = []
        if m.get('SlowLogRecord') is not None:
            for k in m.get('SlowLogRecord'):
                temp_model = DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord()
                self.slow_log_record.append(temp_model.from_map(k))
        return self


class DescribeSlowLogRecordsResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: DescribeSlowLogRecordsResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # Details of the slow query logs.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        dbcluster_id: str = None,
        dbname: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.dbname = dbname
        # The end of the time range to query. The end time must be later than the start time. The maximum time range that can be specified is seven days. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeriesSeriesItem(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: str = None,
    ):
        # The name of the performance metric.
        self.name = name
        # The values of the performance metric.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeries(TeaModel):
    def __init__(
        self,
        series_item: List[DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeriesSeriesItem] = None,
    ):
        self.series_item = series_item

    def validate(self):
        if self.series_item:
            for k in self.series_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SeriesItem'] = []
        if self.series_item is not None:
            for k in self.series_item:
                result['SeriesItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.series_item = []
        if m.get('SeriesItem') is not None:
            for k in m.get('SeriesItem'):
                temp_model = DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeriesSeriesItem()
                self.series_item.append(temp_model.from_map(k))
        return self


class DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItem(TeaModel):
    def __init__(
        self,
        key: str = None,
        series: DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeries = None,
        unit: str = None,
    ):
        # The trend of slow query logs. The value is AnalyticDB_SlowLogTrend.
        self.key = key
        # The performance metrics.
        self.series = series
        # The unit of performance metrics.
        self.unit = unit

    def validate(self):
        if self.series:
            self.series.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.series is not None:
            result['Series'] = self.series.to_map()
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Series') is not None:
            temp_model = DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeries()
            self.series = temp_model.from_map(m['Series'])
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeSlowLogTrendResponseBodyItems(TeaModel):
    def __init__(
        self,
        slow_log_trend_item: List[DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItem] = None,
    ):
        self.slow_log_trend_item = slow_log_trend_item

    def validate(self):
        if self.slow_log_trend_item:
            for k in self.slow_log_trend_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SlowLogTrendItem'] = []
        if self.slow_log_trend_item is not None:
            for k in self.slow_log_trend_item:
                result['SlowLogTrendItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slow_log_trend_item = []
        if m.get('SlowLogTrendItem') is not None:
            for k in m.get('SlowLogTrendItem'):
                temp_model = DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItem()
                self.slow_log_trend_item.append(temp_model.from_map(k))
        return self


class DescribeSlowLogTrendResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        items: DescribeSlowLogTrendResponseBodyItems = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. The end time must be later than the start time. The maximum time range that can be specified is seven days. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The information about the trend of slow query logs.
        self.items = items
        # The request ID.
        self.request_id = request_id
        # The start time of the query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogTrendResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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


class DescribeSqlPatternRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        sql_pattern: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The order by which to sort query results. Specify the parameter value in the JSON string format. Example: `[{"Field":"Pattern","Type":"Asc"}]`. Parameters:
        # 
        # *   `Field` specifies the field by which to sort the query results. Valid values:
        # 
        #     *   `Pattern`: the SQL pattern.
        #     *   `AccessIP`: the IP address of the client.
        #     *   `User`: the username.
        #     *   `QueryCount`: the number of queries performed in association with the SQL pattern within the time range to query.
        #     *   `AvgPeakMemory`: the average peak memory usage of the SQL pattern within the time range to query. Unit: KB.
        #     *   `MaxPeakMemory`: the maximum peak memory usage of the SQL pattern within the time range to query. Unit: KB.
        #     *   `AvgCpuTime`: the average execution duration of the SQL pattern within the time range to query. Unit: milliseconds.
        #     *   `MaxCpuTime`: the maximum execution duration of the SQL pattern within the time range to query. Unit: milliseconds.
        #     *   `AvgStageCount`: the average number of stages.
        #     *   `MaxStageCount`: the maximum number of stages.
        #     *   `AvgTaskCount`: the average number of tasks.
        #     *   `MaxTaskCount`: the maximum number of tasks.
        #     *   `AvgScanSize`: the average amount of data scanned based on the SQL pattern within the time range to query. Unit: KB.
        #     *   `MaxScanSize`: the maximum amount of data scanned based on the SQL pattern within the time range to query. Unit: KB.
        # 
        # *   `Type` specifies the sorting order. Valid values:
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        # 
        # > 
        # 
        # *   If you do not specify this parameter, query results are sorted in ascending order of `Pattern`.
        # 
        # *   If you want to sort query results by `AccessIP`, you must set the `Type` parameter to `accessip`. If you want to sort query results by `User`, you must leave the `Type` parameter empty or set it to `user`.
        self.order = order
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. The value must be a positive integer. Default value: **30**.
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The keyword that is used for the query.
        # 
        # > If you do not specify this parameter, all SQL patterns of the AnalyticDB for MySQL cluster within the time period specified by `StartTime` are returned.
        self.sql_pattern = sql_pattern
        # The start date to query. Specify the time in the *yyyy-MM-dd* format. The time must be in UTC.
        # 
        # > Only data within the last 30 days can be queried.
        self.start_time = start_time
        # The dimension by which to aggregate the SQL patterns. Valid values:
        # 
        # *   `user`: aggregates the SQL patterns by user.
        # *   `accessip`: aggregates the SQL patterns by client IP address.
        # 
        # > If you do not specify this parameter, the SQL patterns are aggregated by `user`.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sql_pattern is not None:
            result['SqlPattern'] = self.sql_pattern
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SqlPattern') is not None:
            self.sql_pattern = m.get('SqlPattern')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSqlPatternResponseBodyItems(TeaModel):
    def __init__(
        self,
        access_ip: str = None,
        avg_cpu_time: str = None,
        avg_peak_memory: str = None,
        avg_scan_size: str = None,
        avg_stage_count: str = None,
        avg_task_count: str = None,
        instance_name: str = None,
        max_cpu_time: str = None,
        max_peak_memory: str = None,
        max_scan_size: str = None,
        max_stage_count: str = None,
        max_task_count: str = None,
        pattern: str = None,
        query_count: str = None,
        report_date: str = None,
        user: str = None,
    ):
        # The IP address of the client.
        # 
        # > This parameter is returned only when `Type` is set to `accessip`.
        self.access_ip = access_ip
        # The average execution duration of the SQL pattern within the time range to query. Unit: milliseconds.
        self.avg_cpu_time = avg_cpu_time
        # The average peak memory usage of the SQL pattern within the query time range. Unit: KB.
        self.avg_peak_memory = avg_peak_memory
        # The average amount of data scanned based on the SQL pattern within the query time range. Unit: KB.
        self.avg_scan_size = avg_scan_size
        # The average number of stages.
        self.avg_stage_count = avg_stage_count
        # The average number of tasks.
        self.avg_task_count = avg_task_count
        # The cluster ID.
        self.instance_name = instance_name
        # The maximum execution duration of the SQL pattern within the time range to query. Unit: milliseconds.
        self.max_cpu_time = max_cpu_time
        # The maximum peak memory usage of the SQL pattern within the query time range. Unit: KB.
        self.max_peak_memory = max_peak_memory
        # The maximum amount of data scanned based on the SQL pattern within the query time range. Unit: KB.
        self.max_scan_size = max_scan_size
        # The maximum number of stages.
        self.max_stage_count = max_stage_count
        # The maximum number of tasks.
        self.max_task_count = max_task_count
        # The SQL pattern.
        self.pattern = pattern
        # The number of queries performed in association with the SQL pattern within the query time range.
        self.query_count = query_count
        # The start date of the query.
        self.report_date = report_date
        # The username.
        # 
        # > This parameter is returned only when `Type` is left empty or set to `user`.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_ip is not None:
            result['AccessIP'] = self.access_ip
        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time
        if self.avg_peak_memory is not None:
            result['AvgPeakMemory'] = self.avg_peak_memory
        if self.avg_scan_size is not None:
            result['AvgScanSize'] = self.avg_scan_size
        if self.avg_stage_count is not None:
            result['AvgStageCount'] = self.avg_stage_count
        if self.avg_task_count is not None:
            result['AvgTaskCount'] = self.avg_task_count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory
        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size
        if self.max_stage_count is not None:
            result['MaxStageCount'] = self.max_stage_count
        if self.max_task_count is not None:
            result['MaxTaskCount'] = self.max_task_count
        if self.pattern is not None:
            result['Pattern'] = self.pattern
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.report_date is not None:
            result['ReportDate'] = self.report_date
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIP') is not None:
            self.access_ip = m.get('AccessIP')
        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')
        if m.get('AvgPeakMemory') is not None:
            self.avg_peak_memory = m.get('AvgPeakMemory')
        if m.get('AvgScanSize') is not None:
            self.avg_scan_size = m.get('AvgScanSize')
        if m.get('AvgStageCount') is not None:
            self.avg_stage_count = m.get('AvgStageCount')
        if m.get('AvgTaskCount') is not None:
            self.avg_task_count = m.get('AvgTaskCount')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')
        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')
        if m.get('MaxStageCount') is not None:
            self.max_stage_count = m.get('MaxStageCount')
        if m.get('MaxTaskCount') is not None:
            self.max_task_count = m.get('MaxTaskCount')
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSqlPatternResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeSqlPatternResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried SQL pattern.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = DescribeSqlPatternResponseBodyItems()
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


class DescribeSqlPatternResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSqlPatternResponseBody = None,
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
            temp_model = DescribeSqlPatternResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTableAccessCountRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
        table_name: str = None,
    ):
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the details of all AnalyticDB for MySQL clusters within a specified region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The order by which to sort query results. Specify the parameter value in the JSON string format. Example: `[{"Field":"TableSchema","Type":"Asc"}]`.
        # 
        # *   `Field` indicates the field that is used to sort the retrieved entries. Valid values:
        # 
        #     *   `TableSchema`: the name of the database to which the table belongs.
        #     *   `TableName`: the name of the table.
        #     *   `AccessCount`: the number of accesses to the table.
        # 
        # *   `Type` indicates the sorting method. Valid values:
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        # 
        # >  If this parameter is not specified, query results are sorted in ascending order of the database to which a specific table belongs.
        self.order = order
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. The value must be a positive integer. Default value: **30**.
        self.page_size = page_size
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the regions and zones supported by AnalyticDB for MySQL, including region IDs.
        self.region_id = region_id
        # The date to query. Specify the time in the *yyyy-MM-dd* format. The time must be in UTC.
        # 
        # >  Only data for the last 30 days can be queried.
        self.start_time = start_time
        # The name of the specific table.
        # 
        # >  If this parameter is not specified, the number of accesses to all tables within the specified cluster for a specified date is returned.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTableAccessCountResponseBodyItems(TeaModel):
    def __init__(
        self,
        access_count: str = None,
        instance_name: str = None,
        report_date: str = None,
        table_name: str = None,
        table_schema: str = None,
    ):
        # The number of accesses to the table.
        self.access_count = access_count
        # The ID of the cluster to which the table belongs.
        self.instance_name = instance_name
        # The date when the table was used.
        self.report_date = report_date
        # The name of the table.
        self.table_name = table_name
        # The database to which the table belongs.
        self.table_schema = table_schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_count is not None:
            result['AccessCount'] = self.access_count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.report_date is not None:
            result['ReportDate'] = self.report_date
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')
        return self


class DescribeTableAccessCountResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeTableAccessCountResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the table usage.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
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
                temp_model = DescribeTableAccessCountResponseBodyItems()
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


class DescribeTableAccessCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTableAccessCountResponseBody = None,
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
            temp_model = DescribeTableAccessCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTableDetailRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTableDetailResponseBodyItemsShard(TeaModel):
    def __init__(
        self,
        id: int = None,
        size: int = None,
    ):
        # The ID of the partition. Only the numeric part of the partition name is returned.
        self.id = id
        # The number of rows in the table.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeTableDetailResponseBodyItems(TeaModel):
    def __init__(
        self,
        shard: List[DescribeTableDetailResponseBodyItemsShard] = None,
    ):
        self.shard = shard

    def validate(self):
        if self.shard:
            for k in self.shard:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Shard'] = []
        if self.shard is not None:
            for k in self.shard:
                result['Shard'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shard = []
        if m.get('Shard') is not None:
            for k in m.get('Shard'):
                temp_model = DescribeTableDetailResponseBodyItemsShard()
                self.shard.append(temp_model.from_map(k))
        return self


class DescribeTableDetailResponseBody(TeaModel):
    def __init__(
        self,
        avg_size: int = None,
        items: DescribeTableDetailResponseBodyItems = None,
        request_id: str = None,
    ):
        # The average number of rows in partitions.
        self.avg_size = avg_size
        # The list of partitions.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_size is not None:
            result['AvgSize'] = self.avg_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgSize') is not None:
            self.avg_size = m.get('AvgSize')
        if m.get('Items') is not None:
            temp_model = DescribeTableDetailResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTableDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTableDetailResponseBody = None,
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
            temp_model = DescribeTableDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTablePartitionDiagnoseRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 30. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeTablePartitionDiagnoseResponseBodyItems(TeaModel):
    def __init__(
        self,
        partition_detail: str = None,
        partition_number: int = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # Details of the inappropriate partitions.
        self.partition_detail = partition_detail
        # The number of partitions.
        self.partition_number = partition_number
        # The name of the database.
        self.schema_name = schema_name
        # The table name.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partition_detail is not None:
            result['PartitionDetail'] = self.partition_detail
        if self.partition_number is not None:
            result['PartitionNumber'] = self.partition_number
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PartitionDetail') is not None:
            self.partition_detail = m.get('PartitionDetail')
        if m.get('PartitionNumber') is not None:
            self.partition_number = m.get('PartitionNumber')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTablePartitionDiagnoseResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: List[DescribeTablePartitionDiagnoseResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        suggest_max_records_per_partition: int = None,
        suggest_min_records_per_partition: int = None,
        total_count: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The information of tables.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The recommended maximum number of rows in each list partition.
        self.suggest_max_records_per_partition = suggest_max_records_per_partition
        # The recommended minimum number of rows in each list partition.
        self.suggest_min_records_per_partition = suggest_min_records_per_partition
        # The total number of entries.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if self.suggest_max_records_per_partition is not None:
            result['SuggestMaxRecordsPerPartition'] = self.suggest_max_records_per_partition
        if self.suggest_min_records_per_partition is not None:
            result['SuggestMinRecordsPerPartition'] = self.suggest_min_records_per_partition
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTablePartitionDiagnoseResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuggestMaxRecordsPerPartition') is not None:
            self.suggest_max_records_per_partition = m.get('SuggestMaxRecordsPerPartition')
        if m.get('SuggestMinRecordsPerPartition') is not None:
            self.suggest_min_records_per_partition = m.get('SuggestMinRecordsPerPartition')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTablePartitionDiagnoseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTablePartitionDiagnoseResponseBody = None,
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
            temp_model = DescribeTablePartitionDiagnoseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTableStatisticsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query details about all AnalyticDB for MySQL clusters in a specific region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The order in which to sort the retrieved records by field. Specify this value in the JSON format. The value is an ordered array that uses the order of the input array and contains `Field` and `Type`. Example: `[{ "Field":"TableName", "Type":"Asc" }]`.
        # 
        # *   In the example, `Field` indicates the field that is used to sort the retrieved records. Set the value of Field to `TableName`.
        # 
        # *   `Type` indicates the sort type. Valid values (case-insensitive):
        # 
        #     *   **Desc**: The entries are sorted in descending order.
        #     *   **Asc**: The entries are sorted in ascending order.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: 30.
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order is not None:
            result['Order'] = self.order
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeTableStatisticsResponseBodyItemsTableStatisticRecords(TeaModel):
    def __init__(
        self,
        cold_data_size: int = None,
        data_size: int = None,
        index_size: int = None,
        partition_count: int = None,
        primary_key_index_size: int = None,
        row_count: int = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The total amount of cold data. Unit: byte.
        # 
        # >  The parameter is returned only when the engine version of the cluster is 3.1.3.4 or later.
        self.cold_data_size = cold_data_size
        # The amount of data in the table. Unit: byte.
        self.data_size = data_size
        # The amount of data in indexes. Unit: byte.
        self.index_size = index_size
        # The number of partitions.
        self.partition_count = partition_count
        # The amount of data in primary key indexes. Unit: byte.
        self.primary_key_index_size = primary_key_index_size
        # The number of rows in the table.
        self.row_count = row_count
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cold_data_size is not None:
            result['ColdDataSize'] = self.cold_data_size
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.index_size is not None:
            result['IndexSize'] = self.index_size
        if self.partition_count is not None:
            result['PartitionCount'] = self.partition_count
        if self.primary_key_index_size is not None:
            result['PrimaryKeyIndexSize'] = self.primary_key_index_size
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdDataSize') is not None:
            self.cold_data_size = m.get('ColdDataSize')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')
        if m.get('PartitionCount') is not None:
            self.partition_count = m.get('PartitionCount')
        if m.get('PrimaryKeyIndexSize') is not None:
            self.primary_key_index_size = m.get('PrimaryKeyIndexSize')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTableStatisticsResponseBodyItems(TeaModel):
    def __init__(
        self,
        table_statistic_records: List[DescribeTableStatisticsResponseBodyItemsTableStatisticRecords] = None,
    ):
        self.table_statistic_records = table_statistic_records

    def validate(self):
        if self.table_statistic_records:
            for k in self.table_statistic_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TableStatisticRecords'] = []
        if self.table_statistic_records is not None:
            for k in self.table_statistic_records:
                result['TableStatisticRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table_statistic_records = []
        if m.get('TableStatisticRecords') is not None:
            for k in m.get('TableStatisticRecords'):
                temp_model = DescribeTableStatisticsResponseBodyItemsTableStatisticRecords()
                self.table_statistic_records.append(temp_model.from_map(k))
        return self


class DescribeTableStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: DescribeTableStatisticsResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # Details about table statistics.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Items') is not None:
            temp_model = DescribeTableStatisticsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTableStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTableStatisticsResponseBody = None,
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
            temp_model = DescribeTableStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTablesRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schema_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the database.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeTablesResponseBodyItemsTable(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTablesResponseBodyItems(TeaModel):
    def __init__(
        self,
        table: List[DescribeTablesResponseBodyItemsTable] = None,
    ):
        self.table = table

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeTablesResponseBodyItemsTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeTablesResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeTablesResponseBodyItems = None,
        request_id: str = None,
    ):
        # The queried tables.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeTablesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTablesResponseBody = None,
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
            temp_model = DescribeTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskInfoResponseBodyTaskInfo(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        finish_time: str = None,
        progress: str = None,
        status: str = None,
        task_id: int = None,
    ):
        # The start time of the task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.begin_time = begin_time
        # The end time of the task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.finish_time = finish_time
        # The progress of the task. Unit: %.
        self.progress = progress
        # The status. Valid values:
        # 
        # *   Waiting
        # *   Running
        # *   Finished
        # *   Failed
        # *   Closed
        # *   Cancel
        # *   Retry
        # *   Pause
        # *   Stop
        self.status = status
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_info: DescribeTaskInfoResponseBodyTaskInfo = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried task.
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskInfo') is not None:
            temp_model = DescribeTaskInfoResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        return self


class DescribeTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskInfoResponseBody = None,
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
            temp_model = DescribeTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The virtual private cloud (VPC) ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the VPC ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vsw_id = vsw_id
        # The zone ID.
        # 
        # > You can call the [DescribeRegions](~~129857~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeVSwitchesResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        bid: str = None,
        cidr_block: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_default: bool = None,
        iz_no: str = None,
        region_no: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        # The ID of the Resource Access Management (RAM) user.
        self.ali_uid = ali_uid
        # The ID of the user channel.
        self.bid = bid
        # The IPv4 CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The time when the vSwitch was created.
        self.gmt_create = gmt_create
        # The time when the vSwitch was modified.
        self.gmt_modified = gmt_modified
        # Indicates whether the vSwitch is the default vSwitch. Valid values: **true**: The vSwitch is the default vSwitch. **false**: The vSwitch is not the default vSwitch.
        self.is_default = is_default
        # The zone ID of the vSwitch.
        self.iz_no = iz_no
        # The region ID of the vSwitch.
        self.region_no = region_no
        # The state of the vSwitch. Valid values: **Pending**: the vSwitch is being configured. **Available**: the vSwitch is available.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The name of the vSwitch.
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.iz_no is not None:
            result['IzNo'] = self.iz_no
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        v_switch: List[DescribeVSwitchesResponseBodyVSwitchesVSwitch] = None,
    ):
        # The queried vSwitch.
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeVSwitchesResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        v_switches: DescribeVSwitchesResponseBodyVSwitches = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried vSwitches.
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitches') is not None:
            temp_model = DescribeVSwitchesResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVSwitchesResponseBody = None,
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
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachUserENIRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query cluster IDs.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DetachUserENIResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DetachUserENIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachUserENIResponseBody = None,
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
            temp_model = DetachUserENIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAdviceServiceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of Data Warehouse Edition (V3.0) clusters.
        self.dbcluster_id = dbcluster_id
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableAdviceServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The message returned for the operation. Valid values:
        # 
        # *   **Success** is returned if the operation is successful.
        # *   An error message is returned if the operation fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableAdviceServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAdviceServiceResponseBody = None,
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
            temp_model = DisableAdviceServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadDiagnosisRecordsRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        dbcluster_id: str = None,
        database: str = None,
        end_time: str = None,
        keyword: str = None,
        lang: str = None,
        max_peak_memory: int = None,
        max_scan_size: int = None,
        min_peak_memory: int = None,
        min_scan_size: int = None,
        query_condition: str = None,
        region_id: str = None,
        resource_group: str = None,
        start_time: str = None,
        user_name: str = None,
    ):
        # The source IP addresses.
        # 
        # > You can call the [DescribeDiagnosisDimensions](~~308210~~) operation to query the resource group, database name, username, and source IP address of the SQL statements to be queried.
        self.client_ip = client_ip
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The name of the database on which the SQL statements are executed.
        # 
        # > You can call the [DescribeDiagnosisDimensions](~~308210~~) operation to query the resource group, database name, username, and source IP address of the SQL statements to be queried.
        self.database = database
        # The end of the time range to query. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > 
        # 
        # *   The end time must be later than the start time.
        # 
        # *   The maximum time range that can be specified is 24 hours.
        self.end_time = end_time
        # The keyword that is used for the query.
        self.keyword = keyword
        # The language of file titles and error messages. Valid values:
        # 
        # *   **zh** (default): simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The maximum peak memory of the SQL statements. Unit: bytes.
        self.max_peak_memory = max_peak_memory
        # The maximum scan size of the SQL statements. Unit: bytes.
        self.max_scan_size = max_scan_size
        # The minimum peak memory of the SQL statements. Unit: bytes.
        self.min_peak_memory = min_peak_memory
        # The minimum scan size of the SQL statements. Unit: bytes.
        self.min_scan_size = min_scan_size
        # The SQL query condition, which can be a combination of the `Type` and `Value` fields or a combination of the Type, `Min`, and `Max` fields. Specify the condition in the JSON format. `Type` specifies the SQL query dimension. Valid values for Type: `maxCost`, `status`, and `cost`. `Value`, `Min`, or `Max` specifies the SQL query range for the dimension. Valid values:
        # 
        # *   `{"Type":"maxCost","Value":"100"}`: queries the top 100 most time-consuming SQL statements. Set `Value` to 100.
        # *   `{"Type":"status","Value":"finished"}`: queries executed SQL statements. You can set `Value` to `running` to query SQL statements that are being executed. You can also set Value to `failed` to query SQL statements that failed to be executed.
        # *   `{"Type":"cost","Min":"10","Max":"200"}`: queries SQL statements whose execution durations are in the range of 10 to 200 milliseconds. You can also customize the maximum and minimum execution durations.
        self.query_condition = query_condition
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The resource group to which the SQL statements belong.
        # 
        # > You can call the [DescribeDiagnosisDimensions](~~308210~~) operation to query the resource group, database name, username, and source IP address of the SQL statements to be queried.
        self.resource_group = resource_group
        # The beginning of the time range to query. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > Only data within the last 14 days can be queried.
        self.start_time = start_time
        # The username that is used to execute the SQL statements.
        # 
        # > You can call the [DescribeDiagnosisDimensions](~~308210~~) operation to query the resource group, database name, username, and source IP address of the SQL statements to be queried.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory
        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size
        if self.min_peak_memory is not None:
            result['MinPeakMemory'] = self.min_peak_memory
        if self.min_scan_size is not None:
            result['MinScanSize'] = self.min_scan_size
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')
        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')
        if m.get('MinPeakMemory') is not None:
            self.min_peak_memory = m.get('MinPeakMemory')
        if m.get('MinScanSize') is not None:
            self.min_scan_size = m.get('MinScanSize')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DownloadDiagnosisRecordsResponseBody(TeaModel):
    def __init__(
        self,
        download_id: int = None,
        request_id: str = None,
    ):
        # The ID of the download task.
        self.download_id = download_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadDiagnosisRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadDiagnosisRecordsResponseBody = None,
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
            temp_model = DownloadDiagnosisRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAdviceServiceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of Data Warehouse Edition (V3.0) clusters.
        self.dbcluster_id = dbcluster_id
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableAdviceServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The message returned for the operation. Valid values:
        # 
        # *   **Success** is returned if the operation is successful.
        # *   An error message is returned if the operation fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableAdviceServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAdviceServiceResponseBody = None,
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
            temp_model = EnableAdviceServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantOperatorPermissionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        expired_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        privileges: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The expiration time of the service account permissions. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.expired_time = expired_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the permissions. Valid values:
        # 
        # *   **Control**: configuration permissions. The service account is granted permissions to query and modify cluster configurations.
        # *   **Data**: data permissions. The service account is granted permissions to query schemas, indexes, and SQL statements.
        self.privileges = privileges
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.privileges is not None:
            result['Privileges'] = self.privileges
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GrantOperatorPermissionResponseBody(TeaModel):
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


class GrantOperatorPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantOperatorPermissionResponseBody = None,
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
            temp_model = GrantOperatorPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillProcessRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        process_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The unique ID of the process. You can call the [DescribeProcessList](~~190092~~) operation to obtain the ID.
        self.process_id = process_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class KillProcessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify multiple tag keys. The tag key cannot be an empty string. Valid values of N: 1 to 20.
        # 
        # > You must specify at least one of the following parameters: ResourceId.N and Tag.N.Key.
        self.key = key
        # The value of the tag. You can specify multiple tag values. The tag value can be an empty string. Valid values of N: 1 to 20.
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster. You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The cluster ID. You can specify multiple cluster IDs. Valid values of N: 1 to 50.
        # 
        # > You must specify at least one of the following parameters: ResourceId.N and Tag.N.Key.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Set the value to **cluster**.
        self.resource_type = resource_type
        # The tags that are added to clusters.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The cluster ID.
        self.resource_id = resource_id
        # The type of the resource. A value of cluster indicates an AnalyticDB for MySQL cluster.
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tags that are added to clusters.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateDBClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class MigrateDBClusterResponseBody(TeaModel):
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


class MigrateDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MigrateDBClusterResponseBody = None,
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
            temp_model = MigrateDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the account. The description must meet the following requirements:
        # 
        # *   The description must start with a letter.
        # *   The description can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The description cannot start with `http://` or `https://`.
        # *   The description must be 2 to 256 characters in length.
        self.account_description = account_description
        # The name of the account.
        self.account_name = account_name
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyAuditLogConfigRequest(TeaModel):
    def __init__(
        self,
        audit_log_status: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The status of SQL audit. Valid values:
        # 
        # *   **on**: SQL audit is enabled.
        # *   **off**: SQL audit is disabled.
        self.audit_log_status = audit_log_status
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region. You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyAuditLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        update_succeed: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the status of SQL audit is updated. Valid values:
        # 
        # *   **true**: The status of SQL audit is updated.
        # *   **false**: The status of SQL audit is not updated.
        self.update_succeed = update_succeed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_succeed is not None:
            result['UpdateSucceed'] = self.update_succeed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateSucceed') is not None:
            self.update_succeed = m.get('UpdateSucceed')
        return self


class ModifyAuditLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAuditLogConfigResponseBody = None,
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
            temp_model = ModifyAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        duration: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period_unit: str = None,
        region_id: str = None,
        renewal_status: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The renewal duration. Default value: **1**.
        # 
        # *   Valid values when PeriodUnit is set to **Month**: 1 to 11. Data type: INTEGER.
        # *   Valid values when PeriodUnit is set to **Year**: 1, 2, 3, and 5. Data type: INTEGER.
        # 
        # > Longer subscription durations offer more savings. Purchasing a cluster for one year is more cost-effective than purchasing the cluster for 10 or 11 months.
        self.duration = duration
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The unit of the renewal period. Default value: **Month**. Valid values:
        # 
        # *   **Year**\
        # *   **Month**\
        self.period_unit = period_unit
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The renewal status of the cluster. Valid values:
        # 
        # *   **AutoRenewal**: The cluster is automatically renewed.
        # *   **Normal**: The cluster is manually renewed.
        # *   **NotRenewal**: The cluster is not renewed.
        self.renewal_status = renewal_status
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyAutoRenewAttributeResponseBody(TeaModel):
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


class ModifyAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAutoRenewAttributeResponseBody = None,
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
            temp_model = ModifyAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        backup_retention_period: str = None,
        dbcluster_id: str = None,
        enable_backup_log: str = None,
        log_backup_retention_period: int = None,
        owner_account: str = None,
        owner_id: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The number of days for which to retain full backup files. Valid values: 7 to 730.
        # 
        # >  If you leave this parameter empty, the default value 7 is used.
        self.backup_retention_period = backup_retention_period
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable real-time log backup. Valid values:
        # 
        # *   **Enable**\
        # 
        # *   **Disable**\
        # 
        # > If you leave this parameter empty, the default value Enable is used.
        self.enable_backup_log = enable_backup_log
        # The number of days for which to retain log backup files. Valid values: 7 to 730.
        # 
        # >  If you leave this parameter empty, the default value 7 is used.
        self.log_backup_retention_period = log_backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The days of the week on which to perform full backup. Separate multiple values with commas (,). Valid values:
        # 
        # *   **Monday**\
        # *   **Tuesday**\
        # *   **Wednesday**\
        # *   **Thursday**\
        # *   **Friday**\
        # *   **Saturday**\
        # *   **Sunday**\
        # 
        # >  To ensure data security, we recommend that you specify at least two values.
        self.preferred_backup_period = preferred_backup_period
        # The start time of the full backup within a time range. Specify the time range in the HH:mmZ-HH:mmZ format. The time must be in UTC.
        # 
        # >  The time range is 1 hour.
        self.preferred_backup_time = preferred_backup_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyClusterConnectionStringRequest(TeaModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        current_connection_string: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The prefix of public endpoints.
        # 
        # *   The prefix can contain lowercase letters, digits, and hyphens (-). It must start with a lowercase letter.
        # *   The prefix can be up to 30 characters in length.
        self.connection_string_prefix = connection_string_prefix
        # The current public endpoint of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusterNetInfo](~~143384~~) operation to query the public endpoint of the cluster.
        self.current_connection_string = current_connection_string
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port number. Set the value to **3306**.
        self.port = port
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyClusterConnectionStringResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyClusterConnectionStringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterConnectionStringResponseBody = None,
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
            temp_model = ModifyClusterConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterRequest(TeaModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_category: str = None,
        dbcluster_id: str = None,
        dbnode_class: str = None,
        dbnode_group_count: str = None,
        dbnode_storage: str = None,
        disk_performance_level: str = None,
        elastic_ioresource: int = None,
        elastic_ioresource_size: str = None,
        executor_count: str = None,
        mode: str = None,
        modify_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_resource: str = None,
    ):
        # The computing resources of the cluster. You can call the [DescribeAvailableResource](~~190632~~) operation to query the computing resources that are available within a region.
        # 
        # > This parameter must be specified when Mode is set to Flexible.
        self.compute_resource = compute_resource
        # The edition of the cluster. Valid values:
        # 
        # *   **Cluster**: reserved mode for Cluster Edition.
        # *   **MixedStorage**: elastic mode for Cluster Edition.
        # 
        # > If you set DBClusterCategory to Cluster, you must set Mode to Reserver. If you set DBClusterCategory to MixedStorage, you must set Mode to Flexible. Otherwise, you fail to change the specifications of the cluster.
        self.dbcluster_category = dbcluster_category
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The node specifications of the cluster. Valid values:
        # 
        # *   **C8**\
        # *   **C32**\
        # 
        # > This parameter must be specified when Mode is set to Reserver.
        self.dbnode_class = dbnode_class
        # The number of node groups. Valid values: 1 to 200.
        # 
        # > This parameter must be specified when Mode is set to Reserver.
        self.dbnode_group_count = dbnode_group_count
        # The storage capacity per node. Unit: GB.
        # 
        # *   Valid values when DBClusterClass is set to C8: 100 to 2000.
        # *   Valid values when DBClusterClass is set to C32: 100 to 8000.
        # 
        # > 
        # 
        # *   This parameter must be specified when Mode is set to Reserver.
        # 
        # *   The storage capacity less than 1,000 GB increases in 100 GB increments. The storage capacity greater than 1,000 GB increases in 1,000 GB increments.
        self.dbnode_storage = dbnode_storage
        # The enhanced SSD (ESSD) performance level of the cluster. Valid values:
        # 
        # *   PL0
        # *   PL1
        # *   PL2
        # *   PL3
        self.disk_performance_level = disk_performance_level
        # The number of EIUs. The number of EIUs that you can purchase varies based on the single-node EIU specifications.
        # 
        # *   If the single-node EIU specifications are 8 cores and 64 GB, you can purchase up to 32 EIUs.
        # *   If the single-node EIU specifications are 12 cores and 96 GB, you can purchase up to 16 EIUs.
        self.elastic_ioresource = elastic_ioresource
        # The single-node specifications of an elastic I/O unit (EIU). Valid values:
        # 
        # *   **8Core64GB**: If you set the parameter to **8Core64GB**, the specifications of an EIU are 24 cores and 192 GB memory.
        # *   **12Core96GB**: If you set the parameter to **12Core96GB**, the specifications of an EIU are 36 cores and 288 GB memory.
        # 
        # >  This parameter takes effect only when your cluster meets the following requirements:
        # 
        # *   The cluster is in elastic mode.
        # 
        # *   If the cluster resides in the China (Guangzhou), China (Shenzhen), China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), or China (Zhangjiakou) region, the cluster has 16 cores and 64 GB memory or higher specifications.
        # 
        # *   If the cluster resides in another region, the cluster has 32 cores and 128 GB memory or higher specifications.
        self.elastic_ioresource_size = elastic_ioresource_size
        # N/A
        self.executor_count = executor_count
        # The mode of the cluster. Valid values:
        # 
        # *   **Reserver**: the reserved mode.
        # *   **Flexible**: the elastic mode.
        self.mode = mode
        # The change type. Valid values:
        # 
        # *   **Upgrade**\
        # *   **Downgrade**\
        self.modify_type = modify_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster. You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # N/A
        self.storage_resource = storage_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.dbcluster_category is not None:
            result['DBClusterCategory'] = self.dbcluster_category
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.elastic_ioresource_size is not None:
            result['ElasticIOResourceSize'] = self.elastic_ioresource_size
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('DBClusterCategory') is not None:
            self.dbcluster_category = m.get('DBClusterCategory')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('ElasticIOResourceSize') is not None:
            self.elastic_ioresource_size = m.get('ElasticIOResourceSize')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        return self


class ModifyDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterResponseBody = None,
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
            temp_model = ModifyDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterAccessWhiteListRequest(TeaModel):
    def __init__(
        self,
        dbcluster_iparray_attribute: str = None,
        dbcluster_iparray_name: str = None,
        dbcluster_id: str = None,
        modify_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_ips: str = None,
    ):
        # The attribute of the IP address whitelist. By default, this parameter is empty. The IP address whitelists that have the **hidden** attribute are not displayed in the console. These IP address whitelists are used to access services such as Data Transmission Service (DTS) and PolarDB-X.
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        # The name of the IP address whitelist that you want to modify. Default value: **Default**. The name of an IP address whitelist must be 2 to 32 characters in length. The name can contain lowercase letters, digits, and underscores (\_). The name must start with a lowercase letter and end with a lowercase letter or digit.
        # 
        # Each cluster supports up to 50 IP address whitelists.
        self.dbcluster_iparray_name = dbcluster_iparray_name
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The method that you want to use to modify the IP address whitelist. Valid values:
        # 
        # *   Cover: overwrites the IP address whitelist.
        # *   Append: adds IP addresses to the IP address whitelist.
        # *   Delete: removes IP addresses from the IP address whitelist.
        # 
        # Default value: Cover.
        self.modify_mode = modify_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IP addresses that you want to use to modify the IP address whitelist of the cluster. Separate multiple IP addresses with commas (,). You can specify up to 500 distinct IP addresses. The following formats are supported:
        # 
        # *   IP address. Example: 10.23.12.24.
        # *   CIDR block. Example: 10.23.12.24/24. In this example, 24 indicates that the prefix of the CIDR block is 24 bits in length. You can replace 24 with a value that ranges from 1 to 32.
        # 
        # >  This parameter must be specified unless ModifyMode is set to Delete.
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class ModifyDBClusterAccessWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyDBClusterAccessWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterAccessWhiteListResponseBody = None,
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
            temp_model = ModifyDBClusterAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the cluster.
        # 
        # *   The description cannot start with `http://` or `https`.
        # *   The description must be 2 to 256 characters in length.
        self.dbcluster_description = dbcluster_description
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyDBClusterDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterDescriptionResponseBody = None,
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
            temp_model = ModifyDBClusterDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterMaintainTimeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        maintain_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the details of all AnalyticDB for MySQL clusters within a specific region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The maintenance window of the cluster. It is in the hh:mmZ-hh:mmZ format.
        # 
        # >  The maintenance window lasts only 1 hour. Specify the beginning and end of the time range on the hour.
        self.maintain_time = maintain_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterMaintainTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyDBClusterMaintainTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterMaintainTimeResponseBody = None,
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
            temp_model = ModifyDBClusterMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterPayTypeRequest(TeaModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        pay_type: str = None,
        period: str = None,
        used_time: str = None,
    ):
        # The cluster ID.
        self.db_cluster_id = db_cluster_id
        # The billing method. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type
        # The subscription type of the subscription cluster. Valid values:
        # 
        # *   **Year**: subscription on a yearly basis.
        # *   **Month**: subscription on a monthly basis.
        # 
        # > This parameter must be specified when PayType is set to Prepaid.
        self.period = period
        # The subscription duration of the subscription cluster.
        # 
        # *   Valid values when Period is set to Year: 1, 2, 3, and 5 (integer).
        # *   Valid values when Period is set to Month: 1 to 11 (integer).
        # 
        # > 
        # 
        # *   This parameter must be specified when PayType is set to Prepaid.
        # 
        # *   Longer subscription durations offer more savings. Purchasing a cluster for one year is more cost-effective than purchasing the cluster for 10 or 11 months.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class ModifyDBClusterPayTypeResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order_id: str = None,
        pay_type: str = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The order ID.
        self.order_id = order_id
        # The billing method. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterPayTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterPayTypeResponseBody = None,
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
            temp_model = ModifyDBClusterPayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        new_resource_group_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The ID of the resource group. For more information, see [View basic information of a resource group](~~151181#task-2398293~~ "This topic describes how to view basic information of a resource group, including the resource group ID, resource group name, and resource group display name.").
        self.new_resource_group_id = new_resource_group_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyDBClusterResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterResourceGroupResponseBody = None,
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
            temp_model = ModifyDBClusterResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBResourceGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        group_type: str = None,
        node_num: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        self.group_name = group_name
        # The query execution mode. Valid values:
        # 
        # *   **interactive**\
        # *   **batch**\
        # 
        # >  For more information, see [Query execution modes](~~189502~~).
        self.group_type = group_type
        # The number of nodes. Default value: 0.
        # 
        # *   Each node is configured with the resources of 16 cores and 64 GB memory.
        # *   Make sure that the amount of resources of the nodes (Number of nodes × 16 cores and 64 GB memory) is less than or equal to the amount of unused resources of the cluster.
        self.node_num = node_num
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ModifyDBResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBResourceGroupResponseBody = None,
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
            temp_model = ModifyDBResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBResourcePoolRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        node_num: int = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_name: str = None,
        query_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The number of nodes.
        # 
        # *   Each node provides 16 cores and 64 GB memory.
        # *   The amount of resources that you want to add to or remove from the cluster cannot exceed the total amount of resources in the cluster.
        # 
        # > - If you do not specify this parameter, the original value is retained.
        # > - You must specify at least one of the QueryType and NodeNum parameters.
        self.node_num = node_num
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the resource group.
        self.pool_name = pool_name
        # The mode in which SQL statements are executed. Valid values:
        # 
        # *   **batch**\
        # *   **interactive**\
        # 
        # > If you do not specify this parameter, the original value is retained.
        self.query_type = query_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBResourcePoolResponseBody(TeaModel):
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


class ModifyDBResourcePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBResourcePoolResponseBody = None,
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
            temp_model = ModifyDBResourcePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticPlanRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_plan_enable: bool = None,
        elastic_plan_end_day: str = None,
        elastic_plan_monthly_repeat: str = None,
        elastic_plan_name: str = None,
        elastic_plan_node_num: int = None,
        elastic_plan_start_day: str = None,
        elastic_plan_time_end: str = None,
        elastic_plan_time_start: str = None,
        elastic_plan_type: str = None,
        elastic_plan_weekly_repeat: str = None,
        elastic_plan_worker_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pool_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # Specifies whether the scaling plan takes effect. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.elastic_plan_enable = elastic_plan_enable
        # The end date of the scaling plan. Specify the date in the yyyy-MM-dd format.
        self.elastic_plan_end_day = elastic_plan_end_day
        self.elastic_plan_monthly_repeat = elastic_plan_monthly_repeat
        # The name of the scaling plan.
        # 
        # *   The name must be 2 to 30 characters in length.
        # *   The name can contain letters, digits, and underscores (\_).
        # 
        # > You can call the [DescribeElasticPlan](~~190596~~) operation to query the information about all scaling plans of a cluster, including the scaling plan names.
        self.elastic_plan_name = elastic_plan_name
        # The number of nodes that are involved in the scaling plan.
        # 
        # *   If ElasticPlanType is set to **worker**, you can set this parameter to 0 or leave this parameter empty.
        # *   If ElasticPlanType is set to **executorcombineworker** or **executor**, you must set this parameter to a value that is greater than 0.
        self.elastic_plan_node_num = elastic_plan_node_num
        # The start date of the scaling plan. Specify the date in the yyyy-MM-dd format.
        self.elastic_plan_start_day = elastic_plan_start_day
        # The restoration time of the scaling plan. Specify the time on the hour in the HH:mm:ss format. The interval between the scale-up time and the restoration time cannot be more than 24 hours.
        self.elastic_plan_time_end = elastic_plan_time_end
        # The scale-up time of the scaling plan. Specify the time on the hour in the HH:mm:ss format.
        self.elastic_plan_time_start = elastic_plan_time_start
        # The type of the scaling plan. Valid values:
        # 
        # *   **worker**: scales only elastic I/O resources.
        # *   **executor**: scales only computing resources.
        # *   **executorcombineworker** (default): scales both elastic I/O resources and computing resources by proportion.
        # 
        # > 
        # 
        # *   If you want to set this parameter to **executorcombineworker**, make sure that the cluster runs a minor version of 3.1.3.2 or later.
        # 
        # *   If you want to set this parameter to **worker** or **executor**, make sure that the cluster runs a minor version of 3.1.6.1 or later and a ticket is submitted. After your request is approved, you can set this parameter to **worker** or **executor**.
        self.elastic_plan_type = elastic_plan_type
        # The days of the week when you want to execute the scaling plan. Valid values: 0 to 6, which indicate Sunday to Saturday. Separate multiple values with commas (,).
        self.elastic_plan_weekly_repeat = elastic_plan_weekly_repeat
        # The resource specifications that can be scaled up by the scaling plan. Valid values:
        # 
        # *   8 Core 64 GB (default)
        # *   16 Core 64 GB
        # *   32 Core 64 GB
        # *   64 Core 128 GB
        # *   12 Core 96 GB
        # *   24 Core 96 GB
        # *   52 Core 86 GB
        self.elastic_plan_worker_spec = elastic_plan_worker_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the resource group.
        # 
        # > You can call the [DescribeDBResourceGroup](~~466685~~) operation to query the resource group name.
        self.resource_pool_name = resource_pool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_enable is not None:
            result['ElasticPlanEnable'] = self.elastic_plan_enable
        if self.elastic_plan_end_day is not None:
            result['ElasticPlanEndDay'] = self.elastic_plan_end_day
        if self.elastic_plan_monthly_repeat is not None:
            result['ElasticPlanMonthlyRepeat'] = self.elastic_plan_monthly_repeat
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.elastic_plan_node_num is not None:
            result['ElasticPlanNodeNum'] = self.elastic_plan_node_num
        if self.elastic_plan_start_day is not None:
            result['ElasticPlanStartDay'] = self.elastic_plan_start_day
        if self.elastic_plan_time_end is not None:
            result['ElasticPlanTimeEnd'] = self.elastic_plan_time_end
        if self.elastic_plan_time_start is not None:
            result['ElasticPlanTimeStart'] = self.elastic_plan_time_start
        if self.elastic_plan_type is not None:
            result['ElasticPlanType'] = self.elastic_plan_type
        if self.elastic_plan_weekly_repeat is not None:
            result['ElasticPlanWeeklyRepeat'] = self.elastic_plan_weekly_repeat
        if self.elastic_plan_worker_spec is not None:
            result['ElasticPlanWorkerSpec'] = self.elastic_plan_worker_spec
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanEnable') is not None:
            self.elastic_plan_enable = m.get('ElasticPlanEnable')
        if m.get('ElasticPlanEndDay') is not None:
            self.elastic_plan_end_day = m.get('ElasticPlanEndDay')
        if m.get('ElasticPlanMonthlyRepeat') is not None:
            self.elastic_plan_monthly_repeat = m.get('ElasticPlanMonthlyRepeat')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('ElasticPlanNodeNum') is not None:
            self.elastic_plan_node_num = m.get('ElasticPlanNodeNum')
        if m.get('ElasticPlanStartDay') is not None:
            self.elastic_plan_start_day = m.get('ElasticPlanStartDay')
        if m.get('ElasticPlanTimeEnd') is not None:
            self.elastic_plan_time_end = m.get('ElasticPlanTimeEnd')
        if m.get('ElasticPlanTimeStart') is not None:
            self.elastic_plan_time_start = m.get('ElasticPlanTimeStart')
        if m.get('ElasticPlanType') is not None:
            self.elastic_plan_type = m.get('ElasticPlanType')
        if m.get('ElasticPlanWeeklyRepeat') is not None:
            self.elastic_plan_weekly_repeat = m.get('ElasticPlanWeeklyRepeat')
        if m.get('ElasticPlanWorkerSpec') is not None:
            self.elastic_plan_worker_spec = m.get('ElasticPlanWorkerSpec')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        return self


class ModifyElasticPlanResponseBody(TeaModel):
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


class ModifyElasticPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyElasticPlanResponseBody = None,
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
            temp_model = ModifyElasticPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        enable_backup_log: str = None,
        log_backup_retention_period: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable log backup. Valid values:
        # 
        # *   **Enable**\
        # *   **Disable**\
        self.enable_backup_log = enable_backup_log
        # The number of days for which to retain backup files. Valid values: 7 to 730.
        # 
        # > The default value is 7.
        self.log_backup_retention_period = log_backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyLogBackupPolicyResponseBody(TeaModel):
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


class ModifyLogBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLogBackupPolicyResponseBody = None,
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
            temp_model = ModifyLogBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMaintenanceActionRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
    ):
        # The ID of the pending O\&M event. You can specify multiple IDs to batch change the switchover time. Separate multiple IDs with commas (,).
        # > - You can call the [DescribeMaintenanceAction](~~271738~~) operation to query the information about pending O\&M events, including the event ID.
        # > - You can change the switchover time only for pending O\&M events. The switchover time of historical O\&M events cannot be changed. For more information about the status of pending and historical O\&M events, see [DescribeMaintenanceAction](~~271738~~).
        self.ids = ids
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the pending O\&M event occurs.
        # 
        # > - You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time when you want the system to perform operations on the pending O\&M event. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.switch_time = switch_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class ModifyMaintenanceActionResponseBody(TeaModel):
    def __init__(
        self,
        ids: str = None,
        request_id: str = None,
    ):
        # The O\&M event ID.
        self.ids = ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyMaintenanceActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMaintenanceActionResponseBody = None,
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
            temp_model = ModifyMaintenanceActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyResubmitConfigRequestRules(TeaModel):
    def __init__(
        self,
        exceed_memory_exception: bool = None,
        group_name: str = None,
        peak_memory: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        # Specifies whether to configure out-of-memory (OOM) check.
        self.exceed_memory_exception = exceed_memory_exception
        # The name of the source resource group.
        self.group_name = group_name
        # The peak memory usage.
        self.peak_memory = peak_memory
        # The duration of the SQL statement. Unit: milliseconds.
        self.query_time = query_time
        # The name of the destination resource group.
        self.target_group_name = target_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exceed_memory_exception is not None:
            result['ExceedMemoryException'] = self.exceed_memory_exception
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.target_group_name is not None:
            result['TargetGroupName'] = self.target_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceedMemoryException') is not None:
            self.exceed_memory_exception = m.get('ExceedMemoryException')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('TargetGroupName') is not None:
            self.target_group_name = m.get('TargetGroupName')
        return self


class ModifyResubmitConfigRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rules: List[ModifyResubmitConfigRequestRules] = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The job resubmission rules.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ModifyResubmitConfigRequestRules()
                self.rules.append(temp_model.from_map(k))
        return self


class ModifyResubmitConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rules_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The job resubmission rules.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')
        return self


class ModifyResubmitConfigResponseBody(TeaModel):
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


class ModifyResubmitConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyResubmitConfigResponseBody = None,
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
            temp_model = ModifyResubmitConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySQAConfigRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sqastatus: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        # 
        # >  You can call the [DescribeDBResourceGroup](~~459446~~) operation to query the resource group name of a cluster.
        self.group_name = group_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable short query acceleration (SQA).
        # 
        # Valid values:
        # 
        # *   on
        # *   off
        self.sqastatus = sqastatus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sqastatus is not None:
            result['SQAStatus'] = self.sqastatus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SQAStatus') is not None:
            self.sqastatus = m.get('SQAStatus')
        return self


class ModifySQAConfigResponseBody(TeaModel):
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


class ModifySQAConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySQAConfigResponseBody = None,
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
            temp_model = ModifySQAConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterPublicConnectionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReleaseClusterPublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class ReleaseClusterPublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseClusterPublicConnectionResponseBody = None,
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
            temp_model = ReleaseClusterPublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        account_type: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The account of the database.
        self.account_name = account_name
        # The account and password of the database.
        # 
        # *   The password must contain uppercase letters, lowercase letters, digits, and special characters.
        # *   Special characters include ! @ # $ % ^ & \* () \_ + - and =\
        # *   A password must be 8 to 32 characters in length.
        self.account_password = account_password
        # Normal: standard account
        # 
        # Super: privileged account
        self.account_type = account_type
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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


class RevokeOperatorPermissionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RevokeOperatorPermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class RevokeOperatorPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeOperatorPermissionResponseBody = None,
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
            temp_model = RevokeOperatorPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. If you want to add multiple tags to a single cluster at a time, click **Add** and enter tag keys and values.
        # 
        # > You can add up to 20 tags at a time.
        self.key = key
        # The value of the tag. If you want to add multiple tags to a single cluster at a time, click **Add** and enter tag keys and values.
        # 
        # > You can add up to 20 tags at a time.
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster. You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the cluster to which to add a tag. If you want to add a tag to multiple clusters, click **Add** and enter the cluster IDs.
        # 
        # > 
        # 
        # *   You can add tags to up to 50 clusters at a time.
        # 
        # *   You can call the [DescribeDBClusters](~~129857~~) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the cluster. Set the value to **ALIYUN::ADB::CLUSTER**.
        self.resource_type = resource_type
        # The tags to add to the cluster.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDBResourceGroupWithUserRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        group_user: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](~~129857~~) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        self.group_name = group_name
        # The database account with which the resource group is associated.
        self.group_user = group_user
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_user is not None:
            result['GroupUser'] = self.group_user
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupUser') is not None:
            self.group_user = m.get('GroupUser')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UnbindDBResourceGroupWithUserResponseBody(TeaModel):
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


class UnbindDBResourceGroupWithUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindDBResourceGroupWithUserResponseBody = None,
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
            temp_model = UnbindDBResourceGroupWithUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDBResourcePoolWithUserRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_name: str = None,
        pool_user: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the resource pool. You cannot unbind users from the default resource pool named USER_DEFAULT.
        self.pool_name = pool_name
        # The user bound to the resource pool.
        self.pool_user = pool_user
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.pool_user is not None:
            result['PoolUser'] = self.pool_user
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('PoolUser') is not None:
            self.pool_user = m.get('PoolUser')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UnbindDBResourcePoolWithUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class UnbindDBResourcePoolWithUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindDBResourcePoolWithUserResponseBody = None,
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
            temp_model = UnbindDBResourcePoolWithUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from clusters. Default value: false. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If you specify TagKey and this parameter, this parameter does not take effect.
        self.all = all
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](~~143074~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of cluster N. Valid values of N: 1 to 50.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Set the value to **ALIYUN::ADB::CLUSTER**.
        self.resource_type = resource_type
        # The key of tag N. Valid values of N: 1 to 20.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


