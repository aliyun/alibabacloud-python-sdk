# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class QueryConvertInstancePriceRequest(DaraModel):
    def __init__(
        self,
        convert_postpay_instance_request: main_models.QueryConvertInstancePriceRequestConvertPostpayInstanceRequest = None,
    ):
        # This parameter is required.
        self.convert_postpay_instance_request = convert_postpay_instance_request

    def validate(self):
        if self.convert_postpay_instance_request:
            self.convert_postpay_instance_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.convert_postpay_instance_request is not None:
            result['ConvertPostpayInstanceRequest'] = self.convert_postpay_instance_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertPostpayInstanceRequest') is not None:
            temp_model = main_models.QueryConvertInstancePriceRequestConvertPostpayInstanceRequest()
            self.convert_postpay_instance_request = temp_model.from_map(m.get('ConvertPostpayInstanceRequest'))

        return self

class QueryConvertInstancePriceRequestConvertPostpayInstanceRequest(DaraModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        is_auto_renew: bool = None,
        namespace_resource_specs: List[main_models.QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs] = None,
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
            for v1 in self.namespace_resource_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew

        result['NamespaceResourceSpecs'] = []
        if self.namespace_resource_specs is not None:
            for k1 in self.namespace_resource_specs:
                result['NamespaceResourceSpecs'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('NamespaceResourceSpecs'):
                temp_model = main_models.QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs()
                self.namespace_resource_specs.append(temp_model.from_map(k1))

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        resource_spec: main_models.QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec = None,
    ):
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.resource_spec = resource_spec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        return self

class QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

