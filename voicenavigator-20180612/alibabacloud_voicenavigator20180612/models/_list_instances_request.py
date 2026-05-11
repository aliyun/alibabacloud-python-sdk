# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_id_list_json_string: str = None,
        name: str = None,
        nlu_service_type_list_json_string: str = None,
        number: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        union_instance_id: str = None,
        union_source: str = None,
    ):
        self.instance_id_list_json_string = instance_id_list_json_string
        self.name = name
        self.nlu_service_type_list_json_string = nlu_service_type_list_json_string
        self.number = number
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.status = status
        self.union_instance_id = union_instance_id
        self.union_source = union_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id_list_json_string is not None:
            result['InstanceIdListJsonString'] = self.instance_id_list_json_string

        if self.name is not None:
            result['Name'] = self.name

        if self.nlu_service_type_list_json_string is not None:
            result['NluServiceTypeListJsonString'] = self.nlu_service_type_list_json_string

        if self.number is not None:
            result['Number'] = self.number

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.union_instance_id is not None:
            result['UnionInstanceId'] = self.union_instance_id

        if self.union_source is not None:
            result['UnionSource'] = self.union_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdListJsonString') is not None:
            self.instance_id_list_json_string = m.get('InstanceIdListJsonString')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluServiceTypeListJsonString') is not None:
            self.nlu_service_type_list_json_string = m.get('NluServiceTypeListJsonString')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnionInstanceId') is not None:
            self.union_instance_id = m.get('UnionInstanceId')

        if m.get('UnionSource') is not None:
            self.union_source = m.get('UnionSource')

        return self

