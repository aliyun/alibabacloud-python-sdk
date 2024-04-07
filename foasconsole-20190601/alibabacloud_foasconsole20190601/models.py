# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        resource_spec: ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec = None,
    ):
        self.namespace = namespace
        self.resource_spec = resource_spec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ResourceSpec') is not None:
            temp_model = ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ConvertInstanceRequestConvertPostpayInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        is_auto_renew: bool = None,
        namespace_resource_specs: List[ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs] = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.is_auto_renew = is_auto_renew
        self.namespace_resource_specs = namespace_resource_specs
        self.pricing_cycle = pricing_cycle
        self.region = region

    def validate(self):
        if self.namespace_resource_specs:
            for k in self.namespace_resource_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        result['NamespaceResourceSpecs'] = []
        if self.namespace_resource_specs is not None:
            for k in self.namespace_resource_specs:
                result['NamespaceResourceSpecs'].append(k.to_map() if k else None)
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAutoRenew') is not None:
            self.is_auto_renew = m.get('IsAutoRenew')
        self.namespace_resource_specs = []
        if m.get('NamespaceResourceSpecs') is not None:
            for k in m.get('NamespaceResourceSpecs'):
                temp_model = ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs()
                self.namespace_resource_specs.append(temp_model.from_map(k))
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ConvertInstanceRequest(TeaModel):
    def __init__(
        self,
        convert_postpay_instance_request: ConvertInstanceRequestConvertPostpayInstanceRequest = None,
    ):
        self.convert_postpay_instance_request = convert_postpay_instance_request

    def validate(self):
        if self.convert_postpay_instance_request:
            self.convert_postpay_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_postpay_instance_request is not None:
            result['ConvertPostpayInstanceRequest'] = self.convert_postpay_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertPostpayInstanceRequest') is not None:
            temp_model = ConvertInstanceRequestConvertPostpayInstanceRequest()
            self.convert_postpay_instance_request = temp_model.from_map(m['ConvertPostpayInstanceRequest'])
        return self


class ConvertInstanceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConvertInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConvertInstanceResponseBody = None,
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
            temp_model = ConvertInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertPrepayInstanceRequestConvertPrepayInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
    ):
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ConvertPrepayInstanceRequest(TeaModel):
    def __init__(
        self,
        convert_prepay_instance_request: ConvertPrepayInstanceRequestConvertPrepayInstanceRequest = None,
    ):
        self.convert_prepay_instance_request = convert_prepay_instance_request

    def validate(self):
        if self.convert_prepay_instance_request:
            self.convert_prepay_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_prepay_instance_request is not None:
            result['ConvertPrepayInstanceRequest'] = self.convert_prepay_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertPrepayInstanceRequest') is not None:
            temp_model = ConvertPrepayInstanceRequestConvertPrepayInstanceRequest()
            self.convert_prepay_instance_request = temp_model.from_map(m['ConvertPrepayInstanceRequest'])
        return self


class ConvertPrepayInstanceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConvertPrepayInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConvertPrepayInstanceResponseBody = None,
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
            temp_model = ConvertPrepayInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestCreateInstanceRequestHaResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class CreateInstanceRequestCreateInstanceRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class CreateInstanceRequestCreateInstanceRequestStorageOss(TeaModel):
    def __init__(
        self,
        bucket: str = None,
    ):
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class CreateInstanceRequestCreateInstanceRequestStorage(TeaModel):
    def __init__(
        self,
        oss: CreateInstanceRequestCreateInstanceRequestStorageOss = None,
    ):
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Oss') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequestStorageOss()
            self.oss = temp_model.from_map(m['Oss'])
        return self


class CreateInstanceRequestCreateInstanceRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec: CreateInstanceRequestCreateInstanceRequestHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_zone_id: str = None,
        instance_name: str = None,
        monitor_type: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_spec: CreateInstanceRequestCreateInstanceRequestResourceSpec = None,
        storage: CreateInstanceRequestCreateInstanceRequestStorage = None,
        use_promotion_code: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.auto_renew = auto_renew
        self.charge_type = charge_type
        self.duration = duration
        self.extra = extra
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_zone_id = ha_zone_id
        self.instance_name = instance_name
        self.monitor_type = monitor_type
        self.pricing_cycle = pricing_cycle
        self.promotion_code = promotion_code
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_spec = resource_spec
        self.storage = storage
        self.use_promotion_code = use_promotion_code
        self.v_switch_ids = v_switch_ids
        # VPC ID。
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()
        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids
        if self.ha_zone_id is not None:
            result['HaZoneId'] = self.ha_zone_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m['HaResourceSpec'])
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')
        if m.get('HaZoneId') is not None:
            self.ha_zone_id = m.get('HaZoneId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceSpec') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('Storage') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequestStorage()
            self.storage = temp_model.from_map(m['Storage'])
        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        create_instance_request: CreateInstanceRequestCreateInstanceRequest = None,
    ):
        self.create_instance_request = create_instance_request

    def validate(self):
        if self.create_instance_request:
            self.create_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_instance_request is not None:
            result['CreateInstanceRequest'] = self.create_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateInstanceRequest') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequest()
            self.create_instance_request = temp_model.from_map(m['CreateInstanceRequest'])
        return self


