# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance: main_models.DescribeDBInstanceAttributeResponseBodyDBInstance = None,
        request_id: str = None,
    ):
        # The database instance information.
        self.dbinstance = dbinstance
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbinstance:
            self.dbinstance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstance') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstance()
            self.dbinstance = temp_model.from_map(m.get('DBInstance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstance(DaraModel):
    def __init__(
        self,
        ai_gateway_enabled: str = None,
        can_not_create_columnar: bool = None,
        cn_node_class_code: str = None,
        cn_node_count: int = None,
        columnar_instance_name: str = None,
        columnar_read_dbinstances: List[str] = None,
        commodity_code: str = None,
        conn_addrs: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs] = None,
        connection_string: str = None,
        cpu_type: str = None,
        create_time: str = None,
        dbinstance_type: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnodes: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes] = None,
        dbtype: str = None,
        dbversion: str = None,
        description: str = None,
        different_dnspec: bool = None,
        dn_node_class_code: str = None,
        dn_node_count: int = None,
        dn_storage_space: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_date: str = None,
        expired: str = None,
        gdn_instance_name: str = None,
        gdn_member_list: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstanceGdnMemberList] = None,
        gdn_role: str = None,
        id: str = None,
        kind_code: int = None,
        ltsversions: List[str] = None,
        latest_minor_version: str = None,
        lock_mode: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        minor_version: str = None,
        network: str = None,
        pay_type: str = None,
        port: str = None,
        primary_instance_id: str = None,
        primary_zone: str = None,
        read_dbinstances: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        rights_separation_enabled: bool = None,
        rights_separation_status: str = None,
        secondary_zone: str = None,
        series: str = None,
        spec_category: str = None,
        status: str = None,
        storage_type: str = None,
        storage_used: int = None,
        tag_set: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstanceTagSet] = None,
        tertiary_zone: str = None,
        topology_type: str = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.ai_gateway_enabled = ai_gateway_enabled
        # Indicates whether the In-Memory Column Index feature is supported.
        self.can_not_create_columnar = can_not_create_columnar
        # The CN node specifications. Valid values:
        # - **polarx.x4.medium.2e**: 2 cores, 8 GB
        # - **polarx.x4.large.2e**: 4 cores, 16 GB
        # - **polarx.x8.large.2e**: 4 cores, 32 GB
        # - **polarx.x4.xlarge.2e**: 8 cores, 32 GB
        # - **polarx.x8.xlarge.2e**: 8 cores, 64 GB
        # - **polarx.x4.2xlarge.2e**: 16 cores, 64 GB
        # - **polarx.x8.2xlarge.2e**: 16 cores, 128 GB
        # - **polarx.x4.4xlarge.2e**: 32 cores, 128 GB
        # - **polarx.x8.4xlarge.2e**: 32 cores, 256 GB
        # - **polarx.st.8xlarge.2e**: 60 cores, 470 GB
        # - **polarx.st.12xlarge.2e**: 90 cores, 720 GB.
        self.cn_node_class_code = cn_node_class_code
        # The number of CN nodes.
        self.cn_node_count = cn_node_count
        # The name of the column store engine instance.
        self.columnar_instance_name = columnar_instance_name
        # The column store read-only instance information.
        self.columnar_read_dbinstances = columnar_read_dbinstances
        # The commodity code of the instance. The value is fixed as drds_polarxpost_public_cn.
        self.commodity_code = commodity_code
        # The endpoint information.
        self.conn_addrs = conn_addrs
        # The internal network connection string.
        self.connection_string = connection_string
        self.cpu_type = cpu_type
        # The creation time.
        self.create_time = create_time
        # The instance type. Valid values:
        # 
        # - **ReadWrite**: primary instance.
        # - **ReadOnly**: read-only instance.
        self.dbinstance_type = dbinstance_type
        # The node specifications of the instance.
        self.dbnode_class = dbnode_class
        # The number of instance nodes.
        self.dbnode_count = dbnode_count
        # The database node information.
        self.dbnodes = dbnodes
        # The database type. The value is fixed as polarx.
        self.dbtype = dbtype
        # The database version.
        self.dbversion = dbversion
        # The instance description.
        self.description = description
        # Indicates whether the DN nodes of the instance have different specifications. Valid values:
        # 
        # - true: The specifications are different.
        # - false: The specifications are the same.
        self.different_dnspec = different_dnspec
        # The DN node specifications. Valid values:
        # - **mysql.n2.medium.25**: 2 cores, 4 GB
        # - **mysql.n4.medium.25**: 2 cores, 8 GB
        # - **mysql.x8.medium.25**: 2 cores, 16 GB
        # - **mysql.n2.large.25**: 4 cores, 8 GB
        # - **mysql.n4.large.25**: 4 cores, 16 GB
        # - **mysql.x8.large.25**: 4 cores, 32 GB
        # - **mysql.n2.xlarge.25**: 8 cores, 16 GB
        # - **mysql.n4.xlarge.25**: 8 cores, 32 GB
        # - **mysql.x8.xlarge.25**: 8 cores, 64 GB
        # - **mysql.n4.2xlarge.25**: 16 cores, 64 GB
        # - **mysql.x8.2xlarge.25**: 16 cores, 128 GB
        # - **mysql.x4.4xlarge.25**: 32 cores, 128 GB
        # - **mysql.x8.4xlarge.25**: 32 cores, 256 GB
        # - **mysql.st.8xlarge.25**: 60 cores, 470 GB
        # - **mysql.st.12xlarge.25**: 90 cores, 720 GB.
        self.dn_node_class_code = dn_node_class_code
        # The number of DN nodes.
        self.dn_node_count = dn_node_count
        # The disk space of the DN data node, in GB.
        self.dn_storage_space = dn_storage_space
        # The database type. The value is fixed as polarx.
        self.engine = engine
        self.engine_version = engine_version
        # The expiration time. Format: yyyy-MM-ddTHH:mm:ss.sss+0000 (UTC).
        self.expire_date = expire_date
        # Indicates whether the instance has expired. Valid values:
        # 
        # - **true**: Expired.
        # - **false**: Not expired.
        self.expired = expired
        self.gdn_instance_name = gdn_instance_name
        self.gdn_member_list = gdn_member_list
        self.gdn_role = gdn_role
        # The ID of the primary instance. If this parameter is not returned, the instance is a primary instance.
        self.id = id
        # The engine version of the instance. This is an internal parameter.
        self.kind_code = kind_code
        # This parameter is required.
        self.ltsversions = ltsversions
        # The latest minor engine version supported by the instance.
        self.latest_minor_version = latest_minor_version
        # The lock mode of the instance. Valid values:
        # 
        # - **Unlock**: Normal.
        # - **ManualLock**: Manually locked.
        # - **LockByExpiration**: Automatically locked due to instance expiration.
        # - **LockByRestoration**: Automatically locked before instance rollback.
        # - **LockByDiskQuota**: Automatically locked due to insufficient disk space.
        # - **LockReadInstanceByDiskQuota**: Read-only instance automatically locked due to insufficient disk space.
        self.lock_mode = lock_mode
        # The end time of the maintenance window. The time is in UTC. Add 8 hours to obtain the maintenance window displayed in the console.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window. The time is in UTC. Add 8 hours to obtain the maintenance window displayed in the console.
        self.maintain_start_time = maintain_start_time
        # The current minor engine version.
        self.minor_version = minor_version
        # The network type of the instance. Only VPC is supported, which indicates Virtual Private Cloud.
        self.network = network
        # The billing method of the instance. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        self.pay_type = pay_type
        # The internal network connection port.
        self.port = port
        self.primary_instance_id = primary_instance_id
        # The primary zone.
        # 
        # This parameter is required.
        self.primary_zone = primary_zone
        # The list of read-only instance names.
        self.read_dbinstances = read_dbinstances
        # The region in which the instance resides.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The three-role mode status. Valid values:
        # 
        # - **false**: Disabled.
        # - **true**: Enabled.
        self.rights_separation_enabled = rights_separation_enabled
        # The three-role mode status. Valid values:
        # 
        # - **disabled**: Disabled.
        # - **enabled**: Enabled.
        # - **processing**: Being processed.
        # - **unknown**: Unknown. This may be caused by the instance being unreachable.
        self.rights_separation_status = rights_separation_status
        # The secondary zone.
        self.secondary_zone = secondary_zone
        # The instance edition. Valid values:
        # 
        # - **enterprise**: Enterprise Edition.
        # - **standard**: Standard Edition.
        self.series = series
        self.spec_category = spec_category
        # The instance status. For more information, see [Instance status table](https://help.aliyun.com/document_detail/339826.html).
        self.status = status
        self.storage_type = storage_type
        # The used storage space, in bytes.
        self.storage_used = storage_used
        # The tag set.
        self.tag_set = tag_set
        # The tertiary zone for Three-zone deployment.
        self.tertiary_zone = tertiary_zone
        # The topology type. Valid values:
        # 
        # - **3azones**: three-zone deployment.
        # - **1azone**: single-zone deployment.
        # 
        # This parameter is required.
        self.topology_type = topology_type
        # The instance type. Valid values:
        # 
        # - **ReadWrite**: primary instance.
        # - **ReadOnly**: read-only instance.
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone in which the instance resides.
        self.zone_id = zone_id

    def validate(self):
        if self.conn_addrs:
            for v1 in self.conn_addrs:
                 if v1:
                    v1.validate()
        if self.dbnodes:
            for v1 in self.dbnodes:
                 if v1:
                    v1.validate()
        if self.gdn_member_list:
            for v1 in self.gdn_member_list:
                 if v1:
                    v1.validate()
        if self.tag_set:
            for v1 in self.tag_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_gateway_enabled is not None:
            result['AiGatewayEnabled'] = self.ai_gateway_enabled

        if self.can_not_create_columnar is not None:
            result['CanNotCreateColumnar'] = self.can_not_create_columnar

        if self.cn_node_class_code is not None:
            result['CnNodeClassCode'] = self.cn_node_class_code

        if self.cn_node_count is not None:
            result['CnNodeCount'] = self.cn_node_count

        if self.columnar_instance_name is not None:
            result['ColumnarInstanceName'] = self.columnar_instance_name

        if self.columnar_read_dbinstances is not None:
            result['ColumnarReadDBInstances'] = self.columnar_read_dbinstances

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k1 in self.conn_addrs:
                result['ConnAddrs'].append(k1.to_map() if k1 else None)

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.cpu_type is not None:
            result['CpuType'] = self.cpu_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count

        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k1 in self.dbnodes:
                result['DBNodes'].append(k1.to_map() if k1 else None)

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.description is not None:
            result['Description'] = self.description

        if self.different_dnspec is not None:
            result['DifferentDNSpec'] = self.different_dnspec

        if self.dn_node_class_code is not None:
            result['DnNodeClassCode'] = self.dn_node_class_code

        if self.dn_node_count is not None:
            result['DnNodeCount'] = self.dn_node_count

        if self.dn_storage_space is not None:
            result['DnStorageSpace'] = self.dn_storage_space

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.gdn_instance_name is not None:
            result['GdnInstanceName'] = self.gdn_instance_name

        result['GdnMemberList'] = []
        if self.gdn_member_list is not None:
            for k1 in self.gdn_member_list:
                result['GdnMemberList'].append(k1.to_map() if k1 else None)

        if self.gdn_role is not None:
            result['GdnRole'] = self.gdn_role

        if self.id is not None:
            result['Id'] = self.id

        if self.kind_code is not None:
            result['KindCode'] = self.kind_code

        if self.ltsversions is not None:
            result['LTSVersions'] = self.ltsversions

        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.network is not None:
            result['Network'] = self.network

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.primary_instance_id is not None:
            result['PrimaryInstanceId'] = self.primary_instance_id

        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone

        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rights_separation_enabled is not None:
            result['RightsSeparationEnabled'] = self.rights_separation_enabled

        if self.rights_separation_status is not None:
            result['RightsSeparationStatus'] = self.rights_separation_status

        if self.secondary_zone is not None:
            result['SecondaryZone'] = self.secondary_zone

        if self.series is not None:
            result['Series'] = self.series

        if self.spec_category is not None:
            result['SpecCategory'] = self.spec_category

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        result['TagSet'] = []
        if self.tag_set is not None:
            for k1 in self.tag_set:
                result['TagSet'].append(k1.to_map() if k1 else None)

        if self.tertiary_zone is not None:
            result['TertiaryZone'] = self.tertiary_zone

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        if self.type is not None:
            result['Type'] = self.type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiGatewayEnabled') is not None:
            self.ai_gateway_enabled = m.get('AiGatewayEnabled')

        if m.get('CanNotCreateColumnar') is not None:
            self.can_not_create_columnar = m.get('CanNotCreateColumnar')

        if m.get('CnNodeClassCode') is not None:
            self.cn_node_class_code = m.get('CnNodeClassCode')

        if m.get('CnNodeCount') is not None:
            self.cn_node_count = m.get('CnNodeCount')

        if m.get('ColumnarInstanceName') is not None:
            self.columnar_instance_name = m.get('ColumnarInstanceName')

        if m.get('ColumnarReadDBInstances') is not None:
            self.columnar_read_dbinstances = m.get('ColumnarReadDBInstances')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k1 in m.get('ConnAddrs'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k1))

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CpuType') is not None:
            self.cpu_type = m.get('CpuType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')

        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k1 in m.get('DBNodes'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes()
                self.dbnodes.append(temp_model.from_map(k1))

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DifferentDNSpec') is not None:
            self.different_dnspec = m.get('DifferentDNSpec')

        if m.get('DnNodeClassCode') is not None:
            self.dn_node_class_code = m.get('DnNodeClassCode')

        if m.get('DnNodeCount') is not None:
            self.dn_node_count = m.get('DnNodeCount')

        if m.get('DnStorageSpace') is not None:
            self.dn_storage_space = m.get('DnStorageSpace')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('GdnInstanceName') is not None:
            self.gdn_instance_name = m.get('GdnInstanceName')

        self.gdn_member_list = []
        if m.get('GdnMemberList') is not None:
            for k1 in m.get('GdnMemberList'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstanceGdnMemberList()
                self.gdn_member_list.append(temp_model.from_map(k1))

        if m.get('GdnRole') is not None:
            self.gdn_role = m.get('GdnRole')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')

        if m.get('LTSVersions') is not None:
            self.ltsversions = m.get('LTSVersions')

        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrimaryInstanceId') is not None:
            self.primary_instance_id = m.get('PrimaryInstanceId')

        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')

        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RightsSeparationEnabled') is not None:
            self.rights_separation_enabled = m.get('RightsSeparationEnabled')

        if m.get('RightsSeparationStatus') is not None:
            self.rights_separation_status = m.get('RightsSeparationStatus')

        if m.get('SecondaryZone') is not None:
            self.secondary_zone = m.get('SecondaryZone')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        if m.get('SpecCategory') is not None:
            self.spec_category = m.get('SpecCategory')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        self.tag_set = []
        if m.get('TagSet') is not None:
            for k1 in m.get('TagSet'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstanceTagSet()
                self.tag_set.append(temp_model.from_map(k1))

        if m.get('TertiaryZone') is not None:
            self.tertiary_zone = m.get('TertiaryZone')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstanceTagSet(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeDBInstanceAttributeResponseBodyDBInstanceGdnMemberList(DaraModel):
    def __init__(
        self,
        member_name: str = None,
        role: str = None,
        status: str = None,
    ):
        self.member_name = member_name
        self.role = role
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes(DaraModel):
    def __init__(
        self,
        compute_node_id: str = None,
        data_node_id: str = None,
        id: str = None,
        node_class: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The name of the compute node.
        self.compute_node_id = compute_node_id
        # The name of the storage node.
        self.data_node_id = data_node_id
        # The logical node ID.
        self.id = id
        # The node specifications.
        self.node_class = node_class
        # The region ID of the node.
        self.region_id = region_id
        # The zone in which the node resides.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_node_id is not None:
            result['ComputeNodeId'] = self.compute_node_id

        if self.data_node_id is not None:
            result['DataNodeId'] = self.data_node_id

        if self.id is not None:
            result['Id'] = self.id

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeNodeId') is not None:
            self.compute_node_id = m.get('ComputeNodeId')

        if m.get('DataNodeId') is not None:
            self.data_node_id = m.get('DataNodeId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        port: int = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        # The endpoint.
        self.connection_string = connection_string
        # The connection port number.
        self.port = port
        # The connection type. **VPC** indicates an internal network connection. **PUBLIC** indicates a public network connection.
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The internal CloudInstanceId within the VPC. You can ignore this parameter.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.port is not None:
            result['Port'] = self.port

        if self.type is not None:
            result['Type'] = self.type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

