# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EkycVerifyV2Request(DaraModel):
    def __init__(
        self,
        authorize: str = None,
        crop: str = None,
        doc_name: str = None,
        doc_no: str = None,
        doc_type: str = None,
        face_picture_base_64: str = None,
        face_picture_file: str = None,
        face_picture_url: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_file: str = None,
        id_ocr_picture_url: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        # Indicates whether to enable authoritative identity verification. This parameter currently applies only to second-generation ID cards issued in the Chinese mainland.
        self.authorize = authorize
        # Indicates whether clipping is allowed. Clipping is disabled by default (T/F).
        # 
        # - T: Detection is required.
        # - F: Detection is required (default is F).
        self.crop = crop
        # The user\\"s real name. When Authorize=\\"T\\" and the certificate type is a Chinese mainland ID card, you must provide at least one of the following: key certificate information (DocName, DocNo) or certificate image (IdOcrPictureBase64/URL). Note: It supports combinations of one or more Chinese characters, excluding special characters except for the interpunct 【·】 used in ethnic minority names.
        self.doc_name = doc_name
        # The user\\"s certificate number. When Authorize=\\"T\\" and the certificate type is a Chinese mainland ID card, you must provide at least one of the following: key certificate information (DocName, DocNo) or certificate image (IdOcrPictureBase64/URL). Note: It supports a combination of letters and digits with a length of 18 characters.
        self.doc_no = doc_no
        # Certificate type
        self.doc_type = doc_type
        # Base64 encoding of the facial image.
        # 
        # Notes:
        # 
        # - If you choose this method to submit the certificate image, check the image size and avoid uploading excessively large images.
        # - You must specify exactly one of FacePictureBase64, FacePictureUrl, or FacePictureFile.
        self.face_picture_base_64 = face_picture_base_64
        # File stream of the facial photo
        self.face_picture_file = face_picture_file
        # URL of the facial photo
        self.face_picture_url = face_picture_url
        # Base64-encoded certificate Image. Notes:
        # 
        # - If you use this method to submit the certificate image, check the image size and avoid uploading excessively large images.
        # - You must specify exactly one of IdOcrPictureBase64, IdOcrPictureUrl, or IdOcrPictureFile.
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # File stream of the front side of the certificate
        self.id_ocr_picture_file = id_ocr_picture_file
        # URL of the front side of the certificate
        self.id_ocr_picture_url = id_ocr_picture_url
        # Custom OCR quality detection threshold mode:
        # 
        # - 0: System default
        # - 1: Strict mode
        # - 2: Loose mode
        # - 3 (default): Shutdown quality detection
        self.id_threshold = id_threshold
        # A custom business UUID defined by the merchant, used for subsequent issue tracking and troubleshooting. It supports a combination of letters and digits with a length of 32 characters. Ensure its uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # Your custom user ID or another identifier that can uniquely identify a specific user, such as a mobile phone number or mailbox address. We strongly recommend pre-masking the value of this field—for example, by applying a hash function.
        self.merchant_user_id = merchant_user_id
        # Product code
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorize is not None:
            result['Authorize'] = self.authorize

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.doc_no is not None:
            result['DocNo'] = self.doc_no

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64

        if self.face_picture_file is not None:
            result['FacePictureFile'] = self.face_picture_file

        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url

        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64

        if self.id_ocr_picture_file is not None:
            result['IdOcrPictureFile'] = self.id_ocr_picture_file

        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url

        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')

        if m.get('FacePictureFile') is not None:
            self.face_picture_file = m.get('FacePictureFile')

        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')

        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')

        if m.get('IdOcrPictureFile') is not None:
            self.id_ocr_picture_file = m.get('IdOcrPictureFile')

        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')

        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

