# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class InstanceConfigDto(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        config_type: str = None,
        config_value: str = None,
        node_group_id: str = None,
    ):
        self.config_key = config_key
        self.config_type = config_type
        self.config_value = config_value
        self.node_group_id = node_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['configKey'] = self.config_key
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.config_value is not None:
            result['configValue'] = self.config_value
        if self.node_group_id is not None:
            result['nodeGroupId'] = self.node_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configKey') is not None:
            self.config_key = m.get('configKey')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('configValue') is not None:
            self.config_value = m.get('configValue')
        if m.get('nodeGroupId') is not None:
            self.node_group_id = m.get('nodeGroupId')
        return self


class ResourceSpec(TeaModel):
    def __init__(
        self,
        cu: int = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
    ):
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.node_number = node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number
        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type
        if self.node_number is not None:
            result['nodeNumber'] = self.node_number
        if self.spec_type is not None:
            result['specType'] = self.spec_type
        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')
        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')
        if m.get('nodeNumber') is not None:
            self.node_number = m.get('nodeNumber')
        if m.get('specType') is not None:
            self.spec_type = m.get('specType')
        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        self.region_id = region_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
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
        # AccessDeniedDetail
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


class CreateInstanceV1RequestAgentNodeGroup(TeaModel):
    def __init__(
        self,
        cu: int = None,
    ):
        self.cu = cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        return self


class CreateInstanceV1RequestBackendNodeGroups(TeaModel):
    def __init__(
        self,
        cu: int = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
        zone_id: str = None,
    ):
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number
        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type
        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number
        if self.spec_type is not None:
            result['specType'] = self.spec_type
        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')
        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')
        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')
        if m.get('specType') is not None:
            self.spec_type = m.get('specType')
        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class CreateInstanceV1RequestFrontendNodeGroups(TeaModel):
    def __init__(
        self,
        cu: int = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
        zone_id: str = None,
    ):
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number
        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type
        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number
        if self.spec_type is not None:
            result['specType'] = self.spec_type
        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')
        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')
        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')
        if m.get('specType') is not None:
            self.spec_type = m.get('specType')
        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class CreateInstanceV1RequestObserverNodeGroups(TeaModel):
    def __init__(
        self,
        cu: int = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
        zone_id: str = None,
    ):
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number
        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type
        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number
        if self.spec_type is not None:
            result['specType'] = self.spec_type
        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')
        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')
        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')
        if m.get('specType') is not None:
            self.spec_type = m.get('specType')
        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class CreateInstanceV1RequestTags(TeaModel):
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


