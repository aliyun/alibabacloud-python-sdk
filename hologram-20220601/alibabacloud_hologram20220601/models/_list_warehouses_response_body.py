# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListWarehousesResponseBody(DaraModel):
    def __init__(
        self,
        warehouse_list: List[main_models.ListWarehousesResponseBodyWarehouseList] = None,
        request_id: str = None,
    ):
        # The list of virtual warehouse instances.
        self.warehouse_list = warehouse_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.warehouse_list:
            for v1 in self.warehouse_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WarehouseList'] = []
        if self.warehouse_list is not None:
            for k1 in self.warehouse_list:
                result['WarehouseList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warehouse_list = []
        if m.get('WarehouseList') is not None:
            for k1 in m.get('WarehouseList'):
                temp_model = main_models.ListWarehousesResponseBodyWarehouseList()
                self.warehouse_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListWarehousesResponseBodyWarehouseList(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

