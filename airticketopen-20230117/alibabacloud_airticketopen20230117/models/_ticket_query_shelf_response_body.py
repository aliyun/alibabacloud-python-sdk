# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TicketQueryShelfResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TicketQueryShelfResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TicketQueryShelfResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TicketQueryShelfResponseBodyData(DaraModel):
    def __init__(
        self,
        shelves: List[main_models.TicketQueryShelfResponseBodyDataShelves] = None,
    ):
        self.shelves = shelves

    def validate(self):
        if self.shelves:
            for v1 in self.shelves:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Shelves'] = []
        if self.shelves is not None:
            for k1 in self.shelves:
                result['Shelves'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shelves = []
        if m.get('Shelves') is not None:
            for k1 in m.get('Shelves'):
                temp_model = main_models.TicketQueryShelfResponseBodyDataShelves()
                self.shelves.append(temp_model.from_map(k1))

        return self

class TicketQueryShelfResponseBodyDataShelves(DaraModel):
    def __init__(
        self,
        shelf_id: int = None,
        shelf_index: int = None,
        shelf_name: str = None,
        tabs: List[main_models.TicketQueryShelfResponseBodyDataShelvesTabs] = None,
    ):
        self.shelf_id = shelf_id
        self.shelf_index = shelf_index
        self.shelf_name = shelf_name
        self.tabs = tabs

    def validate(self):
        if self.tabs:
            for v1 in self.tabs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shelf_id is not None:
            result['ShelfId'] = self.shelf_id

        if self.shelf_index is not None:
            result['ShelfIndex'] = self.shelf_index

        if self.shelf_name is not None:
            result['ShelfName'] = self.shelf_name

        result['Tabs'] = []
        if self.tabs is not None:
            for k1 in self.tabs:
                result['Tabs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShelfId') is not None:
            self.shelf_id = m.get('ShelfId')

        if m.get('ShelfIndex') is not None:
            self.shelf_index = m.get('ShelfIndex')

        if m.get('ShelfName') is not None:
            self.shelf_name = m.get('ShelfName')

        self.tabs = []
        if m.get('Tabs') is not None:
            for k1 in m.get('Tabs'):
                temp_model = main_models.TicketQueryShelfResponseBodyDataShelvesTabs()
                self.tabs.append(temp_model.from_map(k1))

        return self

class TicketQueryShelfResponseBodyDataShelvesTabs(DaraModel):
    def __init__(
        self,
        cells: List[main_models.TicketQueryShelfResponseBodyDataShelvesTabsCells] = None,
        tab_index: int = None,
        tab_name: str = None,
    ):
        self.cells = cells
        self.tab_index = tab_index
        self.tab_name = tab_name

    def validate(self):
        if self.cells:
            for v1 in self.cells:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cells'] = []
        if self.cells is not None:
            for k1 in self.cells:
                result['Cells'].append(k1.to_map() if k1 else None)

        if self.tab_index is not None:
            result['TabIndex'] = self.tab_index

        if self.tab_name is not None:
            result['TabName'] = self.tab_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cells = []
        if m.get('Cells') is not None:
            for k1 in m.get('Cells'):
                temp_model = main_models.TicketQueryShelfResponseBodyDataShelvesTabsCells()
                self.cells.append(temp_model.from_map(k1))

        if m.get('TabIndex') is not None:
            self.tab_index = m.get('TabIndex')

        if m.get('TabName') is not None:
            self.tab_name = m.get('TabName')

        return self

class TicketQueryShelfResponseBodyDataShelvesTabsCells(DaraModel):
    def __init__(
        self,
        spu_id: int = None,
        ticket_kind_id: int = None,
    ):
        self.spu_id = spu_id
        self.ticket_kind_id = ticket_kind_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.spu_id is not None:
            result['SpuId'] = self.spu_id

        if self.ticket_kind_id is not None:
            result['TicketKindId'] = self.ticket_kind_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpuId') is not None:
            self.spu_id = m.get('SpuId')

        if m.get('TicketKindId') is not None:
            self.ticket_kind_id = m.get('TicketKindId')

        return self

