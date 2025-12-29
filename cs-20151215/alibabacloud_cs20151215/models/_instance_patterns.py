# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstancePatterns(DaraModel):
    def __init__(
        self,
        architectures: List[str] = None,
        burst_performance_option: str = None,
        core: int = None,
        cores: int = None,
        cpu_architectures: List[str] = None,
        excluded_instance_types: List[str] = None,
        instance_categories: List[str] = None,
        instance_family_level: str = None,
        instance_type_families: List[str] = None,
        max_cpu_cores: int = None,
        max_memory_size: float = None,
        max_price: float = None,
        maximum_gpu_amount: int = None,
        memory: float = None,
        min_cpu_cores: int = None,
        min_memory_size: float = None,
        minimum_eni_ipv_6address_quantity: int = None,
        minimum_eni_private_ip_address_quantity: int = None,
        minimum_eni_quantity: int = None,
    ):
        self.architectures = architectures
        self.burst_performance_option = burst_performance_option
        self.core = core
        self.cores = cores
        self.cpu_architectures = cpu_architectures
        self.excluded_instance_types = excluded_instance_types
        self.instance_categories = instance_categories
        self.instance_family_level = instance_family_level
        self.instance_type_families = instance_type_families
        self.max_cpu_cores = max_cpu_cores
        self.max_memory_size = max_memory_size
        self.max_price = max_price
        self.maximum_gpu_amount = maximum_gpu_amount
        self.memory = memory
        self.min_cpu_cores = min_cpu_cores
        self.min_memory_size = min_memory_size
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        self.minimum_eni_quantity = minimum_eni_quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architectures is not None:
            result['architectures'] = self.architectures

        if self.burst_performance_option is not None:
            result['burst_performance_option'] = self.burst_performance_option

        if self.core is not None:
            result['core'] = self.core

        if self.cores is not None:
            result['cores'] = self.cores

        if self.cpu_architectures is not None:
            result['cpu_architectures'] = self.cpu_architectures

        if self.excluded_instance_types is not None:
            result['excluded_instance_types'] = self.excluded_instance_types

        if self.instance_categories is not None:
            result['instance_categories'] = self.instance_categories

        if self.instance_family_level is not None:
            result['instance_family_level'] = self.instance_family_level

        if self.instance_type_families is not None:
            result['instance_type_families'] = self.instance_type_families

        if self.max_cpu_cores is not None:
            result['max_cpu_cores'] = self.max_cpu_cores

        if self.max_memory_size is not None:
            result['max_memory_size'] = self.max_memory_size

        if self.max_price is not None:
            result['max_price'] = self.max_price

        if self.maximum_gpu_amount is not None:
            result['maximum_gpu_amount'] = self.maximum_gpu_amount

        if self.memory is not None:
            result['memory'] = self.memory

        if self.min_cpu_cores is not None:
            result['min_cpu_cores'] = self.min_cpu_cores

        if self.min_memory_size is not None:
            result['min_memory_size'] = self.min_memory_size

        if self.minimum_eni_ipv_6address_quantity is not None:
            result['minimum_eni_ipv6_address_quantity'] = self.minimum_eni_ipv_6address_quantity

        if self.minimum_eni_private_ip_address_quantity is not None:
            result['minimum_eni_private_ip_address_quantity'] = self.minimum_eni_private_ip_address_quantity

        if self.minimum_eni_quantity is not None:
            result['minimum_eni_quantity'] = self.minimum_eni_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architectures') is not None:
            self.architectures = m.get('architectures')

        if m.get('burst_performance_option') is not None:
            self.burst_performance_option = m.get('burst_performance_option')

        if m.get('core') is not None:
            self.core = m.get('core')

        if m.get('cores') is not None:
            self.cores = m.get('cores')

        if m.get('cpu_architectures') is not None:
            self.cpu_architectures = m.get('cpu_architectures')

        if m.get('excluded_instance_types') is not None:
            self.excluded_instance_types = m.get('excluded_instance_types')

        if m.get('instance_categories') is not None:
            self.instance_categories = m.get('instance_categories')

        if m.get('instance_family_level') is not None:
            self.instance_family_level = m.get('instance_family_level')

        if m.get('instance_type_families') is not None:
            self.instance_type_families = m.get('instance_type_families')

        if m.get('max_cpu_cores') is not None:
            self.max_cpu_cores = m.get('max_cpu_cores')

        if m.get('max_memory_size') is not None:
            self.max_memory_size = m.get('max_memory_size')

        if m.get('max_price') is not None:
            self.max_price = m.get('max_price')

        if m.get('maximum_gpu_amount') is not None:
            self.maximum_gpu_amount = m.get('maximum_gpu_amount')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('min_cpu_cores') is not None:
            self.min_cpu_cores = m.get('min_cpu_cores')

        if m.get('min_memory_size') is not None:
            self.min_memory_size = m.get('min_memory_size')

        if m.get('minimum_eni_ipv6_address_quantity') is not None:
            self.minimum_eni_ipv_6address_quantity = m.get('minimum_eni_ipv6_address_quantity')

        if m.get('minimum_eni_private_ip_address_quantity') is not None:
            self.minimum_eni_private_ip_address_quantity = m.get('minimum_eni_private_ip_address_quantity')

        if m.get('minimum_eni_quantity') is not None:
            self.minimum_eni_quantity = m.get('minimum_eni_quantity')

        return self