class CreateInstanceResponseBodyOrderInfo(TeaModel):
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


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        order_info: CreateInstanceResponseBodyOrderInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.order_info = order_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.order_info:
            self.order_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderInfo') is not None:
            temp_model = CreateInstanceResponseBodyOrderInfo()
            self.order_info = temp_model.from_map(m['OrderInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class CreateNamespaceRequestCreateNamespaceRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class CreateNamespaceRequestCreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
        resource_spec: CreateNamespaceRequestCreateNamespaceRequestResourceSpec = None,
    ):
        self.ha = ha
        self.instance_id = instance_id
        self.namespace = namespace
        self.region = region
        self.resource_spec = resource_spec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = CreateNamespaceRequestCreateNamespaceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        create_namespace_request: CreateNamespaceRequestCreateNamespaceRequest = None,
    ):
        self.create_namespace_request = create_namespace_request

    def validate(self):
        if self.create_namespace_request:
            self.create_namespace_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_namespace_request is not None:
            result['CreateNamespaceRequest'] = self.create_namespace_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateNamespaceRequest') is not None:
            temp_model = CreateNamespaceRequestCreateNamespaceRequest()
            self.create_namespace_request = temp_model.from_map(m['CreateNamespaceRequest'])
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNamespaceResponseBody = None,
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequestDeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
    ):
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        delete_instance_request: DeleteInstanceRequestDeleteInstanceRequest = None,
    ):
        self.delete_instance_request = delete_instance_request

    def validate(self):
        if self.delete_instance_request:
            self.delete_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_instance_request is not None:
            result['DeleteInstanceRequest'] = self.delete_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteInstanceRequest') is not None:
            temp_model = DeleteInstanceRequestDeleteInstanceRequest()
            self.delete_instance_request = temp_model.from_map(m['DeleteInstanceRequest'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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


class DeleteNamespaceRequestDeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
    ):
        self.instance_id = instance_id
        self.namespace = namespace
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        delete_namespace_request: DeleteNamespaceRequestDeleteNamespaceRequest = None,
    ):
        self.delete_namespace_request = delete_namespace_request

    def validate(self):
        if self.delete_namespace_request:
            self.delete_namespace_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_namespace_request is not None:
            result['DeleteNamespaceRequest'] = self.delete_namespace_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteNamespaceRequest') is not None:
            temp_model = DeleteNamespaceRequestDeleteNamespaceRequest()
            self.delete_namespace_request = temp_model.from_map(m['DeleteNamespaceRequest'])
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNamespaceResponseBody = None,
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
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestDescribeInstancesRequestTags(TeaModel):
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


class DescribeInstancesRequestDescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        charge_type: str = None,
        instance_id: str = None,
        page_index: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
        tags: List[DescribeInstancesRequestDescribeInstancesRequestTags] = None,
    ):
        self.architecture_type = architecture_type
        self.charge_type = charge_type
        self.instance_id = instance_id
        self.page_index = page_index
        self.page_size = page_size
        self.region = region
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeInstancesRequestDescribeInstancesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        describe_instances_request: DescribeInstancesRequestDescribeInstancesRequest = None,
    ):
        self.describe_instances_request = describe_instances_request

    def validate(self):
        if self.describe_instances_request:
            self.describe_instances_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.describe_instances_request is not None:
            result['DescribeInstancesRequest'] = self.describe_instances_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescribeInstancesRequest') is not None:
            temp_model = DescribeInstancesRequestDescribeInstancesRequest()
            self.describe_instances_request = temp_model.from_map(m['DescribeInstancesRequest'])
        return self


class DescribeInstancesResponseBodyInstancesHaResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class DescribeInstancesResponseBodyInstancesHostAliases(TeaModel):
    def __init__(
        self,
        host_names: List[str] = None,
        ip: str = None,
    ):
        self.host_names = host_names
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_names is not None:
            result['HostNames'] = self.host_names
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostNames') is not None:
            self.host_names = m.get('HostNames')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeInstancesResponseBodyInstancesResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class DescribeInstancesResponseBodyInstancesStorageOss(TeaModel):
    def __init__(
        self,
        bucket: str = None,
    ):
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class DescribeInstancesResponseBodyInstancesStorage(TeaModel):
    def __init__(
        self,
        oss: DescribeInstancesResponseBodyInstancesStorageOss = None,
    ):
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Oss') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesStorageOss()
            self.oss = temp_model.from_map(m['Oss'])
        return self


