# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataCenterTableRequest(DaraModel):
    def __init__(
        self,
        call_from: str = None,
        database_name: str = None,
        dms_unit: str = None,
        import_type: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        table_name: str = None,
    ):
        self.call_from = call_from
        self.database_name = database_name
        self.dms_unit = dms_unit
        self.import_type = import_type
        self.instance_name = instance_name
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_from is not None:
            result['CallFrom'] = self.call_from

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        if self.import_type is not None:
            result['ImportType'] = self.import_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallFrom') is not None:
            self.call_from = m.get('CallFrom')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

