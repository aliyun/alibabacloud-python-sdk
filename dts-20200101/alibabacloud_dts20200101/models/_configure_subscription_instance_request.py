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
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because it will be deprecated soon.
        self.account_id = account_id
        self.owner_id = owner_id
        # The ID of the region where the change tracking instance resides. For more information, see
        # [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the change tracking instance. You can call the [DescribeSubscriptionInstances](https://help.aliyun.com/document_detail/49442.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.subscription_instance_id = subscription_instance_id
        # The name of the change tracking instance.
        # > Specify a descriptive name for easy identification. The name does not need to be unique.
        self.subscription_instance_name = subscription_instance_name
        # The network type of the change tracking instance. Set the value to **vpc**, which specifies a virtual private cloud (VPC).
        # 
        # > - If you specify this parameter, the change tracking instance is defined as a new version instance, and you must also correctly set the **SubscriptionInstance.VPCId** and **SubscriptionInstance.VSwitchID** parameters. If you do not specify this parameter, the change tracking instance is defined as a legacy instance.
        # - Legacy change tracking instances support tracking data from self-managed MySQL databases, ApsaraDB RDS for MySQL instances, and DRDS instances. New version change tracking instances support tracking data from self-managed MySQL databases, ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and Oracle databases.
        self.subscription_instance_network_type = subscription_instance_network_type
        # The objects to be tracked. The value is a JSON string and supports specific regular expressions. For more information, see [Configure the objects to be tracked](https://help.aliyun.com/document_detail/141902.html).
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
        # The VPC ID of the change tracking instance.
        # > This parameter is available and required only when **SubscriptionInstanceNetworkType** is set to **vpc**.
        self.vpcid = vpcid
        # The vSwitch ID of the change tracking instance.
        # > This parameter is available and required only when **SubscriptionInstanceNetworkType** is set to **vpc**.
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
        # Specifies whether to track data definition language (DDL) operations. Valid values:
        # 
        # - **true**: yes. This is the default value.
        # - **false**: no.
        # 
        # This parameter is required.
        self.ddl = ddl
        # Specifies whether to track data manipulation language (DML) operations. Valid values:
        # - **true**: yes. This is the default value.
        # - **false**: no.
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
        # The name of the database to be tracked.
        self.database_name = database_name
        # The endpoint of the source database.
        # > This parameter is available and required only when the source database is a self-managed database.
        self.ip = ip
        # The instance ID of the source instance.
        # > This parameter is available and required only when the source database is an ApsaraDB RDS for MySQL instance, a PolarDB-X 1.0 instance, or a PolarDB for MySQL cluster.
        self.instance_id = instance_id
        # The instance type of the source database. Valid values:
        # - **RDS**: ApsaraDB RDS for MySQL.
        # - **PolarDB**: PolarDB for MySQL.
        # - **LocalInstance**: a self-managed database with a public IP address.
        # - **ECS**: a self-managed database hosted on an ECS instance.
        # - **Express**: a self-managed database connected over an Express Connect circuit.
        # - **CEN**: a self-managed database connected over a Cloud Enterprise Network (CEN) instance.
        # - **dg**: a self-managed database connected over a database gateway.
        # 
        # > Self-managed MySQL and Oracle databases are supported. You must call the [CreateSubscriptionInstance](https://help.aliyun.com/document_detail/49436.html) operation to configure the database type in advance.
        self.instance_type = instance_type
        # The system ID (SID) of the Oracle database.
        # > This parameter is available and required only when the source database is a self-managed Oracle database and the Oracle database is not a Real Application Clusters (RAC) instance.
        self.oracle_sid = oracle_sid
        # The Alibaba Cloud account ID of the source instance.
        # > This parameter is available and required only when you configure change tracking across Alibaba Cloud accounts.
        self.owner_id = owner_id
        # The password of the database account of the source instance.
        self.password = password
        # The service port number of the source database.
        # > This parameter is available and required only when the source database is a self-managed database.
        self.port = port
        # The RAM role that is authorized to access the source instance. If the source instance and the change tracking task belong to different Alibaba Cloud accounts, you must specify this parameter to authorize the Alibaba Cloud account that owns the change tracking task to access the source instance.
        # > For more information about the required permissions and authorization methods for the RAM role, see [Configure RAM authorization for cross-account data migration or synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.role = role
        # The database account of the source instance.
        # > The required permissions vary based on the database to be tracked. For more information, see the corresponding configuration examples in [Overview of DTS change tracking solutions](https://help.aliyun.com/document_detail/145715.html).
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