class CreateInstanceV1RequestVSwitches(TeaModel):
    def __init__(
        self,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
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


class CreateInstanceV1Request(TeaModel):
    def __init__(
        self,
        admin_password: str = None,
        agent_node_group: CreateInstanceV1RequestAgentNodeGroup = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        backend_node_groups: List[CreateInstanceV1RequestBackendNodeGroups] = None,
        client_token: str = None,
        duration: int = None,
        encrypted: bool = None,
        frontend_node_groups: List[CreateInstanceV1RequestFrontendNodeGroups] = None,
        gateway_type: str = None,
        instance_name: str = None,
        kms_key_id: str = None,
        observer_node_groups: List[CreateInstanceV1RequestObserverNodeGroups] = None,
        oss_accessing_role_name: str = None,
        package_type: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        promotion_option_no: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        run_mode: str = None,
        tags: List[CreateInstanceV1RequestTags] = None,
        v_switches: List[CreateInstanceV1RequestVSwitches] = None,
        version: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.admin_password = admin_password
        self.agent_node_group = agent_node_group
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.backend_node_groups = backend_node_groups
        self.client_token = client_token
        self.duration = duration
        self.encrypted = encrypted
        self.frontend_node_groups = frontend_node_groups
        self.gateway_type = gateway_type
        # This parameter is required.
        self.instance_name = instance_name
        self.kms_key_id = kms_key_id
        self.observer_node_groups = observer_node_groups
        self.oss_accessing_role_name = oss_accessing_role_name
        # This parameter is required.
        self.package_type = package_type
        # This parameter is required.
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.promotion_option_no = promotion_option_no
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.run_mode = run_mode
        self.tags = tags
        self.v_switches = v_switches
        # This parameter is required.
        self.version = version
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.agent_node_group:
            self.agent_node_group.validate()
        if self.backend_node_groups:
            for k in self.backend_node_groups:
                if k:
                    k.validate()
        if self.frontend_node_groups:
            for k in self.frontend_node_groups:
                if k:
                    k.validate()
        if self.observer_node_groups:
            for k in self.observer_node_groups:
                if k:
                    k.validate()
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
        if self.admin_password is not None:
            result['AdminPassword'] = self.admin_password
        if self.agent_node_group is not None:
            result['AgentNodeGroup'] = self.agent_node_group.to_map()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        result['BackendNodeGroups'] = []
        if self.backend_node_groups is not None:
            for k in self.backend_node_groups:
                result['BackendNodeGroups'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        result['FrontendNodeGroups'] = []
        if self.frontend_node_groups is not None:
            for k in self.frontend_node_groups:
                result['FrontendNodeGroups'].append(k.to_map() if k else None)
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        result['ObserverNodeGroups'] = []
        if self.observer_node_groups is not None:
            for k in self.observer_node_groups:
                result['ObserverNodeGroups'].append(k.to_map() if k else None)
        if self.oss_accessing_role_name is not None:
            result['OssAccessingRoleName'] = self.oss_accessing_role_name
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminPassword') is not None:
            self.admin_password = m.get('AdminPassword')
        if m.get('AgentNodeGroup') is not None:
            temp_model = CreateInstanceV1RequestAgentNodeGroup()
            self.agent_node_group = temp_model.from_map(m['AgentNodeGroup'])
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        self.backend_node_groups = []
        if m.get('BackendNodeGroups') is not None:
            for k in m.get('BackendNodeGroups'):
                temp_model = CreateInstanceV1RequestBackendNodeGroups()
                self.backend_node_groups.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        self.frontend_node_groups = []
        if m.get('FrontendNodeGroups') is not None:
            for k in m.get('FrontendNodeGroups'):
                temp_model = CreateInstanceV1RequestFrontendNodeGroups()
                self.frontend_node_groups.append(temp_model.from_map(k))
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        self.observer_node_groups = []
        if m.get('ObserverNodeGroups') is not None:
            for k in m.get('ObserverNodeGroups'):
                temp_model = CreateInstanceV1RequestObserverNodeGroups()
                self.observer_node_groups.append(temp_model.from_map(k))
        if m.get('OssAccessingRoleName') is not None:
            self.oss_accessing_role_name = m.get('OssAccessingRoleName')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateInstanceV1RequestTags()
                self.tags.append(temp_model.from_map(k))
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = CreateInstanceV1RequestVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateInstanceV1ResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: int = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateInstanceV1ResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: CreateInstanceV1ResponseBodyData = None,
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
            temp_model = CreateInstanceV1ResponseBodyData()
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


class CreateInstanceV1Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceV1ResponseBody = None,
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
            temp_model = CreateInstanceV1ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # AccessDeniedDetail
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.total is not None:
            result['Total'] = self.total
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
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceLinkedRoleResponseBody = None,
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
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
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


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
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
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag_shrink: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
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


class DescribeInstancesResponseBodyDataTags(TeaModel):
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


class DescribeInstancesResponseBodyDataVSwitches(TeaModel):
    def __init__(
        self,
        primary: bool = None,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.primary = primary
        self.vsw_id = vsw_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.primary is not None:
            result['Primary'] = self.primary
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Primary') is not None:
            self.primary = m.get('Primary')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        architecture: str = None,
        begin_time: int = None,
        enable_auto_minor_version_upgrade: bool = None,
        enable_ssl: bool = None,
        enabled_audit_loader: bool = None,
        encrypted: bool = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        isolate_leader: bool = None,
        kms_key_id: str = None,
        maintainable_period: str = None,
        minor_version: str = None,
        monitor_type: str = None,
        oss_location: str = None,
        package_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        run_mode: str = None,
        running_time: int = None,
        security_group_managed: bool = None,
        sg_id: str = None,
        tags: List[DescribeInstancesResponseBodyDataTags] = None,
        v_switches: List[DescribeInstancesResponseBodyDataVSwitches] = None,
        version: str = None,
        vpc_id: str = None,
    ):
        self.acl_id = acl_id
        self.architecture = architecture
        self.begin_time = begin_time
        self.enable_auto_minor_version_upgrade = enable_auto_minor_version_upgrade
        self.enable_ssl = enable_ssl
        self.enabled_audit_loader = enabled_audit_loader
        self.encrypted = encrypted
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.isolate_leader = isolate_leader
        self.kms_key_id = kms_key_id
        self.maintainable_period = maintainable_period
        self.minor_version = minor_version
        self.monitor_type = monitor_type
        self.oss_location = oss_location
        self.package_type = package_type
        self.pay_type = pay_type
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.run_mode = run_mode
        self.running_time = running_time
        self.security_group_managed = security_group_managed
        self.sg_id = sg_id
        self.tags = tags
        self.v_switches = v_switches
        self.version = version
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
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
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.enable_auto_minor_version_upgrade is not None:
            result['EnableAutoMinorVersionUpgrade'] = self.enable_auto_minor_version_upgrade
        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl
        if self.enabled_audit_loader is not None:
            result['EnabledAuditLoader'] = self.enabled_audit_loader
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.isolate_leader is not None:
            result['IsolateLeader'] = self.isolate_leader
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.maintainable_period is not None:
            result['MaintainablePeriod'] = self.maintainable_period
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.oss_location is not None:
            result['OssLocation'] = self.oss_location
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.security_group_managed is not None:
            result['SecurityGroupManaged'] = self.security_group_managed
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EnableAutoMinorVersionUpgrade') is not None:
            self.enable_auto_minor_version_upgrade = m.get('EnableAutoMinorVersionUpgrade')
        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')
        if m.get('EnabledAuditLoader') is not None:
            self.enabled_audit_loader = m.get('EnabledAuditLoader')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('IsolateLeader') is not None:
            self.isolate_leader = m.get('IsolateLeader')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('MaintainablePeriod') is not None:
            self.maintainable_period = m.get('MaintainablePeriod')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('OssLocation') is not None:
            self.oss_location = m.get('OssLocation')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SecurityGroupManaged') is not None:
            self.security_group_managed = m.get('SecurityGroupManaged')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeInstancesResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = DescribeInstancesResponseBodyDataVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeInstancesResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeInstancesResponseBodyData()
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


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeGroupsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        component_type: str = None,
        instance_id: str = None,
        node_group_ids: List[str] = None,
        node_group_name: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.component_type = component_type
        self.instance_id = instance_id
        self.node_group_ids = node_group_ids
        self.node_group_name = node_group_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.component_type is not None:
            result['componentType'] = self.component_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.node_group_ids is not None:
            result['nodeGroupIds'] = self.node_group_ids
        if self.node_group_name is not None:
            result['nodeGroupName'] = self.node_group_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('nodeGroupIds') is not None:
            self.node_group_ids = m.get('nodeGroupIds')
        if m.get('nodeGroupName') is not None:
            self.node_group_name = m.get('nodeGroupName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeNodeGroupsResponseBodyDataNodeInfo(TeaModel):
    def __init__(
        self,
        node_id: str = None,
    ):
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeNodeGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        account_status: str = None,
        architecture: str = None,
        begin_time: int = None,
        billing_instance_id: str = None,
        commodity_code: str = None,
        component_type: str = None,
        cu: int = None,
        default_group: bool = None,
        description: str = None,
        disk_number: int = None,
        elastic_node_number: int = None,
        enable_public_network: bool = None,
        endpoint: str = None,
        expire_time: int = None,
        http_port: int = None,
        instance_id: str = None,
        local_storage_instance_type: str = None,
        memory_cpu_ratio: int = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_info: List[DescribeNodeGroupsResponseBodyDataNodeInfo] = None,
        pay_type: str = None,
        public_address: str = None,
        region_id: str = None,
        resident_node_number: int = None,
        running_time: int = None,
        spec_type: str = None,
        status: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
        target_elastic_node_number: int = None,
        zone_id: str = None,
    ):
        self.account_status = account_status
        self.architecture = architecture
        self.begin_time = begin_time
        self.billing_instance_id = billing_instance_id
        self.commodity_code = commodity_code
        self.component_type = component_type
        self.cu = cu
        self.default_group = default_group
        self.description = description
        self.disk_number = disk_number
        self.elastic_node_number = elastic_node_number
        self.enable_public_network = enable_public_network
        self.endpoint = endpoint
        self.expire_time = expire_time
        self.http_port = http_port
        self.instance_id = instance_id
        self.local_storage_instance_type = local_storage_instance_type
        self.memory_cpu_ratio = memory_cpu_ratio
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.node_info = node_info
        self.pay_type = pay_type
        self.public_address = public_address
        self.region_id = region_id
        self.resident_node_number = resident_node_number
        self.running_time = running_time
        self.spec_type = spec_type
        self.status = status
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size
        self.target_elastic_node_number = target_elastic_node_number
        self.zone_id = zone_id

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.billing_instance_id is not None:
            result['BillingInstanceId'] = self.billing_instance_id
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        if self.cu is not None:
            result['Cu'] = self.cu
        if self.default_group is not None:
            result['DefaultGroup'] = self.default_group
        if self.description is not None:
            result['Description'] = self.description
        if self.disk_number is not None:
            result['DiskNumber'] = self.disk_number
        if self.elastic_node_number is not None:
            result['ElasticNodeNumber'] = self.elastic_node_number
        if self.enable_public_network is not None:
            result['EnablePublicNetwork'] = self.enable_public_network
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.local_storage_instance_type is not None:
            result['LocalStorageInstanceType'] = self.local_storage_instance_type
        if self.memory_cpu_ratio is not None:
            result['MemoryCpuRatio'] = self.memory_cpu_ratio
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.public_address is not None:
            result['PublicAddress'] = self.public_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resident_node_number is not None:
            result['ResidentNodeNumber'] = self.resident_node_number
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_performance_level is not None:
            result['StoragePerformanceLevel'] = self.storage_performance_level
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.target_elastic_node_number is not None:
            result['TargetElasticNodeNumber'] = self.target_elastic_node_number
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('BillingInstanceId') is not None:
            self.billing_instance_id = m.get('BillingInstanceId')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')
        if m.get('DefaultGroup') is not None:
            self.default_group = m.get('DefaultGroup')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiskNumber') is not None:
            self.disk_number = m.get('DiskNumber')
        if m.get('ElasticNodeNumber') is not None:
            self.elastic_node_number = m.get('ElasticNodeNumber')
        if m.get('EnablePublicNetwork') is not None:
            self.enable_public_network = m.get('EnablePublicNetwork')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LocalStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('LocalStorageInstanceType')
        if m.get('MemoryCpuRatio') is not None:
            self.memory_cpu_ratio = m.get('MemoryCpuRatio')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = DescribeNodeGroupsResponseBodyDataNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PublicAddress') is not None:
            self.public_address = m.get('PublicAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResidentNodeNumber') is not None:
            self.resident_node_number = m.get('ResidentNodeNumber')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoragePerformanceLevel') is not None:
            self.storage_performance_level = m.get('StoragePerformanceLevel')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('TargetElasticNodeNumber') is not None:
            self.target_elastic_node_number = m.get('TargetElasticNodeNumber')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeNodeGroupsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[DescribeNodeGroupsResponseBodyData] = None,
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
                temp_model = DescribeNodeGroupsResponseBodyData()
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


class DescribeNodeGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodeGroupsResponseBody = None,
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
            temp_model = DescribeNodeGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCuRequest(TeaModel):
    def __init__(
        self,
        fast_mode: bool = None,
        instance_id: str = None,
        node_group_id: str = None,
        promotion_option_no: str = None,
        target: int = None,
    ):
        # Specifies whether to restart compute nodes in quick restart mode. Default value: false. Valid values:
        # 
        # *   true: Compute nodes are restarted in quick restart mode in multiple batches. The batches are executed in parallel, and the nodes in each batch are restarted at the same time.
        # *   false: Compute nodes are restarted in rolling restart mode.
        self.fast_mode = fast_mode
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        self.promotion_option_no = promotion_option_no
        # The number of CUs to which you want to change.
        # 
        # Valid values:
        # 
        # *   4
        # *   8
        # *   16
        # *   32
        # *   64
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ModifyCuResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: int = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The order ID.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class ModifyCuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCuResponseBody = None,
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
            temp_model = ModifyCuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCuPreCheckRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_group_id: str = None,
        target: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The number of CUs to which you want to change.
        # 
        # Valid values:
        # 
        # *   2
        # *   4
        # *   8
        # *   16
        # *   32
        # *   64
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ModifyCuPreCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        allow: bool = None,
        reason: str = None,
    ):
        # Indicates whether the number of CUs can be modified.
        self.allow = allow
        # The reason why the number of CUs cannot be modified.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow is not None:
            result['Allow'] = self.allow
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Allow') is not None:
            self.allow = m.get('Allow')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ModifyCuPreCheckResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: ModifyCuPreCheckResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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
            temp_model = ModifyCuPreCheckResponseBodyData()
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


class ModifyCuPreCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCuPreCheckResponseBody = None,
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
            temp_model = ModifyCuPreCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskNumberRequest(TeaModel):
    def __init__(
        self,
        fast_mode: bool = None,
        instance_id: str = None,
        node_group_id: str = None,
        promotion_option_no: str = None,
        target: int = None,
    ):
        # Specifies whether to restart compute nodes in quick restart mode. Default value: false. Valid values:
        # 
        # *   true: Compute nodes are restarted in quick restart mode in multiple batches. The batches are executed in parallel, and the nodes in each batch are restarted at the same time.
        # *   false: Compute nodes are restarted in rolling restart mode.
        self.fast_mode = fast_mode
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        self.promotion_option_no = promotion_option_no
        # The number of disks to which you want to change to.
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ModifyDiskNumberResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: int = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The order ID.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class ModifyDiskNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDiskNumberResponseBody = None,
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
            temp_model = ModifyDiskNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskPerformanceLevelRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_group_id: str = None,
        promotion_option_no: str = None,
        target: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        self.promotion_option_no = promotion_option_no
        # The disk performance level to which you want to change.
        # 
        # Valid values:
        # 
        # *   pl0
        # *   pl1
        # *   pl2
        # *   pl3
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ModifyDiskPerformanceLevelResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: int = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The order ID.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class ModifyDiskPerformanceLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDiskPerformanceLevelResponseBody = None,
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
            temp_model = ModifyDiskPerformanceLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskSizeRequest(TeaModel):
    def __init__(
        self,
        fast_mode: bool = None,
        instance_id: str = None,
        node_group_id: str = None,
        promotion_option_no: str = None,
        target: int = None,
    ):
        self.fast_mode = fast_mode
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        self.promotion_option_no = promotion_option_no
        # The disk size to which you want to change to. Unit: GB.
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ModifyDiskSizeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: int = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The order ID.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class ModifyDiskSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDiskSizeResponseBody = None,
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
            temp_model = ModifyDiskSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodeNumberRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_group_id: str = None,
        parallelism: int = None,
        promotion_option_no: str = None,
        target: int = None,
        termination_grace_period_seconds: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        self.parallelism = parallelism
        self.promotion_option_no = promotion_option_no
        # The number of nodes to which you want to change to.
        # 
        # This parameter is required.
        self.target = target
        self.termination_grace_period_seconds = termination_grace_period_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.target is not None:
            result['Target'] = self.target
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        return self


class ModifyNodeNumberResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: int = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The order ID.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class ModifyNodeNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNodeNumberResponseBody = None,
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
            temp_model = ModifyNodeNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodeNumberPreCheckRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_group_id: str = None,
        target: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The number of nodes to which you want to change to.
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ModifyNodeNumberPreCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        allow: bool = None,
        reason: str = None,
    ):
        # Indicates whether the number of nodes can be modified.
        self.allow = allow
        # The reason why the number of nodes cannot be modified.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow is not None:
            result['Allow'] = self.allow
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Allow') is not None:
            self.allow = m.get('Allow')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ModifyNodeNumberPreCheckResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: ModifyNodeNumberPreCheckResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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
            temp_model = ModifyNodeNumberPreCheckResponseBodyData()
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


class ModifyNodeNumberPreCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNodeNumberPreCheckResponseBody = None,
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
            temp_model = ModifyNodeNumberPreCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUpgradableVersionsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        minor: bool = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to query the minor versions that you can upgrade to. Default value: true. Valid values:
        # 
        # *   true: The minor versions that you can upgrade to.
        # *   false: The major versions that you can upgrade to.
        self.minor = minor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.minor is not None:
            result['Minor'] = self.minor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Minor') is not None:
            self.minor = m.get('Minor')
        return self


class QueryUpgradableVersionsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[str] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed information about the failed permission verification.
        self.access_denied_detail = access_denied_detail
        # The versions that you can upgrade to.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class QueryUpgradableVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUpgradableVersionsResponseBody = None,
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
            temp_model = QueryUpgradableVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The instance ID.
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


class ReleaseInstanceResponseBody(TeaModel):
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
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class ReleaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstanceResponseBody = None,
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
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(
        self,
        fast_mode: bool = None,
        instance_id: str = None,
    ):
        # Specifies whether to restart compute nodes in quick restart mode. Default value: false. Valid values:
        # 
        # *   true: Compute nodes are restarted in quick restart mode in multiple batches. The batches are executed in parallel, and the nodes in each batch are restarted at the same time.
        # *   false: Compute nodes are restarted in rolling restart mode.
        self.fast_mode = fast_mode
        # The instance ID.
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
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RestartInstanceResponseBody(TeaModel):
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
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class RestartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartInstanceResponseBody = None,
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
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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


class UnTagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UnTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_key_shrink: str = None,
    ):
        self.all = all
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink
        # This parameter is required.
        self.resource_type = resource_type
        self.tag_key_shrink = tag_key_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id_shrink is not None:
            result['ResourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key_shrink is not None:
            result['TagKey'] = self.tag_key_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id_shrink = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key_shrink = m.get('TagKey')
        return self


class UnTagResourcesResponseBody(TeaModel):
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


class UnTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnTagResourcesResponseBody = None,
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
            temp_model = UnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceNameRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        instance_id: str = None,
    ):
        # The new name of the instance.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The instance ID.
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
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class UpgradeVersionRequest(TeaModel):
    def __init__(
        self,
        fast_mode: bool = None,
        instance_id: str = None,
        minor: bool = None,
        target_version: str = None,
    ):
        self.fast_mode = fast_mode
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the minor version is upgraded. Default value: true. Valid values:
        # 
        # *   true: The minor version is upgraded.
        # *   false: The major version is upgraded.
        self.minor = minor
        # The version to which you want to upgrade.
        # 
        # This parameter is required.
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.minor is not None:
            result['Minor'] = self.minor
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Minor') is not None:
            self.minor = m.get('Minor')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        return self


class UpgradeVersionResponseBody(TeaModel):
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
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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


class UpgradeVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeVersionResponseBody = None,
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
            temp_model = UpgradeVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


