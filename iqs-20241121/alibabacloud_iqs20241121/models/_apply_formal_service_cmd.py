# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ApplyFormalServiceCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        address: str = None,
        apply_service_infos: List[Dict[str, Any]] = None,
        apply_type: str = None,
        contact_name: str = None,
        instance_id: str = None,
        phone: str = None,
        product_name: str = None,
        qps: int = None,
        scene_desc: str = None,
        service_type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.address = address
        self.apply_service_infos = apply_service_infos
        self.apply_type = apply_type
        self.contact_name = contact_name
        self.instance_id = instance_id
        self.phone = phone
        self.product_name = product_name
        self.qps = qps
        self.scene_desc = scene_desc
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.account_name is not None:
            result['accountName'] = self.account_name

        if self.address is not None:
            result['address'] = self.address

        if self.apply_service_infos is not None:
            result['applyServiceInfos'] = self.apply_service_infos

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

        if self.scene_desc is not None:
            result['sceneDesc'] = self.scene_desc

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')

        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('applyServiceInfos') is not None:
            self.apply_service_infos = m.get('applyServiceInfos')

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

        if m.get('sceneDesc') is not None:
            self.scene_desc = m.get('sceneDesc')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        return self

