# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DescribeAccessControlListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeAccessControlListResponseBodyData(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        cidr: List[str] = None,
    ):
        self.acl_id = acl_id
        self.cidr = cidr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        return self


class DescribeAccessControlListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: DescribeAccessControlListResponseBodyData = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = DescribeAccessControlListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAccessControlListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessControlListResponseBody = None,
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
            temp_model = DescribeAccessControlListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceConfigsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceConfigsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bytes = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
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


class DescribeInstanceConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceConfigsResponseBody = None,
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
            temp_model = DescribeInstanceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceDetailResponseBodyDataClusterInfoMilvusResourceInfoList(TeaModel):
    def __init__(
        self,
        component_type: str = None,
        cu_num: int = None,
        disk_size: int = None,
        disk_type: str = None,
        replica: int = None,
    ):
        self.component_type = component_type
        self.cu_num = cu_num
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.replica = replica

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetInstanceDetailResponseBodyDataClusterInfo(TeaModel):
    def __init__(
        self,
        attu_port: int = None,
        internet_url: str = None,
        intranet_url: str = None,
        milvus_resource_info_list: List[GetInstanceDetailResponseBodyDataClusterInfoMilvusResourceInfoList] = None,
        oss_storage_size: str = None,
        oss_storage_timestamp: int = None,
        proxy_port: int = None,
        total_cu_num: int = None,
        total_disk_size: int = None,
    ):
        self.attu_port = attu_port
        self.internet_url = internet_url
        self.intranet_url = intranet_url
        self.milvus_resource_info_list = milvus_resource_info_list
        self.oss_storage_size = oss_storage_size
        self.oss_storage_timestamp = oss_storage_timestamp
        self.proxy_port = proxy_port
        self.total_cu_num = total_cu_num
        self.total_disk_size = total_disk_size

    def validate(self):
        if self.milvus_resource_info_list:
            for k in self.milvus_resource_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attu_port is not None:
            result['AttuPort'] = self.attu_port
        if self.internet_url is not None:
            result['InternetUrl'] = self.internet_url
        if self.intranet_url is not None:
            result['IntranetUrl'] = self.intranet_url
        result['MilvusResourceInfoList'] = []
        if self.milvus_resource_info_list is not None:
            for k in self.milvus_resource_info_list:
                result['MilvusResourceInfoList'].append(k.to_map() if k else None)
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
            for k in m.get('MilvusResourceInfoList'):
                temp_model = GetInstanceDetailResponseBodyDataClusterInfoMilvusResourceInfoList()
                self.milvus_resource_info_list.append(temp_model.from_map(k))
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


class GetInstanceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        begin_time: int = None,
        bucket_name: str = None,
        bucket_path: str = None,
        cluster_info: GetInstanceDetailResponseBodyDataClusterInfo = None,
        cluster_name: str = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_status: str = None,
        open_public_net: bool = None,
        package_type: str = None,
        pay_type: int = None,
        product_code: str = None,
        region_id: str = None,
        running_time: int = None,
        sg_id: str = None,
        template_version: str = None,
        user_config: str = None,
        version: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.acl_id = acl_id
        self.begin_time = begin_time
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.cluster_info = cluster_info
        self.cluster_name = cluster_name
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.open_public_net = open_public_net
        self.package_type = package_type
        self.pay_type = pay_type
        self.product_code = product_code
        self.region_id = region_id
        self.running_time = running_time
        self.sg_id = sg_id
        self.template_version = template_version
        self.user_config = user_config
        self.version = version
        self.vpc_id = vpc_id
        self.vsw_id = vsw_id
        self.zone_id = zone_id

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
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
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
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
            temp_model = GetInstanceDetailResponseBodyDataClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
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
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetInstanceDetailResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: GetInstanceDetailResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetInstanceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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


class GetInstanceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceDetailResponseBody = None,
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
            temp_model = GetInstanceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstancesResponseBodyDataClusterInfoMilvusResourceInfoList(TeaModel):
    def __init__(
        self,
        component_type: str = None,
        cu_num: int = None,
        disk_size: int = None,
        disk_type: str = None,
        replica: int = None,
    ):
        self.component_type = component_type
        self.cu_num = cu_num
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.replica = replica

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListInstancesResponseBodyDataClusterInfo(TeaModel):
    def __init__(
        self,
        attu_port: int = None,
        internet_url: str = None,
        intranet_url: str = None,
        milvus_resource_info_list: List[ListInstancesResponseBodyDataClusterInfoMilvusResourceInfoList] = None,
        proxy_port: int = None,
        total_cu_num: int = None,
        total_disk_size: int = None,
    ):
        self.attu_port = attu_port
        self.internet_url = internet_url
        self.intranet_url = intranet_url
        self.milvus_resource_info_list = milvus_resource_info_list
        self.proxy_port = proxy_port
        self.total_cu_num = total_cu_num
        self.total_disk_size = total_disk_size

    def validate(self):
        if self.milvus_resource_info_list:
            for k in self.milvus_resource_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attu_port is not None:
            result['AttuPort'] = self.attu_port
        if self.internet_url is not None:
            result['InternetUrl'] = self.internet_url
        if self.intranet_url is not None:
            result['IntranetUrl'] = self.intranet_url
        result['MilvusResourceInfoList'] = []
        if self.milvus_resource_info_list is not None:
            for k in self.milvus_resource_info_list:
                result['MilvusResourceInfoList'].append(k.to_map() if k else None)
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
            for k in m.get('MilvusResourceInfoList'):
                temp_model = ListInstancesResponseBodyDataClusterInfoMilvusResourceInfoList()
                self.milvus_resource_info_list.append(temp_model.from_map(k))
        if m.get('ProxyPort') is not None:
            self.proxy_port = m.get('ProxyPort')
        if m.get('TotalCuNum') is not None:
            self.total_cu_num = m.get('TotalCuNum')
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        cluster_info: ListInstancesResponseBodyDataClusterInfo = None,
        cluster_name: str = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_status: str = None,
        open_public_net: bool = None,
        package_type: str = None,
        pay_type: int = None,
        product_code: str = None,
        region_id: str = None,
        running_time: int = None,
        sg_id: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.begin_time = begin_time
        self.cluster_info = cluster_info
        self.cluster_name = cluster_name
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.open_public_net = open_public_net
        self.package_type = package_type
        self.pay_type = pay_type
        self.product_code = product_code
        self.region_id = region_id
        self.running_time = running_time
        self.sg_id = sg_id
        self.vpc_id = vpc_id
        self.vsw_id = vsw_id
        self.zone_id = zone_id

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClusterInfo') is not None:
            temp_model = ListInstancesResponseBodyDataClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
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
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[ListInstancesResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        reason: str = None,
        user_config: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.reason = reason
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class ModifyInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
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


class ModifyInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceConfigResponseBody = None,
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
            temp_model = ModifyInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccessControlListRequest(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        cidr: str = None,
        instance_id: str = None,
    ):
        self.acl_id = acl_id
        self.cidr = cidr
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAccessControlListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAccessControlListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAccessControlListResponseBody = None,
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
            temp_model = UpdateAccessControlListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceNameRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.cluster_name = cluster_name
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateInstanceNameResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
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


class UpdateInstanceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceNameResponseBody = None,
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
            temp_model = UpdateInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicNetworkStatusRequest(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        component_type: str = None,
        instance_id: str = None,
        public_network_enabled: bool = None,
    ):
        # This parameter is required.
        self.cidr = cidr
        # This parameter is required.
        self.component_type = component_type
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.public_network_enabled = public_network_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_network_enabled is not None:
            result['PublicNetworkEnabled'] = self.public_network_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicNetworkEnabled') is not None:
            self.public_network_enabled = m.get('PublicNetworkEnabled')
        return self


class UpdatePublicNetworkStatusResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
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


class UpdatePublicNetworkStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePublicNetworkStatusResponseBody = None,
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
            temp_model = UpdatePublicNetworkStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