class DescribeInstancesResponseBodyInstancesTags(TeaModel):
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


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        ask_cluster_id: str = None,
        charge_type: str = None,
        cluster_status: str = None,
        ha: bool = None,
        ha_resource_spec: DescribeInstancesResponseBodyInstancesHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_zone_id: str = None,
        host_aliases: List[DescribeInstancesResponseBodyInstancesHostAliases] = None,
        instance_id: str = None,
        instance_name: str = None,
        monitor_type: str = None,
        order_state: str = None,
        region: str = None,
        resource_create_time: int = None,
        resource_expired_time: int = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_spec: DescribeInstancesResponseBodyInstancesResourceSpec = None,
        storage: DescribeInstancesResponseBodyInstancesStorage = None,
        tags: List[DescribeInstancesResponseBodyInstancesTags] = None,
        uid: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.ask_cluster_id = ask_cluster_id
        self.charge_type = charge_type
        self.cluster_status = cluster_status
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_zone_id = ha_zone_id
        self.host_aliases = host_aliases
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.monitor_type = monitor_type
        self.order_state = order_state
        self.region = region
        self.resource_create_time = resource_create_time
        self.resource_expired_time = resource_expired_time
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_spec = resource_spec
        self.storage = storage
        self.tags = tags
        self.uid = uid
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.host_aliases:
            for k in self.host_aliases:
                if k:
                    k.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.ask_cluster_id is not None:
            result['AskClusterId'] = self.ask_cluster_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()
        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids
        if self.ha_zone_id is not None:
            result['HaZoneId'] = self.ha_zone_id
        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k in self.host_aliases:
                result['HostAliases'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.order_state is not None:
            result['OrderState'] = self.order_state
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.resource_expired_time is not None:
            result['ResourceExpiredTime'] = self.resource_expired_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('AskClusterId') is not None:
            self.ask_cluster_id = m.get('AskClusterId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m['HaResourceSpec'])
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')
        if m.get('HaZoneId') is not None:
            self.ha_zone_id = m.get('HaZoneId')
        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k in m.get('HostAliases'):
                temp_model = DescribeInstancesResponseBodyInstancesHostAliases()
                self.host_aliases.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('OrderState') is not None:
            self.order_state = m.get('OrderState')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('ResourceExpiredTime') is not None:
            self.resource_expired_time = m.get('ResourceExpiredTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceSpec') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('Storage') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesStorage()
            self.storage = temp_model.from_map(m['Storage'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeInstancesResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.instances = instances
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
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


class DescribeNamespacesRequestDescribeNamespacesRequestTags(TeaModel):
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


class DescribeNamespacesRequestDescribeNamespacesRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        page_index: int = None,
        page_size: int = None,
        region: str = None,
        tags: List[DescribeNamespacesRequestDescribeNamespacesRequestTags] = None,
    ):
        self.ha = ha
        self.instance_id = instance_id
        self.namespace = namespace
        self.page_index = page_index
        self.page_size = page_size
        self.region = region
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeNamespacesRequestDescribeNamespacesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeNamespacesRequest(TeaModel):
    def __init__(
        self,
        describe_namespaces_request: DescribeNamespacesRequestDescribeNamespacesRequest = None,
    ):
        self.describe_namespaces_request = describe_namespaces_request

    def validate(self):
        if self.describe_namespaces_request:
            self.describe_namespaces_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.describe_namespaces_request is not None:
            result['DescribeNamespacesRequest'] = self.describe_namespaces_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescribeNamespacesRequest') is not None:
            temp_model = DescribeNamespacesRequestDescribeNamespacesRequest()
            self.describe_namespaces_request = temp_model.from_map(m['DescribeNamespacesRequest'])
        return self


class DescribeNamespacesResponseBodyNamespacesResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class DescribeNamespacesResponseBodyNamespacesResourceUsed(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        cu: float = None,
        memory_gb: float = None,
    ):
        self.cpu = cpu
        self.cu = cu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cu is not None:
            result['Cu'] = self.cu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class DescribeNamespacesResponseBodyNamespacesTags(TeaModel):
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


class DescribeNamespacesResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        ha: bool = None,
        namespace: str = None,
        resource_spec: DescribeNamespacesResponseBodyNamespacesResourceSpec = None,
        resource_used: DescribeNamespacesResponseBodyNamespacesResourceUsed = None,
        status: str = None,
        tags: List[DescribeNamespacesResponseBodyNamespacesTags] = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.ha = ha
        self.namespace = namespace
        self.resource_spec = resource_spec
        self.resource_used = resource_used
        self.status = status
        self.tags = tags

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()
        if self.resource_used:
            self.resource_used.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.resource_used is not None:
            result['ResourceUsed'] = self.resource_used.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ResourceSpec') is not None:
            temp_model = DescribeNamespacesResponseBodyNamespacesResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('ResourceUsed') is not None:
            temp_model = DescribeNamespacesResponseBodyNamespacesResourceUsed()
            self.resource_used = temp_model.from_map(m['ResourceUsed'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeNamespacesResponseBodyNamespacesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        namespaces: List[DescribeNamespacesResponseBodyNamespaces] = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.namespaces = namespaces
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = DescribeNamespacesResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNamespacesResponseBody = None,
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
            temp_model = DescribeNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSupportedRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: str = None,
        region_name: str = None,
    ):
        self.region = region
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeSupportedRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeSupportedRegionsResponseBodyRegions] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.regions = regions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeSupportedRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSupportedRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSupportedRegionsResponseBody = None,
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
            temp_model = DescribeSupportedRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSupportedZonesRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        region: str = None,
    ):
        self.architecture_type = architecture_type
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeSupportedZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        zone_ids: List[str] = None,
    ):
        self.request_id = request_id
        self.success = success
        self.zone_ids = zone_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')
        return self


class DescribeSupportedZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSupportedZonesResponseBody = None,
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
            temp_model = DescribeSupportedZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        tag_reponse_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        # requestID。
        self.request_id = request_id
        self.success = success
        self.tag_reponse_id = tag_reponse_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tag_reponse_id is not None:
            result['TagReponseId'] = self.tag_reponse_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TagReponseId') is not None:
            self.tag_reponse_id = m.get('TagReponseId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
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


class ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestHaResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec: ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_zone_id: str = None,
        instance_id: str = None,
        region: str = None,
        resource_spec: ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestResourceSpec = None,
    ):
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_zone_id = ha_zone_id
        self.instance_id = instance_id
        self.region = region
        self.resource_spec = resource_spec

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()
        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids
        if self.ha_zone_id is not None:
            result['HaZoneId'] = self.ha_zone_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            temp_model = ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m['HaResourceSpec'])
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')
        if m.get('HaZoneId') is not None:
            self.ha_zone_id = m.get('HaZoneId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ModifyPrepayInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        modify_prepay_instance_spec_request: ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequest = None,
    ):
        self.modify_prepay_instance_spec_request = modify_prepay_instance_spec_request

    def validate(self):
        if self.modify_prepay_instance_spec_request:
            self.modify_prepay_instance_spec_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_prepay_instance_spec_request is not None:
            result['ModifyPrepayInstanceSpecRequest'] = self.modify_prepay_instance_spec_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyPrepayInstanceSpecRequest') is not None:
            temp_model = ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequest()
            self.modify_prepay_instance_spec_request = temp_model.from_map(m['ModifyPrepayInstanceSpecRequest'])
        return self


class ModifyPrepayInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyPrepayInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPrepayInstanceSpecResponseBody = None,
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
            temp_model = ModifyPrepayInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
        resource_spec: ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequestResourceSpec = None,
    ):
        self.instance_id = instance_id
        self.namespace = namespace
        self.region = region
        self.resource_spec = resource_spec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ModifyPrepayNamespaceSpecRequest(TeaModel):
    def __init__(
        self,
        modify_prepay_namespace_spec_request: ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequest = None,
    ):
        self.modify_prepay_namespace_spec_request = modify_prepay_namespace_spec_request

    def validate(self):
        if self.modify_prepay_namespace_spec_request:
            self.modify_prepay_namespace_spec_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_prepay_namespace_spec_request is not None:
            result['ModifyPrepayNamespaceSpecRequest'] = self.modify_prepay_namespace_spec_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyPrepayNamespaceSpecRequest') is not None:
            temp_model = ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequest()
            self.modify_prepay_namespace_spec_request = temp_model.from_map(m['ModifyPrepayNamespaceSpecRequest'])
        return self


class ModifyPrepayNamespaceSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyPrepayNamespaceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPrepayNamespaceSpecResponseBody = None,
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
            temp_model = ModifyPrepayNamespaceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        resource_spec: QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec = None,
    ):
        self.namespace = namespace
        self.resource_spec = resource_spec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ResourceSpec') is not None:
            temp_model = QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class QueryConvertInstancePriceRequestConvertPostpayInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        is_auto_renew: bool = None,
        namespace_resource_specs: List[QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs] = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.is_auto_renew = is_auto_renew
        self.namespace_resource_specs = namespace_resource_specs
        self.pricing_cycle = pricing_cycle
        self.region = region

    def validate(self):
        if self.namespace_resource_specs:
            for k in self.namespace_resource_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        result['NamespaceResourceSpecs'] = []
        if self.namespace_resource_specs is not None:
            for k in self.namespace_resource_specs:
                result['NamespaceResourceSpecs'].append(k.to_map() if k else None)
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAutoRenew') is not None:
            self.is_auto_renew = m.get('IsAutoRenew')
        self.namespace_resource_specs = []
        if m.get('NamespaceResourceSpecs') is not None:
            for k in m.get('NamespaceResourceSpecs'):
                temp_model = QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs()
                self.namespace_resource_specs.append(temp_model.from_map(k))
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryConvertInstancePriceRequest(TeaModel):
    def __init__(
        self,
        convert_postpay_instance_request: QueryConvertInstancePriceRequestConvertPostpayInstanceRequest = None,
    ):
        self.convert_postpay_instance_request = convert_postpay_instance_request

    def validate(self):
        if self.convert_postpay_instance_request:
            self.convert_postpay_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_postpay_instance_request is not None:
            result['ConvertPostpayInstanceRequest'] = self.convert_postpay_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertPostpayInstanceRequest') is not None:
            temp_model = QueryConvertInstancePriceRequestConvertPostpayInstanceRequest()
            self.convert_postpay_instance_request = temp_model.from_map(m['ConvertPostpayInstanceRequest'])
        return self


