# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAccountReviewRecordResponseBody(DaraModel):
    def __init__(
        self,
        address: str = None,
        ali_uid: str = None,
        apply_type: str = None,
        contact_name: str = None,
        instance_id: str = None,
        phone: str = None,
        product_name: str = None,
        qps: int = None,
        request_id: str = None,
        scene_desc: str = None,
        scopes: List[str] = None,
        service_type: str = None,
    ):
        self.address = address
        self.ali_uid = ali_uid
        self.apply_type = apply_type
        self.contact_name = contact_name
        self.instance_id = instance_id
        self.phone = phone
        self.product_name = product_name
        self.qps = qps
        # Id of the request
        self.request_id = request_id
        self.scene_desc = scene_desc
        self.scopes = scopes
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.ali_uid is not None:
            result['aliUid'] = self.ali_uid

        if self.apply_type is not None:
            result['applyType'] = self.apply_type

        if self.contact_name is not None:
            result['contactName'] = self.contact_name

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.phone is not None:
            result['phone'] = self.phone

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.qps is not None:
            result['qps'] = self.qps

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scene_desc is not None:
            result['sceneDesc'] = self.scene_desc

        if self.scopes is not None:
            result['scopes'] = self.scopes

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('aliUid') is not None:
            self.ali_uid = m.get('aliUid')

        if m.get('applyType') is not None:
            self.apply_type = m.get('applyType')

        if m.get('contactName') is not None:
            self.contact_name = m.get('contactName')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('qps') is not None:
            self.qps = m.get('qps')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sceneDesc') is not None:
            self.scene_desc = m.get('sceneDesc')

        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        return self

