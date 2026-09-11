# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class ConfigureSubscriptionInstanceRequest(DaraModel):
    def __init__(
        self,
        source_endpoint: main_models.ConfigureSubscriptionInstanceRequestSourceEndpoint = None,
        subscription_data_type: main_models.ConfigureSubscriptionInstanceRequestSubscriptionDataType = None,
        subscription_instance: main_models.ConfigureSubscriptionInstanceRequestSubscriptionInstance = None,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_instance_network_type: str = None,
        subscription_object: str = None,
    ):
        self.source_endpoint = source_endpoint
        self.subscription_data_type = subscription_data_type
        self.subscription_instance = subscription_instance
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because it will be deprecated.
        self.account_id = account_id
        self.owner_id = owner_id
        # The ID of the region where the change tracking instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the change tracking instance. You can call the [DescribeSubscriptionInstances](https://help.aliyun.com/document_detail/49442.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.subscription_instance_id = subscription_instance_id
        # The name of the change tracking instance.
        # > Specify a descriptive name for easy identification. The name does not need to be unique.
        self.subscription_instance_name = subscription_instance_name
        # The network type of the change tracking instance. The only valid value is **vpc**, which indicates a virtual private cloud (VPC).
        # 
        # > - If you specify this parameter, the change tracking instance is defined as the new version. You must also correctly set the **SubscriptionInstance.VPCId** and **SubscriptionInstance.VSwitchID** parameters. If you do not specify this parameter, the change tracking instance is defined as the legacy version.
        # > - The legacy version supports change tracking for self-managed MySQL, ApsaraDB RDS for MySQL, and DRDS. The new version supports change tracking for self-managed MySQL, ApsaraDB RDS for MySQL, PolarDB for MySQL, and Oracle.
        self.subscription_instance_network_type = subscription_instance_network_type
        # The objects to be subscribed to. The value is a JSON string that supports regular expressions. For more information, see [Subscription object configuration](https://help.aliyun.com/document_detail/141902.html).
        # 
        # This parameter is required.
        self.subscription_object = subscription_object

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_instance:
            self.subscription_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()

        if self.subscription_instance is not None:
            result['SubscriptionInstance'] = self.subscription_instance.to_map()

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id

        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name

        if self.subscription_instance_network_type is not None:
            result['SubscriptionInstanceNetworkType'] = self.subscription_instance_network_type

        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.ConfigureSubscriptionInstanceRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('SubscriptionDataType') is not None:
            temp_model = main_models.ConfigureSubscriptionInstanceRequestSubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m.get('SubscriptionDataType'))

        if m.get('SubscriptionInstance') is not None:
            temp_model = main_models.ConfigureSubscriptionInstanceRequestSubscriptionInstance()
            self.subscription_instance = temp_model.from_map(m.get('SubscriptionInstance'))

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')

        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')

        if m.get('SubscriptionInstanceNetworkType') is not None:
            self.subscription_instance_network_type = m.get('SubscriptionInstanceNetworkType')

        if m.get('SubscriptionObject') is not None:
            self.subscription_object = m.get('SubscriptionObject')

        return self

class ConfigureSubscriptionInstanceRequestSubscriptionInstance(DaraModel):
    def __init__(
        self,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # 订阅实例的专有网络ID。
        # > 当**SubscriptionInstanceNetworkType**取值为**vpc**时，本参数才可用且必须传入。
        self.vpcid = vpcid
        # 订阅实例的虚拟交换机ID。
        # > 当**SubscriptionInstanceNetworkType**取值为**vpc**时，本参数才可用且必须传入。
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class ConfigureSubscriptionInstanceRequestSubscriptionDataType(DaraModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        # 是否订阅DDL类型的数据，取值：
        # 
        # - **true**：是，为默认值。
        # - **false**：否。
        # 
        # This parameter is required.
        self.ddl = ddl
        # 是否订阅DML类型的数据，取值：
        # - **true**：是，为默认值。
        # - **false**：否。
        # 
        # This parameter is required.
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddl is not None:
            result['DDL'] = self.ddl

        if self.dml is not None:
            result['DML'] = self.dml

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')

        if m.get('DML') is not None:
            self.dml = m.get('DML')

        return self

class ConfigureSubscriptionInstanceRequestSourceEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        owner_id: str = None,
        password: str = None,
        port: str = None,
        role: str = None,
        user_name: str = None,
    ):
        # 待订阅的数据库名称。
        self.database_name = database_name
        # 源数据库的连接地址。
        # > 当源数据库为自建数据库时，本参数才可用且必须传入。
        self.ip = ip
        # 源实例ID。
        # > 源数据库的实例类型为RDS MySQL、PolarDB-X 1.0、PolarDB MySQL时，本参数才可用且必须传入。
        self.instance_id = instance_id
        # 源数据库的实例类型，取值：
        # - **RDS**：RDS MySQL。
        # - **PolarDB**：PolarDB MySQL。
        # - **LocalInstance**：有公网IP的自建数据库。
        # - **ECS**：ECS上的自建数据库。
        # - **Express**：通过专线接入的自建数据库。
        # - **CEN**：通过云企业网CEN接入的自建数据库。
        # - **dg**：通过数据库网关接入的自建数据库。
        # 
        # > 支持自建数据库的数据库类型为MySQL、Oracle，您需要提前调用[CreateSubscriptionInstance](https://help.aliyun.com/document_detail/49436.html)设置。
        self.instance_type = instance_type
        # Oracle数据库的SID信息。
        # > 当源数据库为自建Oracle时，且Oracle数据库为非RAC实例时，本参数才可用且必须传入。
        self.oracle_sid = oracle_sid
        # 源实例所属的阿里云账号ID。
        # > 仅在配置跨阿里云账号的数据订阅时本参数才可用，且必须传入。
        self.owner_id = owner_id
        # 源实例的数据库账号密码。
        self.password = password
        # 源数据库的服务端口。
        # > 当源数据库为自建数据库时，本参数才可用且必须传入。
        self.port = port
        # 源实例的授权角色。当源实例与配置订阅任务所属阿里云账号不同时，需传入该参数，来指定源实例的授权角色，以允许配置订阅任务所属阿里云账号访问源实例的实例信息。
        # > 角色所需的权限及授权方式，请参见[跨阿里云账号数据迁移或同步时如何配置RAM授权](https://help.aliyun.com/document_detail/48468.html)。
        self.role = role
        # 源实例的数据库账号。
        # > 订阅不同的数据库所需的权限有所差异，详情请参见[DTS数据订阅方案概览](https://help.aliyun.com/document_detail/145715.html)中对应的配置案例。
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.ip is not None:
            result['IP'] = self.ip

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.role is not None:
            result['Role'] = self.role

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

