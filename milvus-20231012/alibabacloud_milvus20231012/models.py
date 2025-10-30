# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class InstanceDetailComponents(TeaModel):
    def __init__(
        self,
        cu_num: int = None,
        cu_type: str = None,
        disk_size_type: str = None,
        replica: int = None,
        type: str = None,
    ):
        self.cu_num = cu_num
        self.cu_type = cu_type
        self.disk_size_type = disk_size_type
        self.replica = replica
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_num is not None:
            result['cuNum'] = self.cu_num
        if self.cu_type is not None:
            result['cuType'] = self.cu_type
        if self.disk_size_type is not None:
            result['diskSizeType'] = self.disk_size_type
        if self.replica is not None:
            result['replica'] = self.replica
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuNum') is not None:
            self.cu_num = m.get('cuNum')
        if m.get('cuType') is not None:
            self.cu_type = m.get('cuType')
        if m.get('diskSizeType') is not None:
            self.disk_size_type = m.get('diskSizeType')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InstanceDetailTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class InstanceDetailVSwitchIds(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vsw_id is not None:
            result['vswId'] = self.vsw_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vswId') is not None:
            self.vsw_id = m.get('vswId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class InstanceDetail(TeaModel):
    def __init__(
        self,
        auto_backup: bool = None,
        components: List[InstanceDetailComponents] = None,
        configuration: str = None,
        create_time: str = None,
        db_version: str = None,
        encrypted: bool = None,
        expire_time: str = None,
        ha: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        kms_key_id: str = None,
        multi_zone_mode: str = None,
        order_id: str = None,
        payment_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        running_time: int = None,
        security_group_ids: List[str] = None,
        status: str = None,
        tags: List[InstanceDetailTags] = None,
        v_switch_ids: List[InstanceDetailVSwitchIds] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.auto_backup = auto_backup
        self.components = components
        self.configuration = configuration
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        self.db_version = db_version
        self.encrypted = encrypted
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.expire_time = expire_time
        self.ha = ha
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.kms_key_id = kms_key_id
        self.multi_zone_mode = multi_zone_mode
        self.order_id = order_id
        self.payment_type = payment_type
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.running_time = running_time
        self.security_group_ids = security_group_ids
        self.status = status
        self.tags = tags
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.v_switch_ids:
            for k in self.v_switch_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_backup is not None:
            result['autoBackup'] = self.auto_backup
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        if self.configuration is not None:
            result['configuration'] = self.configuration
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.db_version is not None:
            result['dbVersion'] = self.db_version
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.ha is not None:
            result['ha'] = self.ha
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.kms_key_id is not None:
            result['kmsKeyId'] = self.kms_key_id
        if self.multi_zone_mode is not None:
            result['multiZoneMode'] = self.multi_zone_mode
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.running_time is not None:
            result['runningTime'] = self.running_time
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['vSwitchIds'] = []
        if self.v_switch_ids is not None:
            for k in self.v_switch_ids:
                result['vSwitchIds'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBackup') is not None:
            self.auto_backup = m.get('autoBackup')
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = InstanceDetailComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dbVersion') is not None:
            self.db_version = m.get('dbVersion')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('ha') is not None:
            self.ha = m.get('ha')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('kmsKeyId') is not None:
            self.kms_key_id = m.get('kmsKeyId')
        if m.get('multiZoneMode') is not None:
            self.multi_zone_mode = m.get('multiZoneMode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('runningTime') is not None:
            self.running_time = m.get('runningTime')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = InstanceDetailTags()
                self.tags.append(temp_model.from_map(k))
        self.v_switch_ids = []
        if m.get('vSwitchIds') is not None:
            for k in m.get('vSwitchIds'):
                temp_model = InstanceDetailVSwitchIds()
                self.v_switch_ids.append(temp_model.from_map(k))
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class CreateDefaultRoleResponseBody(TeaModel):
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
        # The details about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The returned result.
        self.data = data
        # The error code
        self.err_code = err_code
        # The error message returned.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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


class CreateDefaultRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDefaultRoleResponseBody = None,
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
            temp_model = CreateDefaultRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessControlListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the instance.
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
        # AclId for public network access control.
        self.acl_id = acl_id
        # The CIDR blocks.
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
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The returned result.
        self.data = data
        # The error message.
        self.err_message = err_message
        # The error code returned.
        self.error_code = error_code
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
        # The ID of the instance.
        # 
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
        # The ID of the instance.
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
        cu_ratio: int = None,
        disk_size: int = None,
        disk_type: str = None,
        replica: int = None,
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
        if self.cu_ratio is not None:
            result['CuRatio'] = self.cu_ratio
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
        if m.get('CuRatio') is not None:
            self.cu_ratio = m.get('CuRatio')
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


class GetInstanceDetailResponseBodyDataMeasureConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetInstanceDetailResponseBodyDataTags(TeaModel):
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


class GetInstanceDetailResponseBodyDataVSwitches(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetInstanceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        begin_time: int = None,
        bucket_name: str = None,
        bucket_path: str = None,
        cluster_info: GetInstanceDetailResponseBodyDataClusterInfo = None,
        cluster_name: str = None,
        enable_ha: bool = None,
        encrypted: str = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_status: str = None,
        kms_key_id: str = None,
        measure_config: GetInstanceDetailResponseBodyDataMeasureConfig = None,
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
        tags: List[GetInstanceDetailResponseBodyDataTags] = None,
        template_version: str = None,
        user_config: str = None,
        v_switches: List[GetInstanceDetailResponseBodyDataVSwitches] = None,
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
        if self.measure_config:
            self.measure_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

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
        if self.enable_ha is not None:
            result['EnableHa'] = self.enable_ha
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
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
        if m.get('EnableHa') is not None:
            self.enable_ha = m.get('EnableHa')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('MeasureConfig') is not None:
            temp_model = GetInstanceDetailResponseBodyDataMeasureConfig()
            self.measure_config = temp_model.from_map(m['MeasureConfig'])
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
            for k in m.get('Tags'):
                temp_model = GetInstanceDetailResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = GetInstanceDetailResponseBodyDataVSwitches()
                self.v_switches.append(temp_model.from_map(k))
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


class ListInstancesRequestTag(TeaModel):
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


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[ListInstancesRequestTag] = None,
    ):
        # The instance ID.
        self.cluster_id = cluster_id
        # The instance name.
        self.cluster_name = cluster_name
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region code.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag_shrink: str = None,
    ):
        # The instance ID.
        self.cluster_id = cluster_id
        # The instance name.
        self.cluster_name = cluster_name
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region code.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.tag_shrink = tag_shrink

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
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


class ListInstancesResponseBodyDataTags(TeaModel):
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


class ListInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_backup: bool = None,
        begin_time: int = None,
        cluster_info: ListInstancesResponseBodyDataClusterInfo = None,
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
        tags: List[ListInstancesResponseBodyDataTags] = None,
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
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
            for k in m.get('Tags'):
                temp_model = ListInstancesResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The reason for the update.
        # 
        # This parameter is required.
        self.reason = reason
        # User-defined configuration.
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
        # Indicates whether the call was successful.
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
        # The ID of public network access control
        self.acl_id = acl_id
        # The CIDR blocks.
        self.cidr = cidr
        # The ID of the instance.
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
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The returned result.
        self.data = data
        # The error message.
        self.err_message = err_message
        # The error code returned.
        self.error_code = error_code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        # The instance ID.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The ID of the instance.
        # 
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
        # The CIDR blocks.
        self.cidr = cidr
        # The component type. Valid values:
        # 
        # *   Proxy
        # 
        # This parameter is required.
        self.component_type = component_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Enable /disable the Internet.
        # 
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


