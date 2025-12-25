# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.ListInstancesResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
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
        # The total number.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_backup: bool = None,
        begin_time: int = None,
        cluster_info: main_models.ListInstancesResponseBodyDataClusterInfo = None,
        cluster_name: str = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_status: str = None,
        node_type: str = None,
        open_public_net: bool = None,
        package_type: str = None,
        pay_type: int = None,
        product_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        running_time: int = None,
        sg_id: str = None,
        tags: List[main_models.ListInstancesResponseBodyDataTags] = None,
        version: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.auto_backup = auto_backup
        # The start time.
        self.begin_time = begin_time
        # The instance details.
        self.cluster_info = cluster_info
        # The instance name.
        self.cluster_name = cluster_name
        # The expiration time.
        self.expire_time = expire_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the bastion host. Valid values:
        # 
        # *   creating.
        # *   running.
        # *   updating. Cluster scaling (up/down), configuration changes, and enabling/disabling public network access.
        # *   disable. The cluster has expired and needs to be renewed for activation.
        # *   deleting.
        # *   deleted.
        self.instance_status = instance_status
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
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_backup is not None:
            result['AutoBackup'] = self.auto_backup

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

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
        if m.get('AutoBackup') is not None:
            self.auto_backup = m.get('AutoBackup')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('ClusterInfo') is not None:
            temp_model = main_models.ListInstancesResponseBodyDataClusterInfo()
            self.cluster_info = temp_model.from_map(m.get('ClusterInfo'))

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

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
                temp_model = main_models.ListInstancesResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListInstancesResponseBodyDataTags(DaraModel):
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

class ListInstancesResponseBodyDataClusterInfo(DaraModel):
    def __init__(
        self,
        attu_port: int = None,
        internet_url: str = None,
        intranet_url: str = None,
        milvus_resource_info_list: List[main_models.ListInstancesResponseBodyDataClusterInfoMilvusResourceInfoList] = None,
        proxy_port: int = None,
        total_cu_num: int = None,
        total_disk_size: int = None,
    ):
        # The port of the Attu component.
        self.attu_port = attu_port
        # The public IP address.
        self.internet_url = internet_url
        # The internal endpoint.
        self.intranet_url = intranet_url
        # The resource details.
        self.milvus_resource_info_list = milvus_resource_info_list
        # The proxy port.
        self.proxy_port = proxy_port
        # The number of CUs.
        self.total_cu_num = total_cu_num
        # The total capacity of the disk.
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
                temp_model = main_models.ListInstancesResponseBodyDataClusterInfoMilvusResourceInfoList()
                self.milvus_resource_info_list.append(temp_model.from_map(k1))

        if m.get('ProxyPort') is not None:
            self.proxy_port = m.get('ProxyPort')

        if m.get('TotalCuNum') is not None:
            self.total_cu_num = m.get('TotalCuNum')

        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')

        return self

class ListInstancesResponseBodyDataClusterInfoMilvusResourceInfoList(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        cu_num: int = None,
        disk_size: int = None,
        disk_type: str = None,
        replica: int = None,
    ):
        # The type of the component. Valid values:
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
        # The disk size.
        self.disk_size = disk_size
        # The disk type.
        self.disk_type = disk_type
        # The number of replicas.
        self.replica = replica

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

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.replica is not None:
            result['Replica'] = self.replica

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Replica') is not None:
            self.replica = m.get('Replica')

        return self

