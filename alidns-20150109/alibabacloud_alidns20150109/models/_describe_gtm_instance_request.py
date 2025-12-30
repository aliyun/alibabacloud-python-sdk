# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGtmInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        need_detail_attributes: bool = None,
    ):
        # The ID of the GTM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the values of specific response parameters.
        self.lang = lang
        # Specifies whether additional information is required. Default value: **false**. If the value is **true**, the AccessStrategyNum and AddressPoolNum parameters are returned.
        self.need_detail_attributes = need_detail_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.need_detail_attributes is not None:
            result['NeedDetailAttributes'] = self.need_detail_attributes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NeedDetailAttributes') is not None:
            self.need_detail_attributes = m.get('NeedDetailAttributes')

        return self

