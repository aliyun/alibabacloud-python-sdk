# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppServiceProfile(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        design_type: str = None,
        design_type_text: str = None,
        instance_id: str = None,
        order_id: str = None,
        service_spec: str = None,
        service_spec_text: str = None,
    ):
        self.biz_id = biz_id
        self.design_type = design_type
        self.design_type_text = design_type_text
        self.instance_id = instance_id
        self.order_id = order_id
        self.service_spec = service_spec
        self.service_spec_text = service_spec_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.design_type is not None:
            result['DesignType'] = self.design_type

        if self.design_type_text is not None:
            result['DesignTypeText'] = self.design_type_text

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec

        if self.service_spec_text is not None:
            result['ServiceSpecText'] = self.service_spec_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DesignType') is not None:
            self.design_type = m.get('DesignType')

        if m.get('DesignTypeText') is not None:
            self.design_type_text = m.get('DesignTypeText')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')

        if m.get('ServiceSpecText') is not None:
            self.service_spec_text = m.get('ServiceSpecText')

        return self

