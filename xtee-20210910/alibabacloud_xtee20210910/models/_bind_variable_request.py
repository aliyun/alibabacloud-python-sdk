# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindVariableRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        api_region_id: str = None,
        api_type: str = None,
        create_type: str = None,
        define_id: str = None,
        define_ids: str = None,
        description: str = None,
        event_code: str = None,
        exception_value: str = None,
        id: int = None,
        output_field: str = None,
        output_type: str = None,
        params: str = None,
        params_list: str = None,
        reg_id: str = None,
        source_type: str = None,
        title: str = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The API region ID.
        self.api_region_id = api_region_id
        # The API type.
        self.api_type = api_type
        # The creation type.
        self.create_type = create_type
        # The primary key ID of the associated variable definition.
        self.define_id = define_id
        # The variable definition IDs. You can specify multiple IDs separated by commas.
        self.define_ids = define_ids
        # The description.
        self.description = description
        # The event code.
        # 
        # This parameter is required.
        self.event_code = event_code
        # The exception value.
        self.exception_value = exception_value
        # The primary key ID of the variable.
        self.id = id
        # The output field path.
        self.output_field = output_field
        # The output type.
        self.output_type = output_type
        # The input parameter information for the binding.
        self.params = params
        # The event parameter mapping 2.0. Either params or paramsList must be non-empty. This is a List JSON structure.
        self.params_list = params_list
        # The region code.
        self.reg_id = reg_id
        # The variable source.
        self.source_type = source_type
        # The title.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.api_region_id is not None:
            result['apiRegionId'] = self.api_region_id

        if self.api_type is not None:
            result['apiType'] = self.api_type

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.define_ids is not None:
            result['defineIds'] = self.define_ids

        if self.description is not None:
            result['description'] = self.description

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.exception_value is not None:
            result['exceptionValue'] = self.exception_value

        if self.id is not None:
            result['id'] = self.id

        if self.output_field is not None:
            result['outputField'] = self.output_field

        if self.output_type is not None:
            result['outputType'] = self.output_type

        if self.params is not None:
            result['params'] = self.params

        if self.params_list is not None:
            result['paramsList'] = self.params_list

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('apiRegionId') is not None:
            self.api_region_id = m.get('apiRegionId')

        if m.get('apiType') is not None:
            self.api_type = m.get('apiType')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('defineIds') is not None:
            self.define_ids = m.get('defineIds')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('exceptionValue') is not None:
            self.exception_value = m.get('exceptionValue')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('outputField') is not None:
            self.output_field = m.get('outputField')

        if m.get('outputType') is not None:
            self.output_type = m.get('outputType')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('paramsList') is not None:
            self.params_list = m.get('paramsList')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