class QueryConvertInstancePriceResponseBodyPriceInfoDepreciateInfo(TeaModel):
    def __init__(
        self,
        cheap_rate: str = None,
        cheap_stand_amount: str = None,
        is_show: bool = None,
        month_price: str = None,
        original_stand_amount: str = None,
        start_time: str = None,
    ):
        self.cheap_rate = cheap_rate
        self.cheap_stand_amount = cheap_stand_amount
        self.is_show = is_show
        self.month_price = month_price
        self.original_stand_amount = original_stand_amount
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cheap_rate is not None:
            result['CheapRate'] = self.cheap_rate
        if self.cheap_stand_amount is not None:
            result['CheapStandAmount'] = self.cheap_stand_amount
        if self.is_show is not None:
            result['IsShow'] = self.is_show
        if self.month_price is not None:
            result['MonthPrice'] = self.month_price
        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')
        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')
        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')
        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')
        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions(TeaModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
        selected: bool = None,
    ):
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_no = promotion_option_no
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class QueryConvertInstancePriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class QueryConvertInstancePriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        currency: str = None,
        depreciate_info: QueryConvertInstancePriceResponseBodyPriceInfoDepreciateInfo = None,
        discount_amount: float = None,
        is_contract_activity: bool = None,
        message: str = None,
        optional_promotions: List[QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions] = None,
        original_amount: float = None,
        rules: List[QueryConvertInstancePriceResponseBodyPriceInfoRules] = None,
        stand_discount_price: str = None,
        stand_price: str = None,
        trade_amount: float = None,
    ):
        self.code = code
        self.currency = currency
        self.depreciate_info = depreciate_info
        self.discount_amount = discount_amount
        self.is_contract_activity = is_contract_activity
        self.message = message
        self.optional_promotions = optional_promotions
        self.original_amount = original_amount
        self.rules = rules
        self.stand_discount_price = stand_discount_price
        self.stand_price = stand_price
        self.trade_amount = trade_amount

    def validate(self):
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.optional_promotions:
            for k in self.optional_promotions:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity
        if self.message is not None:
            result['Message'] = self.message
        result['OptionalPromotions'] = []
        if self.optional_promotions is not None:
            for k in self.optional_promotions:
                result['OptionalPromotions'].append(k.to_map() if k else None)
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price
        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DepreciateInfo') is not None:
            temp_model = QueryConvertInstancePriceResponseBodyPriceInfoDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m['DepreciateInfo'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.optional_promotions = []
        if m.get('OptionalPromotions') is not None:
            for k in m.get('OptionalPromotions'):
                temp_model = QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions()
                self.optional_promotions.append(temp_model.from_map(k))
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = QueryConvertInstancePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')
        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class QueryConvertInstancePriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: QueryConvertInstancePriceResponseBodyPriceInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.price_info = price_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = QueryConvertInstancePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryConvertInstancePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryConvertInstancePriceResponseBody = None,
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
            temp_model = QueryConvertInstancePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConvertPrepayInstancePriceRequestConvertPrepayInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
    ):
        self.instance_id = instance_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryConvertPrepayInstancePriceRequest(TeaModel):
    def __init__(
        self,
        convert_prepay_instance_request: QueryConvertPrepayInstancePriceRequestConvertPrepayInstanceRequest = None,
    ):
        self.convert_prepay_instance_request = convert_prepay_instance_request

    def validate(self):
        if self.convert_prepay_instance_request:
            self.convert_prepay_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_prepay_instance_request is not None:
            result['ConvertPrepayInstanceRequest'] = self.convert_prepay_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertPrepayInstanceRequest') is not None:
            temp_model = QueryConvertPrepayInstancePriceRequestConvertPrepayInstanceRequest()
            self.convert_prepay_instance_request = temp_model.from_map(m['ConvertPrepayInstanceRequest'])
        return self


