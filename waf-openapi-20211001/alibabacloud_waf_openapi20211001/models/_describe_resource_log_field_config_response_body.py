# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceLogFieldConfigResponseBody(DaraModel):
    def __init__(
        self,
        add_list: str = None,
        del_list: str = None,
        delivery_type: str = None,
        extend_config: str = None,
        field_list: str = None,
        log_delivery_strategy: str = None,
        request_id: str = None,
    ):
        # The list of additional log fields configured in addition to the default log fields. The value is in the "a,b,c,..." format.
        self.add_list = add_list
        # The list of log fields that are not configured compared to the default log fields. The value is in the "a,b,c,..." format.
        self.del_list = del_list
        # The log delivery type. Valid values:
        # 
        # - **sls**: Simple Log Service.
        # - **kafka**: External delivery to Kafka.
        # - **syslog**: External delivery to Syslog.
        self.delivery_type = delivery_type
        # The extended configuration for log delivery. The value is a string converted from a JSON object constructed with a series of parameters.
        # > For detailed parameter information, see the description of the **ExtendConfig** parameter in the [ModifyResourceLogFieldConfig](~~ModifyResourceLogFieldConfig~~) operation.
        self.extend_config = extend_config
        # The list of delivered log fields. The value is in the "a,b,c,..." format.
        self.field_list = field_list
        # The log delivery policies. Multiple policies are supported. The value is a string converted from a JSON array constructed with a series of parameters.
        # 
        # > For detailed parameter information, see the description of the **LogDeliveryStrategy** parameter in the [ModifyResourceLogFieldConfig](~~ModifyResourceLogFieldConfig~~) operation.
        self.log_delivery_strategy = log_delivery_strategy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_list is not None:
            result['AddList'] = self.add_list

        if self.del_list is not None:
            result['DelList'] = self.del_list

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.extend_config is not None:
            result['ExtendConfig'] = self.extend_config

        if self.field_list is not None:
            result['FieldList'] = self.field_list

        if self.log_delivery_strategy is not None:
            result['LogDeliveryStrategy'] = self.log_delivery_strategy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddList') is not None:
            self.add_list = m.get('AddList')

        if m.get('DelList') is not None:
            self.del_list = m.get('DelList')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('ExtendConfig') is not None:
            self.extend_config = m.get('ExtendConfig')

        if m.get('FieldList') is not None:
            self.field_list = m.get('FieldList')

        if m.get('LogDeliveryStrategy') is not None:
            self.log_delivery_strategy = m.get('LogDeliveryStrategy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

