# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserLogFieldConfigResponseBody(DaraModel):
    def __init__(
        self,
        add_list: str = None,
        config_status: str = None,
        del_list: str = None,
        delivery_type: str = None,
        extend_config: str = None,
        field_list: str = None,
        log_delivery_strategy: str = None,
        request_id: str = None,
    ):
        # The additional log fields that are added to the default configuration. Multiple fields are separated by commas (,) in the `a,b,c,...` format.
        self.add_list = add_list
        # The status of the log field configuration. Valid values:
        # 
        # - **initial**: The log field configuration is being initialized.
        # 
        # - **updating**: The log field configuration is being updated.
        # 
        # - **failed_finished**: The log field configuration update failed.
        # 
        # - **success_finished**: The log field configuration update succeeded.
        self.config_status = config_status
        # The default log fields that are excluded from the log delivery configuration. Multiple fields are separated by commas (,) in the `a,b,c,...` format.
        self.del_list = del_list
        # The log delivery type. Valid values:
        # 
        # - **sls**: Simple Log Service.
        self.delivery_type = delivery_type
        # The extended configuration for log delivery. The value is a JSON-formatted string that contains configuration key-value pairs, such as custom request headers.
        # 
        # > For more information, see the **ExtendConfig** parameter description in [ModifyUserLogFieldConfig](~~ModifyUserLogFieldConfig~~).
        self.extend_config = extend_config
        # The complete list of log fields that are delivered. Multiple fields are separated by commas (,) in the `a,b,c,...` format.
        self.field_list = field_list
        # The log delivery policies. Multiple policies are supported. The value is a JSON-formatted string that contains an array of policy objects.
        # 
        # > For more information, see the **LogDeliveryStrategy** parameter description in [ModifyUserLogFieldConfig](~~ModifyUserLogFieldConfig~~).
        self.log_delivery_strategy = log_delivery_strategy
        # The ID of the request.
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

        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status

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

        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')

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

