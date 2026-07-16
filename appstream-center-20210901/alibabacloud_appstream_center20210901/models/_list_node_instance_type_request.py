# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodeInstanceTypeRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        cpu: float = None,
        gpu: float = None,
        gpu_memory: int = None,
        instance_type_for_modify: str = None,
        language: str = None,
        memory: int = None,
        node_instance_type: str = None,
        node_instance_type_family: str = None,
        order_by: str = None,
        order_type: str = None,
        os_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        sort_type: str = None,
    ):
        # The region ID of the resource. For more information about supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        self.biz_region_id = biz_region_id
        # The number of CPU cores.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU memory size. This parameter is meaningful only for GPU-accelerated cloud desktops. Unit: MB.
        self.gpu_memory = gpu_memory
        self.instance_type_for_modify = instance_type_for_modify
        # The language type.
        self.language = language
        # The memory size. Unit: MB.
        self.memory = memory
        # The resource specification type to query. If you leave this parameter empty, all specification types are returned.
        self.node_instance_type = node_instance_type
        # The instance family.
        self.node_instance_type_family = node_instance_type_family
        # CPU/Memory.
        self.order_by = order_by
        self.order_type = order_type
        # The supported operating system type.
        self.os_type = os_type
        # The page number of the query results to display.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of query results per page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # DESC/ASC.
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.instance_type_for_modify is not None:
            result['InstanceTypeForModify'] = self.instance_type_for_modify

        if self.language is not None:
            result['Language'] = self.language

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type

        if self.node_instance_type_family is not None:
            result['NodeInstanceTypeFamily'] = self.node_instance_type_family

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('InstanceTypeForModify') is not None:
            self.instance_type_for_modify = m.get('InstanceTypeForModify')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')

        if m.get('NodeInstanceTypeFamily') is not None:
            self.node_instance_type_family = m.get('NodeInstanceTypeFamily')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

