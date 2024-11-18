# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        new_resource_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.new_resource_group_id = new_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.new_resource_group_id is not None:
            result['newResourceGroupId'] = self.new_resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('newResourceGroupId') is not None:
            self.new_resource_group_id = m.get('newResourceGroupId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CreateHoloWarehouseRequest(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        name: str = None,
    ):
        # The specifications of the virtual warehouse. The number of vCPUs must be an integer multiple of 16 CPUs. Minimum value: 16.
        # 
        # This parameter is required.
        self.cpu = cpu
        # The name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateHoloWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the request was successful. Valid values: true and false.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHoloWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHoloWarehouseResponseBody = None,
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
            temp_model = CreateHoloWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        charge_type: str = None,
        cold_storage_size: int = None,
        cpu: int = None,
        duration: int = None,
        enable_serverless_computing: bool = None,
        gateway_count: int = None,
        initial_databases: str = None,
        instance_name: str = None,
        instance_type: str = None,
        leader_instance_id: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_size: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable auto-payment. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        # 
        # > The default value is true. If the balance of your account is insufficient, you can set this parameter to false. In this case, an unpaid order is generated. You can log on to the User Center to pay for the order.
        self.auto_pay = auto_pay
        # Specifies whether to enable monthly auto-renewal. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        # 
        # > This parameter is invalid for shared instances. Shared instances have fixed specifications and are pay-as-you-go instances.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The infrequent access (IA) storage space of the instance. Unit: GB.
        # 
        # > This parameter is invalid for pay-as-you-go instances.
        self.cold_storage_size = cold_storage_size
        # The instance specifications. Valid values:
        # 
        # *   8-core 32 GB (number of compute nodes: 1)
        # *   16-core 64 GB (number of compute nodes: 1)
        # *   32-core 128 GB (number of compute nodes: 2)
        # *   64-core 256 GB (number of compute nodes: 4)
        # *   96-core 384 GB (number of compute nodes: 6)
        # *   128-core 512 GB (number of compute nodes: 8)
        # *   Others
        # 
        # > 
        # 
        # *   Set this parameter to the number of cores.
        # 
        # *   If you want to set this parameter to specifications with more than 1,024 compute units (CUs), you must submit a ticket.
        # 
        # *   If you want to purchase a shared instance, you do not need to configure this parameter.
        # 
        # *   The specifications of 8-core 32 GB (number of compute nodes: 1) are for trial use only and cannot be used for production.
        self.cpu = cpu
        # The validity period of the instance that you want to purchase. For example, you can specify a validity period of two months.
        # 
        # > You do not need to configure this parameter for pay-as-you-go instances.
        self.duration = duration
        self.enable_serverless_computing = enable_serverless_computing
        # The number of gateways. Valid values: 2 to 50.
        # 
        # > This parameter is required only for virtual warehouse instances.
        self.gateway_count = gateway_count
        self.initial_databases = initial_databases
        # The name of the Hologres instance that you want to purchase. The name must be 2 to 64 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The type of the instance. Valid values:
        # 
        # *   Standard: general-purpose instance
        # *   Follower: read-only secondary instance
        # *   Warehouse: virtual warehouse instance
        # *   Shared: shared instance
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The ID of the primary instance. This parameter is required for read-only secondary instances.
        # 
        # > The primary instance and secondary instances must meet the following requirements:
        # 
        # *   The primary instance is in the Running state.
        # 
        # *   The primary instance and secondary instances are deployed in the same region.
        # 
        # *   The primary instance and secondary instances are deployed in the same zone.
        # 
        # *   Less than 10 secondary instances are associated with the primary instance.
        # 
        # *   The primary and secondary instances belong to the same Alibaba Cloud account.
        self.leader_instance_id = leader_instance_id
        # The billing cycle. Valid values:
        # 
        # *   Month
        # *   Hour
        # 
        # > 
        # 
        # *   This parameter can only be set to Month for subscription instances.
        # 
        # *   This parameter can only be set to Hour for pay-as-you-go instances.
        # 
        # *   By default, this parameter is set to Hour for shared instances.
        self.pricing_cycle = pricing_cycle
        # The ID of the region. You can go to the [OpenAPI Explorer](https://api.aliyun.com/product/Hologram) or the Usage notes section to view the ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group. If you do not specify this parameter, the default resource group of the account is used.
        self.resource_group_id = resource_group_id
        # The standard storage space of the instance. Unit: GB.
        # 
        # > This parameter is invalid for pay-as-you-go instances.
        self.storage_size = storage_size
        # The ID of the vSwitch. The zone in which the vSwitch resides must be the same as the zone in which the instance resides.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC). The region in which the VPC resides must be the same as the region in which the Hologres instance resides.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the zone. For more information about how to obtain the ID of the zone, see the Usage notes section.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['autoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.cold_storage_size is not None:
            result['coldStorageSize'] = self.cold_storage_size
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.duration is not None:
            result['duration'] = self.duration
        if self.enable_serverless_computing is not None:
            result['enableServerlessComputing'] = self.enable_serverless_computing
        if self.gateway_count is not None:
            result['gatewayCount'] = self.gateway_count
        if self.initial_databases is not None:
            result['initialDatabases'] = self.initial_databases
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.leader_instance_id is not None:
            result['leaderInstanceId'] = self.leader_instance_id
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoPay') is not None:
            self.auto_pay = m.get('autoPay')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('coldStorageSize') is not None:
            self.cold_storage_size = m.get('coldStorageSize')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('enableServerlessComputing') is not None:
            self.enable_serverless_computing = m.get('enableServerlessComputing')
        if m.get('gatewayCount') is not None:
            self.gateway_count = m.get('gatewayCount')
        if m.get('initialDatabases') is not None:
            self.initial_databases = m.get('initialDatabases')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('leaderInstanceId') is not None:
            self.leader_instance_id = m.get('leaderInstanceId')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class CreateInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        order_id: str = None,
        success: str = None,
    ):
        # The error code returned.
        self.code = code
        # The instance ID.
        self.instance_id = instance_id
        # The error details.
        self.message = message
        # The order ID.
        self.order_id = order_id
        # Indicates whether the instance was created.
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateInstanceResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHoloWarehouseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteHoloWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the request was successful. Valid values: true and false.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHoloWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHoloWarehouseResponseBody = None,
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
            temp_model = DeleteHoloWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The ID of the region in which the Hologres instance resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result, which indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status Code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceResponseBody = None,
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableHiveAccessRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableHiveAccessResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableHiveAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableHiveAccessResponseBody = None,
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
            temp_model = DisableHiveAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableHiveAccessRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableHiveAccessResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableHiveAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableHiveAccessResponseBody = None,
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
            temp_model = EnableHiveAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyInstanceEndpoints(TeaModel):
    def __init__(
        self,
        alternative_endpoints: str = None,
        enabled: bool = None,
        endpoint: str = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
    ):
        # The endpoint. This parameter is returned if both the AnyTunnel and SingleTunnel modes are enabled for an instance, and the instance is switched from the AnyTunnel mode to the SingleTunnel mode. In this case, two endpoints are returned.
        self.alternative_endpoints = alternative_endpoints
        # Indicates whether the network is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enabled = enabled
        # The endpoint.
        self.endpoint = endpoint
        # The network type.
        # 
        # Valid values:
        # 
        # *   VPCSingleTunnel
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     virtual private cloud (VPC)
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Intranet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     internal network
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   VPCAnyTunnel
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     not supported by new instances
        # 
        #     <!-- -->
        # 
        # *   Internet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Internet
        # 
        #     <!-- -->
        # 
        #     .
        self.type = type
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the instance belongs.
        self.vpc_id = vpc_id
        # The ID of the instance that is deployed in the VPC.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alternative_endpoints is not None:
            result['AlternativeEndpoints'] = self.alternative_endpoints
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlternativeEndpoints') is not None:
            self.alternative_endpoints = m.get('AlternativeEndpoints')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class GetInstanceResponseBodyInstanceTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
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


class GetInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        auto_renewal: str = None,
        cold_storage: int = None,
        commodity_code: str = None,
        compute_node_count: int = None,
        cpu: int = None,
        creation_time: str = None,
        disk: str = None,
        enable_hive_access: str = None,
        enable_serverless: bool = None,
        endpoints: List[GetInstanceResponseBodyInstanceEndpoints] = None,
        expiration_time: str = None,
        gateway_count: int = None,
        gateway_cpu: int = None,
        gateway_memory: int = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_owner: str = None,
        instance_status: str = None,
        instance_type: str = None,
        leader_instance_id: str = None,
        memory: int = None,
        region_id: str = None,
        replica_role: str = None,
        resource_group_id: str = None,
        suspend_reason: str = None,
        tags: List[GetInstanceResponseBodyInstanceTags] = None,
        version: str = None,
        zone_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.auto_renewal = auto_renewal
        # The cold storage capacity of the instance. Unit: GB. Standard SSD is used for hot storage, and HDD is used for cold storage.
        self.cold_storage = cold_storage
        # The commodity code.
        # 
        # Valid values:
        # 
        # *   hologram_maxcomputeAccelerate_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Lakehouse Acceleration Edition
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_combo_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Subscription
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_prepay_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Subscription
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_storage_dp_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Storage plan
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_postpay_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_postpay_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Pay-as-you-go
        # 
        #     <!-- -->
        # 
        # *   hologram_maxcomputeAccelerate_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Lakehouse Acceleration Edition
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_cu_dp_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Compute plan
        # 
        #     <!-- -->
        self.commodity_code = commodity_code
        # The number of compute nodes. In a typical configuration, a node has 16 CPU cores and 32 GB of memory.
        self.compute_node_count = compute_node_count
        # The number of CPU cores.
        self.cpu = cpu
        # The time when the instance was created.
        self.creation_time = creation_time
        # The amount of data that can be stored in the disk of the Standard storage class. Unit: GB.
        self.disk = disk
        # Indicates whether data lake acceleration is enabled.
        self.enable_hive_access = enable_hive_access
        self.enable_serverless = enable_serverless
        # The list of endpoints.
        self.endpoints = endpoints
        # The expiration time. This parameter is invalid for pay-as-you-go instances.
        self.expiration_time = expiration_time
        # The number of gateway nodes.
        self.gateway_count = gateway_count
        # The number of CPU cores of the gateway. Unit: core.
        self.gateway_cpu = gateway_cpu
        # The size of memory resources of the gateway. Unit: GB.
        self.gateway_memory = gateway_memory
        # The billing method of the instance.
        # 
        # Valid values:
        # 
        # *   PostPaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   PrePaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     subscription
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_charge_type = instance_charge_type
        # The instance ID.
        self.instance_id = instance_id
        # The instance name. The instance name must be 2 to 64 characters in length.
        self.instance_name = instance_name
        # The owner of the instance.
        self.instance_owner = instance_owner
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Suspended
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Allocating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.instance_status = instance_status
        # The type of the instance.
        # 
        # Valid values:
        # 
        # *   Follower
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     read-only secondary instance
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     normal instance
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_type = instance_type
        # The ID of the primary instance.
        self.leader_instance_id = leader_instance_id
        # The memory size. Unit: GB.
        self.memory = memory
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        self.replica_role = replica_role
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The reason for the suspension.
        # 
        # Valid values:
        # 
        # *   Indebet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance has an overdue payment
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Manual
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance is manually suspended
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Overdue
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance has expired
        # 
        #     <!-- -->
        # 
        #     .
        self.suspend_reason = suspend_reason
        # The instance tag.
        self.tags = tags
        # The instance version.
        self.version = version
        # The ID of the zone where the instance resides.
        self.zone_id = zone_id

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.compute_node_count is not None:
            result['ComputeNodeCount'] = self.compute_node_count
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.enable_hive_access is not None:
            result['EnableHiveAccess'] = self.enable_hive_access
        if self.enable_serverless is not None:
            result['EnableServerless'] = self.enable_serverless
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        if self.gateway_count is not None:
            result['GatewayCount'] = self.gateway_count
        if self.gateway_cpu is not None:
            result['GatewayCpu'] = self.gateway_cpu
        if self.gateway_memory is not None:
            result['GatewayMemory'] = self.gateway_memory
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_owner is not None:
            result['InstanceOwner'] = self.instance_owner
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.leader_instance_id is not None:
            result['LeaderInstanceId'] = self.leader_instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_role is not None:
            result['ReplicaRole'] = self.replica_role
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.suspend_reason is not None:
            result['SuspendReason'] = self.suspend_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComputeNodeCount') is not None:
            self.compute_node_count = m.get('ComputeNodeCount')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('EnableHiveAccess') is not None:
            self.enable_hive_access = m.get('EnableHiveAccess')
        if m.get('EnableServerless') is not None:
            self.enable_serverless = m.get('EnableServerless')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = GetInstanceResponseBodyInstanceEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        if m.get('GatewayCount') is not None:
            self.gateway_count = m.get('GatewayCount')
        if m.get('GatewayCpu') is not None:
            self.gateway_cpu = m.get('GatewayCpu')
        if m.get('GatewayMemory') is not None:
            self.gateway_memory = m.get('GatewayMemory')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceOwner') is not None:
            self.instance_owner = m.get('InstanceOwner')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LeaderInstanceId') is not None:
            self.leader_instance_id = m.get('LeaderInstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaRole') is not None:
            self.replica_role = m.get('ReplicaRole')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SuspendReason') is not None:
            self.suspend_reason = m.get('SuspendReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetInstanceResponseBodyInstanceTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        instance: GetInstanceResponseBodyInstance = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code that is returned if the request failed.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The information about the instance.
        self.instance = instance
        # The request ID.
        self.request_id = request_id
        # The request result, which indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Instance') is not None:
            temp_model = GetInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWarehouseDetailResponseBodyWarehouseDetailWarehouseList(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        default_warehouse: bool = None,
        elastic_cpu: int = None,
        id: int = None,
        mem: int = None,
        name: str = None,
        node_count: int = None,
        rebalance_status: str = None,
        status: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        self.default_warehouse = default_warehouse
        self.elastic_cpu = elastic_cpu
        # The ID.
        self.id = id
        # The memory capacity.
        self.mem = mem
        # The name of the virtual warehouse instance.
        self.name = name
        # The number of compute nodes.
        self.node_count = node_count
        self.rebalance_status = rebalance_status
        # The status.
        # 
        # Valid values:
        # 
        # *   kRunning
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kSuspended
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kInit
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kAllocating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.default_warehouse is not None:
            result['DefaultWarehouse'] = self.default_warehouse
        if self.elastic_cpu is not None:
            result['ElasticCpu'] = self.elastic_cpu
        if self.id is not None:
            result['Id'] = self.id
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.name is not None:
            result['Name'] = self.name
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.rebalance_status is not None:
            result['RebalanceStatus'] = self.rebalance_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DefaultWarehouse') is not None:
            self.default_warehouse = m.get('DefaultWarehouse')
        if m.get('ElasticCpu') is not None:
            self.elastic_cpu = m.get('ElasticCpu')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('RebalanceStatus') is not None:
            self.rebalance_status = m.get('RebalanceStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetWarehouseDetailResponseBodyWarehouseDetail(TeaModel):
    def __init__(
        self,
        remaining_cpu: str = None,
        reserved_cpu: str = None,
        timed_elastic_cpu: str = None,
        warehouse_list: List[GetWarehouseDetailResponseBodyWarehouseDetailWarehouseList] = None,
    ):
        # The remaining unallocated computing resources of the virtual warehouse instance.
        self.remaining_cpu = remaining_cpu
        # The reserved computing resources. The amount of computing resources in all running virtual warehouses in an instance cannot exceed the amount of reserved computing resources in the virtual warehouses.
        self.reserved_cpu = reserved_cpu
        self.timed_elastic_cpu = timed_elastic_cpu
        # The list of virtual warehouses.
        self.warehouse_list = warehouse_list

    def validate(self):
        if self.warehouse_list:
            for k in self.warehouse_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remaining_cpu is not None:
            result['RemainingCpu'] = self.remaining_cpu
        if self.reserved_cpu is not None:
            result['ReservedCpu'] = self.reserved_cpu
        if self.timed_elastic_cpu is not None:
            result['TimedElasticCpu'] = self.timed_elastic_cpu
        result['WarehouseList'] = []
        if self.warehouse_list is not None:
            for k in self.warehouse_list:
                result['WarehouseList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemainingCpu') is not None:
            self.remaining_cpu = m.get('RemainingCpu')
        if m.get('ReservedCpu') is not None:
            self.reserved_cpu = m.get('ReservedCpu')
        if m.get('TimedElasticCpu') is not None:
            self.timed_elastic_cpu = m.get('TimedElasticCpu')
        self.warehouse_list = []
        if m.get('WarehouseList') is not None:
            for k in m.get('WarehouseList'):
                temp_model = GetWarehouseDetailResponseBodyWarehouseDetailWarehouseList()
                self.warehouse_list.append(temp_model.from_map(k))
        return self


class GetWarehouseDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        warehouse_detail: GetWarehouseDetailResponseBodyWarehouseDetail = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The values returned.
        self.warehouse_detail = warehouse_detail

    def validate(self):
        if self.warehouse_detail:
            self.warehouse_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.warehouse_detail is not None:
            result['WarehouseDetail'] = self.warehouse_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WarehouseDetail') is not None:
            temp_model = GetWarehouseDetailResponseBodyWarehouseDetail()
            self.warehouse_detail = temp_model.from_map(m['WarehouseDetail'])
        return self


class GetWarehouseDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWarehouseDetailResponseBody = None,
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
            temp_model = GetWarehouseDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBackupDataRequest(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        instance_id: str = None,
    ):
        self.backup_type = backup_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['backupType'] = self.backup_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backupType') is not None:
            self.backup_type = m.get('backupType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListBackupDataResponseBodyBackupDataList(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        cold_data_size: int = None,
        data_desc: str = None,
        data_gran: str = None,
        data_size: int = None,
        data_time: str = None,
        end_time: str = None,
        id: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_region: str = None,
        instance_type: str = None,
        instance_zone_id: str = None,
        snapshot_region: str = None,
        snapshot_zone_id: str = None,
        start_time: str = None,
        status: str = None,
        trigger_type: str = None,
    ):
        self.backup_type = backup_type
        self.cold_data_size = cold_data_size
        self.data_desc = data_desc
        self.data_gran = data_gran
        self.data_size = data_size
        self.data_time = data_time
        self.end_time = end_time
        self.id = id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_region = instance_region
        self.instance_type = instance_type
        self.instance_zone_id = instance_zone_id
        self.snapshot_region = snapshot_region
        self.snapshot_zone_id = snapshot_zone_id
        self.start_time = start_time
        self.status = status
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cold_data_size is not None:
            result['ColdDataSize'] = self.cold_data_size
        if self.data_desc is not None:
            result['DataDesc'] = self.data_desc
        if self.data_gran is not None:
            result['DataGran'] = self.data_gran
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_region is not None:
            result['InstanceRegion'] = self.instance_region
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_zone_id is not None:
            result['InstanceZoneId'] = self.instance_zone_id
        if self.snapshot_region is not None:
            result['SnapshotRegion'] = self.snapshot_region
        if self.snapshot_zone_id is not None:
            result['SnapshotZoneId'] = self.snapshot_zone_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ColdDataSize') is not None:
            self.cold_data_size = m.get('ColdDataSize')
        if m.get('DataDesc') is not None:
            self.data_desc = m.get('DataDesc')
        if m.get('DataGran') is not None:
            self.data_gran = m.get('DataGran')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceRegion') is not None:
            self.instance_region = m.get('InstanceRegion')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceZoneId') is not None:
            self.instance_zone_id = m.get('InstanceZoneId')
        if m.get('SnapshotRegion') is not None:
            self.snapshot_region = m.get('SnapshotRegion')
        if m.get('SnapshotZoneId') is not None:
            self.snapshot_zone_id = m.get('SnapshotZoneId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class ListBackupDataResponseBody(TeaModel):
    def __init__(
        self,
        backup_data_list: List[ListBackupDataResponseBodyBackupDataList] = None,
        request_id: str = None,
    ):
        self.backup_data_list = backup_data_list
        self.request_id = request_id

    def validate(self):
        if self.backup_data_list:
            for k in self.backup_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupDataList'] = []
        if self.backup_data_list is not None:
            for k in self.backup_data_list:
                result['BackupDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_data_list = []
        if m.get('BackupDataList') is not None:
            for k in m.get('BackupDataList'):
                temp_model = ListBackupDataResponseBodyBackupDataList()
                self.backup_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBackupDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBackupDataResponseBody = None,
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
            temp_model = ListBackupDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequestTag(TeaModel):
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


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        cms_instance_type: str = None,
        resource_group_id: str = None,
        tag: List[ListInstancesRequestTag] = None,
    ):
        self.cms_instance_type = cms_instance_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags to add to the resource.
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
        if self.cms_instance_type is not None:
            result['cmsInstanceType'] = self.cms_instance_type
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmsInstanceType') is not None:
            self.cms_instance_type = m.get('cmsInstanceType')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBodyInstanceListEndpoints(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        endpoint: str = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
    ):
        # Indicates whether the endpoint is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enabled = enabled
        # The endpoint.
        self.endpoint = endpoint
        # The network type.
        # 
        # Valid values:
        # 
        # *   VPCSingleTunnel
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     virtual private cloud (VPC)
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Intranet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     internal network
        # 
        #     <!-- -->
        # 
        # *   VPCAnyTunnel
        # 
        #     <!-- -->
        # 
        #     : This value is not supported by new instances
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Internet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Internet
        # 
        #     <!-- -->
        # 
        #     .
        self.type = type
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the VPC to which the instance belongs.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class ListInstancesResponseBodyInstanceListTags(TeaModel):
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


class ListInstancesResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        creation_time: str = None,
        enable_hive_access: str = None,
        endpoints: List[ListInstancesResponseBodyInstanceListEndpoints] = None,
        expiration_time: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        leader_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        suspend_reason: str = None,
        tags: List[ListInstancesResponseBodyInstanceListTags] = None,
        version: str = None,
        zone_id: str = None,
    ):
        # The commodity code, which is the same as that on the Billing Management page.
        self.commodity_code = commodity_code
        # The time when the cluster was created.
        self.creation_time = creation_time
        # Indicates whether lakehouse acceleration is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_hive_access = enable_hive_access
        # The list of endpoints.
        self.endpoints = endpoints
        # The time when the cluster expires.
        self.expiration_time = expiration_time
        # The billing method of the instance. Valid values:
        # 
        # Valid values:
        # 
        # *   PostPaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   PrePaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     subscription
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_charge_type = instance_charge_type
        # The instance ID.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Suspended
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Allocating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.instance_status = instance_status
        # The type of the instance.
        # 
        # Valid values:
        # 
        # *   Follower
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     read-only secondary instance
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     normal instance
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_type = instance_type
        # The ID of the primary instance.
        self.leader_instance_id = leader_instance_id
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The reason for the suspension.
        self.suspend_reason = suspend_reason
        # The tags that are added to the resource.
        self.tags = tags
        # The version of the cluster.
        self.version = version
        self.zone_id = zone_id

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.enable_hive_access is not None:
            result['EnableHiveAccess'] = self.enable_hive_access
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.leader_instance_id is not None:
            result['LeaderInstanceId'] = self.leader_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.suspend_reason is not None:
            result['SuspendReason'] = self.suspend_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EnableHiveAccess') is not None:
            self.enable_hive_access = m.get('EnableHiveAccess')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListInstancesResponseBodyInstanceListEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LeaderInstanceId') is not None:
            self.leader_instance_id = m.get('LeaderInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SuspendReason') is not None:
            self.suspend_reason = m.get('SuspendReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInstancesResponseBodyInstanceListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        instance_list: List[ListInstancesResponseBodyInstanceList] = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list of queried instances.
        self.instance_list = instance_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = ListInstancesResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class ListWarehousesResponseBodyWarehouseList(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        id: int = None,
        mem: int = None,
        name: str = None,
        node_count: int = None,
        status: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The ID.
        self.id = id
        # The memory capacity.
        self.mem = mem
        # The name of the virtual warehouse instance.
        self.name = name
        # The number of compute nodes.
        self.node_count = node_count
        # The status.
        # 
        # Valid values:
        # 
        # *   kRunning
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kSuspended
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kInit
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kAllocating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.id is not None:
            result['Id'] = self.id
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.name is not None:
            result['Name'] = self.name
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWarehousesResponseBody(TeaModel):
    def __init__(
        self,
        warehouse_list: List[ListWarehousesResponseBodyWarehouseList] = None,
        request_id: str = None,
    ):
        # The list of virtual warehouse instances.
        self.warehouse_list = warehouse_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.warehouse_list:
            for k in self.warehouse_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WarehouseList'] = []
        if self.warehouse_list is not None:
            for k in self.warehouse_list:
                result['WarehouseList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warehouse_list = []
        if m.get('WarehouseList') is not None:
            for k in m.get('WarehouseList'):
                temp_model = ListWarehousesResponseBodyWarehouseList()
                self.warehouse_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListWarehousesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWarehousesResponseBody = None,
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
            temp_model = ListWarehousesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebalanceHoloWarehouseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RebalanceHoloWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # Indicates whether the request was successful. Valid values: true and false.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebalanceHoloWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebalanceHoloWarehouseResponseBody = None,
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
            temp_model = RebalanceHoloWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameHoloWarehouseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        new_warehouse_name: str = None,
    ):
        # The original name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name
        # The new name of the virtual warehouse.
        # 
        # This parameter is required.
        self.new_warehouse_name = new_warehouse_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.new_warehouse_name is not None:
            result['newWarehouseName'] = self.new_warehouse_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('newWarehouseName') is not None:
            self.new_warehouse_name = m.get('newWarehouseName')
        return self


class RenameHoloWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the request was successful. Valid values: true and false.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenameHoloWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameHoloWarehouseResponseBody = None,
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
            temp_model = RenameHoloWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
    ):
        # Specifies whether to enable monthly auto-renewal. The default value is false. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  If you enable auto-renewal for an instance for which auto-renewal is enabled, an error is reported.
        self.auto_renew = auto_renew
        # The renewal duration. Unit: month.
        # 
        # This parameter is required.
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self


class RenewInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.code = code
        # The error details.
        self.message = message
        # The ID of the order.
        self.order_id = order_id
        # Indicates whether the renewal was successful.
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: RenewInstanceResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # The request result, which indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RenewInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewInstanceResponseBody = None,
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartHoloWarehouseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RestartHoloWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the request was successful. Valid values: true and false.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartHoloWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartHoloWarehouseResponseBody = None,
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
            temp_model = RestartHoloWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Indicates whether the operation was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # The request result, which indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class ResumeHoloWarehouseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ResumeHoloWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the request was successful. Valid values: true and false.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeHoloWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeHoloWarehouseResponseBody = None,
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
            temp_model = ResumeHoloWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result, which indicates whether the operation was successful.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # The request result, which indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeInstanceResponseBody = None,
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
            temp_model = ResumeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleHoloWarehouseRequest(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        name: str = None,
    ):
        # The specifications of the virtual warehouse. The number of vCPUs must be an integer multiple of 16.
        # 
        # This parameter is required.
        self.cpu = cpu
        # The name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ScaleHoloWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the request was successful. Valid values: true and false.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ScaleHoloWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScaleHoloWarehouseResponseBody = None,
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
            temp_model = ScaleHoloWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleInstanceRequest(TeaModel):
    def __init__(
        self,
        cold_storage_size: int = None,
        cpu: int = None,
        enable_serverless_computing: bool = None,
        gateway_count: int = None,
        scale_type: str = None,
        storage_size: int = None,
    ):
        # The infrequent access (IA) storage space of the instance. Unit: GB.
        # 
        # > Ignore this parameter for pay-as-you-go instances.
        self.cold_storage_size = cold_storage_size
        # The specifications of the instance. Valid values:
        # 
        # *   8-core 32GB (number of compute nodes: 1)
        # *   16-core 64GB (number of compute nodes: 1)
        # *   32-core 128GB (number of compute nodes: 2)
        # *   64-core 256GB (number of compute nodes: 4)
        # *   96-core 384GB (number of compute nodes: 6)
        # *   128-core 512GB (number of compute nodes: 8)
        # *   Others
        # 
        # > 
        # 
        # *   Set this parameter to the number of cores.
        # 
        # *   If you want to set this parameter to specifications with more than 1,024 compute units (CUs), you must submit a ticket.
        # 
        # *   This parameter is invalid for Hologres Shared Cluster instances.
        # 
        # *   The specifications of 8-core 32GB (number of compute nodes: 1) are for trial use only and cannot be used for production.
        self.cpu = cpu
        self.enable_serverless_computing = enable_serverless_computing
        # The number of gateways. Valid values: 2 to 50.
        # 
        # > This parameter is required only for virtual warehouse instances.
        self.gateway_count = gateway_count
        # The specification change type. Valid values:
        # 
        # *   UPGRADE
        # *   DOWNGRADE
        # 
        # > 
        # 
        # *   If you set this parameter to UPGRADE, the new specifications must be higher than the original specifications. You must configure at least one of the cpu, storageSize, and coldStorageSize parameters. If you leave a parameter empty, the related configuration remains unchanged.
        # 
        # *   If you set this parameter to DOWNGRADE, the new specifications must be lower than the original specifications. You must configure at least one of the cpu, storageSize, and coldStorageSize parameters. If you leave a parameter empty, the related configuration remains unchanged.
        # 
        # This parameter is required.
        self.scale_type = scale_type
        # The standard storage space of the instance. Unit: GB.
        # 
        # > Ignore this parameter for pay-as-you-go instances.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cold_storage_size is not None:
            result['coldStorageSize'] = self.cold_storage_size
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.enable_serverless_computing is not None:
            result['enableServerlessComputing'] = self.enable_serverless_computing
        if self.gateway_count is not None:
            result['gatewayCount'] = self.gateway_count
        if self.scale_type is not None:
            result['scaleType'] = self.scale_type
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('coldStorageSize') is not None:
            self.cold_storage_size = m.get('coldStorageSize')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('enableServerlessComputing') is not None:
            self.enable_serverless_computing = m.get('enableServerlessComputing')
        if m.get('gatewayCount') is not None:
            self.gateway_count = m.get('gatewayCount')
        if m.get('scaleType') is not None:
            self.scale_type = m.get('scaleType')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        return self


class ScaleInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.code = code
        # The error details.
        self.message = message
        # The ID of the order.
        self.order_id = order_id
        # Indicates whether the change to specifications was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScaleInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: ScaleInstanceResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ScaleInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ScaleInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScaleInstanceResponseBody = None,
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
            temp_model = ScaleInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result, which indicates whether the operation was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # The request result, which indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstanceResponseBody = None,
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendHoloWarehouseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class SuspendHoloWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # Indicates whether the request was successful. Valid values: true and false.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SuspendHoloWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SuspendHoloWarehouseResponseBody = None,
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
            temp_model = SuspendHoloWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceNameRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        # The new name of the instance.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        return self


class UpdateInstanceNameResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result, which indicates whether the operation was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # The request result, which indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class UpdateInstanceNetworkTypeRequest(TeaModel):
    def __init__(
        self,
        any_tunnel_to_single_tunnel: str = None,
        network_types: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_owner_id: str = None,
        vpc_region_id: str = None,
    ):
        # Specifies whether to change the network type from AnyTunnel to SingleTunnel. This parameter is invalid for new instances. For new instances, this parameter is set to null by default.
        # 
        # Valid values:
        # 
        # *   others/null
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.any_tunnel_to_single_tunnel = any_tunnel_to_single_tunnel
        # A list of network types that you want to enable. The list of enabled network types is randomly ordered. For example, the Internet, internal network, and VPCSingleTunnel network types are enabled. If you want to disable the Internet type, set this parameter to Intranet,VPCSingleTunnel.
        self.network_types = network_types
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the instance belongs.
        self.vpc_id = vpc_id
        # The owner ID of the VPC, which is the ID of the Alibaba Cloud account.
        self.vpc_owner_id = vpc_owner_id
        # The region ID of the VPC.
        self.vpc_region_id = vpc_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.any_tunnel_to_single_tunnel is not None:
            result['anyTunnelToSingleTunnel'] = self.any_tunnel_to_single_tunnel
        if self.network_types is not None:
            result['networkTypes'] = self.network_types
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['vpcOwnerId'] = self.vpc_owner_id
        if self.vpc_region_id is not None:
            result['vpcRegionId'] = self.vpc_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anyTunnelToSingleTunnel') is not None:
            self.any_tunnel_to_single_tunnel = m.get('anyTunnelToSingleTunnel')
        if m.get('networkTypes') is not None:
            self.network_types = m.get('networkTypes')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcOwnerId') is not None:
            self.vpc_owner_id = m.get('vpcOwnerId')
        if m.get('vpcRegionId') is not None:
            self.vpc_region_id = m.get('vpcRegionId')
        return self


class UpdateInstanceNetworkTypeResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result, which indicates whether the operation was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceNetworkTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceNetworkTypeResponseBody = None,
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
            temp_model = UpdateInstanceNetworkTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


