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
        face_quality_check: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_file: str = None,
        id_ocr_picture_url: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        # Specifies whether to enable authoritative identity verification. Currently, this parameter applies only to second-generation mainland China ID cards.
        self.authorize = authorize
        # Specifies whether cropping is allowed. By default, cropping is not allowed. Valid values:
        # 
        # - T: Detection is required.
        # - F: Detection is required (default value: F).
        self.crop = crop
        # The real name of the user. When Authorize=\\"T\\" and the document type is a mainland China ID card, you must provide at least one of the following: key document information (DocName, DocNo) or document images (IdOcrPictureBase64/URL). Note: Supports a combination of Chinese characters with a minimum length of 1 character. No special characters are allowed, except for the middle dot (·) used in ethnic minority names.
        self.doc_name = doc_name
        # The document number of the user. When Authorize=\\"T\\" and the document type is a mainland China ID card, you must provide at least one of the following: key document information (DocName, DocNo) or document images (IdOcrPictureBase64/URL). Note: Supports a combination of letters and numbers with a length of 18 characters.
        self.doc_no = doc_no
        # The document type.
        self.doc_type = doc_type
        # The Base64-encoded face image.
        # 
        # Note:
        # 
        # - If you choose this method to pass in the face image, check the photo size and do not pass in an excessively large photo.
        # - Specify one of the following parameters: FacePictureBase64, FacePictureUrl, or FacePictureFile.
        self.face_picture_base_64 = face_picture_base_64
        # The file stream of the face photo.
        self.face_picture_file = face_picture_file
        # The URL of the face photo.
        self.face_picture_url = face_picture_url
        # Specifies whether to enable face quality detection.
        self.face_quality_check = face_quality_check
        # The Base64-encoded identity document image. Note:
        # 
        # - If you choose this method to pass in the document image, check the photo size and do not pass in an excessively large photo.
        # - Specify one of the following parameters: IdOcrPictureBase64, IdOcrPictureUrl, or IdOcrPictureFile.
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # The file stream of the front side of the identity document image.
        self.id_ocr_picture_file = id_ocr_picture_file
        # The URL of the front side of the identity document image.
        self.id_ocr_picture_url = id_ocr_picture_url
        # Specifies whether to enable document anti-spoofing.
        self.id_spoof = id_spoof
        # The custom OCR quality detection threshold mode. Valid values:
        # 
        # - 0: system default.
        # - 1: strict mode.
        # - 2: loose mode.
        # - 3 (default): quality detection disabled.
        self.id_threshold = id_threshold
        # A custom business unique identifier defined by the merchant, used for subsequent issue tracking and troubleshooting. Supports a combination of letters and numbers up to 32 characters in length. Ensure that this value is unique.
        self.merchant_biz_id = merchant_biz_id
        # A custom user ID or other identifier that can identify a specific user, such as a phone number or email address. We strongly recommend that you desensitize the value of this field in advance, for example, by hashing the value.
        self.merchant_user_id = merchant_user_id
        # The product code.
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

        if self.face_quality_check is not None:
            result['FaceQualityCheck'] = self.face_quality_check

        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64

        if self.id_ocr_picture_file is not None:
            result['IdOcrPictureFile'] = self.id_ocr_picture_file

        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url

        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof

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

        if m.get('FaceQualityCheck') is not None:
            self.face_quality_check = m.get('FaceQualityCheck')

        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')

        if m.get('IdOcrPictureFile') is not None:
            self.id_ocr_picture_file = m.get('IdOcrPictureFile')

        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')

        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')

        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

