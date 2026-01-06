# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlidingAssistantResponseBody(DaraModel):
    def __init__(
        self,
        aliding_assistant_id: str = None,
        app_code: str = None,
        jump_url: str = None,
        process_instance_id: str = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.aliding_assistant_id = aliding_assistant_id
        self.app_code = app_code
        self.jump_url = jump_url
        self.process_instance_id = process_instance_id
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliding_assistant_id is not None:
            result['alidingAssistantId'] = self.aliding_assistant_id

        if self.app_code is not None:
            result['appCode'] = self.app_code

        if self.jump_url is not None:
            result['jumpUrl'] = self.jump_url

        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alidingAssistantId') is not None:
            self.aliding_assistant_id = m.get('alidingAssistantId')

        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')

        if m.get('jumpUrl') is not None:
            self.jump_url = m.get('jumpUrl')

        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

