# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChatbotInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        nlu_service_params_json: str = None,
        nlu_service_type: str = None,
        page_number: int = None,
        page_size: int = None,
        union_source: str = None,
    ):
        self.instance_id = instance_id
        self.nlu_service_params_json = nlu_service_params_json
        self.nlu_service_type = nlu_service_type
        # This parameter is required.
        self.page_number = page_number
        self.page_size = page_size
        self.union_source = union_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nlu_service_params_json is not None:
            result['NluServiceParamsJson'] = self.nlu_service_params_json

        if self.nlu_service_type is not None:
            result['NluServiceType'] = self.nlu_service_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.union_source is not None:
            result['UnionSource'] = self.union_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NluServiceParamsJson') is not None:
            self.nlu_service_params_json = m.get('NluServiceParamsJson')

        if m.get('NluServiceType') is not None:
            self.nlu_service_type = m.get('NluServiceType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UnionSource') is not None:
            self.union_source = m.get('UnionSource')

        return self

