# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class EkycVerifyV2AdvanceRequest(DaraModel):
    def __init__(
        self,
        authorize: str = None,
        crop: str = None,
        doc_name: str = None,
        doc_no: str = None,
        doc_type: str = None,
        face_picture_base_64: str = None,
        face_picture_file_object: BinaryIO = None,
        face_picture_url: str = None,
        face_quality_check: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_file_object: BinaryIO = None,
        id_ocr_picture_url: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        # Specifies whether to enable authoritative identity verification. This feature applies only to second-generation ID cards in mainland China.
        self.authorize = authorize
        # Specifies whether to allow cropping. Default value: F. Valid values:
        # 
        # - T: Allowed.
        # - F: Not allowed (default).
        self.crop = crop
        # The real name of the user. If Authorize is set to T and the document type is a mainland China ID card, you must provide at least one of the following: key document information (DocName and DocNo) or document images (IdOcrPictureBase64 or URL). Note: The value must contain one or more Chinese characters and no special characters, except for the middle dot (·) used in ethnic minority names.
        self.doc_name = doc_name
        # The document number of the user. If Authorize is set to T and the document type is a mainland China ID card, you must provide at least one of the following: key document information (DocName and DocNo) or document images (IdOcrPictureBase64 or URL). Note: The value must be an 18-character combination of letters and digits.
        self.doc_no = doc_no
        # The document type.
        self.doc_type = doc_type
        # The Base64-encoded facial image. Notes:
        # 
        # - If you use this method to pass the facial image, check the image size and do not upload oversized images.
        # - Specify only one of FacePictureBase64, FacePictureUrl, and FacePictureFile.
        self.face_picture_base_64 = face_picture_base_64
        # The file stream of the facial image.
        self.face_picture_file_object = face_picture_file_object
        # The URL of the facial image.
        self.face_picture_url = face_picture_url
        # Specifies whether to enable facial quality check.
        self.face_quality_check = face_quality_check
        # The Base64-encoded image of the document. Notes:
        # 
        # - If you use this method to pass the document image, check the image size and do not upload oversized images.
        # - Specify only one of IdOcrPictureBase64, IdOcrPictureUrl, and IdOcrPictureFile.
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # The file stream of the front image of the document.
        self.id_ocr_picture_file_object = id_ocr_picture_file_object
        # The URL of the front image of the document.
        self.id_ocr_picture_url = id_ocr_picture_url
        # Specifies whether to enable document anti-spoofing.
        self.id_spoof = id_spoof
        # The custom OCR quality check threshold mode. Valid values:
        # 
        # - 0: System default.
        # - 1: Strict mode.
        # - 2: Loose mode.
        # - 3: Quality check disabled (default).
        self.id_threshold = id_threshold
        # The custom unique business identifier on the merchant side, used for subsequent troubleshooting. The value must be a unique combination of up to 32 letters and digits.
        self.merchant_biz_id = merchant_biz_id
        # The custom user ID or other identifier that identifies a specific user, such as a mobile phone number or email address. Desensitize the value of this field in advance, such as by hashing the value.
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

        if self.face_picture_file_object is not None:
            result['FacePictureFile'] = self.face_picture_file_object

        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url

        if self.face_quality_check is not None:
            result['FaceQualityCheck'] = self.face_quality_check

        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64

        if self.id_ocr_picture_file_object is not None:
            result['IdOcrPictureFile'] = self.id_ocr_picture_file_object

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
            self.face_picture_file_object = m.get('FacePictureFile')

        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')

        if m.get('FaceQualityCheck') is not None:
            self.face_quality_check = m.get('FaceQualityCheck')

        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')

        if m.get('IdOcrPictureFile') is not None:
            self.id_ocr_picture_file_object = m.get('IdOcrPictureFile')

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

