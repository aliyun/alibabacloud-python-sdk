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
        # A security token that you generate to prevent replay attacks and data tampering.
        # If this value is set, the CallbackToken field is included in the callback to CallbackUrl.
        self.callback_token = callback_token
        # The callback URL for OCR results. The callback request method is GET by default. The callback URL must start with https. After OCR is completed, a callback is sent to this URL with the certifyId and subcode fields automatically appended.
        # > Warning
        # - The URL is validated for public network access before the API is invoked. If the URL is not publicly accessible, a 400 error is returned.
        # - The callback is executed immediately after the OCR invocation is completed, but may be delayed due to network issues. Accept the request completion notification from the client side first, and then invoke the query API to obtain the result details.
        self.callback_url = callback_url
        # The number of card pages collected by the SDK. Valid values:
        # - "1": front side only
        # - "2": both front and back sides.
        # 
        # This parameter is required.
        self.card_page_number = card_page_number
        # The document type. Set the value to IDENTITY_CARD.
        # 
        # This parameter is required.
        self.card_type = card_type
        # The OCR document scan pattern. Valid values:
        # - shoot (default): photo capture
        # - scan: scan
        # - auto: automatic switchover between photo capture and scan.
        self.doc_scan_mode = doc_scan_mode
        # Specifies whether to enable the document anti-forgery detection feature. Valid values:
        # - Y: Enabled.
        # - N: Disabled. This is the default value.
        self.id_spoof = id_spoof
        # The MetaInfo environment parameter, which must be obtained from the client SDK.
        # 
        # This parameter is required.
        self.meta_info = meta_info
        # A custom business unique identifier that you specify for subsequent troubleshooting.
        # 
        # The value can contain letters (both uppercase and lowercase) and digits, with a maximum length of 32 characters.
        # 
        # This parameter is required.
        self.outer_order_no = outer_order_no
        # The product solution to use. Set the value to ID_OCR.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The China Chinese authentication scenario ID.
        # 
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

