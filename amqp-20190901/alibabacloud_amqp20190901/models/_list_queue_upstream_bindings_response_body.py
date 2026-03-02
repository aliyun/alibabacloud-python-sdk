# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class ListQueueUpstreamBindingsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListQueueUpstreamBindingsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListQueueUpstreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListQueueUpstreamBindingsResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        vo_list: main_models.ListQueueUpstreamBindingsResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('VoList') is not None:
            temp_model = main_models.ListQueueUpstreamBindingsResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m.get('VoList'))

        return self

class ListQueueUpstreamBindingsResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        binding_vo: List[main_models.ListQueueUpstreamBindingsResponseBodyDataVoListBindingVO] = None,
    ):
        self.binding_vo = binding_vo

    def validate(self):
        if self.binding_vo:
            for v1 in self.binding_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BindingVO'] = []
        if self.binding_vo is not None:
            for k1 in self.binding_vo:
                result['BindingVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.binding_vo = []
        if m.get('BindingVO') is not None:
            for k1 in m.get('BindingVO'):
                temp_model = main_models.ListQueueUpstreamBindingsResponseBodyDataVoListBindingVO()
                self.binding_vo.append(temp_model.from_map(k1))

        return self

class ListQueueUpstreamBindingsResponseBodyDataVoListBindingVO(DaraModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: int = None,
        dst_name: str = None,
        src_name: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.dst_name = dst_name
        self.src_name = src_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.argument is not None:
            result['Argument'] = self.argument

        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key

        if self.binding_type is not None:
            result['BindingType'] = self.binding_type

        if self.dst_name is not None:
            result['DstName'] = self.dst_name

        if self.src_name is not None:
            result['SrcName'] = self.src_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')

        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')

        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')

        if m.get('DstName') is not None:
            self.dst_name = m.get('DstName')

        if m.get('SrcName') is not None:
            self.src_name = m.get('SrcName')

        return self

