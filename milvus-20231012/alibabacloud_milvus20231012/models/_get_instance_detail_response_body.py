# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class GetInstanceDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.GetInstanceDetailResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The returned result.
        self.data = data
        # The error code returned.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.GetInstanceDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        begin_time: int = None,
        bucket_name: str = None,
        bucket_path: str = None,
        cluster_info: main_models.GetInstanceDetailResponseBodyDataClusterInfo = None,
        cluster_name: str = None,
        enable_ha: bool = None,
        encrypted: str = None,
        expire_time: int = None,
        high_availability: main_models.GetInstanceDetailResponseBodyDataHighAvailability = None,
        instance_id: str = None,
        instance_status: str = None,
        kms_key_id: str = None,
        measure_config: main_models.GetInstanceDetailResponseBodyDataMeasureConfig = None,
        multi_zone_mode: str = None,
        node_type: str = None,
        open_public_net: bool = None,
        package_type: str = None,
        pay_type: int = None,
        product_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        running_time: int = None,
        sg_id: str = None,
        tags: List[main_models.GetInstanceDetailResponseBodyDataTags] = None,
        template_version: str = None,
        user_config: str = None,
        v_switches: List[main_models.GetInstanceDetailResponseBodyDataVSwitches] = None,
        version: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        # AclId for Public Network Access Control.
        self.acl_id = acl_id
        # The start time.
        self.begin_time = begin_time
        # The name of the bucket.
        self.bucket_name = bucket_name
        # The address of the bucket.
        self.bucket_path = bucket_path
        # The instance details.
        self.cluster_info = cluster_info
        # The instance name.
        self.cluster_name = cluster_name
        self.enable_ha = enable_ha
        self.encrypted = encrypted
        # The expiration time.
        self.expire_time = expire_time
        self.high_availability = high_availability
        # The ID of the instance.
        self.instance_id = instance_id
        # The instance status. Valid values:
        # 
        # *   creating.
        # *   running.
        # *   updating. Cluster scaling (up/down), configuration changes, and enabling/disabling public network access.
        # *   disable. The cluster has expired and needs to be renewed for activation.
        # *   deleting.
        # *   deleted.
        self.instance_status = instance_status
        self.kms_key_id = kms_key_id
        self.measure_config = measure_config
        self.multi_zone_mode = multi_zone_mode
        self.node_type = node_type
        # Indicates whether Internet access is enabled.
        self.open_public_net = open_public_net
        # The specification details. Valid values:
        # 
        # *   trial.
        # *   standard.
        self.package_type = package_type
        # The billing method of the instance. Valid values:
        # 
        # *   0: pay-as-you-go
        # *   1: subscription
        self.pay_type = pay_type
        # The commodity code.
        self.product_code = product_code
        # The region code.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The runtime.
        self.running_time = running_time
        # The security group ID.
        self.sg_id = sg_id
        self.tags = tags
        # The version of the software stack.
        self.template_version = template_version
        # User-defined configuration.
        self.user_config = user_config
        self.v_switches = v_switches
        # The kernel version.
        self.version = version
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vsw_id = vsw_id
        # The zone.
        self.zone_id = zone_id

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()
        if self.high_availability:
            self.high_availability.validate()
        if self.measure_config:
            self.measure_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.bucket_path is not None:
            result['BucketPath'] = self.bucket_path

        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.enable_ha is not None:
            result['EnableHa'] = self.enable_ha

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.high_availability is not None:
            result['HighAvailability'] = self.high_availability.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.measure_config is not None:
            result['MeasureConfig'] = self.measure_config.to_map()

        if self.multi_zone_mode is not None:
            result['MultiZoneMode'] = self.multi_zone_mode

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.open_public_net is not None:
            result['OpenPublicNet'] = self.open_public_net

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.running_time is not None:
            result['RunningTime'] = self.running_time

        if self.sg_id is not None:
            result['SgId'] = self.sg_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.user_config is not None:
            result['UserConfig'] = self.user_config

        result['VSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['VSwitches'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('BucketPath') is not None:
            self.bucket_path = m.get('BucketPath')

        if m.get('ClusterInfo') is not None:
            temp_model = main_models.GetInstanceDetailResponseBodyDataClusterInfo()
            self.cluster_info = temp_model.from_map(m.get('ClusterInfo'))

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('EnableHa') is not None:
            self.enable_ha = m.get('EnableHa')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HighAvailability') is not None:
            temp_model = main_models.GetInstanceDetailResponseBodyDataHighAvailability()
            self.high_availability = temp_model.from_map(m.get('HighAvailability'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('MeasureConfig') is not None:
            temp_model = main_models.GetInstanceDetailResponseBodyDataMeasureConfig()
            self.measure_config = temp_model.from_map(m.get('MeasureConfig'))

        if m.get('MultiZoneMode') is not None:
            self.multi_zone_mode = m.get('MultiZoneMode')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OpenPublicNet') is not None:
            self.open_public_net = m.get('OpenPublicNet')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')

        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetInstanceDetailResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')

        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k1 in m.get('VSwitches'):
                temp_model = main_models.GetInstanceDetailResponseBodyDataVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetInstanceDetailResponseBodyDataVSwitches(DaraModel):
    def __init__(
        self,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.vsw_id = vsw_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetInstanceDetailResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class GetInstanceDetailResponseBodyDataMeasureConfig(DaraModel):
    def __init__(
        self,
        data_node_cu_num: int = None,
        data_node_replica: int = None,
        index_node_cu_num: int = None,
        index_node_replica: int = None,
        mix_coodinator_node_cu_num: int = None,
        mix_coodinator_node_replica: int = None,
        proxy_node_cu_num: int = None,
        proxy_node_replica: int = None,
        query_node_cu_num: int = None,
        query_node_replica: int = None,
    ):
        self.data_node_cu_num = data_node_cu_num
        self.data_node_replica = data_node_replica
        self.index_node_cu_num = index_node_cu_num
        self.index_node_replica = index_node_replica
        self.mix_coodinator_node_cu_num = mix_coodinator_node_cu_num
        self.mix_coodinator_node_replica = mix_coodinator_node_replica
        self.proxy_node_cu_num = proxy_node_cu_num
        self.proxy_node_replica = proxy_node_replica
        self.query_node_cu_num = query_node_cu_num
        self.query_node_replica = query_node_replica

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_node_cu_num is not None:
            result['DataNodeCuNum'] = self.data_node_cu_num

        if self.data_node_replica is not None:
            result['DataNodeReplica'] = self.data_node_replica

        if self.index_node_cu_num is not None:
            result['IndexNodeCuNum'] = self.index_node_cu_num

        if self.index_node_replica is not None:
            result['IndexNodeReplica'] = self.index_node_replica

        if self.mix_coodinator_node_cu_num is not None:
            result['MixCoodinatorNodeCuNum'] = self.mix_coodinator_node_cu_num

        if self.mix_coodinator_node_replica is not None:
            result['MixCoodinatorNodeReplica'] = self.mix_coodinator_node_replica

        if self.proxy_node_cu_num is not None:
            result['ProxyNodeCuNum'] = self.proxy_node_cu_num

        if self.proxy_node_replica is not None:
            result['ProxyNodeReplica'] = self.proxy_node_replica

        if self.query_node_cu_num is not None:
            result['QueryNodeCuNum'] = self.query_node_cu_num

        if self.query_node_replica is not None:
            result['QueryNodeReplica'] = self.query_node_replica

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataNodeCuNum') is not None:
            self.data_node_cu_num = m.get('DataNodeCuNum')

        if m.get('DataNodeReplica') is not None:
            self.data_node_replica = m.get('DataNodeReplica')

        if m.get('IndexNodeCuNum') is not None:
            self.index_node_cu_num = m.get('IndexNodeCuNum')

        if m.get('IndexNodeReplica') is not None:
            self.index_node_replica = m.get('IndexNodeReplica')

        if m.get('MixCoodinatorNodeCuNum') is not None:
            self.mix_coodinator_node_cu_num = m.get('MixCoodinatorNodeCuNum')

        if m.get('MixCoodinatorNodeReplica') is not None:
            self.mix_coodinator_node_replica = m.get('MixCoodinatorNodeReplica')

        if m.get('ProxyNodeCuNum') is not None:
            self.proxy_node_cu_num = m.get('ProxyNodeCuNum')

        if m.get('ProxyNodeReplica') is not None:
            self.proxy_node_replica = m.get('ProxyNodeReplica')

        if m.get('QueryNodeCuNum') is not None:
            self.query_node_cu_num = m.get('QueryNodeCuNum')

        if m.get('QueryNodeReplica') is not None:
            self.query_node_replica = m.get('QueryNodeReplica')

        return self

class GetInstanceDetailResponseBodyDataHighAvailability(DaraModel):
    def __init__(
        self,
        current_active_az: str = None,
        mode: str = None,
        primary_zone_id: str = None,
        secondary_zone_id: str = None,
    ):
        self.current_active_az = current_active_az
        self.mode = mode
        self.primary_zone_id = primary_zone_id
        self.secondary_zone_id = secondary_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_active_az is not None:
            result['CurrentActiveAZ'] = self.current_active_az

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentActiveAZ') is not None:
            self.current_active_az = m.get('CurrentActiveAZ')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        return self

class GetInstanceDetailResponseBodyDataClusterInfo(DaraModel):
    def __init__(
        self,
        attu_port: int = None,
        internet_url: str = None,
        intranet_url: str = None,
        milvus_resource_info_list: List[main_models.GetInstanceDetailResponseBodyDataClusterInfoMilvusResourceInfoList] = None,
        oss_storage_size: str = None,
        oss_storage_timestamp: int = None,
        proxy_port: int = None,
        total_cu_num: int = None,
        total_disk_size: int = None,
    ):
        # The port of the Attu component.
        self.attu_port = attu_port
        # The public IP address.
        self.internet_url = internet_url
        # The internal IP address.
        self.intranet_url = intranet_url
        # The resource details.
        self.milvus_resource_info_list = milvus_resource_info_list
        # The size of the data stored in OSS.
        self.oss_storage_size = oss_storage_size
        # The timestamp when the OSS metric is stored.
        self.oss_storage_timestamp = oss_storage_timestamp
        # The proxy port.
        self.proxy_port = proxy_port
        # The total number of CUs.
        self.total_cu_num = total_cu_num
        # The total number of disks.
        self.total_disk_size = total_disk_size

    def validate(self):
        if self.milvus_resource_info_list:
            for v1 in self.milvus_resource_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attu_port is not None:
            result['AttuPort'] = self.attu_port

        if self.internet_url is not None:
            result['InternetUrl'] = self.internet_url

        if self.intranet_url is not None:
            result['IntranetUrl'] = self.intranet_url

        result['MilvusResourceInfoList'] = []
        if self.milvus_resource_info_list is not None:
            for k1 in self.milvus_resource_info_list:
                result['MilvusResourceInfoList'].append(k1.to_map() if k1 else None)

        if self.oss_storage_size is not None:
            result['OssStorageSize'] = self.oss_storage_size

        if self.oss_storage_timestamp is not None:
            result['OssStorageTimestamp'] = self.oss_storage_timestamp

        if self.proxy_port is not None:
            result['ProxyPort'] = self.proxy_port

        if self.total_cu_num is not None:
            result['TotalCuNum'] = self.total_cu_num

        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttuPort') is not None:
            self.attu_port = m.get('AttuPort')

        if m.get('InternetUrl') is not None:
            self.internet_url = m.get('InternetUrl')

        if m.get('IntranetUrl') is not None:
            self.intranet_url = m.get('IntranetUrl')

        self.milvus_resource_info_list = []
        if m.get('MilvusResourceInfoList') is not None:
            for k1 in m.get('MilvusResourceInfoList'):
                temp_model = main_models.GetInstanceDetailResponseBodyDataClusterInfoMilvusResourceInfoList()
                self.milvus_resource_info_list.append(temp_model.from_map(k1))

        if m.get('OssStorageSize') is not None:
            self.oss_storage_size = m.get('OssStorageSize')

        if m.get('OssStorageTimestamp') is not None:
            self.oss_storage_timestamp = m.get('OssStorageTimestamp')

        if m.get('ProxyPort') is not None:
            self.proxy_port = m.get('ProxyPort')

        if m.get('TotalCuNum') is not None:
            self.total_cu_num = m.get('TotalCuNum')

        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')

        return self

class GetInstanceDetailResponseBodyDataClusterInfoMilvusResourceInfoList(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        cu_num: int = None,
        cu_ratio: int = None,
        disk_size: int = None,
        disk_type: str = None,
        replica: int = None,
        zone_id: str = None,
    ):
        # The component type. Valid values:
        # 
        # *   standalone
        # *   proxy
        # *   mix_coordinator
        # *   query
        # *   index
        # *   data
        self.component_type = component_type
        # The number of CUs.
        self.cu_num = cu_num
        self.cu_ratio = cu_ratio
        # The disk size.
        self.disk_size = disk_size
        # The disk type.
        self.disk_type = disk_type
        # The number of replicas.
        self.replica = replica
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.cu_num is not None:
            result['CuNum'] = self.cu_num

        if self.cu_ratio is not None:
            result['CuRatio'] = self.cu_ratio

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.replica is not None:
            result['Replica'] = self.replica

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')

        if m.get('CuRatio') is not None:
            self.cu_ratio = m.get('CuRatio')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Replica') is not None:
            self.replica = m.get('Replica')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

