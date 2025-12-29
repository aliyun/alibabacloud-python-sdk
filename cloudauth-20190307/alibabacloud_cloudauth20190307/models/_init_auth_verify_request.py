# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitAuthVerifyRequest(DaraModel):
    def __init__(
        self,
        callback_token: str = None,
        callback_url: str = None,
        card_page_number: str = None,
        card_type: str = None,
        doc_scan_mode: str = None,
        id_spoof: str = None,
        meta_info: str = None,
        outer_order_no: str = None,
        product_code: str = None,
        scene_id: int = None,
    ):
        self.callback_token = callback_token
        self.callback_url = callback_url
        # This parameter is required.
        self.card_page_number = card_page_number
        # This parameter is required.
        self.card_type = card_type
        self.doc_scan_mode = doc_scan_mode
        self.id_spoof = id_spoof
        # This parameter is required.
        self.meta_info = meta_info
        # This parameter is required.
        self.outer_order_no = outer_order_no
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.card_page_number is not None:
            result['CardPageNumber'] = self.card_page_number

        if self.card_type is not None:
            result['CardType'] = self.card_type

        if self.doc_scan_mode is not None:
            result['DocScanMode'] = self.doc_scan_mode

        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof

        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info

        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('CardPageNumber') is not None:
            self.card_page_number = m.get('CardPageNumber')

        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')

        if m.get('DocScanMode') is not None:
            self.doc_scan_mode = m.get('DocScanMode')

        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')

        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')

        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

