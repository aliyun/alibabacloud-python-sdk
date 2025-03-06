# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ConvertHybridInstanceRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class ConvertHybridInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        resource_spec: ConvertHybridInstanceRequestResourceSpec = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region
        # This parameter is required.
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
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = ConvertHybridInstanceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ConvertHybridInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec_shrink = resource_spec_shrink

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
        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')
        return self


class ConvertHybridInstanceResponseBodyOrderInfo(TeaModel):
    def __init__(
        self,
        elastic_instance_id: str = None,
        instance_id: str = None,
        order_id: int = None,
    ):
        self.elastic_instance_id = elastic_instance_id
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_instance_id is not None:
            result['ElasticInstanceId'] = self.elastic_instance_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticInstanceId') is not None:
            self.elastic_instance_id = m.get('ElasticInstanceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ConvertHybridInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        order_info: ConvertHybridInstanceResponseBodyOrderInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('OrderInfo') is not None:
            temp_model = ConvertHybridInstanceResponseBodyOrderInfo()
            self.order_info = temp_model.from_map(m['OrderInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConvertHybridInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConvertHybridInstanceResponseBody = None,
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
            temp_model = ConvertHybridInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertInstanceRequestNamespaceResourceSpecsResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class ConvertInstanceRequestNamespaceResourceSpecs(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        resource_spec: ConvertInstanceRequestNamespaceResourceSpecsResourceSpec = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
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
            temp_model = ConvertInstanceRequestNamespaceResourceSpecsResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ConvertInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        is_auto_renew: bool = None,
        namespace_resource_specs: List[ConvertInstanceRequestNamespaceResourceSpecs] = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.is_auto_renew = is_auto_renew
        # This parameter is required.
        self.namespace_resource_specs = namespace_resource_specs
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # This parameter is required.
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
                temp_model = ConvertInstanceRequestNamespaceResourceSpecs()
                self.namespace_resource_specs.append(temp_model.from_map(k))
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ConvertInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        is_auto_renew: bool = None,
        namespace_resource_specs_shrink: str = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.is_auto_renew = is_auto_renew
        # This parameter is required.
        self.namespace_resource_specs_shrink = namespace_resource_specs_shrink
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # This parameter is required.
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
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        if self.namespace_resource_specs_shrink is not None:
            result['NamespaceResourceSpecs'] = self.namespace_resource_specs_shrink
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
        if m.get('NamespaceResourceSpecs') is not None:
            self.namespace_resource_specs_shrink = m.get('NamespaceResourceSpecs')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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


class ConvertPrepayInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
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


class CreateInstanceRequestHaResourceSpec(TeaModel):
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


class CreateInstanceRequestResourceSpec(TeaModel):
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


class CreateInstanceRequestStorageOss(TeaModel):
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


class CreateInstanceRequestStorage(TeaModel):
    def __init__(
        self,
        fully_managed: bool = None,
        oss: CreateInstanceRequestStorageOss = None,
    ):
        self.fully_managed = fully_managed
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fully_managed is not None:
            result['FullyManaged'] = self.fully_managed
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullyManaged') is not None:
            self.fully_managed = m.get('FullyManaged')
        if m.get('Oss') is not None:
            temp_model = CreateInstanceRequestStorageOss()
            self.oss = temp_model.from_map(m['Oss'])
        return self


class CreateInstanceRequestTag(TeaModel):
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


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec: CreateInstanceRequestHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        instance_name: str = None,
        monitor_type: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_spec: CreateInstanceRequestResourceSpec = None,
        storage: CreateInstanceRequestStorage = None,
        tag: List[CreateInstanceRequestTag] = None,
        use_promotion_code: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.auto_renew = auto_renew
        # This parameter is required.
        self.charge_type = charge_type
        self.duration = duration
        self.extra = extra
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        # This parameter is required.
        self.instance_name = instance_name
        self.monitor_type = monitor_type
        self.pricing_cycle = pricing_cycle
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_spec = resource_spec
        # This parameter is required.
        self.storage = storage
        self.tag = tag
        self.use_promotion_code = use_promotion_code
        # This parameter is required.
        self.v_switch_ids = v_switch_ids
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
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
            temp_model = CreateInstanceRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m['HaResourceSpec'])
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')
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
            temp_model = CreateInstanceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('Storage') is not None:
            temp_model = CreateInstanceRequestStorage()
            self.storage = temp_model.from_map(m['Storage'])
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec_shrink: str = None,
        ha_vswitch_ids_shrink: str = None,
        instance_name: str = None,
        monitor_type: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_spec_shrink: str = None,
        storage_shrink: str = None,
        tag_shrink: str = None,
        use_promotion_code: bool = None,
        v_switch_ids_shrink: str = None,
        vpc_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.auto_renew = auto_renew
        # This parameter is required.
        self.charge_type = charge_type
        self.duration = duration
        self.extra = extra
        self.ha = ha
        self.ha_resource_spec_shrink = ha_resource_spec_shrink
        self.ha_vswitch_ids_shrink = ha_vswitch_ids_shrink
        # This parameter is required.
        self.instance_name = instance_name
        self.monitor_type = monitor_type
        self.pricing_cycle = pricing_cycle
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_spec_shrink = resource_spec_shrink
        # This parameter is required.
        self.storage_shrink = storage_shrink
        self.tag_shrink = tag_shrink
        self.use_promotion_code = use_promotion_code
        # This parameter is required.
        self.v_switch_ids_shrink = v_switch_ids_shrink
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

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
        if self.ha_resource_spec_shrink is not None:
            result['HaResourceSpec'] = self.ha_resource_spec_shrink
        if self.ha_vswitch_ids_shrink is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids_shrink
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
        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink
        if self.storage_shrink is not None:
            result['Storage'] = self.storage_shrink
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code
        if self.v_switch_ids_shrink is not None:
            result['VSwitchIds'] = self.v_switch_ids_shrink
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
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
            self.ha_resource_spec_shrink = m.get('HaResourceSpec')
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids_shrink = m.get('HaVSwitchIds')
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
            self.resource_spec_shrink = m.get('ResourceSpec')
        if m.get('Storage') is not None:
            self.storage_shrink = m.get('Storage')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids_shrink = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateInstanceResponseBodyOrderInfo(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: int = None,
        storage_instance_id: str = None,
        storage_order_id: int = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id
        self.storage_instance_id = storage_instance_id
        self.storage_order_id = storage_order_id

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
        if self.storage_instance_id is not None:
            result['StorageInstanceId'] = self.storage_instance_id
        if self.storage_order_id is not None:
            result['StorageOrderId'] = self.storage_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('StorageInstanceId') is not None:
            self.storage_instance_id = m.get('StorageInstanceId')
        if m.get('StorageOrderId') is not None:
            self.storage_order_id = m.get('StorageOrderId')
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


class CreateNamespaceRequestResourceSpec(TeaModel):
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


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
        resource_spec: CreateNamespaceRequestResourceSpec = None,
    ):
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
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
            temp_model = CreateNamespaceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class CreateNamespaceShrinkRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
    ):
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.region = region
        self.resource_spec_shrink = resource_spec_shrink

    def validate(self):
        pass

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
        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink
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
            self.resource_spec_shrink = m.get('ResourceSpec')
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


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
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


class DeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
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


class DescribeInstancesRequestTags(TeaModel):
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
        architecture_type: str = None,
        charge_type: str = None,
        instance_id: str = None,
        page_index: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
        tags: List[DescribeInstancesRequestTags] = None,
    ):
        self.architecture_type = architecture_type
        self.charge_type = charge_type
        self.instance_id = instance_id
        self.page_index = page_index
        self.page_size = page_size
        # This parameter is required.
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
                temp_model = DescribeInstancesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        charge_type: str = None,
        instance_id: str = None,
        page_index: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
    ):
        self.architecture_type = architecture_type
        self.charge_type = charge_type
        self.instance_id = instance_id
        self.page_index = page_index
        self.page_size = page_size
        # This parameter is required.
        self.region = region
        self.resource_group_id = resource_group_id
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

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
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
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
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class DescribeInstancesResponseBodyInstancesClusterStateClusterStageTotalStageWithWeight(TeaModel):
    def __init__(
        self,
        step_index: int = None,
        step_name: str = None,
        weight: int = None,
    ):
        self.step_index = step_index
        self.step_name = step_name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step_index is not None:
            result['StepIndex'] = self.step_index
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StepIndex') is not None:
            self.step_index = m.get('StepIndex')
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeInstancesResponseBodyInstancesClusterStateClusterStage(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_stage: int = None,
        message: str = None,
        status: str = None,
        total_stage_with_weight: List[DescribeInstancesResponseBodyInstancesClusterStateClusterStageTotalStageWithWeight] = None,
    ):
        self.cluster_id = cluster_id
        self.current_stage = current_stage
        self.message = message
        self.status = status
        self.total_stage_with_weight = total_stage_with_weight

    def validate(self):
        if self.total_stage_with_weight:
            for k in self.total_stage_with_weight:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.current_stage is not None:
            result['CurrentStage'] = self.current_stage
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        result['TotalStageWithWeight'] = []
        if self.total_stage_with_weight is not None:
            for k in self.total_stage_with_weight:
                result['TotalStageWithWeight'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.total_stage_with_weight = []
        if m.get('TotalStageWithWeight') is not None:
            for k in m.get('TotalStageWithWeight'):
                temp_model = DescribeInstancesResponseBodyInstancesClusterStateClusterStageTotalStageWithWeight()
                self.total_stage_with_weight.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesClusterStateUserSlbDtoUserSlbListeners(TeaModel):
    def __init__(
        self,
        listeners_status: str = None,
        port: str = None,
    ):
        self.listeners_status = listeners_status
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners_status is not None:
            result['ListenersStatus'] = self.listeners_status
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenersStatus') is not None:
            self.listeners_status = m.get('ListenersStatus')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeInstancesResponseBodyInstancesClusterStateUserSlbDto(TeaModel):
    def __init__(
        self,
        exist_slb: bool = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_status: str = None,
        user_slb_listeners: List[DescribeInstancesResponseBodyInstancesClusterStateUserSlbDtoUserSlbListeners] = None,
    ):
        self.exist_slb = exist_slb
        self.slb_id = slb_id
        self.slb_ip = slb_ip
        self.slb_status = slb_status
        self.user_slb_listeners = user_slb_listeners

    def validate(self):
        if self.user_slb_listeners:
            for k in self.user_slb_listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_slb is not None:
            result['ExistSlb'] = self.exist_slb
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_status is not None:
            result['SlbStatus'] = self.slb_status
        result['UserSlbListeners'] = []
        if self.user_slb_listeners is not None:
            for k in self.user_slb_listeners:
                result['UserSlbListeners'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistSlb') is not None:
            self.exist_slb = m.get('ExistSlb')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbStatus') is not None:
            self.slb_status = m.get('SlbStatus')
        self.user_slb_listeners = []
        if m.get('UserSlbListeners') is not None:
            for k in m.get('UserSlbListeners'):
                temp_model = DescribeInstancesResponseBodyInstancesClusterStateUserSlbDtoUserSlbListeners()
                self.user_slb_listeners.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesClusterState(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_stage: DescribeInstancesResponseBodyInstancesClusterStateClusterStage = None,
        create_timeout: bool = None,
        status: str = None,
        sub_status: str = None,
        url: str = None,
        user_slb_dto: DescribeInstancesResponseBodyInstancesClusterStateUserSlbDto = None,
        vpc_cidr: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_stage = cluster_stage
        self.create_timeout = create_timeout
        self.status = status
        self.sub_status = sub_status
        self.url = url
        self.user_slb_dto = user_slb_dto
        self.vpc_cidr = vpc_cidr

    def validate(self):
        if self.cluster_stage:
            self.cluster_stage.validate()
        if self.user_slb_dto:
            self.user_slb_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_stage is not None:
            result['ClusterStage'] = self.cluster_stage.to_map()
        if self.create_timeout is not None:
            result['CreateTimeout'] = self.create_timeout
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.url is not None:
            result['Url'] = self.url
        if self.user_slb_dto is not None:
            result['UserSlbDto'] = self.user_slb_dto.to_map()
        if self.vpc_cidr is not None:
            result['VpcCidr'] = self.vpc_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterStage') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesClusterStateClusterStage()
            self.cluster_stage = temp_model.from_map(m['ClusterStage'])
        if m.get('CreateTimeout') is not None:
            self.create_timeout = m.get('CreateTimeout')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserSlbDto') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesClusterStateUserSlbDto()
            self.user_slb_dto = temp_model.from_map(m['UserSlbDto'])
        if m.get('VpcCidr') is not None:
            self.vpc_cidr = m.get('VpcCidr')
        return self


class DescribeInstancesResponseBodyInstancesClusterUsedResources(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        elastic_used_cpu: float = None,
        elastic_used_memory: float = None,
        elastic_used_resource: float = None,
        guaranteed_used_cpu: float = None,
        guaranteed_used_memory: float = None,
        guaranteed_used_resource: float = None,
        ha: bool = None,
        ha_used_cpu: float = None,
        ha_used_memory: float = None,
        ha_used_resource: float = None,
        used_cpu: float = None,
        used_memory: float = None,
        used_resource: float = None,
    ):
        self.cluster_id = cluster_id
        self.elastic_used_cpu = elastic_used_cpu
        self.elastic_used_memory = elastic_used_memory
        self.elastic_used_resource = elastic_used_resource
        self.guaranteed_used_cpu = guaranteed_used_cpu
        self.guaranteed_used_memory = guaranteed_used_memory
        self.guaranteed_used_resource = guaranteed_used_resource
        self.ha = ha
        self.ha_used_cpu = ha_used_cpu
        self.ha_used_memory = ha_used_memory
        self.ha_used_resource = ha_used_resource
        self.used_cpu = used_cpu
        self.used_memory = used_memory
        self.used_resource = used_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.elastic_used_cpu is not None:
            result['ElasticUsedCpu'] = self.elastic_used_cpu
        if self.elastic_used_memory is not None:
            result['ElasticUsedMemory'] = self.elastic_used_memory
        if self.elastic_used_resource is not None:
            result['ElasticUsedResource'] = self.elastic_used_resource
        if self.guaranteed_used_cpu is not None:
            result['GuaranteedUsedCpu'] = self.guaranteed_used_cpu
        if self.guaranteed_used_memory is not None:
            result['GuaranteedUsedMemory'] = self.guaranteed_used_memory
        if self.guaranteed_used_resource is not None:
            result['GuaranteedUsedResource'] = self.guaranteed_used_resource
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_used_cpu is not None:
            result['HaUsedCpu'] = self.ha_used_cpu
        if self.ha_used_memory is not None:
            result['HaUsedMemory'] = self.ha_used_memory
        if self.ha_used_resource is not None:
            result['HaUsedResource'] = self.ha_used_resource
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        if self.used_resource is not None:
            result['UsedResource'] = self.used_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ElasticUsedCpu') is not None:
            self.elastic_used_cpu = m.get('ElasticUsedCpu')
        if m.get('ElasticUsedMemory') is not None:
            self.elastic_used_memory = m.get('ElasticUsedMemory')
        if m.get('ElasticUsedResource') is not None:
            self.elastic_used_resource = m.get('ElasticUsedResource')
        if m.get('GuaranteedUsedCpu') is not None:
            self.guaranteed_used_cpu = m.get('GuaranteedUsedCpu')
        if m.get('GuaranteedUsedMemory') is not None:
            self.guaranteed_used_memory = m.get('GuaranteedUsedMemory')
        if m.get('GuaranteedUsedResource') is not None:
            self.guaranteed_used_resource = m.get('GuaranteedUsedResource')
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaUsedCpu') is not None:
            self.ha_used_cpu = m.get('HaUsedCpu')
        if m.get('HaUsedMemory') is not None:
            self.ha_used_memory = m.get('HaUsedMemory')
        if m.get('HaUsedResource') is not None:
            self.ha_used_resource = m.get('HaUsedResource')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        if m.get('UsedResource') is not None:
            self.used_resource = m.get('UsedResource')
        return self


class DescribeInstancesResponseBodyInstancesClusterUsedStorage(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        used_storage: float = None,
    ):
        self.cluster_id = cluster_id
        self.used_storage = used_storage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.used_storage is not None:
            result['UsedStorage'] = self.used_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('UsedStorage') is not None:
            self.used_storage = m.get('UsedStorage')
        return self


class DescribeInstancesResponseBodyInstancesElasticResourceSpec(TeaModel):
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


class DescribeInstancesResponseBodyInstancesHaVSwitchInfo(TeaModel):
    def __init__(
        self,
        available_ip_address_count: int = None,
        description: str = None,
        region_id: str = None,
        v_switch_cidr: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.available_ip_address_count = available_ip_address_count
        self.description = description
        self.region_id = region_id
        self.v_switch_cidr = v_switch_cidr
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_cidr is not None:
            result['VSwitchCidr'] = self.v_switch_cidr
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchCidr') is not None:
            self.v_switch_cidr = m.get('VSwitchCidr')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesResponseBodyInstancesHostAliases(TeaModel):
    def __init__(
        self,
        host_names: List[str] = None,
        ip: str = None,
    ):
        # This parameter is required.
        self.host_names = host_names
        # This parameter is required.
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


class DescribeInstancesResponseBodyInstancesOssInfo(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_key: str = None,
        bucket: str = None,
        bucket_versioning_status: str = None,
        endpoint: str = None,
    ):
        self.access_id = access_id
        self.access_key = access_key
        self.bucket = bucket
        self.bucket_versioning_status = bucket_versioning_status
        self.endpoint = endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.bucket_versioning_status is not None:
            result['BucketVersioningStatus'] = self.bucket_versioning_status
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('BucketVersioningStatus') is not None:
            self.bucket_versioning_status = m.get('BucketVersioningStatus')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
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
        fully_managed: bool = None,
        order_state: str = None,
        oss: DescribeInstancesResponseBodyInstancesStorageOss = None,
    ):
        self.fully_managed = fully_managed
        self.order_state = order_state
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fully_managed is not None:
            result['FullyManaged'] = self.fully_managed
        if self.order_state is not None:
            result['OrderState'] = self.order_state
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullyManaged') is not None:
            self.fully_managed = m.get('FullyManaged')
        if m.get('OrderState') is not None:
            self.order_state = m.get('OrderState')
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


class DescribeInstancesResponseBodyInstancesVSwitchInfo(TeaModel):
    def __init__(
        self,
        available_ip_address_count: str = None,
        description: str = None,
        region_id: str = None,
        v_switch_cidr: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.available_ip_address_count = available_ip_address_count
        self.description = description
        self.region_id = region_id
        self.v_switch_cidr = v_switch_cidr
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_cidr is not None:
            result['VSwitchCidr'] = self.v_switch_cidr
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchCidr') is not None:
            self.v_switch_cidr = m.get('VSwitchCidr')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesResponseBodyInstancesVpcInfo(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        region_id: str = None,
        status: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.description = description
        self.region_id = region_id
        self.status = status
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        ansm: bool = None,
        architecture_type: str = None,
        ask_cluster_id: str = None,
        charge_type: str = None,
        cluster_state: DescribeInstancesResponseBodyInstancesClusterState = None,
        cluster_status: str = None,
        cluster_used_resources: DescribeInstancesResponseBodyInstancesClusterUsedResources = None,
        cluster_used_storage: DescribeInstancesResponseBodyInstancesClusterUsedStorage = None,
        elastic: bool = None,
        elastic_order_state: str = None,
        elastic_resource_spec: DescribeInstancesResponseBodyInstancesElasticResourceSpec = None,
        ha: bool = None,
        ha_resource_spec: DescribeInstancesResponseBodyInstancesHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_vswitch_info: List[DescribeInstancesResponseBodyInstancesHaVSwitchInfo] = None,
        ha_zone_id: str = None,
        host_aliases: List[DescribeInstancesResponseBodyInstancesHostAliases] = None,
        instance_id: str = None,
        instance_name: str = None,
        monitor_type: str = None,
        order_state: str = None,
        oss_info: DescribeInstancesResponseBodyInstancesOssInfo = None,
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
        v_switch_info: List[DescribeInstancesResponseBodyInstancesVSwitchInfo] = None,
        vpc_id: str = None,
        vpc_info: DescribeInstancesResponseBodyInstancesVpcInfo = None,
        zone_id: str = None,
    ):
        self.ansm = ansm
        self.architecture_type = architecture_type
        self.ask_cluster_id = ask_cluster_id
        self.charge_type = charge_type
        self.cluster_state = cluster_state
        self.cluster_status = cluster_status
        self.cluster_used_resources = cluster_used_resources
        self.cluster_used_storage = cluster_used_storage
        self.elastic = elastic
        self.elastic_order_state = elastic_order_state
        self.elastic_resource_spec = elastic_resource_spec
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_vswitch_info = ha_vswitch_info
        self.ha_zone_id = ha_zone_id
        # This parameter is required.
        self.host_aliases = host_aliases
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.monitor_type = monitor_type
        self.order_state = order_state
        self.oss_info = oss_info
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
        self.v_switch_info = v_switch_info
        self.vpc_id = vpc_id
        self.vpc_info = vpc_info
        self.zone_id = zone_id

    def validate(self):
        if self.cluster_state:
            self.cluster_state.validate()
        if self.cluster_used_resources:
            self.cluster_used_resources.validate()
        if self.cluster_used_storage:
            self.cluster_used_storage.validate()
        if self.elastic_resource_spec:
            self.elastic_resource_spec.validate()
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.ha_vswitch_info:
            for k in self.ha_vswitch_info:
                if k:
                    k.validate()
        if self.host_aliases:
            for k in self.host_aliases:
                if k:
                    k.validate()
        if self.oss_info:
            self.oss_info.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.v_switch_info:
            for k in self.v_switch_info:
                if k:
                    k.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ansm is not None:
            result['Ansm'] = self.ansm
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.ask_cluster_id is not None:
            result['AskClusterId'] = self.ask_cluster_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state.to_map()
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_used_resources is not None:
            result['ClusterUsedResources'] = self.cluster_used_resources.to_map()
        if self.cluster_used_storage is not None:
            result['ClusterUsedStorage'] = self.cluster_used_storage.to_map()
        if self.elastic is not None:
            result['Elastic'] = self.elastic
        if self.elastic_order_state is not None:
            result['ElasticOrderState'] = self.elastic_order_state
        if self.elastic_resource_spec is not None:
            result['ElasticResourceSpec'] = self.elastic_resource_spec.to_map()
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()
        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids
        result['HaVSwitchInfo'] = []
        if self.ha_vswitch_info is not None:
            for k in self.ha_vswitch_info:
                result['HaVSwitchInfo'].append(k.to_map() if k else None)
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
        if self.oss_info is not None:
            result['OssInfo'] = self.oss_info.to_map()
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
        result['VSwitchInfo'] = []
        if self.v_switch_info is not None:
            for k in self.v_switch_info:
                result['VSwitchInfo'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_info is not None:
            result['VpcInfo'] = self.vpc_info.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ansm') is not None:
            self.ansm = m.get('Ansm')
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('AskClusterId') is not None:
            self.ask_cluster_id = m.get('AskClusterId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterState') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesClusterState()
            self.cluster_state = temp_model.from_map(m['ClusterState'])
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterUsedResources') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesClusterUsedResources()
            self.cluster_used_resources = temp_model.from_map(m['ClusterUsedResources'])
        if m.get('ClusterUsedStorage') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesClusterUsedStorage()
            self.cluster_used_storage = temp_model.from_map(m['ClusterUsedStorage'])
        if m.get('Elastic') is not None:
            self.elastic = m.get('Elastic')
        if m.get('ElasticOrderState') is not None:
            self.elastic_order_state = m.get('ElasticOrderState')
        if m.get('ElasticResourceSpec') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesElasticResourceSpec()
            self.elastic_resource_spec = temp_model.from_map(m['ElasticResourceSpec'])
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m['HaResourceSpec'])
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')
        self.ha_vswitch_info = []
        if m.get('HaVSwitchInfo') is not None:
            for k in m.get('HaVSwitchInfo'):
                temp_model = DescribeInstancesResponseBodyInstancesHaVSwitchInfo()
                self.ha_vswitch_info.append(temp_model.from_map(k))
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
        if m.get('OssInfo') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesOssInfo()
            self.oss_info = temp_model.from_map(m['OssInfo'])
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
        self.v_switch_info = []
        if m.get('VSwitchInfo') is not None:
            for k in m.get('VSwitchInfo'):
                temp_model = DescribeInstancesResponseBodyInstancesVSwitchInfo()
                self.v_switch_info.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInfo') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesVpcInfo()
            self.vpc_info = temp_model.from_map(m['VpcInfo'])
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


class DescribeNamespacesRequestTags(TeaModel):
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


class DescribeNamespacesRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        page_index: int = None,
        page_size: int = None,
        region: str = None,
        tags: List[DescribeNamespacesRequestTags] = None,
    ):
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        self.namespace = namespace
        self.page_index = page_index
        self.page_size = page_size
        # This parameter is required.
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
                temp_model = DescribeNamespacesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeNamespacesShrinkRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        page_index: int = None,
        page_size: int = None,
        region: str = None,
        tags_shrink: str = None,
    ):
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        self.namespace = namespace
        self.page_index = page_index
        self.page_size = page_size
        # This parameter is required.
        self.region = region
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

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
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
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
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class DescribeNamespacesResponseBodyNamespacesElasticResourceSpec(TeaModel):
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


class DescribeNamespacesResponseBodyNamespacesGuaranteedResourceSpec(TeaModel):
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
        elastic_resource_spec: DescribeNamespacesResponseBodyNamespacesElasticResourceSpec = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        guaranteed_resource_spec: DescribeNamespacesResponseBodyNamespacesGuaranteedResourceSpec = None,
        ha: bool = None,
        namespace: str = None,
        resource_spec: DescribeNamespacesResponseBodyNamespacesResourceSpec = None,
        resource_used: DescribeNamespacesResponseBodyNamespacesResourceUsed = None,
        status: str = None,
        tags: List[DescribeNamespacesResponseBodyNamespacesTags] = None,
    ):
        self.elastic_resource_spec = elastic_resource_spec
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.guaranteed_resource_spec = guaranteed_resource_spec
        self.ha = ha
        self.namespace = namespace
        self.resource_spec = resource_spec
        self.resource_used = resource_used
        self.status = status
        self.tags = tags

    def validate(self):
        if self.elastic_resource_spec:
            self.elastic_resource_spec.validate()
        if self.guaranteed_resource_spec:
            self.guaranteed_resource_spec.validate()
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
        if self.elastic_resource_spec is not None:
            result['ElasticResourceSpec'] = self.elastic_resource_spec.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.guaranteed_resource_spec is not None:
            result['GuaranteedResourceSpec'] = self.guaranteed_resource_spec.to_map()
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
        if m.get('ElasticResourceSpec') is not None:
            temp_model = DescribeNamespacesResponseBodyNamespacesElasticResourceSpec()
            self.elastic_resource_spec = temp_model.from_map(m['ElasticResourceSpec'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GuaranteedResourceSpec') is not None:
            temp_model = DescribeNamespacesResponseBodyNamespacesGuaranteedResourceSpec()
            self.guaranteed_resource_spec = temp_model.from_map(m['GuaranteedResourceSpec'])
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
        description: str = None,
        extra: str = None,
        region: str = None,
        region_name: str = None,
    ):
        self.description = description
        self.extra = extra
        self.region = region
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.region is not None:
            result['Region'] = self.region
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeSupportedRegionsResponseBody(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        regions: List[DescribeSupportedRegionsResponseBodyRegions] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.regions = regions
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

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
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
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
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeSupportedRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
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
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
        zone_ids: List[str] = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page
        self.zone_ids = zone_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # This parameter is required.
        self.region_id = region_id
        self.resource_id = resource_id
        # This parameter is required.
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


class ModifyElasticResourceSpecRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class ModifyElasticResourceSpecRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        resource_spec: ModifyElasticResourceSpecRequestResourceSpec = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region
        # This parameter is required.
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
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = ModifyElasticResourceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ModifyElasticResourceSpecShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec_shrink = resource_spec_shrink

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
        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')
        return self


class ModifyElasticResourceSpecResponseBody(TeaModel):
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


class ModifyElasticResourceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyElasticResourceSpecResponseBody = None,
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
            temp_model = ModifyElasticResourceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVswitchRequest(TeaModel):
    def __init__(
        self,
        ha_vswitch_ids: List[str] = None,
        instance_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.ha_vswitch_ids = ha_vswitch_ids
        # This parameter is required.
        self.instance_id = instance_id
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class ModifyInstanceVswitchShrinkRequest(TeaModel):
    def __init__(
        self,
        ha_vswitch_ids_shrink: str = None,
        instance_id: str = None,
        v_switch_ids_shrink: str = None,
    ):
        self.ha_vswitch_ids_shrink = ha_vswitch_ids_shrink
        # This parameter is required.
        self.instance_id = instance_id
        self.v_switch_ids_shrink = v_switch_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ha_vswitch_ids_shrink is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.v_switch_ids_shrink is not None:
            result['VSwitchIds'] = self.v_switch_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids_shrink = m.get('HaVSwitchIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids_shrink = m.get('VSwitchIds')
        return self


class ModifyInstanceVswitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyInstanceVswitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceVswitchResponseBody = None,
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
            temp_model = ModifyInstanceVswitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNamespaceSpecV2RequestElasticResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class ModifyNamespaceSpecV2RequestGuaranteedResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class ModifyNamespaceSpecV2Request(TeaModel):
    def __init__(
        self,
        elastic_resource_spec: ModifyNamespaceSpecV2RequestElasticResourceSpec = None,
        guaranteed_resource_spec: ModifyNamespaceSpecV2RequestGuaranteedResourceSpec = None,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
    ):
        self.elastic_resource_spec = elastic_resource_spec
        self.guaranteed_resource_spec = guaranteed_resource_spec
        # This parameter is required.
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.region = region

    def validate(self):
        if self.elastic_resource_spec:
            self.elastic_resource_spec.validate()
        if self.guaranteed_resource_spec:
            self.guaranteed_resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_resource_spec is not None:
            result['ElasticResourceSpec'] = self.elastic_resource_spec.to_map()
        if self.guaranteed_resource_spec is not None:
            result['GuaranteedResourceSpec'] = self.guaranteed_resource_spec.to_map()
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticResourceSpec') is not None:
            temp_model = ModifyNamespaceSpecV2RequestElasticResourceSpec()
            self.elastic_resource_spec = temp_model.from_map(m['ElasticResourceSpec'])
        if m.get('GuaranteedResourceSpec') is not None:
            temp_model = ModifyNamespaceSpecV2RequestGuaranteedResourceSpec()
            self.guaranteed_resource_spec = temp_model.from_map(m['GuaranteedResourceSpec'])
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ModifyNamespaceSpecV2ShrinkRequest(TeaModel):
    def __init__(
        self,
        elastic_resource_spec_shrink: str = None,
        guaranteed_resource_spec_shrink: str = None,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
    ):
        self.elastic_resource_spec_shrink = elastic_resource_spec_shrink
        self.guaranteed_resource_spec_shrink = guaranteed_resource_spec_shrink
        # This parameter is required.
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_resource_spec_shrink is not None:
            result['ElasticResourceSpec'] = self.elastic_resource_spec_shrink
        if self.guaranteed_resource_spec_shrink is not None:
            result['GuaranteedResourceSpec'] = self.guaranteed_resource_spec_shrink
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticResourceSpec') is not None:
            self.elastic_resource_spec_shrink = m.get('ElasticResourceSpec')
        if m.get('GuaranteedResourceSpec') is not None:
            self.guaranteed_resource_spec_shrink = m.get('GuaranteedResourceSpec')
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ModifyNamespaceSpecV2ResponseBody(TeaModel):
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


class ModifyNamespaceSpecV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNamespaceSpecV2ResponseBody = None,
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
            temp_model = ModifyNamespaceSpecV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPrepayInstanceSpecRequestHaResourceSpec(TeaModel):
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


class ModifyPrepayInstanceSpecRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class ModifyPrepayInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec: ModifyPrepayInstanceSpecRequestHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_zone_id: str = None,
        instance_id: str = None,
        region: str = None,
        resource_spec: ModifyPrepayInstanceSpecRequestResourceSpec = None,
    ):
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_zone_id = ha_zone_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region
        # This parameter is required.
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
            temp_model = ModifyPrepayInstanceSpecRequestHaResourceSpec()
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
            temp_model = ModifyPrepayInstanceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ModifyPrepayInstanceSpecShrinkRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec_shrink: str = None,
        ha_vswitch_ids_shrink: str = None,
        ha_zone_id: str = None,
        instance_id: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
    ):
        self.ha = ha
        self.ha_resource_spec_shrink = ha_resource_spec_shrink
        self.ha_vswitch_ids_shrink = ha_vswitch_ids_shrink
        self.ha_zone_id = ha_zone_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec_shrink = resource_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_resource_spec_shrink is not None:
            result['HaResourceSpec'] = self.ha_resource_spec_shrink
        if self.ha_vswitch_ids_shrink is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids_shrink
        if self.ha_zone_id is not None:
            result['HaZoneId'] = self.ha_zone_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            self.ha_resource_spec_shrink = m.get('HaResourceSpec')
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids_shrink = m.get('HaVSwitchIds')
        if m.get('HaZoneId') is not None:
            self.ha_zone_id = m.get('HaZoneId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')
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


class ModifyPrepayNamespaceSpecRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class ModifyPrepayNamespaceSpecRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
        resource_spec: ModifyPrepayNamespaceSpecRequestResourceSpec = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.region = region
        # This parameter is required.
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
            temp_model = ModifyPrepayNamespaceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ModifyPrepayNamespaceSpecShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec_shrink = resource_spec_shrink

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
        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink
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
            self.resource_spec_shrink = m.get('ResourceSpec')
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


class QueryConvertInstancePriceRequestNamespaceResourceSpecsResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class QueryConvertInstancePriceRequestNamespaceResourceSpecs(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        resource_spec: QueryConvertInstancePriceRequestNamespaceResourceSpecsResourceSpec = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
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
            temp_model = QueryConvertInstancePriceRequestNamespaceResourceSpecsResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class QueryConvertInstancePriceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        is_auto_renew: bool = None,
        namespace_resource_specs: List[QueryConvertInstancePriceRequestNamespaceResourceSpecs] = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.is_auto_renew = is_auto_renew
        # This parameter is required.
        self.namespace_resource_specs = namespace_resource_specs
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # This parameter is required.
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
                temp_model = QueryConvertInstancePriceRequestNamespaceResourceSpecs()
                self.namespace_resource_specs.append(temp_model.from_map(k))
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryConvertInstancePriceShrinkRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        is_auto_renew: bool = None,
        namespace_resource_specs_shrink: str = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.is_auto_renew = is_auto_renew
        # This parameter is required.
        self.namespace_resource_specs_shrink = namespace_resource_specs_shrink
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # This parameter is required.
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
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        if self.namespace_resource_specs_shrink is not None:
            result['NamespaceResourceSpecs'] = self.namespace_resource_specs_shrink
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
        if m.get('NamespaceResourceSpecs') is not None:
            self.namespace_resource_specs_shrink = m.get('NamespaceResourceSpecs')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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


class QueryConvertPrepayInstancePriceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
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


class QueryCreateInstancePriceRequestHaResourceSpec(TeaModel):
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


class QueryCreateInstancePriceRequestResourceSpec(TeaModel):
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


class QueryCreateInstancePriceRequestStorageOss(TeaModel):
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


class QueryCreateInstancePriceRequestStorage(TeaModel):
    def __init__(
        self,
        oss: QueryCreateInstancePriceRequestStorageOss = None,
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
            temp_model = QueryCreateInstancePriceRequestStorageOss()
            self.oss = temp_model.from_map(m['Oss'])
        return self


class QueryCreateInstancePriceRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec: QueryCreateInstancePriceRequestHaResourceSpec = None,
        instance_name: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_spec: QueryCreateInstancePriceRequestResourceSpec = None,
        storage: QueryCreateInstancePriceRequestStorage = None,
        use_promotion_code: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.auto_renew = auto_renew
        # This parameter is required.
        self.charge_type = charge_type
        self.duration = duration
        self.extra = extra
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.instance_name = instance_name
        self.pricing_cycle = pricing_cycle
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        self.resource_spec = resource_spec
        self.storage = storage
        self.use_promotion_code = use_promotion_code
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

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
            temp_model = QueryCreateInstancePriceRequestHaResourceSpec()
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
            temp_model = QueryCreateInstancePriceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('Storage') is not None:
            temp_model = QueryCreateInstancePriceRequestStorage()
            self.storage = temp_model.from_map(m['Storage'])
        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class QueryCreateInstancePriceShrinkRequest(TeaModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec_shrink: str = None,
        instance_name: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
        storage_shrink: str = None,
        use_promotion_code: bool = None,
        v_switch_ids_shrink: str = None,
        vpc_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.auto_renew = auto_renew
        # This parameter is required.
        self.charge_type = charge_type
        self.duration = duration
        self.extra = extra
        self.ha = ha
        self.ha_resource_spec_shrink = ha_resource_spec_shrink
        self.instance_name = instance_name
        self.pricing_cycle = pricing_cycle
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        self.resource_spec_shrink = resource_spec_shrink
        self.storage_shrink = storage_shrink
        self.use_promotion_code = use_promotion_code
        self.v_switch_ids_shrink = v_switch_ids_shrink
        self.vpc_id = vpc_id

    def validate(self):
        pass

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
        if self.ha_resource_spec_shrink is not None:
            result['HaResourceSpec'] = self.ha_resource_spec_shrink
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink
        if self.storage_shrink is not None:
            result['Storage'] = self.storage_shrink
        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code
        if self.v_switch_ids_shrink is not None:
            result['VSwitchIds'] = self.v_switch_ids_shrink
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
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
            self.ha_resource_spec_shrink = m.get('HaResourceSpec')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')
        if m.get('Storage') is not None:
            self.storage_shrink = m.get('Storage')
        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids_shrink = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
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


class QueryModifyInstancePriceRequestHaResourceSpec(TeaModel):
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


class QueryModifyInstancePriceRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
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


class QueryModifyInstancePriceRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec: QueryModifyInstancePriceRequestHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        instance_id: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_spec: QueryModifyInstancePriceRequestResourceSpec = None,
        use_promotion_code: bool = None,
    ):
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        # This parameter is required.
        self.instance_id = instance_id
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec = resource_spec
        self.use_promotion_code = use_promotion_code

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            temp_model = QueryModifyInstancePriceRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m['HaResourceSpec'])
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = QueryModifyInstancePriceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')
        return self


class QueryModifyInstancePriceShrinkRequest(TeaModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec_shrink: str = None,
        ha_vswitch_ids_shrink: str = None,
        instance_id: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
        use_promotion_code: bool = None,
    ):
        self.ha = ha
        self.ha_resource_spec_shrink = ha_resource_spec_shrink
        self.ha_vswitch_ids_shrink = ha_vswitch_ids_shrink
        # This parameter is required.
        self.instance_id = instance_id
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec_shrink = resource_spec_shrink
        self.use_promotion_code = use_promotion_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ha is not None:
            result['Ha'] = self.ha
        if self.ha_resource_spec_shrink is not None:
            result['HaResourceSpec'] = self.ha_resource_spec_shrink
        if self.ha_vswitch_ids_shrink is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink
        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')
        if m.get('HaResourceSpec') is not None:
            self.ha_resource_spec_shrink = m.get('HaResourceSpec')
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids_shrink = m.get('HaVSwitchIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')
        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')
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


class QueryRenewInstancePriceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # This parameter is required.
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


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        pricing_cycle: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # This parameter is required.
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


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # orderId
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