class QueryConvertPrepayInstancePriceResponseBodyPriceInfoDepreciateInfo(TeaModel):
    def __init__(
        self,
        cheap_rate: str = None,
        cheap_stand_amount: str = None,
        is_show: bool = None,
        month_price: str = None,
        original_stand_amount: str = None,
        start_time: str = None,
    ):
        self.cheap_rate = cheap_rate
        self.cheap_stand_amount = cheap_stand_amount
        self.is_show = is_show
        self.month_price = month_price
        self.original_stand_amount = original_stand_amount
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cheap_rate is not None:
            result['CheapRate'] = self.cheap_rate
        if self.cheap_stand_amount is not None:
            result['CheapStandAmount'] = self.cheap_stand_amount
        if self.is_show is not None:
            result['IsShow'] = self.is_show
        if self.month_price is not None:
            result['MonthPrice'] = self.month_price
        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')
        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')
        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')
        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')
        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryConvertPrepayInstancePriceResponseBodyPriceInfoOptionalPromotions(TeaModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
        selected: bool = None,
    ):
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_no = promotion_option_no
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class QueryConvertPrepayInstancePriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class QueryConvertPrepayInstancePriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        currency: str = None,
        depreciate_info: QueryConvertPrepayInstancePriceResponseBodyPriceInfoDepreciateInfo = None,
        discount_amount: float = None,
        is_contract_activity: bool = None,
        message: str = None,
        optional_promotions: List[QueryConvertPrepayInstancePriceResponseBodyPriceInfoOptionalPromotions] = None,
        original_amount: float = None,
        rules: List[QueryConvertPrepayInstancePriceResponseBodyPriceInfoRules] = None,
        stand_discount_price: str = None,
        stand_price: str = None,
        trade_amount: float = None,
    ):
        self.code = code
        self.currency = currency
        self.depreciate_info = depreciate_info
        self.discount_amount = discount_amount
        self.is_contract_activity = is_contract_activity
        self.message = message
        self.optional_promotions = optional_promotions
        self.original_amount = original_amount
        self.rules = rules
        self.stand_discount_price = stand_discount_price
        self.stand_price = stand_price
        self.trade_amount = trade_amount

    def validate(self):
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.optional_promotions:
            for k in self.optional_promotions:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity
        if self.message is not None:
            result['Message'] = self.message
        result['OptionalPromotions'] = []
        if self.optional_promotions is not None:
            for k in self.optional_promotions:
                result['OptionalPromotions'].append(k.to_map() if k else None)
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price
        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DepreciateInfo') is not None:
            temp_model = QueryConvertPrepayInstancePriceResponseBodyPriceInfoDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m['DepreciateInfo'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.optional_promotions = []
        if m.get('OptionalPromotions') is not None:
            for k in m.get('OptionalPromotions'):
                temp_model = QueryConvertPrepayInstancePriceResponseBodyPriceInfoOptionalPromotions()
                self.optional_promotions.append(temp_model.from_map(k))
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = QueryConvertPrepayInstancePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')
        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class QueryConvertPrepayInstancePriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: QueryConvertPrepayInstancePriceResponseBodyPriceInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.price_info = price_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = QueryConvertPrepayInstancePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryConvertPrepayInstancePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryConvertPrepayInstancePriceResponseBody = None,
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
            temp_model = QueryConvertPrepayInstancePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCreateInstancePriceRequestCreateInstanceRequestHaResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class QueryCreateInstancePriceRequestCreateInstanceRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class QueryCreateInstancePriceRequestCreateInstanceRequestStorageOss(TeaModel):
    def __init__(
        self,
        bucket: str = None,
    ):
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class QueryCreateInstancePriceRequestCreateInstanceRequestStorage(TeaModel):
    def __init__(
        self,
        oss: QueryCreateInstancePriceRequestCreateInstanceRequestStorageOss = None,
    ):
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Oss') is not None:
            temp_model = QueryCreateInstancePriceRequestCreateInstanceRequestStorageOss()
            self.oss = temp_model.from_map(m['Oss'])
        return self


class QueryCreateInstancePriceRequestCreateInstanceRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec: QueryCreateInstancePriceRequestCreateInstanceRequestHaResourceSpec = None,
        instance_name: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_spec: QueryCreateInstancePriceRequestCreateInstanceRequestResourceSpec = None,
        storage: QueryCreateInstancePriceRequestCreateInstanceRequestStorage = None,
        use_promotion_code: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.auto_renew = auto_renew
        self.charge_type = charge_type
        self.duration = duration
        self.extra = extra
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.instance_name = instance_name
        self.pricing_cycle = pricing_cycle
        self.promotion_code = promotion_code
        self.region = region
        self.resource_spec = resource_spec
        self.storage = storage
        self.use_promotion_code = use_promotion_code
        self.v_switch_ids = v_switch_ids
        # VPC ID。
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            temp_model = QueryCreateInstancePriceRequestCreateInstanceRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m['HaResourceSpec'])
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = QueryCreateInstancePriceRequestCreateInstanceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('Storage') is not None:
            temp_model = QueryCreateInstancePriceRequestCreateInstanceRequestStorage()
            self.storage = temp_model.from_map(m['Storage'])
        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class QueryCreateInstancePriceRequest(TeaModel):
    def __init__(
        self,
        create_instance_request: QueryCreateInstancePriceRequestCreateInstanceRequest = None,
    ):
        self.create_instance_request = create_instance_request

    def validate(self):
        if self.create_instance_request:
            self.create_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_instance_request is not None:
            result['CreateInstanceRequest'] = self.create_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateInstanceRequest') is not None:
            temp_model = QueryCreateInstancePriceRequestCreateInstanceRequest()
            self.create_instance_request = temp_model.from_map(m['CreateInstanceRequest'])
        return self


