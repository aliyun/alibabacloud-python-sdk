# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefundInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        immediately_release: str = None,
        instance_id: str = None,
        product_code: str = None,
        product_type: str = None,
    ):
        # Required for idempotent scenarios. A UUID-generated string. This field is used for idempotence. If the same value is passed in multiple calls, the result of the first call is returned. If a result is returned after the call, you can parse the refund order ID, which indicates that the call is successful.
        self.client_token = client_token
        # Required for unsubscription scenarios. Valid values: 1: immediately releases the instance. 0: stops the instance first based on the shutdown policy. Only some products support this value. Default value: 1.
        self.immediately_release = immediately_release
        # Required for unsubscription scenarios. The instance ID, not the custom name.
        self.instance_id = instance_id
        # Required for unsubscription scenarios. The product code. If the error code returned after the call indicates that the product is not supported, submit a ticket to request that the cloud service enable this feature.
        self.product_code = product_code
        # Required for unsubscription scenarios. The product type. Unless otherwise specified, pass an empty string. In the debugging tool, you do not need to manually enter a value. Hover over the input box, and a button labeled "Enter empty string" appears. Click this button. When initiating an unsubscription through code, pass an empty string "".
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.immediately_release is not None:
            result['ImmediatelyRelease'] = self.immediately_release

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ImmediatelyRelease') is not None:
            self.immediately_release = m.get('ImmediatelyRelease')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