class QueryCreateInstancePriceResponseBodyPriceInfoDepreciateInfo(TeaModel):
    def __init__(
        self,
        cheap_rate: str = None,
        cheap_stand_amount: str = None,
        is_show: bool = None,
        month_price: str = None,
        original_stand_amount: str = None,
        start_time: str = None,
    ):
        self.cheap_rate = cheap_rate
        self.cheap_stand_amount = cheap_stand_amount
        self.is_show = is_show
        self.month_price = month_price
        self.original_stand_amount = original_stand_amount
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cheap_rate is not None:
            result['CheapRate'] = self.cheap_rate
        if self.cheap_stand_amount is not None:
            result['CheapStandAmount'] = self.cheap_stand_amount
        if self.is_show is not None:
            result['IsShow'] = self.is_show
        if self.month_price is not None:
            result['MonthPrice'] = self.month_price
        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')
        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')
        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')
        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')
        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryCreateInstancePriceResponseBodyPriceInfoOptionalPromotions(TeaModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
        selected: bool = None,
    ):
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_no = promotion_option_no
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class QueryCreateInstancePriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class QueryCreateInstancePriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        currency: str = None,
        depreciate_info: QueryCreateInstancePriceResponseBodyPriceInfoDepreciateInfo = None,
        discount_amount: float = None,
        is_contract_activity: bool = None,
        message: str = None,
        optional_promotions: List[QueryCreateInstancePriceResponseBodyPriceInfoOptionalPromotions] = None,
        original_amount: float = None,
        rules: List[QueryCreateInstancePriceResponseBodyPriceInfoRules] = None,
        stand_discount_price: str = None,
        stand_price: str = None,
        trade_amount: float = None,
    ):
        self.code = code
        self.currency = currency
        self.depreciate_info = depreciate_info
        self.discount_amount = discount_amount
        self.is_contract_activity = is_contract_activity
        self.message = message
        self.optional_promotions = optional_promotions
        self.original_amount = original_amount
        self.rules = rules
        self.stand_discount_price = stand_discount_price
        self.stand_price = stand_price
        self.trade_amount = trade_amount

    def validate(self):
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.optional_promotions:
            for k in self.optional_promotions:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity
        if self.message is not None:
            result['Message'] = self.message
        result['OptionalPromotions'] = []
        if self.optional_promotions is not None:
            for k in self.optional_promotions:
                result['OptionalPromotions'].append(k.to_map() if k else None)
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price
        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DepreciateInfo') is not None:
            temp_model = QueryCreateInstancePriceResponseBodyPriceInfoDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m['DepreciateInfo'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.optional_promotions = []
        if m.get('OptionalPromotions') is not None:
            for k in m.get('OptionalPromotions'):
                temp_model = QueryCreateInstancePriceResponseBodyPriceInfoOptionalPromotions()
                self.optional_promotions.append(temp_model.from_map(k))
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = QueryCreateInstancePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')
        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class QueryCreateInstancePriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: QueryCreateInstancePriceResponseBodyPriceInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.price_info = price_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = QueryCreateInstancePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCreateInstancePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCreateInstancePriceResponseBody = None,
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
            temp_model = QueryCreateInstancePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestHaResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec: QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_zone_id: str = None,
        instance_id: str = None,
        region: str = None,
        resource_spec: QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestResourceSpec = None,
    ):
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_zone_id = ha_zone_id
        self.instance_id = instance_id
        self.region = region
        self.resource_spec = resource_spec

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()
        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids
        if self.ha_zone_id is not None:
            result['HaZoneId'] = self.ha_zone_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            temp_model = QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m['HaResourceSpec'])
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')
        if m.get('HaZoneId') is not None:
            self.ha_zone_id = m.get('HaZoneId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class QueryModifyInstancePriceRequest(TeaModel):
    def __init__(
        self,
        modify_prepay_instance_spec_request: QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequest = None,
    ):
        self.modify_prepay_instance_spec_request = modify_prepay_instance_spec_request

    def validate(self):
        if self.modify_prepay_instance_spec_request:
            self.modify_prepay_instance_spec_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_prepay_instance_spec_request is not None:
            result['ModifyPrepayInstanceSpecRequest'] = self.modify_prepay_instance_spec_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyPrepayInstanceSpecRequest') is not None:
            temp_model = QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequest()
            self.modify_prepay_instance_spec_request = temp_model.from_map(m['ModifyPrepayInstanceSpecRequest'])
        return self


class QueryModifyInstancePriceResponseBodyPriceInfoDepreciateInfo(TeaModel):
    def __init__(
        self,
        cheap_rate: str = None,
        cheap_stand_amount: str = None,
        is_show: bool = None,
        month_price: str = None,
        original_stand_amount: str = None,
        start_time: str = None,
    ):
        self.cheap_rate = cheap_rate
        self.cheap_stand_amount = cheap_stand_amount
        self.is_show = is_show
        self.month_price = month_price
        self.original_stand_amount = original_stand_amount
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cheap_rate is not None:
            result['CheapRate'] = self.cheap_rate
        if self.cheap_stand_amount is not None:
            result['CheapStandAmount'] = self.cheap_stand_amount
        if self.is_show is not None:
            result['IsShow'] = self.is_show
        if self.month_price is not None:
            result['MonthPrice'] = self.month_price
        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')
        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')
        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')
        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')
        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryModifyInstancePriceResponseBodyPriceInfoOptionalPromotions(TeaModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
        selected: bool = None,
    ):
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_no = promotion_option_no
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class QueryModifyInstancePriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class QueryModifyInstancePriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        currency: str = None,
        depreciate_info: QueryModifyInstancePriceResponseBodyPriceInfoDepreciateInfo = None,
        discount_amount: float = None,
        is_contract_activity: bool = None,
        message: str = None,
        optional_promotions: List[QueryModifyInstancePriceResponseBodyPriceInfoOptionalPromotions] = None,
        original_amount: float = None,
        rules: List[QueryModifyInstancePriceResponseBodyPriceInfoRules] = None,
        stand_discount_price: str = None,
        stand_price: str = None,
        trade_amount: float = None,
    ):
        self.code = code
        self.currency = currency
        self.depreciate_info = depreciate_info
        self.discount_amount = discount_amount
        self.is_contract_activity = is_contract_activity
        self.message = message
        self.optional_promotions = optional_promotions
        self.original_amount = original_amount
        self.rules = rules
        self.stand_discount_price = stand_discount_price
        self.stand_price = stand_price
        self.trade_amount = trade_amount

    def validate(self):
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.optional_promotions:
            for k in self.optional_promotions:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity
        if self.message is not None:
            result['Message'] = self.message
        result['OptionalPromotions'] = []
        if self.optional_promotions is not None:
            for k in self.optional_promotions:
                result['OptionalPromotions'].append(k.to_map() if k else None)
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price
        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DepreciateInfo') is not None:
            temp_model = QueryModifyInstancePriceResponseBodyPriceInfoDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m['DepreciateInfo'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.optional_promotions = []
        if m.get('OptionalPromotions') is not None:
            for k in m.get('OptionalPromotions'):
                temp_model = QueryModifyInstancePriceResponseBodyPriceInfoOptionalPromotions()
                self.optional_promotions.append(temp_model.from_map(k))
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = QueryModifyInstancePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')
        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class QueryModifyInstancePriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: QueryModifyInstancePriceResponseBodyPriceInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.price_info = price_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = QueryModifyInstancePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryModifyInstancePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryModifyInstancePriceResponseBody = None,
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
            temp_model = QueryModifyInstancePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRenewInstancePriceRequestRenewInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.pricing_cycle = pricing_cycle
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryRenewInstancePriceRequest(TeaModel):
    def __init__(
        self,
        renew_instance_request: QueryRenewInstancePriceRequestRenewInstanceRequest = None,
    ):
        self.renew_instance_request = renew_instance_request

    def validate(self):
        if self.renew_instance_request:
            self.renew_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.renew_instance_request is not None:
            result['RenewInstanceRequest'] = self.renew_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenewInstanceRequest') is not None:
            temp_model = QueryRenewInstancePriceRequestRenewInstanceRequest()
            self.renew_instance_request = temp_model.from_map(m['RenewInstanceRequest'])
        return self


class QueryRenewInstancePriceResponseBodyPriceInfoDepreciateInfo(TeaModel):
    def __init__(
        self,
        cheap_rate: str = None,
        cheap_stand_amount: str = None,
        is_show: bool = None,
        month_price: str = None,
        original_stand_amount: str = None,
        start_time: str = None,
    ):
        self.cheap_rate = cheap_rate
        self.cheap_stand_amount = cheap_stand_amount
        self.is_show = is_show
        self.month_price = month_price
        self.original_stand_amount = original_stand_amount
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cheap_rate is not None:
            result['CheapRate'] = self.cheap_rate
        if self.cheap_stand_amount is not None:
            result['CheapStandAmount'] = self.cheap_stand_amount
        if self.is_show is not None:
            result['IsShow'] = self.is_show
        if self.month_price is not None:
            result['MonthPrice'] = self.month_price
        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')
        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')
        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')
        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')
        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryRenewInstancePriceResponseBodyPriceInfoOptionalPromotions(TeaModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
        selected: bool = None,
    ):
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_no = promotion_option_no
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class QueryRenewInstancePriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class QueryRenewInstancePriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        currency: str = None,
        depreciate_info: QueryRenewInstancePriceResponseBodyPriceInfoDepreciateInfo = None,
        discount_amount: float = None,
        is_contract_activity: bool = None,
        message: str = None,
        optional_promotions: List[QueryRenewInstancePriceResponseBodyPriceInfoOptionalPromotions] = None,
        original_amount: float = None,
        rules: List[QueryRenewInstancePriceResponseBodyPriceInfoRules] = None,
        stand_discount_price: str = None,
        stand_price: str = None,
        trade_amount: float = None,
    ):
        self.code = code
        self.currency = currency
        self.depreciate_info = depreciate_info
        self.discount_amount = discount_amount
        self.is_contract_activity = is_contract_activity
        self.message = message
        self.optional_promotions = optional_promotions
        self.original_amount = original_amount
        self.rules = rules
        self.stand_discount_price = stand_discount_price
        self.stand_price = stand_price
        self.trade_amount = trade_amount

    def validate(self):
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.optional_promotions:
            for k in self.optional_promotions:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity
        if self.message is not None:
            result['Message'] = self.message
        result['OptionalPromotions'] = []
        if self.optional_promotions is not None:
            for k in self.optional_promotions:
                result['OptionalPromotions'].append(k.to_map() if k else None)
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price
        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DepreciateInfo') is not None:
            temp_model = QueryRenewInstancePriceResponseBodyPriceInfoDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m['DepreciateInfo'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.optional_promotions = []
        if m.get('OptionalPromotions') is not None:
            for k in m.get('OptionalPromotions'):
                temp_model = QueryRenewInstancePriceResponseBodyPriceInfoOptionalPromotions()
                self.optional_promotions.append(temp_model.from_map(k))
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = QueryRenewInstancePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')
        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class QueryRenewInstancePriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: QueryRenewInstancePriceResponseBodyPriceInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.price_info = price_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = QueryRenewInstancePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRenewInstancePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRenewInstancePriceResponseBody = None,
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
            temp_model = QueryRenewInstancePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequestRenewInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.pricing_cycle = pricing_cycle
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        renew_instance_request: RenewInstanceRequestRenewInstanceRequest = None,
    ):
        self.renew_instance_request = renew_instance_request

    def validate(self):
        if self.renew_instance_request:
            self.renew_instance_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.renew_instance_request is not None:
            result['RenewInstanceRequest'] = self.renew_instance_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenewInstanceRequest') is not None:
            temp_model = RenewInstanceRequestRenewInstanceRequest()
            self.renew_instance_request = temp_model.from_map(m['RenewInstanceRequest'])
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
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
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tag_response_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.tag_response_id = tag_response_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tag_response_id is not None:
            result['TagResponseId'] = self.tag_response_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TagResponseId') is not None:
            self.tag_response_id = m.get('TagResponseId')
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


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
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


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tag_response_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.tag_response_id = tag_response_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tag_response_id is not None:
            result['TagResponseId'] = self.tag_response_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TagResponseId') is not None:
            self.tag_response_id = m.get('TagResponseId')
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


